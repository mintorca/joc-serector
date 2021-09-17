int val=0;// 변수의 초기 값 설정
int val_map=0;
int preval = 0;
int preval_map=0;
int count =1;
int interrupt =0;
int state =0;
int prestate =0;
int Hzdisplay =0;
float BPM=0;

#include<MsTimer2.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x3f, 20, 4);

void setup() {
  MsTimer2::set(10, sampling); 
  MsTimer2::start();
  Serial.begin(115200);
  Serial.println(analogRead(A0));
  delay(100);
   lcd.init();
  lcd.init();
  lcd.backlight();
}
void sampling()// sampling 함수
{
  val = analogRead(A0); 
  val_map = map(val, 0, 1023, 0, 5);
  interrupt = 1; //
  if (interrupt == 1) //
  {
    interrupt = 0; //
    if (preval_map < val_map) 
    {
      state = 1; // state는 1
    }
    else if (preval_map > val_map) 
    {
      state = -1; // state는 -1
    }
    else if (preval_map == val_map)
    {
      state = prestate; // state와 prestate과 같다고 설정
    }
    if ((state == -1) && (prestate == 1)) //변곡점일 때,
    {
      BPM = (float)60 * 100 / (float)(count);
      count = 1; 
    }
    else
    {
      count++;
    }
    preval = val;
    preval_map = val_map; 
    prestate = state; 
  }
  //Serial.println(analogRead(val_map));
}

void loop() {
  
  Serial.print(val);
  Serial.println(val);//
    lcd.setCursor(5, 0);
  lcd.print("BPM");
  lcd.setCursor(5, 1);
  lcd.print(BPM);
}
