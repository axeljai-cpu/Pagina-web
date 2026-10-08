<?php
/**
 * Estudio J, C & S — Envío de formularios de contacto.
 *
 * Recibe los formularios del sitio y los envía por email al estudio.
 * Responde JSON cuando se llama desde JavaScript y redirige a /gracias/
 * cuando el navegador envía el formulario sin JavaScript.
 *
 * Configuración: cambiá $DESTINO y $REMITENTE si hace falta. El remitente
 * debe ser una casilla del mismo dominio (creala en el panel de Hostinger)
 * para que los correos no terminen en spam.
 */

$DESTINO   = 'info@estudiojcs.com.ar';
$REMITENTE = 'web@estudiojcs.com.ar';

header('X-Content-Type-Options: nosniff');

$quiereJson = isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false;

function responder($ok, $error = '') {
    global $quiereJson;
    if ($quiereJson) {
        header('Content-Type: application/json; charset=utf-8');
        http_response_code($ok ? 200 : 400);
        echo json_encode(array('ok' => $ok, 'error' => $error));
    } else {
        header('Location: ' . ($ok ? '/gracias/' : '/contacto/'), true, 303);
    }
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    header('Allow: POST');
    exit;
}

// Anti-spam: campo trampa y tiempo mínimo de llenado
if (!empty($_POST['sitio_web'])) {
    responder(true); // se descarta en silencio
}
$t = isset($_POST['_t']) ? (int) $_POST['_t'] : 0;
if ($t > 0 && (round(microtime(true) * 1000) - $t) < 2500) {
    responder(true);
}

function limpiar($valor, $max = 2000) {
    $valor = is_string($valor) ? trim($valor) : '';
    $valor = str_replace(array("\r\n", "\r"), "\n", $valor);
    return mb_substr(strip_tags($valor), 0, $max, 'UTF-8');
}
function linea($valor) {
    // Sin saltos de línea: evita inyección de cabeceras
    return preg_replace('/[\r\n]+/', ' ', limpiar($valor, 200));
}

$tipo     = linea(!empty($_POST['motivo']) ? $_POST['motivo'] : 'Consulta');
$nombre   = linea(isset($_POST['nombre']) ? $_POST['nombre'] : '');
$email    = linea(isset($_POST['email']) ? $_POST['email'] : '');
$telefono = linea(isset($_POST['telefono']) ? $_POST['telefono'] : '');
$acepta   = isset($_POST['acepta']);

if ($nombre === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || strlen(preg_replace('/\D/', '', $telefono)) < 8 || !$acepta) {
    responder(false, 'datos');
}

$campos = array(
    'motivo'  => 'Motivo de consulta',
    'pagina'  => 'Enviado desde',
    'utm'     => 'Origen de campaña',
    'mensaje' => 'Mensaje',
);

$cuerpo  = "Nueva consulta desde el sitio web\n";
$cuerpo .= "==================================\n\n";
$cuerpo .= "Nombre: $nombre\n";
$cuerpo .= "Email: $email\n";
$cuerpo .= "Teléfono: $telefono\n";
foreach ($campos as $clave => $etiqueta) {
    if (!empty($_POST[$clave])) {
        $valor = $clave === 'mensaje' ? limpiar($_POST[$clave], 5000) : linea($_POST[$clave]);
        $cuerpo .= ($clave === 'mensaje' ? "\n$etiqueta:\n" : "$etiqueta: ") . $valor . "\n";
    }
}
$cuerpo .= "\n----------------------------------\n";
$cuerpo .= 'Enviado: ' . date('d/m/Y H:i') . "\n";

$asunto = '=?UTF-8?B?' . base64_encode("[Web] $tipo — $nombre") . '?=';
$cabeceras  = "From: Estudio J, C & S <$REMITENTE>\r\n";
$cabeceras .= "Reply-To: $email\r\n";
$cabeceras .= "MIME-Version: 1.0\r\n";
$cabeceras .= "Content-Type: text/plain; charset=UTF-8\r\n";
$cabeceras .= "Content-Transfer-Encoding: 8bit\r\n";

$enviado = @mail($DESTINO, $asunto, $cuerpo, $cabeceras, '-f' . $REMITENTE);

responder((bool) $enviado, $enviado ? '' : 'mail');
