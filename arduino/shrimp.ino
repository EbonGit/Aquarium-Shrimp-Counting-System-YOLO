const int segmentPins[] = {2, 3, 4, 5, 6, 7, 8};  // Digital pins for segments
                         //b  a  f  c  g  d  e
const int numSegments = 7;

int seg0[] = {B01111011};
int seg1[] = {B01001000};
int seg2[] = {B01100111};
int seg3[] = {B01101110};
int seg4[] = {B01011100};
int seg5[] = {B00111110};
int seg6[] = {B00111111};
int seg7[] = {B01101000};
int seg8[] = {B01111111};
int seg9[] = {B01111100};

int* seg[] = {seg0, seg1, seg2, seg3, seg4, seg5, seg6, seg7, seg8, seg9};

char receceivedBytes;
int receceivedChar = 0;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < numSegments; i++) {
    pinMode(segmentPins[i], OUTPUT);
  }
}

void loop() {
  if(Serial.available()){
    receceivedBytes = Serial.read();
    receceivedChar = receceivedBytes - '0';
   
  }
  
  for (int i = 0; i < numSegments; i++) {
    digitalWrite(segmentPins[i], bitRead(seg[receceivedChar][0], i));
  }

  

}
