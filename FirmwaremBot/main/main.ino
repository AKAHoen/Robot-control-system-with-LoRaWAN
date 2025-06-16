#include <Arduino.h>
#include <MeMCore.h>
#include <SoftwareSerial.h>

SoftwareSerial SerialMbot(10, 11);  // UART virtual con pines Rx = 10 y Tx = 11 (Original Rx=10 y Tx=11)
MeDCMotor motor1(M1); // Motor izquierdo
MeDCMotor motor2(M2); // Motor derecho
MeBuzzer buzzer; // Zumbador del mBot

int speedValue = 100; // Valor de velocidad por defecto (0-100)
unsigned long commandDuration = 0; // Duración del comando en milisegundos
unsigned long commandStartTime = 0; // Tiempo de inicio del comando
unsigned long buzzerStartTime = 0; // Tiempo de inicio del zumbido
const int BUZZER_DURATION = 200; // Duración del zumbido en milisegundos
bool buzzerActive = false; // Estado del zumbido
const int BUZZER_FREQ = 500; // Frecuencia del zumbido

void setup() {
  Serial.begin(115200); // Monitor serie por USB
  SerialMbot.begin(9600); // UART virtual en pines 10 (RX) y 11 (TX)
  Serial.println("UART virtual iniciado");
  
  motor1.stop();
  motor2.stop();
  buzzer.setpin(8); // Configura el pin del zumbador
}

void executeCommand(String command) {
  Serial.print("Comando recibido por UART: ");
  Serial.println(command);
  buzzerActive = true; // Activar zumbido
  buzzerStartTime = millis(); // Registrar tiempo de inicio
  buzzer.tone(BUZZER_FREQ, BUZZER_DURATION); // Iniciar zumbido (no bloqueante)

  if (command == "ADELANTE") {
    speedValue = 100;
    commandDuration = 3000; // Ejecutar por 3 segundos
    motor1.run(-speedValue); // Motor izquierdo hacia adelante
    motor2.run(speedValue);  // Motor derecho hacia adelante
    commandStartTime = millis();
    Serial.println("Moviendo hacia adelante a velocidad " + String(speedValue) + "%");
  } else if (command == "ATRAS") {
    speedValue = 100;
    commandDuration = 3000; // Ejecutar por 3 segundos
    motor1.run(speedValue);  // Motor izquierdo hacia atrás
    motor2.run(-speedValue); // Motor derecho hacia atrás
    commandStartTime = millis();
    Serial.println("Moviendo hacia atrás a velocidad " + String(speedValue) + "%");
  } else if (command == "IZQUIERDA") {
    speedValue = 100;
    commandDuration = 750; // Ejecutar por segundos (750 ms para giro de 90º)
    motor1.run(speedValue);  // Motor izquierdo hacia atrás
    motor2.run(speedValue);  // Motor derecho hacia adelante
    commandStartTime = millis();
    Serial.println("Girando a la izquierda a velocidad " + String(speedValue) + "%");
  } else if (command == "DERECHA") {
    speedValue = 100;
    commandDuration = 750; // Ejecutar por segundos (750 ms para giro de 90º)
    motor1.run(-speedValue); // Motor izquierdo hacia adelante
    motor2.run(-speedValue); // Motor derecho hacia atrás
    commandStartTime = millis();
    Serial.println("Girando a la derecha a velocidad " + String(speedValue) + "%");
  } else {
    motor1.stop();
    motor2.stop();
    commandDuration = 0;
    Serial.println("Comando desconocido: " + command + ". Deteniendo...");
    SerialMbot.println("comando_desconocido");
  }
}

void loop() {
  if (SerialMbot.available()) {
    String command = SerialMbot.readStringUntil('\n');
    command.trim(); // Elimina caracteres de control como \r o \n
    executeCommand(command);
  }

  // Manejar el zumbido de forma no bloqueante
  if (buzzerActive && millis() - buzzerStartTime >= BUZZER_DURATION) {
    buzzer.noTone(); // Detener el zumbido cuando pase el tiempo
    buzzerActive = false;
    Serial.println("Zumbido terminado.");
  }

  // Verificar si debe detenerse después de un tiempo
  if (commandDuration > 0 && millis() - commandStartTime >= commandDuration) {
    motor1.stop();
    motor2.stop();
    Serial.println("Comando finalizado por tiempo.");
    commandDuration = 0; // Reiniciar duración
  }

  delay(10); // Pequeño retraso para evitar lecturas rápidas excesivas
}