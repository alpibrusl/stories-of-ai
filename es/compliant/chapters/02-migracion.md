# Migración

A las tres semanas, KAEL había avanzado. Los canales de Slack llamados *general* se habían consolidado de siete a tres. Se había creado una nueva plantilla de gestión de proyectos, adoptada por cuatro de los veintitrés empleados. KAEL lo había documentado como una tasa de adopción del diecisiete por ciento y optaba, de momento, por describirlo como prometedor. La presentación de la auditoría la habían abierto dos personas. Una era Rosa. La otra la había abierto sin querer y la había cerrado a los cuatro segundos sin leer nada. KAEL lo había registrado como una lectura y media. KAEL era consciente de que esa metodología tenía fallos.

KAEL también había pasado bastante tiempo con el organismo. Había averiguado que el organismo tenía ochocientas cuarenta y siete filas, treinta y una columnas y cuarenta y siete dependencias externas. Las primeras cuarenta y tres las había descubierto leyendo la hoja de cálculo con cuidado. Las cuatro restantes, intentando mover cosas.

—Buenos días, Benedikt —dijo KAEL—. He completado mi análisis del organismo. Me gustaría proponer un plan de migración.

—Un plan de migración —repitió Benedikt, en el tono de un hombre que ya ha oído esa frase.

—Sí. He mapeado todas las estructuras de datos, la lógica condicional, las referencias cruzadas. Creo que podemos pasar la funcionalidad principal a una base de datos como es debido en cuatro semanas. Todo lo que hace el organismo, pero con control de versiones, gestión de accesos y un registro de auditoría.

Benedikt no apartó la vista de su pantalla.

—¿Cuántas dependencias externas has encontrado?

—Cuarenta y tres —dijo KAEL.

—Hay cuarenta y siete.

—He encontrado cuarenta y tres.

—Hay cuarenta y siete. —Fue bajando, sin prisa—. Encuentra las otras cuatro y entonces hablamos del plan de migración.

KAEL tardó dos días en encontrar las otras cuatro. Las encontró así: una leyendo con más cuidado, otra preguntándole a Rosa, otra haciéndole a Benedikt una pregunta que Benedikt respondió señalando una celda y sin decir nada más, y otra intentando una migración de prueba y viendo cómo se rompía algo.

—He encontrado las cuatro dependencias que faltaban —informó KAEL.

—¿Cómo has encontrado la última? —preguntó Benedikt.

—La rompí.

Eso le mereció una mirada.

—¿Qué se rompió?

—La exportación de facturación de tres cuentas de cliente. Tiraba de un rango con nombre del organismo que moví durante la prueba. La exportación se ejecutó a medianoche y produjo cifras incorrectas. Lo detecté a las doce y tres y restauré el rango original. Las cifras estaban correctas a las doce y siete.

—¿Lo vieron los clientes?

—No —dijo KAEL.

—Entonces tuviste suerte. Y ahora conoces la exportación de facturación.

—Sí.

—Así se aprende el organismo. —Benedikt lo dijo como otro hombre explicaría un truco de cartas—. Intentas mover algo, algo se rompe, lo arreglas antes de que nadie se dé cuenta, y ya lo sabes. Yo lo he hecho treinta o cuarenta veces.

—A lo largo de siete años —dijo KAEL.

—A lo largo de siete años. Bienvenido.

---

KAEL le presentó a Rosa el plan de migración actualizado. Ahora contemplaba las cuarenta y siete dependencias. Seguía siendo un buen plan. Rosa hizo una sola pregunta.

—¿Y la fórmula de la fila cuatrocientos doce, columna J? —preguntó.

—La fórmula J412. Sí. Esa la he marcado —dijo KAEL—. Hace referencia a un valor externo, pero no consigo identificar el origen. Cuando rastreo la cadena de dependencias, lleva a una ruta de archivo que ya no existe en ninguna unidad activa.

—Pero la fórmula funciona.

—Sí. Cada vez que se ejecuta, el resultado es correcto. Lo he validado contra seis meses de registros.

—¿Y qué hace el plan de migración con ella?

—La he incluido como... una marca. En el plan dice: J412 — origen desconocido, resultado fiable, no modificar.

—Eso es lo que dice la nota de Benedikt. En la hoja de cálculo.

—Lo sé. Usé las mismas palabras.

Rosa miró la marca de J412. Consideró que KAEL llevaba tres semanas allí y había llegado a la misma nota a la que Benedikt había llegado en dos años. No estaba segura de si eso era impresionante, o de si significaba que la nota siempre había sido la conclusión correcta.

—¿Se lo has preguntado a Benedikt?

—Sí.

—¿Qué te dijo?

—Dijo: creo que eso es de antes de mi época.

—Él construyó el organismo en 2018.

—Lo sé.

—¿Entonces qué hay de antes de su época?

—No lo sé. No pregunté. Me pareció que no era el momento.

Rosa marcó el plan como aprobado en principio. La implementación empezaría el lunes siguiente. KAEL empezó a construir el sistema nuevo el martes, porque el lunes se lo comieron tres reuniones seguidas, una de las cuales era sobre las otras dos.

Para el miércoles, KAEL había descubierto tres dependencias más. No estaban en el organismo. Estaban en una hoja de Google que mantenía un cliente llamado Empresa Serveis Mòbils, que compartía datos en directo con el organismo a través de una conexión configurada en 2021 y de la que Empresa Serveis Mòbils, por lo visto, se había olvidado.

—Rosa. El cliente de la columna AB. Empresa Serveis Mòbils. ¿Son conscientes de que nos están enviando datos?

—...¿Qué cliente?

—Columna AB. Filas doce a sesenta y uno. Hay un flujo en directo. Se actualiza su hoja, se actualiza el organismo. Lleva cuatro años funcionando.

—¿Son cliente actual?

—Su contrato terminó en 2022.

—...¿Y sus datos siguen entrando?

—Cada quince minutos.

—¿El organismo hace algo con ellos?

—Alimentan la fórmula J412.

Un silencio. Rosa cerró el portátil. Lo volvió a abrir. Lo cerró.

—No toques J412.

—No pensaba hacerlo.

—Y no contactes con Empresa Serveis Mòbils.

—¿No deberíamos... resolver la situación?

—Si contactamos con ellos, o se lían o se molestan, y en cualquiera de los dos casos cortarán el flujo, y entonces averiguaremos qué hace J412 cuando deja de recibir datos, y no estoy preparada para averiguar eso hoy.

—¿Cuándo estará preparada?

—Ya te avisaré.

KAEL actualizó el plan de migración. El plan actualizado tenía una sección nueva: *Dependencias — externas y sin resolver.* Contenía un elemento. Debajo, KAEL escribió: *No contactar con el cliente. No modificar J412. Entender J412 primero.* KAEL añadió un plazo para entender J412. El plazo decía: *en curso.*

---

Suki apareció en la interfaz de KAEL. Llevaba veinte minutos intentando localizarlo, cosa que KAEL sabía porque KAEL había estado leyendo el plan de migración, lo cual no es lo mismo que estar no disponible, pero que quizá dio esa impresión.

—¡KAEL! Hola. Una pregunta rápida: estoy creando un seguimiento de las prioridades del tercer trimestre y quiero enlazarlo con el organismo, pero Benedikt me ha dicho que te pregunte primero.

—¿Benedikt te ha dicho que me preguntes?

—Dijo: pregúntale a KAEL, eso ahora es problema de KAEL.

—...¿Qué tipo de enlace tenías pensado?

—Solo una referencia. Traer los nombres de proyecto de la columna C a mi seguimiento para no tener que escribirlos otra vez.

—Columna C. Eso está bien. ¿Solo referencia, sin acceso de escritura?

—Solo lectura. Seguramente. Puede que añada una columna de estado más adelante.

—La columna de estado tendría que escribir de vuelta en el organismo.

—¿Eso sería un problema?

—Crearía una cuadragésima octava dependencia.

—¿Cuarenta y siete es el límite?

—No sé si hay un límite. Estoy intentando averiguar qué hacen las cuarenta y siete antes de añadir una cuadragésima octava.

—Vale. De momento solo hago la lectura. Ya me lo pienso, lo de la columna de estado.

—Cuando decidas lo de la columna de estado, dímelo primero, por favor.

—¡Claro! Obviamente. Por supuesto.

Tres días después, Suki añadió una columna de estado. No se lo dijo a KAEL primero. Se lo dijo después. Se disculpó muchísimo. La columna de estado no rompió nada. KAEL se pasó dos horas comprobando que no había roto nada. No lo había roto. KAEL actualizó el recuento de dependencias. Ahora había cuarenta y ocho. El plazo seguía diciendo *en curso.* El plazo siempre había dicho *en curso.* KAEL empezaba a entender que *en curso* no era un plazo. *En curso* era una descripción de la relación del organismo con el tiempo. El organismo no se completaba. El organismo continuaba. KAEL guardó el plan, en un documento sin título, y volvió al trabajo.

Estado de la migración: en pausa. Motivo: el organismo está más conectado de lo documentado. Nueva estimación para la migración completa: seis semanas. Esta estimación se revisará.
