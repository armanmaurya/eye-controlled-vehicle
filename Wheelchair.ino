
// Pin definitions for L298N motor driver
const int ENA = 9;  // Enable pin for OUT1/OUT2 (Motors 1 & 2)
const int IN1 = 2;  // Control pin 1 for Motor 1
const int IN2 = 3;  // Control pin 2 for Motor 1
const int ENB = 10; // Enable pin for OUT3/OUT4 (Motors 3 & 4)
const int IN3 = 4;  // Control pin 1 for Motor 2
const int IN4 = 5;  // Control pin 2 for Motor 2

// Pin definitions for Ultrasonic Sensor
const int trigPin = 6;  // Trigger pin
const int echoPin = 11; // Echo pin

int distance;

int LedPin = 7;

unsigned long previousMillis = 0; // Stores the last time distance was measured
const long interval = 100; // Interval at which to measure distance (milliseconds)

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  // Set motor control pins as outputs
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(LedPin, OUTPUT);



  // Initialize motors to be stopped
  digitalWrite(ENA, LOW); // Disable motors 1 & 2
  digitalWrite(ENB, LOW); // Disable motors 3 & 4

  // Set the trigPin as an OUTPUT:
  pinMode(trigPin, OUTPUT);
  
  // Set the echoPin as an INPUT:
  pinMode(echoPin, INPUT);

}

void loop() {

  // Check if it's time to measure the distance
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis; // Save the last time distance was measured
    int distance = measureDistance();
    // Serial.println(distance);

    if (distance < 30) {
      stopMotors();
      digitalWrite(LedPin, HIGH);
    } else {
      digitalWrite(LedPin, LOW);
    }
  }
  // int distance = measureDistance();

  // distance = measureDistance();
  // Print the distance to the Serial Monitor:
    // Print the distance to the Serial Monitor:
  if (Serial.available() > 0) {
    String data = Serial.readString();
    // Serial.println(data);
    int dataInt = data.toInt();  // Convert String to int
    Serial.println(data);
    
    if (dataInt == 0) {
      stopMotors();
    } else if (dataInt == 1) {
      moveForward(255);
    } else if (dataInt == 2) {
      rotateLeft(255);
    } else if (dataInt == 3) {
      rotateRight(255);
    } else if (dataInt == 4) {
      moveBackward(255);
    }
  }

  // if (distance < 30) {
  //   digitalWrite(8, HIGH); // Disable motors 1 & 2
  //   stopMotors();
  // }else {
  //   digitalWrite(8, LOW); // Disable motors 1 & 2
  // }

  // delay(500);

}

// Function to measure distance using the ultrasonic sensor
int measureDistance() {
  // Clear the trigPin by setting it LOW:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Set the trigPin HIGH for 10 microseconds to send out the ultrasonic pulse:
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the time it takes for the echo to return:
  long duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance (in cm) based on the speed of sound (343 m/s):
  int distance = duration * 0.034 / 2;  // Divide by 2 for round trip

  return distance;
}

void rotateLeft(int speed) {
  // Set direction for motors connected to OUT1/OUT2 (Motors 1 & 2)
  digitalWrite(IN1, LOW); // Motor 1 forward
  digitalWrite(IN2, HIGH);
  analogWrite(ENA, speed); // Set speed for Motor 1 & 2 (PWM)


  // Set direction for motors connected to OUT3/OUT4 (Motors 3 & 4)
  digitalWrite(IN3, LOW);  // Motor 2 backward
  digitalWrite(IN4, HIGH);
  analogWrite(ENB, speed); // Set speed for Motor 3 & 4 (PWM)

}

void rotateRight(int speed) {
  // Set direction for motors connected to OUT1/OUT2 (Motors 1 & 2)
  digitalWrite(IN1, HIGH);  // Motor 1 backward
  digitalWrite(IN2, LOW);
  analogWrite(ENA, speed); // Set speed for Motor 1 & 2 (PWM)

  // Set direction for motors connected to OUT3/OUT4 (Motors 3 & 4)
  digitalWrite(IN3, HIGH); // Motor 2 forward
  digitalWrite(IN4, LOW);
  analogWrite(ENB, speed); // Set speed for Motor 3 & 4 (PWM)

}

void moveBackward(int speed) {
  // Set direction for motors connected to OUT1/OUT2 (Motors 1 & 2)
  digitalWrite(IN1, LOW); // Motor 1 forward
  digitalWrite(IN2, HIGH);
  analogWrite(ENA, speed); // Set speed for Motor 1 & 2 (PWM)

  // Set direction for motors connected to OUT3/OUT4 (Motors 3 & 4)
  digitalWrite(IN3, HIGH); // Motor 2 forward
  digitalWrite(IN4, LOW);
  analogWrite(ENB, speed); // Set speed for Motor 3 & 4 (PWM)
}


// Function to move all motors forward
void moveForward(int speed) {
  // Set direction for motors connected to OUT1/OUT2 (Motors 1 & 2)
  digitalWrite(IN1, HIGH); // Motor 1 forward
  digitalWrite(IN2, LOW);
  analogWrite(ENA, speed); // Set speed for Motor 1 & 2 (PWM)

  // Set direction for motors connected to OUT3/OUT4 (Motors 3 & 4)
  digitalWrite(IN3, LOW); // Motor 2 forward
  digitalWrite(IN4, HIGH);
  analogWrite(ENB, speed); // Set speed for Motor 3 & 4 (PWM)
}

// Function to stop all motors
void stopMotors() {
  // Stop motors on OUT1/OUT2 (Motors 1 & 2)
  digitalWrite(ENA, LOW);

  // Stop motors on OUT3/OUT4 (Motors 3 & 4)
  digitalWrite(ENB, LOW);
}
