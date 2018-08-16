//Build a circuit that lights an LED when it is sufficiently dark in a room. Demonstrate the circuit by covering the photoresistor to simulate darkness.
//Create a video (or a screencast) of your circuit in action.
//If you have real hardware then demonstrate the real circuit. If you do not have real hardware then use the simulator.
// Demonstartion - https://www.youtube.com/edit?o=U&video_id=8_Aj51vQfC4

int sensorPin = A0;
int ledPin= 13;
int brightness = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(ledPin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  brightness = analogRead(sensorPin);
  if (brightness > 500){
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED on (HIGH is the voltage level)
  }
  else if (brightness < 500){
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  }                
}
