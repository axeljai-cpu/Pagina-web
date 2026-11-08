# -*- coding: utf-8 -*-
"""
Contenido de las herramientas y guías de conversión:
  - Calculadora de indemnización por despido y ART
  - Guía "¿Cuánto cuesta una sucesión?"

Los textos son información general y prudente. Revisar ante cambios normativos.
"""

ACTUALIZACION = "noviembre de 2026"

CALCULADORA = {
    "slug": "calculadora-indemnizacion-despido",
    "title": "Calculadora de indemnización por despido 2026 | J, C & S",
    "description": "Calculá tu indemnización por despido sin causa con la Ley Bases: antigüedad, preaviso, integración, SAC y vacaciones. Incluye calculadora de indemnización ART.",
    "h1": "Calculadora de indemnización por despido",
    "lead": "Calculá en un minuto cuánto te corresponde por un despido sin causa, con las reglas vigentes después de la Ley Bases. También podés estimar la indemnización de la ART por un accidente de trabajo.",
    "rubros": [
        ("Indemnización por antigüedad (art. 245 LCT)",
         "Un mes de la mejor remuneración mensual, normal y habitual del último año por cada año trabajado o fracción mayor de tres meses. Desde la Ley Bases, la base no incluye el aguinaldo ni otros conceptos de pago semestral o anual. Puede tener un tope fijado por el convenio colectivo, que no puede reducir la base en más de un 33 %."),
        ("Preaviso (arts. 231 y 232 LCT)",
         "Si el empleador no avisó el despido con anticipación, debe pagar una indemnización equivalente: 15 días durante el período de prueba, un mes con antigüedad de hasta cinco años y dos meses si es mayor."),
        ("Integración del mes de despido (art. 233 LCT)",
         "Si el despido sin preaviso no coincide con el último día del mes, corresponden los salarios de los días que faltan hasta fin de mes."),
        ("Días trabajados, aguinaldo y vacaciones",
         "Se suman los días trabajados del mes, el aguinaldo (SAC) proporcional del semestre y las vacaciones no gozadas proporcionales al tiempo trabajado en el año, con su aguinaldo."),
    ],
    "cambios": [
        "El período de prueba pasó a ser, en general, de seis meses. Durante ese período no corresponde indemnización por antigüedad, aunque sí el preaviso de 15 días.",
        "La base de la indemnización por antigüedad no incluye el aguinaldo ni los conceptos de pago semestral o anual.",
        "Se derogaron varias multas por trabajo no registrado que antes se sumaban a la liquidación.",
        "Los convenios colectivos pueden reemplazar la indemnización por un fondo o sistema de cese laboral.",
    ],
    "faqs": [
        ("¿Cómo se calcula la indemnización por despido sin causa?",
         "Se toma la mejor remuneración mensual, normal y habitual del último año y se multiplica por los años de antigüedad, contando como año completo la fracción mayor de tres meses. A eso se suman el preaviso, la integración del mes de despido, los días trabajados, el aguinaldo y las vacaciones proporcionales."),
        ("¿Qué cambió con la Ley Bases en la indemnización?",
         "Entre otros cambios, se amplió el período de prueba a seis meses, se excluyó el aguinaldo de la base de la indemnización por antigüedad y se derogaron varias multas por trabajo no registrado. Cada caso debe analizarse según la fecha del despido y el convenio aplicable."),
        ("¿La indemnización se cobra en bruto o en neto?",
         "La indemnización por antigüedad, el preaviso y la integración no tienen descuentos de aportes. Los días trabajados, el aguinaldo y las vacaciones sí pueden tenerlos. Por eso el monto que figura en el recibo puede ser algo menor que el total de la calculadora."),
        ("¿Qué pasa si me despidieron durante el período de prueba?",
         "En general no corresponde la indemnización por antigüedad, pero sí el preaviso de 15 días, los días trabajados, el aguinaldo y las vacaciones proporcionales."),
        ("¿Cuánto tiempo tiene el empleador para pagar la liquidación final?",
         "La ley prevé que se abone dentro de los cuatro días hábiles posteriores a la finalización de la relación laboral."),
        ("¿Cómo se calcula la indemnización de la ART?",
         "Por una incapacidad permanente, la fórmula general es 53 × ingreso base mensual × porcentaje de incapacidad × 65 / edad. Si el accidente ocurrió en el lugar de trabajo, se suma un adicional del 20 %. Además existen montos mínimos que se actualizan periódicamente."),
    ],
}

SUCESION = {
    "slug": "cuanto-cuesta-una-sucesion",
    "title": "¿Cuánto cuesta una sucesión en CABA? Costos y plazos",
    "description": "Cuánto cuesta y cuánto tarda una sucesión en CABA: honorarios, tasa de justicia, edictos e inscripción. Cuándo es obligatoria y qué es el tracto abreviado.",
    "h1": "¿Cuánto cuesta una sucesión en Buenos Aires?",
    "lead": "Te explicamos de qué se compone el costo de una sucesión, cuánto suele tardar, cuándo es obligatoria y cómo se puede vender una casa heredada con el tracto abreviado.",
    "costos": [
        ("Honorarios del abogado",
         "Se calculan sobre el valor de los bienes de la herencia según la ley de honorarios, aunque pueden acordarse por escrito antes de empezar. En el estudio te pasamos un presupuesto cerrado según tu caso."),
        ("Tasa de justicia",
         "Es un impuesto que se paga al iniciar o durante el juicio sucesorio. Se calcula como un porcentaje del valor de los bienes, según las reglas que fija la ley."),
        ("Publicación de edictos",
         "La sucesión se publica en el Boletín Oficial para convocar a posibles herederos y acreedores. Tiene un costo fijo por publicación."),
        ("Informes y certificados",
         "Informes de dominio e inhibiciones, certificados del Registro de la Propiedad y otros trámites registrales necesarios para avanzar."),
        ("Inscripción de los bienes",
         "Una vez dictada la declaratoria de herederos, se inscriben los inmuebles, vehículos u otros bienes a nombre de los herederos, con sus aranceles."),
        ("Escribano, si se vende",
         "Si los herederos venden un inmueble, la escritura la hace un escribano. Con el tracto abreviado se puede vender sin inscribirlo antes a nombre de los herederos."),
    ],
    "factores": [
        "El valor y la cantidad de bienes: no cuesta lo mismo una sucesión con una casa que con varios inmuebles, autos y cuentas.",
        "Si los herederos están de acuerdo y actúan con un mismo abogado.",
        "Si hay testamento.",
        "Si la documentación está completa (partidas, títulos, datos de los bienes).",
        "Si se van a inscribir los bienes o se van a vender con tracto abreviado.",
    ],
    "etapas": [
        ("Inicio", "Presentación de la partida de defunción, las partidas que acreditan el vínculo y la información de los bienes."),
        ("Edictos", "Publicación en el Boletín Oficial para que se presenten otros posibles herederos o acreedores."),
        ("Declaratoria de herederos", "El juez reconoce quiénes son los herederos. Si hay testamento, se analiza su validez."),
        ("Inventario e inscripción", "Se determinan los bienes y se inscriben a nombre de los herederos, o se venden con tracto abreviado."),
    ],
    "faqs": [
        ("¿Cuánto cuesta una sucesión de una casa?",
         "Depende principalmente del valor del inmueble, porque tanto la tasa de justicia como los honorarios se calculan en función de ese valor. A eso se suman gastos fijos como edictos, informes e inscripción. Con los datos del inmueble te podemos pasar un presupuesto por escrito."),
        ("¿Cuánto tarda una sucesión?",
         "Cuando los herederos están de acuerdo y la documentación está completa, una sucesión simple suele resolverse en algunos meses. Si hay conflictos, testamento o muchos bienes, puede llevar más tiempo. Los plazos también dependen del juzgado."),
        ("¿Es obligatorio hacer la sucesión?",
         "No hay un plazo breve para iniciarla, pero sin sucesión los herederos no pueden vender, transferir ni inscribir a su nombre inmuebles, autos o fondos de la persona fallecida. El derecho a aceptar la herencia caduca a los diez años."),
        ("¿Qué es el tracto abreviado?",
         "Es un mecanismo que permite a los herederos vender un inmueble de la sucesión directamente al comprador, sin inscribirlo antes a su nombre. Ahorra tiempo y algunos gastos de inscripción."),
        ("¿Se puede vender una casa heredada sin hacer la sucesión?",
         "No. Primero hay que iniciar la sucesión y obtener la declaratoria de herederos. Después se puede vender con tracto abreviado, sin necesidad de inscribir el inmueble a nombre de los herederos."),
        ("¿Quién paga los gastos de la sucesión?",
         "En general los herederos, en proporción a lo que reciben. Muchas veces se acuerda pagarlos con el producto de la venta de los bienes."),
    ],
}
