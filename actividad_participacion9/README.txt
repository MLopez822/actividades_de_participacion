ANTES DE LA EXPLICACION DEL CODIGO QUIERO DECIRLE QUE LO INTENTE 
PERO NO PUDE NO ENTENDI PORQUE NO FUNCIONA ESPERO LO REVISE Y ME
CORRIJA 

EXPLICACION DEL CODIGO
Importaciones

Counter: Se importa de la biblioteca collections. Esta clase se utiliza para contar elementos hashables en una colección,
lo que es útil para determinar la dirección predominante del viento.
Tuple: Se importa de la biblioteca typing para especificar el tipo de retorno de la función ProcesarDatos.

Clase DatosMeteorologicos

Se define una clase llamada DatosMeteorologicos.
Atributo de Clase
Este es un diccionario que mapea las direcciones del viento (como "N", "NE", "E", etc.) a sus respectivos ángulos en grados. 
Esto puede ser útil para análisis posteriores.

Constructor

El método __init__ es el constructor de la clase, que se ejecuta cuando se crea una instancia de DatosMeteorologicos. 
Toma un parámetro nombre_archivo (una cadena que representa la ruta al archivo que contiene los datos meteorológicos) y lo 
almacena como un atributo de instancia.

Método ProcesarDatos
Este método se encarga de procesar los datos del archivo y calcular promedios de diferentes variables meteorológicas. 
Se especifica que devuelve una tupla con cuatro valores de tipo float y uno de tipo str.

Inicialización de Variables

Se inicializan variables para almacenar la suma de las temperaturas, humedad, presión, velocidad del viento y una lista 
para almacenar las direcciones del viento. También se inicializa un contador para los registros.

Lectura del Archivo

Se abre el archivo en modo lectura y se itera sobre cada línea del archivo.

Procesamiento de Cada Línea

Para cada línea que contiene "Temperatura", se incrementa el contador de registros. Luego, se extraen y convierten a 
float los valores de temperatura, humedad, presión y velocidad del viento. La dirección del viento se extrae y se limpia de espacios.

Suma de Datos

Se suman los valores extraídos a sus respectivas variables y se agrega la dirección del viento a la lista.

Cálculo de Promedios

Se calculan los promedios dividiendo las sumas acumuladas por el número de registros, asegurándose de evitar la división por cero.

Cálculo de la Dirección Predominante del Viento

Counter(direcciones_viento): Se crea un objeto Counter que cuenta la ocurrencia de cada dirección del viento almacenada en la lista 
direcciones_viento.
most_common(1): Este método devuelve una lista de los elementos más comunes y sus conteos. En este caso, se obtiene la dirección 
del viento que más veces aparece (la más común).
[0][0]: Se accede al primer elemento de la lista devuelta, que es una tupla con la dirección predominante y su conteo. 
Se extrae solo la dirección.
Si no hay direcciones de viento registradas, se establece direccion_predominante como una cadena vacía.

Retorno de Resultados

Finalmente, el método devuelve una tupla con los promedios de temperatura, humedad, presión, velocidad del viento y 
la dirección predominante del viento.