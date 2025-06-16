# Robot-control-system-with-LoRaWAN

Este proyecto se ha basado en el repositorio de jorgenavarroortiz (https://github.com/jorgenavarroortiz/t-beam-lorawan) para conectar la placa Lilygo T-Beam con módulo SX1262 a TTN y enviar la posición de la misma y se ha modificado para interpretar mensajes recibidos desde TTN y realizar un comunicación UART para enviar los mensajes recibidos. También se ha desarrollado una aplicación de usuario en Python con una interfaz gráfica para enviar instrucciones y se ha programado un mBot para que sea capaz de recibir las instrucciones por UART de la mota e interpretarlas para realizar acciones.

Manual de usuario
1.	Descargar los firmwares: Accede al repositorio de mi github personal [34] para descargar todo el contenido del proyecto.
2.	Configuración de TTN: Seguir los pasos que se han realizado en el apartado 4.3 para configurar TTN.
3.	Preparar los entornos de programación: Descargar las librerías necesarias para que funciones el firmware de todos los dispositivos.
4.	Configuración de la aplicación de usuario: En el firmware de la aplicación de usuario, cambiar el valor de las variables de acuerdo a los dispositivos que se vayan a utilizar y a la configuración de TTN. No hay que olvidar generar la clave para utilizar la integración MQTT de TTN.
5.	Configuración del gateway: En el firmware del gateway modificar las variables necesarias como la lista de dispositivo añadir la red WiFi a la que se conecte el gateway para recibir una IP fija.
6.	Configuración de la mota: En el firmware de la mota, escribir en el archivo credentials.h las credenciales que se necesiten según se utilice OTAA o ABP y cambiar los parámetros del archivo configuration.h según la placa que se utilice y necesidades de red.
7.	Compilar firmwares: Compilar los firmwares en el dispositivo correspondiente para que empiecen a ponerse en marcha.
8.	Monitorizar del entorno: Para comprobar que todo funciona, monitorizar la consola de TTN para verificar la recepción y envío de mensajes por la red LoRaWAN y utilizar las herramientas de depuración para comprobar que la comunicación UART entre la mota y el mBot funciona.

Gestión de errores:
En este apartado se van a cubrir algunos de los posibles errores que pueden surgir durante la replicación del proyecto. Los errores que se pueden encontrar con TTN son:
	- Dispositivos mal registrados: Para saber si un dispositivo no se ha registrado bien, simplemente se comprobará la consola del dispositivo. Para el gateway, si está conectado (con los LEDs que indican está              conectado a una red WiFi encendidos) pero no aparecen mensajes por su consola significa que no está bien registrado. Con los dispositivos finales será igual, aunque se puede dar el caso que por la consola del          gateway se reciban mensajes de la mota pero no aparezcan en la consola de TTN. Para solucionar estos problemas simplemente se eliminarán de TTN y se volverán a registrar los dispositivos.
  - La mota funciona una vez pero cuando se desconecta no vuelve a funcionar: Si se ha utilizado ABP, en los ajustes del dispositivo final hay que marcar la opción Resets frame counter ya que es posible que cuando se      reconecte el dispositivo su contador de tramas continúe por donde se desconectó. Con esta opción, el contador de tramas siempre se resetea cuando se conecta a TTN.

En la aplicación de usuario no hay mucho margen de error ya que lo único que hay que hacer es cambiar las variables de acuerdo a nuestra configuración con TTN. Si se ha hecho correctamente no debería de surgir ningún error.

En la configuración del gateway y sucede lo mismo. Lo único que hay que hacer es cambiar las variables y añadir la red a la que se va a conectar el gateway. Si estos pasos se realizan correctamente no debería de surgir ningún error.

Con el mBot pueden surgir errores como:
  - No funciona comunicación UART: Hay que comprobar que en el firmware se han definido bien los pines Rx y Tx y que están bien conectados todos los pines, tanto a la placa como al conversor. También hay que tener en      cuenta que, si por ejemplo se utilizan los pines digitales del lado derecho (Tienen los puertos RJ25 al lado), no se pueden utilizar los puertos RJ25.
  - Mal funcionamiento del mBot: Si el mBot no funciona correctamente, hay que comprobar que el montaje se ha realizado correctamente.
  - Arduino no detecta el puerto al que está conectado: Para poder subir código el mBot tiene que estar encendido para que se detecta el puerto al que está conectado. Tener en cuenta también que al compilar en Arduino     hay que utilizar la placa Arduino Uno.

Con la mota pueden surgir los siguientes errores:
  - Errores de compilación: Si surgen errores de compilación puede ser porque alguna librería no está bien instalada, porque se modificado algún parámetro con un valor que no puede contener o se ha utilizado la placa      que no es (hay que utilizar la placa T-Beam).
  - Compila, pero no funciona: Si se ha compilado en la placa pueden pasar dos cosas para que no funciones: la placa no ha pillado la posición GPS y por eso no envía mensajes o las credenciales del modo de activación      no son correctas y por eso no se reciben mensajes en TTN.
  - La comunicación UART no funciona: Hay que comprobar que en la configuración se han elegido pines libres para Rx y Tx y que todos los pines utilizados están bien conectados a la placa y al conversor.
