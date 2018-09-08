#include <SD.h>

#include <CapacitiveSensor.h>

#define total 80                   //define sensitivity, high value for decreases sensitivity, low value increases
#define sensor 1                  //define number of samples Arduino takes, high value will increase stability while increasing response time
#define debounce 50
int led = 13;                                         
long time = 0;

int state = HIGH;


boolean yes12;
boolean previous12 = false;

boolean yes11;
boolean previous11 = false;

boolean yes10;
boolean previous10 = false;

boolean yes9;
boolean previous9 = false;

boolean yes8;
boolean previous8 = false;

boolean yes7;
boolean previous7 = false;

boolean yes6;
boolean previous6 = false;

boolean yes5;
boolean previous5 = false;

boolean yes4;
boolean previous4 = false;

boolean yes3;
boolean previous3 = false;

boolean yes14;
boolean previous14 = false;

boolean yes15;
boolean previous15 = false;


//CapacitiveSensor   cs_2_13 = CapacitiveSensor(2,13);
CapacitiveSensor   cs_2_12 = CapacitiveSensor(2,12);        // 2.2M resistor between pins 2 & 12, pin 2 is send pin, pin 12 is sensor pin
CapacitiveSensor   cs_2_11 = CapacitiveSensor(2,11);        // 2.2M resistor between pins 2 & 11, pin 2 is send pin, pin 11 is sensor pin
CapacitiveSensor   cs_2_10 = CapacitiveSensor(2,10);        // 2.2M resistor between pins 2 & 10, pin 2 is send pin, pin 10 is sensor pin
CapacitiveSensor   cs_2_9 = CapacitiveSensor(2,9);        
CapacitiveSensor   cs_2_8 = CapacitiveSensor(2,8);        
CapacitiveSensor   cs_2_7 = CapacitiveSensor(2,7);       
CapacitiveSensor   cs_2_6 = CapacitiveSensor(2,6);      
CapacitiveSensor   cs_2_5 = CapacitiveSensor(2,5);        
CapacitiveSensor   cs_2_4 = CapacitiveSensor(2,4);      
CapacitiveSensor   cs_2_3 = CapacitiveSensor(2,3);  
CapacitiveSensor   cs_2_14 = CapacitiveSensor(2,14);   
CapacitiveSensor   cs_2_15 = CapacitiveSensor(2,15);  


void setup()                    
{
   //cs_2_13.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_12.set_CS_AutocaL_Millis(0xFFFFFFFF);  //Calibrate the sensor... 
   cs_2_11.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_10.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_9.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_8.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_7.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_6.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_5.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_4.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_3.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_14.set_CS_AutocaL_Millis(0xFFFFFFFF);
   cs_2_15.set_CS_AutocaL_Millis(0xFFFFFFFF);

   pinMode(led, OUTPUT);
   Serial.begin(115200);
}


void loop()                    
{    
  
    long total112 =  cs_2_12.capacitiveSensor(sensor);
    long total111 =  cs_2_11.capacitiveSensor(sensor);
    long total110 =  cs_2_10.capacitiveSensor(sensor);
    long total19 =  cs_2_9.capacitiveSensor(sensor);
    long total18 =  cs_2_8.capacitiveSensor(sensor);
    long total17 =  cs_2_7.capacitiveSensor(sensor);
    long total16 =  cs_2_6.capacitiveSensor(sensor);
    long total15 =  cs_2_5.capacitiveSensor(sensor);
    long total14 =  cs_2_4.capacitiveSensor(sensor);
    long total13 =  cs_2_3.capacitiveSensor(sensor);
    long total114 = cs_2_14.capacitiveSensor(sensor);
    long total115 = cs_2_15.capacitiveSensor(sensor);
    
    if (total112 > total){yes12 = true;}
    else {yes12 = false;} 
 
    if (total111 > total){yes11 = true;}
    else {yes11 = false;}

    if (total110 > total){yes10 = true;}
    else {yes10 = false;} 
 
    if (total19 > total){yes9 = true;}
    else {yes9 = false;}

    if (total18 > total){yes8 = true;}
    else {yes8 = false;}
   
    if (total17 > total){yes7 = true;}
    else {yes7 = false;} 
   
    if (total16 > total){yes6 = true;}
    else {yes6 = false;}
  
    if (total15 > total){yes5 = true;}
    else {yes5 = false;} 
   
    if (total14 > total){yes4 = true;}
    else {yes4 = false;}
   
    if (total13 > total){yes3 = true;}
    else {yes3 = false;} 

    if (total114 > total){yes14 = true;}
    else {yes14 = false;}

    if (total115 > total){yes15 = true;}
    else {yes15 = false;}
     
    
    if(yes12 == true && previous12  == false && millis() - time>debounce)
    
    {
      
        state = LOW;
        time = millis();
        Serial.println("c");     
       
    }

    else if (yes12 == false && previous12 == true){
      state = HIGH;
      Serial.println("cn");
    }
        
    
    if(yes11 == true && previous11  == false && millis() - time>debounce)

    {
  
         state = LOW;
        time = millis();
        Serial.println("c#");     
    
     }
    else if (yes11 == false && previous11 == true){
      state = HIGH;
      Serial.println("c#n");
    }
   
    if(yes10 == true && previous10  == false && millis() - time>debounce)
    
    {
      
         state = LOW;
        time = millis();
        Serial.println("d");     
       
    }
    else if (yes10 == false && previous10 == true){
      state = HIGH;
      Serial.println("dn");
    }
  
    if(yes9 == true && previous9  == false && millis() - time>debounce)
    
    {
      
         state = LOW;
        time = millis();
        Serial.println("d#");     
       
    }
   else if (yes9 == false && previous9 == true){
      state = HIGH;
      Serial.println("d#n");
    }
     
   if(yes8 == true && previous8  == false && millis() - time>debounce)
    
    {
      
         state = LOW;
        time = millis();
        Serial.println("e");     
       
    }
    else if (yes8 == false && previous8 == true){
      state = HIGH;
      Serial.println("en");
    }
   
   if(yes7 == true && previous7  == false && millis() - time>debounce)
    
    {

         state = LOW;
        time = millis();
        Serial.println("f");     
       
    }

    else if (yes7 == false && previous7 == true){
      state = HIGH;
      Serial.println("fn");
    }
    
  if(yes6 == true && previous6  == false && millis() - time>debounce)
    
    {
 
         state = LOW;
        time = millis();
        Serial.println("f#");     
       
    }
    else if (yes6 == false && previous6 == true){
      state = HIGH;
      Serial.println("f#n");
    }

 
  if(yes5 == true && previous5  == false && millis() - time>debounce)
    
    {
      
         state = LOW;
        time = millis();
        Serial.println("g");     
       
    }
    else if (yes5 == false && previous5 == true){
      state = HIGH;
      Serial.println("gn");
    }


   if(yes4 == true && previous4  == false && millis() - time>debounce)
    
    {

         state = LOW;
        time = millis();
        Serial.println("g#");     
       
    }
    else if (yes4 == false && previous4 == true){
      state = HIGH;
      Serial.println("g#n");
    }


    if(yes3 == true && previous3  == false && millis() - time>debounce)
    
    {

         state = LOW;
        time = millis();
        Serial.println("a");     
       
    }  
    else if (yes3 == false && previous3 == true){
      state = HIGH;
      Serial.println("an");
    }


    if(yes14 == true && previous14  == false && millis() - time>debounce)
    
    {

         state = LOW;
        time = millis();
        Serial.println("a#");     
       
    }
    else if (yes14 == false && previous14 == true){
      state = HIGH;
      Serial.println("a#n");
    }

    if(yes15 == true && previous15  == false && millis() - time>debounce)
    
    {

         state = LOW;
        time = millis();
        Serial.println("b");     
       
    }
    else if (yes15 == false && previous15 == true){
      state = HIGH;
      Serial.println("bn");
    }
         
      digitalWrite(led, state);
      previous12 = yes12;
      previous11 = yes11;
      previous10 = yes10;
      previous9 = yes9;
      previous8 = yes8;
      previous7 = yes7;
      previous6 = yes6;
      previous5 = yes5;
      previous4 = yes4;
      previous3 = yes3;
      previous14 = yes14;
      previous15 = yes15;
        
     
  
      
      delay(2);


}
