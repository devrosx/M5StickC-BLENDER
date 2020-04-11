import paho.mqtt.client as mqtt
import json
import math
import time
from numpy import interp

previous = 0

def on_message(client,userdata,msg):
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    data=json.loads(m_decode)
    angle = (data['angle'])
    angle = scale(angle, (0.0, 1024.0), (0, +6.28))
    angle = round(angle, 2)
    print (angle)

    # interp(50, [0,99], [-1,1])
    # map value from 0 to  6,28
    # try:
    #     data=json.loads(m_decode)
    #     print (data)
    #     AX = (data['AX'])
    #     AX_old = accel_merge(AX)
    #     AX = AX + AX_old

    #     AY = (data['AY'])
    #     AY_old = accel_merge(AY)
    #     AY = AY + AY_old

    #     AZ = (data['AZ'])
    #     AZ_old = accel_merge(AZ)
    #     AZ = AZ + AZ_old -2
    #     # print (str(AX) + 'old was' + str(AX_old))
    # except Exception as e:
    #     print (e)
    # print (str(AZ) + ' ' + str(AY) + ' ' + str(AX)) 

def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    """
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def accel_merge (input_val):
	input_val_old = input_val
	return input_val_old

def conv (input_val):
	# input_val = input_val * 180 / math.pi
	input_val = input_val / 65

	input_val = round(input_val, 2)
	return input_val
	
mqttc= mqtt.Client()
mqttc.on_message=on_message
mqttc.connect("192.168.3.187",1883,10)
mqttc.subscribe("M5STACK", 0)
mqttc.loop_forever()