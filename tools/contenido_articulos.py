# -*- coding: utf-8 -*-
"""
Artículos de la sección "Información jurídica".

Para agregar un artículo, sumá un diccionario a ARTICULOS. En el cuerpo podés
enlazar servicios con la sintaxis {{s:slug-del-servicio|texto del enlace}} y
otros artículos con {{a:slug-del-articulo|texto}}. Fechas en formato AAAA-MM-DD.
"""

CATEGORIAS = {
    "derecho-civil": {
        "nombre": "Derecho Civil",
        "descripcion": "Accidentes de tránsito, seguros, daños y perjuicios: qué hacer y cómo reclamar.",
    },
    "derecho-comercial": {
        "nombre": "Derecho Comercial",
        "descripcion": "Cheques rechazados, cobro de créditos y planes de ahorro.",
    },
    "derecho-laboral": {
        "nombre": "Derecho Laboral",
        "descripcion": "Despidos, liquidaciones, indemnizaciones y accidentes de trabajo.",
    },
    "derecho-de-familia": {
        "nombre": "Derecho de Familia",
        "descripcion": "Sucesiones y otras cuestiones familiares explicadas con claridad.",
    },
    "consorcios-y-expensas": {
        "nombre": "Consorcios y Expensas",
        "descripcion": "Información para administraciones, consorcios y propietarios.",
    },
    "sociedades": {
        "nombre": "Sociedades",
        "descripcion": "Cómo elegir y constituir una sociedad: SAS, SRL y más.",
    },
}

FECHA = "2026-10-08"

ARTICULOS = [
    {
        "slug": "que-hacer-despues-de-un-accidente-de-transito",
        "categoria": "derecho-civil",
        "servicio": "accidentes-de-transito",
        "titulo": "Qué hacer después de un accidente de tránsito",
        "title": "Qué hacer después de un accidente de tránsito: guía paso a paso",
        "description": "Qué hacer después de un choque: datos que tenés que pedir, pruebas que conviene guardar, cómo hacer la denuncia al seguro y cuándo reclamar una indemnización.",
        "resumen": "Los primeros minutos y días después de un choque son decisivos para el reclamo. Te contamos qué hacer, qué datos pedir y qué errores evitar.",
        "fecha": FECHA,
        "cuerpo": """
<p>Un accidente de tránsito siempre toma por sorpresa. Sin embargo, lo que hagas en los minutos y días siguientes puede definir si después vas a poder reclamar los daños de manera ágil o si el reclamo se va a complicar. Esta guía resume los pasos más importantes.</p>

<h2>1. Primero, la seguridad</h2>
<p>Si hay personas lesionadas, pedí asistencia médica de inmediato. Si es posible, señalizá el lugar para evitar un nuevo accidente. Recordá que la atención de los heridos siempre está por delante de cualquier trámite.</p>

<h2>2. Intercambiá datos con el otro conductor</h2>
<p>Pedí y anotá, como mínimo:</p>
<ul>
  <li>Nombre completo y DNI del conductor.</li>
  <li>Patente, marca y modelo del vehículo.</li>
  <li>Compañía de seguros y número de póliza.</li>
  <li>Nombre del titular del vehículo, si no es quien manejaba.</li>
</ul>
<p>Si el otro conductor se niega a dar sus datos, anotá la patente y, si es posible, sacale una foto al vehículo.</p>

<h2>3. Guardá pruebas</h2>
<p>Las pruebas que se pierden ese día difícilmente se recuperan después. Sacá fotos de los vehículos, de su posición, de las señales de tránsito y del lugar. Si hubo testigos, pediles nombre y teléfono. Si en la zona hay cámaras, anotá dónde están: pueden ser útiles más adelante.</p>

<h2>4. Hacé la denuncia ante tu aseguradora</h2>
<p>La denuncia del siniestro ante tu propia compañía de seguros es obligatoria y tiene un plazo breve, que en general es de tres días. Hacela aunque no hayas sido responsable y aunque pienses reclamarle al seguro del otro conductor. Pedí siempre una constancia de la denuncia.</p>

<h2>5. Si hubo lesiones, documentalas</h2>
<p>Hacete atender aunque las lesiones parezcan leves: algunas molestias aparecen días después. Guardá las constancias médicas, los estudios y los comprobantes de gastos. Todo eso forma parte del reclamo.</p>

<h2>6. No firmes acuerdos apresurados</h2>
<p>Es habitual recibir una oferta rápida para cerrar el tema. Antes de aceptar, conviene saber qué estás resignando: algunos acuerdos impiden reclamar después daños que todavía no se conocían.</p>

<h2>¿Quién paga los daños?</h2>
<p>En principio, quien causó el accidente y su aseguradora deben reparar los daños. El reclamo puede incluir la reparación del vehículo, la desvalorización, los días sin poder usarlo, los gastos médicos, la incapacidad y el daño moral, según el caso. Para profundizar, podés leer {{a:como-reclamar-danos-y-perjuicios|cómo reclamar daños y perjuicios}}.</p>

<h2>¿Cuánto tiempo hay para reclamar?</h2>
<p>El plazo general para reclamar daños es de tres años, aunque hay situaciones con plazos distintos. En la práctica, conviene iniciar el reclamo cuanto antes, mientras las pruebas están disponibles.</p>

<p>Si tuviste un choque y no sabés cómo seguir, en nuestra página de {{s:accidentes-de-transito|abogados de accidentes de tránsito}} te explicamos cómo podemos ayudarte.</p>
""",
    },
    {
        "slug": "que-hacer-si-la-compania-de-seguros-no-paga",
        "categoria": "derecho-civil",
        "servicio": "seguros",
        "titulo": "Qué hacer si la compañía de seguros no paga",
        "title": "Qué hacer si la compañía de seguros no paga el siniestro",
        "description": "¿El seguro rechazó el siniestro o demora el pago? Qué plazos tiene la aseguradora, cómo reclamar ante la Superintendencia y cuándo ir a juicio.",
        "resumen": "Rechazos sin fundamento, demoras y ofertas bajas son reclamos frecuentes. Te explicamos qué plazos tiene la aseguradora y cómo hacer valer tu póliza.",
        "fecha": FECHA,
        "cuerpo": """
<p>Pagar un seguro durante años y encontrarse con un rechazo o con una demora interminable justo cuando más se lo necesita es una situación lamentablemente frecuente. La buena noticia es que la ley establece reglas y plazos que la aseguradora tiene que cumplir.</p>

<h2>Revisá la póliza y la denuncia</h2>
<p>El primer paso es tener a mano la póliza completa —incluidas las condiciones generales y particulares— y la constancia de la denuncia del siniestro. La cobertura y las exclusiones están ahí, y son la base de cualquier reclamo.</p>

<h2>Los plazos de la aseguradora</h2>
<p>La ley de seguros establece que la compañía debe pronunciarse sobre el siniestro dentro de los 30 días de recibida la información necesaria. Si no lo hace, su silencio, en principio, se interpreta como aceptación. Una vez aceptado o determinado el monto, la aseguradora también tiene un plazo para pagar.</p>
<p>Por eso es importante dejar constancia de cada presentación y de cada documento que entregás: esas fechas marcan el inicio de los plazos.</p>

<h2>Si la compañía rechaza el siniestro</h2>
<p>El rechazo debe ser fundado. Muchas veces se apoya en interpretaciones discutibles de la póliza o en supuestos incumplimientos del asegurado. No lo des por definitivo: puede cuestionarse.</p>
<ul>
  <li>Pedí el rechazo por escrito, con sus fundamentos.</li>
  <li>Respondé por un medio fehaciente, como una carta documento.</li>
  <li>Reuní toda la documentación que acredite el siniestro y el daño.</li>
</ul>

<h2>Si la oferta es insuficiente</h2>
<p>Antes de aceptar un pago, compará la oferta con el daño real: presupuestos de reparación, valor del bien, gastos. Algunos acuerdos implican renunciar a reclamos posteriores, así que conviene analizarlos con cuidado.</p>

<h2>Las vías de reclamo</h2>
<ul>
  <li><strong>Reclamo directo</strong> ante la aseguradora, por escrito.</li>
  <li><strong>Denuncia ante la Superintendencia de Seguros de la Nación</strong>, el organismo que controla a las compañías.</li>
  <li><strong>Reclamo ante defensa del consumidor</strong>, cuando corresponde.</li>
  <li><strong>Acción judicial</strong>, si las instancias anteriores no dan resultado.</li>
</ul>
<p>Los reclamos contra la aseguradora tienen plazos de prescripción que pueden ser breves, por lo que no conviene esperar.</p>

<p>Si tu seguro no responde, en nuestra página de {{s:seguros|reclamos frente a compañías de seguros}} te contamos cómo trabajamos estos casos.</p>
""",
    },
    {
        "slug": "como-reclamar-danos-y-perjuicios",
        "categoria": "derecho-civil",
        "servicio": "danos-y-perjuicios",
        "titulo": "Cómo reclamar daños y perjuicios",
        "title": "Cómo reclamar daños y perjuicios: qué se puede pedir y cómo",
        "description": "Cómo reclamar daños y perjuicios en Argentina: qué daños se indemnizan, qué pruebas necesitás, la mediación previa y los plazos para iniciar el reclamo.",
        "resumen": "Qué daños pueden reclamarse, qué pruebas reunir y cómo es el camino desde el reclamo extrajudicial hasta el juicio.",
        "fecha": FECHA,
        "cuerpo": """
<p>Cuando alguien sufre un daño causado por otra persona o por una empresa, la ley le reconoce el derecho a ser reparado. Pero para que ese derecho se traduzca en una indemnización, el reclamo tiene que estar bien planteado y bien probado.</p>

<h2>Qué daños se pueden reclamar</h2>
<ul>
  <li><strong>Daño emergente:</strong> los gastos y pérdidas concretas que causó el hecho, como reparaciones, tratamientos o medicamentos.</li>
  <li><strong>Lucro cesante:</strong> lo que dejaste de ganar, por ejemplo, los días que no pudiste trabajar.</li>
  <li><strong>Incapacidad:</strong> las secuelas físicas o psíquicas que afectan tu vida o tu capacidad de generar ingresos.</li>
  <li><strong>Daño moral:</strong> las consecuencias no patrimoniales, como el dolor, la angustia o la alteración de la vida cotidiana.</li>
</ul>

<h2>Qué tiene que existir para reclamar</h2>
<p>En términos generales, tiene que haber un daño, una relación entre ese daño y el hecho, y un responsable al que se le pueda atribuir. En muchos casos, como en los accidentes con vehículos, la ley facilita el reclamo de la víctima.</p>

<h2>Las pruebas</h2>
<p>Un buen reclamo se apoya en pruebas: fotos y videos, testigos, informes, constancias médicas, facturas y presupuestos. Cuanto antes se reúnan, mejor. Algunas pruebas, como las imágenes de cámaras, se pierden en pocos días.</p>

<h2>El camino del reclamo</h2>
<h3>Reclamo extrajudicial</h3>
<p>Muchas veces el primer paso es una intimación formal al responsable o a su aseguradora. Puede abrir una negociación y evitar un juicio.</p>
<h3>Mediación previa</h3>
<p>En la Ciudad de Buenos Aires, antes de iniciar un juicio por daños, en general es obligatorio pasar por una mediación. Es una instancia en la que las partes, con la ayuda de un mediador, intentan llegar a un acuerdo.</p>
<h3>Juicio</h3>
<p>Si no hay acuerdo, se inicia la demanda. En el proceso se producen las pruebas, como pericias médicas o mecánicas, y finalmente el juez resuelve.</p>

<h2>Los plazos</h2>
<p>El plazo general de prescripción para reclamar daños es de tres años, aunque hay casos con plazos distintos. Dejar pasar el tiempo no solo pone en riesgo el plazo: también hace más difícil probar lo ocurrido.</p>

<p>Si querés saber si tu caso puede reclamarse, mirá nuestra página de {{s:danos-y-perjuicios|reclamos por daños y perjuicios}}. Si el daño ocurrió en un choque, te puede servir también {{a:que-hacer-despues-de-un-accidente-de-transito|qué hacer después de un accidente de tránsito}}.</p>
""",
    },
    {
        "slug": "como-constituir-una-sas-en-argentina",
        "categoria": "sociedades",
        "servicio": "constitucion-de-sas",
        "titulo": "Cómo constituir una SAS en Argentina",
        "title": "Cómo constituir una SAS en Argentina: requisitos y pasos",
        "description": "Cómo crear una SAS en Argentina: qué es una Sociedad por Acciones Simplificada, requisitos, capital mínimo, documentación y pasos para constituirla e inscribirla.",
        "resumen": "Qué es una SAS, qué necesitás para crearla y cuáles son los pasos para constituirla y ponerla en funcionamiento.",
        "fecha": FECHA,
        "cuerpo": """
<p>La Sociedad por Acciones Simplificada, conocida como SAS, se convirtió en una de las alternativas más elegidas para formalizar un emprendimiento en Argentina. En esta guía te explicamos qué es, qué necesitás y cómo es el proceso para constituirla.</p>

<h2>Qué es una SAS</h2>
<p>La SAS es un tipo societario creado por la Ley 27.349. Sus principales características son:</p>
<ul>
  <li>Puede constituirse con <strong>uno o más socios</strong>.</li>
  <li>El capital se divide en <strong>acciones</strong>.</li>
  <li>En principio, los socios <strong>limitan su responsabilidad</strong> a su aporte.</li>
  <li>Tiene una <strong>estructura flexible</strong>, que se adapta a las necesidades del proyecto.</li>
</ul>

<h2>Qué necesitás para constituir una SAS</h2>
<ul>
  <li>Los datos personales y fiscales de cada socio.</li>
  <li>Un nombre para la sociedad, con alternativas por si no está disponible.</li>
  <li>El objeto: la actividad o las actividades que va a desarrollar.</li>
  <li>El capital social, que no puede ser inferior al equivalente a dos salarios mínimos, vitales y móviles.</li>
  <li>El domicilio de la sede.</li>
  <li>La designación de quienes van a administrar y representar a la sociedad.</li>
</ul>

<h2>Los pasos para constituirla</h2>
<h3>1. Definir la estructura</h3>
<p>Antes de cualquier trámite conviene decidir quiénes son los socios, cuánto aporta cada uno, quién administra y cómo se toman las decisiones. Son definiciones que después es más difícil cambiar.</p>
<h3>2. Redactar el instrumento constitutivo</h3>
<p>Es el documento que contiene el estatuto de la sociedad. Existen modelos estándar, pero muchas veces conviene adaptar algunas cláusulas al proyecto y a la relación entre los socios.</p>
<h3>3. Inscribir la sociedad</h3>
<p>El instrumento se presenta ante el registro público que corresponde según la jurisdicción. Los requisitos y los tiempos pueden variar según el organismo.</p>
<h3>4. Obtener el CUIT y empezar a operar</h3>
<p>Una vez inscripta, la sociedad obtiene su CUIT y puede empezar a facturar, abrir una cuenta bancaria y cumplir con sus obligaciones iniciales.</p>

<h2>¿SAS o SRL?</h2>
<p>Depende del proyecto. Si estás evaluando ambas opciones, te recomendamos leer {{a:diferencia-entre-sas-y-srl|cuál es la diferencia entre SAS y SRL}}.</p>

<p>Si querés constituir tu sociedad con acompañamiento profesional, en nuestra página de {{s:constitucion-de-sas|constitución de SAS}} te explicamos cómo trabajamos.</p>
""",
    },
    {
        "slug": "diferencia-entre-sas-y-srl",
        "categoria": "sociedades",
        "servicio": "constitucion-de-sociedades",
        "titulo": "Cuál es la diferencia entre SAS y SRL",
        "title": "Diferencia entre SAS y SRL: cuál conviene para tu negocio",
        "description": "SAS o SRL: diferencias en cantidad de socios, capital, administración, flexibilidad y transferencia de participaciones para elegir la sociedad adecuada.",
        "resumen": "Las dos son muy elegidas por emprendedores y pymes. Comparamos sus diferencias principales para ayudarte a elegir.",
        "fecha": FECHA,
        "cuerpo": """
<p>Cuando llega el momento de formalizar un negocio, una de las primeras preguntas es qué tipo de sociedad conviene. La SAS y la SRL son las alternativas más frecuentes para emprendedores y pymes. Ambas limitan, en principio, la responsabilidad de los socios, pero tienen diferencias importantes.</p>

<h2>Cantidad de socios</h2>
<p>La <strong>SAS</strong> puede tener un solo socio, lo que la vuelve muy útil para quien emprende sin socios. La <strong>SRL</strong>, en cambio, requiere al menos dos socios y admite hasta cincuenta.</p>

<h2>Cómo se divide el capital</h2>
<p>En la SAS el capital se divide en <strong>acciones</strong>; en la SRL, en <strong>cuotas</strong>. En la práctica, las acciones suelen facilitar la incorporación de nuevos socios o inversores.</p>

<h2>Flexibilidad</h2>
<p>La SAS fue pensada para ofrecer una estructura más flexible: el estatuto permite adaptar la organización y las reglas internas al proyecto. La SRL tiene un funcionamiento más tradicional y previsible, con reglas más definidas por la ley.</p>

<h2>Transferencia de participaciones</h2>
<p>En la SRL, la transferencia de cuotas a terceros suele estar sujeta a limitaciones y a la conformidad de los demás socios. En la SAS, las reglas de transferencia de acciones se definen en el estatuto.</p>

<h2>Administración</h2>
<p>En ambas, la administración puede estar a cargo de una o más personas. En la SRL se habla de gerentes; en la SAS, de administradores. Definir bien quién decide y cómo es clave en cualquiera de las dos.</p>

<h2>Entonces, ¿cuál conviene?</h2>
<ul>
  <li>Si emprendés solo o buscás una estructura ágil y flexible, la <strong>SAS</strong> suele ser una buena opción.</li>
  <li>Si son varios socios y prefieren un esquema tradicional, con mayor control sobre el ingreso de terceros, la <strong>SRL</strong> puede ser adecuada.</li>
</ul>
<p>No hay una respuesta única: depende de la actividad, de los socios, de cómo piensan financiarse y de los planes a futuro. Las normas y los criterios de los registros también pueden cambiar con el tiempo, por eso conviene analizarlo con asesoramiento.</p>

<p>Te ayudamos a elegir y a constituir la sociedad adecuada: conocé nuestro servicio de {{s:constitucion-de-sociedades|constitución de sociedades}} o, si ya elegiste, el de {{s:constitucion-de-sas|constitución de SAS}}.</p>
""",
    },
    {
        "slug": "que-hacer-ante-un-despido",
        "categoria": "derecho-laboral",
        "servicio": "despidos",
        "titulo": "Qué hacer ante un despido",
        "title": "Qué hacer ante un despido: primeros pasos y qué te corresponde",
        "description": "Te despidieron: qué hacer primero, qué no firmar, qué rubros incluye la liquidación final, cuándo deben pagarte y cómo es el reclamo laboral en Buenos Aires.",
        "resumen": "Las primeras decisiones después de un despido son importantes. Qué revisar, qué no firmar y qué te puede corresponder.",
        "fecha": FECHA,
        "cuerpo": """
<p>Recibir un despido es una situación difícil. En medio de la preocupación, es importante no tomar decisiones apresuradas y conocer cuáles son tus derechos. Estos son los primeros pasos.</p>

<h2>1. Guardá la comunicación del despido</h2>
<p>El despido debe comunicarse por escrito, normalmente por telegrama o carta documento. Guardala: indica la fecha y, si el empleador invoca una causa, cuál es. Esa causa no puede cambiarse después.</p>

<h2>2. No firmes lo que no entiendas</h2>
<p>Es habitual que te pidan firmar recibos, renuncias o acuerdos. Antes de firmar, asegurate de entender qué estás firmando. Si recibís dinero, podés firmar el recibo dejando constancia de que lo recibís a cuenta de lo que te corresponde.</p>

<h2>3. Reuní la documentación</h2>
<ul>
  <li>Recibos de sueldo.</li>
  <li>La comunicación del despido.</li>
  <li>Constancias de registración, si las tenés.</li>
  <li>Mensajes, mails y cualquier prueba de la relación laboral, especialmente si no estabas registrado o lo estabas de forma incorrecta.</li>
</ul>

<h2>Qué te puede corresponder</h2>
<p>Si el despido es sin causa, en general corresponde:</p>
<ul>
  <li>Una <strong>indemnización por antigüedad</strong>.</li>
  <li>El <strong>preaviso</strong>, si no fue otorgado.</li>
  <li>La <strong>integración del mes de despido</strong>, según el caso.</li>
  <li>Los <strong>proporcionales de aguinaldo y vacaciones</strong>.</li>
  <li>Los días trabajados del mes.</li>
</ul>
<p>El cálculo exacto depende de tu antigüedad, tu remuneración y tu situación particular. Además, el empleador debe entregarte los certificados de trabajo.</p>

<h2>¿Cuándo tienen que pagarte?</h2>
<p>La liquidación final debe abonarse dentro de los cuatro días hábiles posteriores a la finalización de la relación laboral.</p>

<h2>Si no te pagan o el monto no es correcto</h2>
<p>El reclamo suele comenzar con un intercambio de telegramas. En la Ciudad de Buenos Aires, antes de un juicio, el reclamo pasa por el Servicio de Conciliación Laboral Obligatoria (SECLO), donde muchas veces se llega a un acuerdo. Si no, se inicia la demanda ante la justicia laboral.</p>

<h2>Los plazos</h2>
<p>Las acciones laborales prescriben, en general, a los dos años. Pero hay comunicaciones que deben responderse en plazos mucho más cortos, por eso conviene consultar cuanto antes.</p>

<p>Si te despidieron, en nuestra página de {{s:despidos|abogados para despidos}} te explicamos cómo podemos ayudarte.</p>
""",
    },
    {
        "slug": "que-cubre-la-art",
        "categoria": "derecho-laboral",
        "servicio": "art-accidentes-de-trabajo",
        "titulo": "Qué cubre la ART",
        "title": "Qué cubre la ART: accidentes y enfermedades laborales",
        "description": "Qué cubre la ART: accidentes de trabajo, in itinere y enfermedades profesionales. Prestaciones, días de baja, incapacidad y qué hacer ante un rechazo.",
        "resumen": "Qué situaciones cubre la Aseguradora de Riesgos del Trabajo, qué prestaciones tenés que recibir y qué hacer si rechazan tu accidente.",
        "fecha": FECHA,
        "cuerpo": """
<p>Todos los trabajadores registrados están cubiertos por una Aseguradora de Riesgos del Trabajo (ART), contratada por el empleador. Pero muchas personas recién descubren qué cubre cuando sufren un accidente. Esto es lo que tenés que saber.</p>

<h2>Qué situaciones cubre</h2>
<ul>
  <li><strong>Accidentes de trabajo:</strong> los que ocurren por el hecho o en ocasión del trabajo.</li>
  <li><strong>Accidentes in itinere:</strong> los que ocurren en el trayecto entre tu casa y el trabajo, siempre que no hayas interrumpido o alterado el recorrido por motivos personales.</li>
  <li><strong>Enfermedades profesionales:</strong> las causadas por las tareas o el ambiente de trabajo.</li>
</ul>

<h2>Qué prestaciones tenés que recibir</h2>
<h3>Prestaciones en especie</h3>
<p>Atención médica, medicamentos, prótesis, rehabilitación y traslados necesarios, hasta tu curación completa o mientras persistan los síntomas incapacitantes.</p>
<h3>Prestaciones dinerarias</h3>
<p>Durante la baja, la ART debe pagar lo que dejás de percibir. Y si al finalizar el tratamiento quedan secuelas, corresponde una indemnización por la incapacidad permanente, calculada según el porcentaje de incapacidad, tu edad y tus ingresos.</p>

<h2>Qué hacer después de un accidente</h2>
<ul>
  <li>Avisá de inmediato a tu empleador y pedí que se haga la denuncia ante la ART.</li>
  <li>Si el empleador no la hace, podés hacerla vos directamente.</li>
  <li>Guardá todas las constancias médicas y los estudios.</li>
</ul>

<h2>Si la ART rechaza el accidente o te da el alta antes de tiempo</h2>
<p>Son situaciones frecuentes. El rechazo o el alta pueden cuestionarse. En la Ciudad de Buenos Aires y en otras jurisdicciones adheridas al sistema, el trámite comienza ante la comisión médica jurisdiccional, que es la primera instancia obligatoria. Luego, la decisión puede revisarse judicialmente.</p>

<h2>La importancia del porcentaje de incapacidad</h2>
<p>La indemnización depende directamente del porcentaje de incapacidad que se determine. Por eso es importante contar con asesoramiento al momento de la evaluación médica, para que se tengan en cuenta todas las secuelas.</p>

<p>Si tuviste un accidente de trabajo, conocé cómo trabajamos los {{s:art-accidentes-de-trabajo|reclamos a la ART}}. Si además tu relación laboral terminó, te puede interesar {{a:que-hacer-ante-un-despido|qué hacer ante un despido}}.</p>
""",
    },
    {
        "slug": "como-iniciar-una-sucesion",
        "categoria": "derecho-de-familia",
        "servicio": "sucesiones",
        "titulo": "Cómo iniciar una sucesión",
        "title": "Cómo iniciar una sucesión en Buenos Aires: pasos y documentación",
        "description": "Cómo iniciar una sucesión: dónde se tramita, qué documentación se necesita, qué es la declaratoria de herederos y cuáles son las etapas del proceso sucesorio.",
        "resumen": "Dónde se inicia, qué documentos se necesitan y cuáles son las etapas del proceso sucesorio, explicado de forma simple.",
        "fecha": FECHA,
        "cuerpo": """
<p>Cuando fallece un familiar que tenía bienes a su nombre —un inmueble, un auto, dinero en el banco—, los herederos necesitan hacer la sucesión para poder disponer de ellos. Es un trámite judicial, pero no tiene por qué ser complicado si se lo encara de forma ordenada.</p>

<h2>Qué es la sucesión</h2>
<p>Es el proceso judicial que permite determinar quiénes son los herederos de una persona fallecida y transmitirles sus bienes, derechos y también sus deudas, en la medida de lo que se hereda.</p>

<h2>Dónde se inicia</h2>
<p>La sucesión se inicia ante el juzgado del último domicilio de la persona fallecida. Por ejemplo, si vivía en la Ciudad de Buenos Aires, se tramita ante los juzgados civiles de la Ciudad.</p>

<h2>Qué documentación se necesita</h2>
<ul>
  <li>Partida de defunción.</li>
  <li>Partidas que acrediten el vínculo con la persona fallecida, como partidas de nacimiento o de matrimonio.</li>
  <li>DNI de los herederos.</li>
  <li>Información sobre los bienes: escrituras, títulos de vehículos, datos de cuentas.</li>
  <li>El testamento, si existe.</li>
</ul>

<h2>Las etapas del proceso</h2>
<h3>1. Inicio</h3>
<p>Se presenta la documentación ante el juzgado y se solicita la apertura de la sucesión.</p>
<h3>2. Edictos</h3>
<p>Se publican edictos para convocar a otros posibles herederos o acreedores.</p>
<h3>3. Declaratoria de herederos</h3>
<p>Si no hay testamento, el juez dicta la declaratoria de herederos, que reconoce quiénes son. Si hay testamento, se analiza su validez.</p>
<h3>4. Inventario y avalúo</h3>
<p>Se determinan los bienes que integran la herencia y su valor.</p>
<h3>5. Inscripción o partición</h3>
<p>Finalmente, los bienes se inscriben a nombre de los herederos o se dividen entre ellos. También pueden venderse, si así lo deciden.</p>

<h2>¿Cuánto demora?</h2>
<p>Depende de la cantidad y el tipo de bienes, de si hay acuerdo entre los herederos y de los tiempos del juzgado. Cuando los herederos están de acuerdo y la documentación está completa, el trámite suele ser más ágil.</p>

<h2>¿Hay un plazo para iniciarla?</h2>
<p>No existe un plazo breve para iniciar la sucesión, pero demorarla puede traer complicaciones: bienes que se deterioran, deudas que crecen o dificultades para reunir documentación con el paso del tiempo.</p>

<p>Si necesitás iniciar una sucesión, conocé cómo te acompañamos en nuestra página de {{s:sucesiones|abogados de sucesiones}}.</p>
""",
    },
    {
        "slug": "que-hacer-si-un-propietario-no-paga-las-expensas",
        "categoria": "consorcios-y-expensas",
        "servicio": "cobro-de-expensas",
        "titulo": "Qué hacer si un propietario no paga las expensas",
        "title": "Qué hacer si un propietario no paga las expensas del consorcio",
        "description": "Guía para administradores: qué hacer si un propietario no paga las expensas, cómo intimarlo, qué es el certificado de deuda y cuándo ejecutar.",
        "resumen": "Una guía práctica para administradores y consorcios frente a propietarios que dejan de pagar las expensas.",
        "fecha": FECHA,
        "cuerpo": """
<p>Cuando un propietario deja de pagar las expensas, el problema no es solo suyo: el resto del consorcio termina cubriendo la diferencia o resignando servicios y mantenimiento. Por eso es importante actuar con un esquema claro y desde el inicio.</p>

<h2>1. No dejar crecer la deuda</h2>
<p>Una deuda de uno o dos meses es mucho más fácil de regularizar que una de un año. Conviene tener un criterio definido sobre cuándo y cómo se inicia el reclamo, para que todos los propietarios reciban el mismo tratamiento.</p>

<h2>2. Contactar al propietario</h2>
<p>Muchas veces un llamado o una nota de la administración alcanza para ordenar la situación o acordar un plan de pagos. Si se llega a un acuerdo, conviene documentarlo por escrito.</p>

<h2>3. Intimar formalmente</h2>
<p>Si el contacto informal no da resultado, el paso siguiente es una intimación fehaciente, por ejemplo, por carta documento, con el detalle de la deuda y un plazo para pagar.</p>

<h2>4. Emitir el certificado de deuda</h2>
<p>El administrador puede emitir un certificado de deuda de expensas. La ley le otorga a ese certificado el carácter de título ejecutivo, lo que permite iniciar un juicio más ágil que un proceso común.</p>

<h2>5. Iniciar la ejecución de expensas</h2>
<p>Si la deuda no se regulariza, el consorcio, representado por su administrador, puede iniciar la ejecución. Conocé cómo funciona en {{a:como-se-ejecutan-las-expensas|cómo se ejecutan las expensas}}.</p>

<h2>Recomendaciones para la administración</h2>
<ul>
  <li>Mantener ordenadas las liquidaciones y los comprobantes de cada período.</li>
  <li>Tener a mano el reglamento de propiedad horizontal y las actas de asamblea.</li>
  <li>Informar a los propietarios sobre el estado de los reclamos.</li>
  <li>Definir con el consorcio una política de cobro clara y homogénea.</li>
</ul>

<p>Si tenés deudores en tu consorcio, en nuestra página de {{s:cobro-de-expensas|cobro y ejecución de expensas}} te explicamos cómo trabajamos con administraciones.</p>
""",
    },
    {
        "slug": "como-se-ejecutan-las-expensas",
        "categoria": "consorcios-y-expensas",
        "servicio": "cobro-de-expensas",
        "titulo": "Cómo se ejecutan las expensas",
        "title": "Cómo se ejecutan las expensas: el juicio ejecutivo paso a paso",
        "description": "Cómo funciona la ejecución de expensas: el certificado de deuda como título ejecutivo, las etapas del juicio, los embargos y cuánto puede demorar el cobro.",
        "resumen": "El juicio ejecutivo de expensas explicado paso a paso: qué se necesita, cómo avanza y qué medidas pueden pedirse.",
        "fecha": FECHA,
        "cuerpo": """
<p>La ejecución de expensas es la herramienta judicial que tiene el consorcio para cobrar las expensas adeudadas por un propietario. Es un proceso más rápido que un juicio ordinario porque se basa en un documento que la ley considera suficiente para reclamar: el certificado de deuda.</p>

<h2>El certificado de deuda</h2>
<p>Es el documento emitido por el administrador que detalla las expensas impagas de una unidad. Para que pueda usarse en la ejecución, debe cumplir con los requisitos del reglamento de propiedad horizontal y de la ley. Por eso es importante revisarlo antes de iniciar el juicio.</p>

<h2>Las etapas del juicio ejecutivo</h2>
<h3>1. Demanda</h3>
<p>Se presenta la demanda con el certificado de deuda, el reglamento y la documentación que acredita la representación del administrador.</p>
<h3>2. Intimación de pago</h3>
<p>El juzgado ordena intimar al propietario a pagar. En esta etapa muchas veces el deudor propone un acuerdo.</p>
<h3>3. Defensas del deudor</h3>
<p>En el juicio ejecutivo, las defensas que puede plantear el deudor son limitadas. No se discute, en principio, si los gastos eran convenientes, sino si la deuda existe y es exigible.</p>
<h3>4. Sentencia</h3>
<p>Si el deudor no paga ni presenta defensas válidas, el juez ordena llevar adelante la ejecución.</p>
<h3>5. Cobro</h3>
<p>Con la sentencia, se avanza sobre los bienes del deudor para obtener el pago. Puede embargarse su cuenta, sus ingresos o la propia unidad.</p>

<h2>¿Se puede rematar el departamento?</h2>
<p>Si la deuda no se paga, en última instancia puede ordenarse la subasta de la unidad. Es una medida extrema: en la práctica, la mayoría de los casos se resuelven antes, con el pago o con un acuerdo.</p>

<h2>¿Hace falta mediación?</h2>
<p>En la Ciudad de Buenos Aires, los procesos de ejecución, en general, no requieren mediación previa, lo que contribuye a que el reclamo sea más ágil.</p>

<h2>¿Cuánto demora?</h2>
<p>Depende de la notificación al deudor, de su actitud y de los tiempos del juzgado. El inicio del juicio suele acelerar la regularización de la deuda.</p>

<p>Si necesitás iniciar una ejecución, conocé nuestro servicio de {{s:cobro-de-expensas|cobro de expensas para consorcios}}. También podés leer {{a:que-hacer-si-un-propietario-no-paga-las-expensas|qué hacer si un propietario no paga las expensas}}.</p>
""",
    },
    {
        "slug": "que-hacer-con-un-cheque-rechazado",
        "categoria": "derecho-comercial",
        "servicio": "cheques-sin-fondos",
        "titulo": "Qué hacer con un cheque rechazado",
        "title": "Qué hacer con un cheque rechazado o sin fondos | J, C & S",
        "description": "Te rechazaron un cheque: qué hacer, qué plazos hay que respetar, contra quién se puede reclamar y cómo es la acción ejecutiva para cobrarlo.",
        "resumen": "Qué hacer apenas te rechazan un cheque, qué plazos tenés que cuidar y cómo se reclama su cobro.",
        "fecha": FECHA,
        "cuerpo": """
<p>Recibir un cheque rechazado es un golpe para cualquier negocio. Pero el cheque tiene una ventaja: es un título que permite reclamar el cobro por una vía más rápida que un juicio común. Para aprovecharla, hay que actuar a tiempo.</p>

<h2>1. Conservá el cheque y la constancia de rechazo</h2>
<p>Cuando el banco rechaza un cheque, deja constancia del motivo. Esa constancia, junto con el cheque, es la base del reclamo. Si es un e-cheq, guardá la información del rechazo que te brinda tu banco.</p>
<p>No devuelvas el cheque al deudor a cambio de una promesa de pago: sin el documento, el reclamo se complica.</p>

<h2>2. Revisá los plazos</h2>
<p>Los plazos en materia de cheques son breves. Hay un plazo para presentar el cheque al cobro y, una vez rechazado, la acción para reclamarlo prescribe en general al año desde el vencimiento del plazo de presentación. Si dejás pasar ese tiempo, la vía rápida se pierde.</p>

<h2>3. Intimá el pago</h2>
<p>Una intimación formal al librador —por ejemplo, por carta documento— suele ser el primer paso. A veces alcanza para obtener el pago o un acuerdo.</p>

<h2>4. Iniciá la acción ejecutiva</h2>
<p>Si no hay respuesta, se puede iniciar un juicio ejecutivo. Como el cheque es un título ejecutivo, las defensas del deudor son limitadas y el proceso es más ágil. Además, pueden pedirse medidas como embargos para asegurar el cobro.</p>

<h2>¿Contra quién se puede reclamar?</h2>
<p>En general, contra quien libró el cheque y contra quienes lo endosaron antes que vos. Analizar a quién conviene reclamar depende de cada caso.</p>

<h2>¿Y si el cheque era de pago diferido?</h2>
<p>Los cheques de pago diferido también pueden reclamarse por esta vía, con sus propias reglas de presentación. Lo mismo sucede con los cheques electrónicos.</p>

<h2>Aspectos penales</h2>
<p>En determinados casos, librar un cheque sin fondos puede tener consecuencias penales. Es una cuestión que debe analizarse con cuidado y no reemplaza el reclamo civil del cobro.</p>

<p>Si tenés un cheque rechazado, conocé cómo trabajamos el {{s:cheques-sin-fondos|cobro de cheques sin fondos y recupero de créditos}}.</p>
""",
    },
    {
        "slug": "problemas-con-un-plan-de-ahorro",
        "categoria": "derecho-comercial",
        "servicio": "planes-de-ahorro",
        "titulo": "Qué hacer ante un problema con un plan de ahorro",
        "title": "Problemas con un plan de ahorro: qué hacer y cómo reclamar",
        "description": "Aumentos de cuotas, demoras en la entrega o cobros indebidos en tu plan de ahorro: qué derechos tenés como suscriptor y cómo reclamar ante la administradora.",
        "resumen": "Cuotas que suben, entregas que no llegan o cargos que no entendés: qué derechos tenés y cómo reclamar.",
        "fecha": FECHA,
        "cuerpo": """
<p>Los planes de ahorro son una forma muy difundida de acceder a un auto. Pero son contratos largos, con muchas cláusulas, y con el tiempo pueden aparecer problemas. Estos son los más frecuentes y cómo encararlos.</p>

<h2>Los problemas más habituales</h2>
<ul>
  <li><strong>Aumentos de cuotas</strong> que, por la actualización del valor del vehículo, se vuelven difíciles de afrontar.</li>
  <li><strong>Demoras en la entrega</strong> del vehículo una vez adjudicado.</li>
  <li><strong>Cargos poco claros</strong>: seguros, gastos administrativos o conceptos que no se informaron correctamente.</li>
  <li><strong>Dificultades para renunciar</strong> al plan o para recuperar lo pagado.</li>
  <li><strong>Problemas con la concesionaria</strong> en la entrega, la documentación o el estado del vehículo.</li>
</ul>

<h2>Tus derechos como suscriptor</h2>
<p>En general, la relación entre el suscriptor y la administradora del plan es una relación de consumo. Eso significa que tenés derecho a información clara y detallada, a un trato digno y a que las cláusulas abusivas no se apliquen en tu contra.</p>

<h2>Cómo reclamar</h2>
<h3>1. Reuní la documentación</h3>
<p>El contrato o la solicitud de adhesión, los comprobantes de pago, los resúmenes y todas las comunicaciones con la administradora y la concesionaria.</p>
<h3>2. Hacé un reclamo formal</h3>
<p>Presentá el reclamo por escrito ante la administradora y guardá el número de gestión. Si no responde o la respuesta no es satisfactoria, podés enviar una carta documento.</p>
<h3>3. Acudí a los organismos de control</h3>
<p>Existen instancias administrativas de defensa del consumidor y de control de los planes de ahorro ante las que se puede presentar el reclamo.</p>
<h3>4. La vía judicial</h3>
<p>Si las instancias anteriores no dan resultado, se puede iniciar una acción judicial. En algunos casos pueden pedirse medidas para proteger al suscriptor mientras dura el reclamo.</p>

<h2>Antes de dejar de pagar</h2>
<p>Dejar de pagar las cuotas puede tener consecuencias, como la pérdida de beneficios o el inicio de reclamos por parte de la administradora. Antes de tomar esa decisión, conviene analizar las alternativas.</p>

<p>Si tenés un problema con tu plan, conocé cómo trabajamos los {{s:planes-de-ahorro|reclamos por planes de ahorro}}.</p>
""",
    },
]
