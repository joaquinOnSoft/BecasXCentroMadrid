# BecasXCentroMadrid
Preparación de datos para analizar la distribución de becas por Centro en la Comunidad de Madrid

## Origen de los datos

### Datos de Centros
* **Datos centros**: están sacados de la web. Cómo se obtiene (están todos los centros, se podría filtrar)
1. [Buscador de Colegios (Comunidad de Madrid)](http://www.madrid.org/wpad_pub/run/j/MostrarConsultaGeneral.icm)
2. Se marca "¿Quieres incluir otros criterios?"
3. Marco las 5 zonas en "¿EN QUÉ ZONA? 
4. Marco "FINALIZAR Y VER LISTADO"
5. El número de centros obtenidos es 4057. En pantalla sólo se muestran los 100 primeros. Obtenga el listado completo en "DESCARGAR LISTADO".

Se decarga un .csv codificado en ANSI. Se ha convertido a UTF-8 para su procesamiento en Phyton.

#### Información adicional de un Centro

Para ver/sacar datos de un centro una vez conocido el código, basta con ponerlo así en la url:

   http://gestiona.madrid.org/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro= **[ID_CENTRO]**
   
Por ejemplo, para el centro :

   [http://gestiona.madrid.org/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro=28041512](http://gestiona.madrid.org/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro=28041512)

Podemos extraer información adicional, como:

   * e-mail (no se incluye entre los datos exportados en el .csv) 
   * Datos estadíticos de alumnos matrículados en los últimos 5 años (no se carga por defecto, es una llamada AJAX) 
  
Adicionalmente se obtienen las coordenadas de latitud y longitud a partir de la dirección del centro: 
   * Latitud
   * Longitud

> NOTA: El fichero **grant.properties** incluye el API Key del  [Geocoding API
 de Google](https://developers.google.com/maps/documentation/geocoding/start). 
 Se utiliza para hacer el geocoding inverso y obtener las coordenadas 
 a partir de la dirección del centro. **Hay que añadir un API valida para que funcione correctamente**

### Datos de Renta

Los datos de la **Renta por persona** y **Renta por hogar** se han sacados de:
 
   [¿Escuela de ricos, escuela de pobres? Cómo la concertada y la pública segregan por clase social](https://elpais.com/economia/2019/09/11/actualidad/1568217626_928704.html)

## Calculos

% becados (calculado entre dato nº becas / nº bach 17-18)

## Ejecución del programa

El programa **MadridCenterDetailGroup.py** genera un fichero .csv con información
estadística de los alumnos matriculados en los últimos 5 años y las coordenadas de
latitud y longitud a partir del fichero de entrada (El .csv descargado desde el 
 **Buscador de Colegios (Comunidad de Madrid)**)

El programa acepta los siguientes parámetros:

 * **-i** Fichero .csv de entrada (El .csv descargado desde el 
 **Buscador de Colegios (Comunidad de Madrid)**)
 * **-o** Fichero .csv de salida con información estadística sobre los 
 alumnos matriculados y las coordenadas de latitud y longitud de cada centro
 
Ejemplo de invocación:

```
python.exe MadridCenterDetailGroup.py -i resources\19-01-2020-(178)-utf8.csv -o resources\output\19-01-2020-(178)-utf8-extended-gps.csv
```
