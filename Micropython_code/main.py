from m5stack import *
from m5ui import *
from uiflow import *
import imu
import wifiCfg
from m5mqtt import M5mqtt
import ujson
wifiCfg.doConnect('XXX', 'XXX')

imu0 = imu.IMU()
# lcd.clear()
lcd.font(lcd.FONT_Small)
lcd.setTextColor(lcd.WHITE, lcd.BLACK)
if wifiCfg.isconnected() == True:
 
 lcd.print('WIFI and MQQT connected', 80, 80, 0xffffff)
 m5mqtt = M5mqtt('1', '192.168.3.187', 1883, '', '', 300)
 m5mqtt.start()
 print("All OK")
#  lcd.print("ACCEL: {:+7.2f}  {:+7.2f}  {:+7.2f}".format(imu0.acceleration[0], imu0.acceleration[1], imu0.acceleration[2]), lcd.CENTER, 20)
#  lcd.print("GETXYZ:  {:+7.2f}  {:+7.2f}  {:+7.2f}".format(imu0.ypr[0], imu0.ypr[1], imu0.ypr[2]), lcd.CENTER, 40)
#  lcd.print("GYR:   {:+7.2f}  {:+7.2f}  {:+7.2f}".format(imu0.gyro[0], imu0.gyro[1], imu0.gyro[2]), lcd.CENTER, 60)


while True:
 if btnA.isPressed():
  lcd.print("AX: {:+7.2f}  {:+7.2f}  {:+7.2f}".format(imu0.acceleration[0], imu0.acceleration[1], imu0.acceleration[2]), lcd.CENTER, 20)
  data_sent = {"AX": imu0.acceleration[0], "AY": imu0.acceleration[1], "AZ": imu0.acceleration[2]}
  m5mqtt.publish(str('M5STACK'),ujson.dumps(data_sent))
  wait_ms(90)
  pass
 if btnB.isPressed():
  lcd.print("GYRO: {:+7.2f}  {:+7.2f}  {:+7.2f}".format(imu0.gyro[0], imu0.gyro[1], imu0.gyro[2]), lcd.CENTER, 60)
  data_sent = {"X": imu0.gyro[0], "Y": imu0.gyro[1], "Z": imu0.gyro[2]}
  m5mqtt.publish(str('M5STACK'),ujson.dumps(data_sent))
  wait_ms(90)
