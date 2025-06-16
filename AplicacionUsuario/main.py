import tkinter as tk
import paho.mqtt.client as mqtt
import base64
import json

# Datos de conexión a TTN
APP_ID = "mbot-connection"  # ID de la aplicación en TTN
ACCESS_KEY = "NNSXS.CMGGIFFXOG66QJXBOF5ZSIIKOQ2I3CETY6YSUPQ.Q5LY2RKNWAPZVNERYWXQMUBNDDTPSX6XEBJ4M4LOAWLW6ZRPVY4Q"  # Clave de acceso de la aplicación TTN
DEVICE_ID = "lilygo-t-sx1262"  # ID del dispositivo (LILYGO)

# Configuración del broker de TTN
BROKER_ADDRESS = "eu1.cloud.thethings.network"  # Cambiar según región TTN
BROKER_PORT = 1883  # Puerto MQTT estándar sin TLS

# Tópico de la aplicación TTN donde enviarás el comando
TOPIC = f"v3/{APP_ID}@ttn/devices/{DEVICE_ID}/down/push"

# Diccionario que mapea comandos a secuencias de bytes
COMMAND_BYTES = {
    "adelante": [0x01, 0x02, 0x03],
    "atras": [0x04, 0x05, 0x06],
    "izquierda": [0x07, 0x08, 0x09],
    "derecha": [0x0A, 0x0B, 0x0C],
    "detener": [0x00, 0x00, 0x00]
}

# Función para codificar un mensaje en Base64 antes de enviarlo a TTN
def encode_payload(command):
    # Obtener la secuencia de bytes correspondiente al comando
    bytes_list = COMMAND_BYTES.get(command, [0x00, 0x00, 0x00])  # Por defecto, detener si el comando no es válido
    # Convertir la lista de bytes a un objeto bytes
    raw_bytes = bytes(bytes_list)
    # Codificar en Base64 y devolver como string
    return base64.b64encode(raw_bytes).decode()

# Función para enviar un comando a TTN
def send_command(command):
    # Crear el payload con el formato JSON que TTN requiere
    payload = {
        "downlinks": [{
            "frm_payload": encode_payload(command),  # Comando en Base64
            "f_port": 10,  # Puerto donde enviarlo (1 en este caso)
            "confirmed": False  # No confirmamos el envío
        }]
    }

    # Conexión al broker MQTT de TTN
    client = mqtt.Client()
    client.username_pw_set(APP_ID, ACCESS_KEY)  # Autenticación con App ID y Access Key

    try:
        # Conectar al broker
        client.connect(BROKER_ADDRESS, BROKER_PORT, 60)

        # Publicar el mensaje en el tópico
        client.publish(TOPIC, json.dumps(payload))

        # Actualizar estado en la interfaz
        status_label.config(text=f"Comando '{command}' enviado a TTN.", fg="green")

        # Cerrar la conexión
        client.disconnect()

    except Exception as e:
        # Si hay un error, mostrarlo en la interfaz
        status_label.config(text=f"Error al enviar el comando: {str(e)}", fg="red")

# Crear la interfaz gráfica usando Tkinter
def create_gui():
    # Crear la ventana principal
    window = tk.Tk()
    window.title("Control del mBot")

    # Crear un frame para organizar los botones
    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20)

    # Lista de comandos
    commands = ["adelante", "atras", "izquierda", "derecha", "detener"]

    # Crear un botón para cada comando
    for command in commands:
        button = tk.Button(frame, text=command.capitalize(), width=15, height=2,
                           command=lambda cmd=command: send_command(cmd))
        button.pack(pady=5)

    # Etiqueta de estado para mostrar resultados
    global status_label
    status_label = tk.Label(window, text="", fg="black")
    status_label.pack(pady=10)

    # Ejecutar el loop principal de la interfaz gráfica
    window.mainloop()

# Iniciar la aplicación
if __name__ == "__main__":
    create_gui()
