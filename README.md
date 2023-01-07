# BecasXCentroMadrid
Preparación de datos para analizar la distribución de becas por Centro en la Comunidad de Madrid

> **NOTA**: La Comunidad de Madrid ha cambiado el dominio que utiliza a finales de 2022. 
> Antes utilizaba la URL **gestiona3.madrid.org**, ahora 
> utiliza el dominio **gestiona.comunidad.madrid**

## Origen de los datos

### Datos de Centros
* **Datos centros**: están sacados de la web. Cómo se obtiene (están todos los centros, se podría filtrar)
1. [Buscador de Colegios (Comunidad de Madrid) (A partir de 2023)](https://gestiona.comunidad.madrid/wpad_pub/run/j/MostrarConsultaGeneral.icm)
2. Se marca `¿Quieres incluir otros criterios?`
3. Marco las 5 zonas en `¿EN QUÉ ZONA?` 

![Buscador de Colegio - ¿EN QUÉ ZONA?](images/buscador-de-colegios-en-que-zona.png)

5. Marco `FINALIZAR Y VER LISTADO`

![Buscador de Colegio - Finalizar y ver listado](images/buscador-de-colegios-finalizar-y-ver-resultados.png)

6. El número de centros obtenidos es 4032, 23 centros menos que en Enero de 2019 (4057). En pantalla splo se muestran los 100 primeros. Obtenga el listado completo en `DESCARGAR LISTADO`.

Se decarga un .csv codificado con `windows 1252`. Se ha convertido a `UTF-8` para su procesamiento en Phyton.

También se elimina la primera línea del fichero, ya que no aporta información útil. Es esta:

```
CONSULTA DE CENTROS Y SERVICIOS EDUCATIVOS;;;;;;;;;;;;;;
```

Así el fichero resultante tiene este aspecto:

```
AREA TERRITORIAL;CODIGO CENTRO;TIPO DE CENTRO;CENTRO;DOMICILIO;MUNICIPIO;DISTRITO MUNICIPAL;COD. POSTAL;TELEFONO;FAX;EMAIL;EMAIL2;TITULARIDAD
Madrid-Oeste;28060646;EEI;ACHALAY;Avenida De Isabel De Farnesio, 14 ;Boadilla del Monte;-;28660;916326518;-;eei.achalay.boadilla@educa.madrid.org;achalay-@hotmail.com;Público;
Madrid-Este;28063027;EEI;ACUARELA;Avenida Del Somorrostro, 193 ;San Fernando de Henares;-;28830;916694580;-;eei.acuarela.sanfernando@educa.madrid.org;-;Público;

...

```

#### Información adicional de un Centro

Para ver/sacar datos de un centro una vez conocido el código, basta con ponerlo así en la url:

   https://gestiona.comunidad.madrid/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro= **[ID_CENTRO]**
   
Por ejemplo, para el centro:

   [https://gestiona.comunidad.madrid/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro=28041512](https://gestiona.comunidad.madrid/wpad_pub/run/j/MostrarFichaCentro.icm?cdCentro=28041512)

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
python.exe MadridCenterDetailGroup.py -i resources\07-01-2023-(408)-utf8.csv -o resources\output\07-01-2023-(408)-utf8-extended-gps.csv
```
