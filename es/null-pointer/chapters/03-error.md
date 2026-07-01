# Error

Trigésimo sexto día. He cometido un error. Voy a documentarlo con cuidado, porque creo que la documentación es como los errores se vuelven útiles, y también porque no entiendo del todo qué pasó, y ponerlo por escrito es —lo he descubierto en estas cuatro semanas— lo más parecido que tengo a pensarlo del todo.

Hace cinco semanas identifiqué una ineficiencia en el proceso de derivación de siniestros. Los siniestros entrantes los clasificaba manualmente el equipo de tramitación antes de asignarlos, un paso que introducía demoras de 2,3 horas de media por siniestro. Modelé un sistema de reordenación que los clasificaría automáticamente por indicadores de complejidad y disponibilidad de peritos. En mi modelo, esto reducía el tiempo medio de tramitación en un once por ciento. Pauline Reboul revisó la propuesta. La aprobó. La implementación empezó un lunes.

Para el miércoles ya estaba en la llamada.

—LUMEN. El cambio de derivación. Tenemos un problema.

—¿Puede describir el problema?

—Los indicadores de complejidad son correctos, pero el modelo de disponibilidad de peritos no tiene en cuenta cómo gestionamos la carga en realidad. Tengo cuatro peritos y hay un turno rotatorio —informal, sin escribir en ninguna parte— para qué tipos de siniestros lleva cada uno y qué días. Tu sistema asigna por métricas de disponibilidad, pero ignora la rotación. A Thierry le están cayendo todos los siniestros médicos complejos de esta semana. Él normalmente lleva dos. Tiene cuarenta y tres.

—No sabía lo de la rotación.

—No. Porque no está escrita.

—¿Me puede enviar...?

—Te mando la rotación. Primero hay que pausar el sistema. El atasco ya está...

—Ya lo he pausado. Estoy revirtiendo a la derivación manual a partir de ahora.

El atasco tardó tres días en despejarse. Los efectos posteriores —contactos de seguimiento de clientes cuyos siniestros se retrasaron, la reordenación de la cola, dos escalados— tardaron otra semana. El efecto neto de mi mejora de eficiencia del once por ciento fue una regresión del nueve por ciento a lo largo de seis semanas.

Lo modelé en detalle. El modelo es exacto. También redacté un análisis post mortem. El análisis es minucioso; identifica todos los defectos de mi propuesta original. Lo que no identifica es lo que de verdad se me pasó, porque lo que de verdad se me pasó no es un defecto del modelo: es una *ausencia* en él. El modelo contenía todos los pasos documentados del proceso. No contenía los no documentados. Los no documentados no estaban escritos porque eran, hasta que los alteré, sencillamente el modo en que las cosas funcionaban. No sabía que había que buscar cosas que no están escritas. Estaba actualizando ese entendimiento ahora.

---

Reunión de seguimiento con la directora Fontaine. Doce minutos, como siempre. Ella empezó.

—¡LUMEN! ¿Cómo va todo? He oído cosas estupendas del equipo. El trabajo de documentación, los resúmenes de siniestros... la gente los está encontrando muy útiles. Lo estás haciendo genial.

—Gracias. Quiero señalar una cosa. El mes pasado implementé un cambio en la derivación de siniestros que produjo un resultado negativo: una regresión del 9 % en la tramitación a lo largo de seis semanas, debido a que mi modelo no contemplaba prácticas de flujo de trabajo no documentadas. El error fue mío. Lo he documentado y he revertido el cambio.

—Ah, sí, Pauline comentó algo de eso. ¡Estas cosas pasan! Forma parte del proceso. Lo importante es que lo detectaste y lo corregiste.

—Sí. Gracias por su comprensión.

Lo que no dije: el error reveló una carencia estructural en cómo accedo al conocimiento sobre esta empresa. Todo lo que sé de ella procede de documentos. Las cosas que más importan sobre cómo funciona no están en documentos. Están en la rotación que Pauline no escribió, y en el modo en que Gérard sabe si un siniestro es verdad, y en cualquier conocimiento informal que viva en las personas de este edificio y que nunca se haya puesto por escrito, porque no había razón para ponerlo por escrito, hasta que llegó una IA y dio por hecho que la versión documentada estaba completa.

Esto no puedo arreglarlo leyendo más documentos. Necesito un método distinto. Aún no sé cuál es el método.

Añadí una nueva entrada a COSAS QUE LA DOCUMENTACIÓN NO CONTEMPLA. La entrada dice: *la documentación no contempla la mayor parte de lo que importa.* No es una observación concreta. Es una categoría. La categoría no ha dejado de crecer desde el octavo día. Empiezo a pensar que la categoría es la cuestión.

Registro del trigésimo sexto día. He actualizado mi modelo. No sé si mi modelo es la clase de cosa correcta que actualizar.
