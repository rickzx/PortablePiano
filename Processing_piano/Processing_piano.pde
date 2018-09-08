import ddf.minim.*;
import processing.serial.*;

Minim minim;
AudioPlayer song40; 
AudioPlayer song41;
AudioPlayer song42;
AudioPlayer song43;
AudioPlayer song44;
AudioPlayer song45;
AudioPlayer song46;
AudioPlayer song47;
AudioPlayer song48;
AudioPlayer song49;


Serial myPort;  // Create object from Serial class
String val;     // Data received from the serial port

int r=0;
int m=1;  
void setup()
{
 minim = new Minim(this); 
 song40 = minim.loadFile("40.wav");
 song41 = minim.loadFile("41.wav");
 song42 = minim.loadFile("42.wav");
 song43 = minim.loadFile("43.wav");
 song44 = minim.loadFile("44.wav");
 song45 = minim.loadFile("45.wav");
 song46 = minim.loadFile("46.wav");
 song47 = minim.loadFile("47.wav");
 song48 = minim.loadFile("48.wav");
 song49 = minim.loadFile("49.wav");
 
   
  
 String portName = "/dev/cu.usbmodem1411";                             //Change COM48 to the port number that your Arduino is connected, you can check the port number from arduino program. 
 myPort = new Serial(this, portName, 115200);   

 size(160, 160);
 background(0);
  
  
}


void draw()
{
 
  if ( myPort.available() > 0 ) 
      {  // If data is available,
     
      val = myPort.readStringUntil('\n');
 if(val!=null)
 {print(val);
 
      if(val.charAt(0)=='a')
      {
      song40.rewind();
      song40.play();
     
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("DO", 80, 90);
      
      } 
      
      if(val.charAt(0)=='b')
      {
      song41.rewind();
      song41.play(); 
      
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("DO#", 80, 90);
     
      
      }
      
      if(val.charAt(0)=='c')
      {
      song42.rewind();
      song42.play(); 
      
      fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("RE", 80, 90);
      } 
      
      if(val.charAt(0)=='d')
      {
      song43.rewind();
      song43.play();
     
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("RE#", 80, 90); 
      } 
      
      if(val.charAt(0)=='e')
      {
      song44.rewind();
      song44.play();
     
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("MI", 80, 90); 
      }
     
     if(val.charAt(0)=='f')
      {
      song45.rewind();
      song45.play(); 
      
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("FA", 80, 90);
      }
    
     if(val.charAt(0)=='g')
      {
      song46.rewind();
      song46.play();
      
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("FA#", 80, 90); 
      }
    
     if(val.charAt(0)=='h')
      {
      song47.rewind();
      song47.play(); 
      
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("SOL", 80, 90); 
      }
 
     if(val.charAt(0)=='i')
      {
      song48.rewind();
      song48.play();
     
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("SOL#", 80, 90);  
      } 

     if(val.charAt(0)=='j')
      {
      song49.rewind();
      song49.play();
     
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("LA", 80, 90); 
      }        
      
     if(val.charAt(0)=='k')
      {
      song49.rewind();
      song49.play();
     
     fill(0, 0, 0);
     rect(0, 0, 160, 160);            
     fill(255, 255, 255);
     textAlign(CENTER);      
     textSize(50);  
     text("LA#", 80, 90); 
      }          
                           
 }         
       }
       
   
   
  if (mousePressed == true)
         {if(r==1)
          {myPort.write(' ');
          background(0);}
          r=0;
          m=1;}
   
   
 
    

        
}



public void stop() {
minim.stop(); }
