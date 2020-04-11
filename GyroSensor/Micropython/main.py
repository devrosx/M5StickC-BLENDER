from m5stack import *
from m5ui import *
from uiflow import *
import imu
import wifiCfg
from m5mqtt import M5mqtt
import ujson
import unit
wifiCfg.doConnect('XXX', 'XXX')


setScreenColor(0x111111)
angle0 = unit.get(unit.ANGLE, unit.PORTA)



imu0 = imu.IMU()
# lcd.clear()
lcd.font(lcd.FONT_Small)
lcd.setTextColor(lcd.WHITE, lcd.BLACK)
if wifiCfg.isconnected() == True:
 
 lcd.print('WIFI and MQQT connected', 80, 80, 0xffffff)
 m5mqtt = M5mqtt('1', 'XXX', 1883, '', '', 300)
 m5mqtt.start()
 print("All OK")
#  lcd.print("ACCEL: {:+7.2f}  {:+7.2f}  {:+7.2f}".format(imu0.acceleration[0], imu0.acceleration[1], imu0.acceleration[2]), lcd.CENTER, 20)
#  lcd.print("GETXYZ:  {:+7.2f}  {:+7.2f}  {:+7.2f}".format(imu0.ypr[0], imu0.ypr[1], imu0.ypr[2]), lcd.CENTER, 40)
#  lcd.print("GYR:   {:+7.2f}  {:+7.2f}  {:+7.2f}".format(imu0.gyro[0], imu0.gyro[1], imu0.gyro[2]), lcd.CENTER, 60)


while True:
 if btnA.isPressed():
  # print (angle0.read())
  data_sent = {"angle": angle0.read()}
  m5mqtt.publish(str('M5STACK'),ujson.dumps(data_sent))
  wait_ms(90)


  pass
 if btnB.isPressed():
  lcd.print("GYRO: {:+7.2f}  {:+7.2f}  {:+7.2f}".format(imu0.gyro[0], imu0.gyro[1], imu0.gyro[2]), lcd.CENTER, 60)
  data_sent = {"X": imu0.gyro[0], "Y": imu0.gyro[1], "Z": imu0.gyro[2]}
  # print (data_sent)
  m5mqtt.publish(str('M5STACK'),ujson.dumps(data_sent))
  wait_ms(90)
