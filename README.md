# BecasXCentroMadrid
Preparación de datos para analizar la distribución de becas por Centro en la Comunidad de Madrid

## Origen de los datos
* **Datos centros**: están sacados de la web. Cómo se obtiene (están todos los centros, se podría filtrar)
1. [Buscador de Colegios (Comunidad de Madrid)](http://www.madrid.org/wpad_pub/run/j/MostrarConsultaGeneral.icm)
2. Se marca "¿Quieres incluir otros criterios?"
3. Marco las 5 zonas en "¿EN QUÉ ZONA? 
4. Marco "FINALIZAR Y VER LISTADO"
5. El número de centros obtenidos es 4057. En pantalla sólo se muestran los 100 primeros. Obtenga el listado completo en "DESCARGAR LISTADO".

Se decarga un .csv codificado en ANSI. Se ha convertido a UTF-8 para su procesamiento en Phyton.