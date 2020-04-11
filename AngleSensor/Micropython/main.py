from m5stack import *
from uiflow import *
from m5stack import lcd
from m5mqtt import M5mqtt
import ujson
import unit
import wifiCfg
wifiCfg.doConnect('XXX', 'XXX')
lcd.print('WIFI and MQQT connected', 80, 80, 0xffffff)
m5mqtt = M5mqtt('1', 'XXX', 1883, '', '', 300)
m5mqtt.start()
print("All OK")
angle0 = unit.get(unit.ANGLE, unit.PORTA)

tft = lcd
tft.orient(tft.LANDSCAPE)
lcd.font(lcd.FONT_DefaultSmall)
tft.text(10,10,'BLENDER',tft.ORANGE)
lcd.font(lcd.FONT_DejaVu72)
tft.text(int((160-tft.textWidth('XYZ'))/2),8,'XYZ',tft.WHITE)
time_space = 100
axp.setLcdBrightness(35)
# Determine if the  button is pressed,buttonA_wasPressed is callback function.
def buttonA_wasPressed():
 tft.text(int((160-tft.textWidth('XYZ'))/2),8,'XYZ',tft.WHITE)
 while True:
  # print('X: ' + str(angle0.read()))
  tft.text(int((160-tft.textWidth('X'))/2-47),8,'X',tft.RED)
  data_sent = {"angle_x": angle0.read()}
  m5mqtt.publish(str('M5STACK'),ujson.dumps(data_sent))
  wait_ms(time_space)
  if btnB.isPressed():
   print ('B1')
   break
  # pass
 tft.text(int((160-tft.textWidth('XYZ'))/2),8,'XYZ',tft.WHITE)
 while True:
  # print('Y: ' + str(angle0.read()))
  tft.text(int((160-tft.textWidth('Y'))/2),8,'Y',tft.GREEN)
  data_sent = {"angle_y": angle0.read()}
  m5mqtt.publish(str('M5STACK'),ujson.dumps(data_sent))
  wait_ms(time_space)
  if btnB.isPressed():
   print ('B2')
   break
  # pass
 tft.text(int((160-tft.textWidth('XYZ'))/2),8,'XYZ',tft.WHITE)
 while True:
  # print('Z: ' + str(angle0.read()))
  tft.text(int((160-tft.textWidth('Z'))/2+47),8,'Z',tft.BLUE)
  data_sent = {"angle_z": angle0.read()}
  m5mqtt.publish(str('M5STACK'),ujson.dumps(data_sent))
  wait_ms(time_space)
  if btnB.isPressed():
   print ('B3')
   break
  # pass

def buttonB_wasPressed():
 buttonA_wasPressed()
 pass

btnA.wasPressed(buttonA_wasPressed)
btnB.wasPressed(buttonB_wasPressed)