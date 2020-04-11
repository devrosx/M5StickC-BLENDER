import paho.mqtt.client as mqtt
import json
import bpy
import math
import time
import mathutils

def on_message(client,userdata,msg):
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    try:
        data=json.loads(m_decode)
        AX = (data['AX'])
        # AX_old = accel_merge(AX)
        # AX = AX + AX_old

        AY = (data['AY'])
        # AY_old = accel_merge(AY)
        # AY = AY + AY_old

        AZ = (data['AZ'])
        # AZ_old = accel_merge(AZ)
        # AZ = AZ + AZ_old -2
        # print (str(AX) + 'old was' + str(AX_old))
    except Exception as e:
        print (e)
    print (str(AZ) + ' ' + str(AY) + ' ' + str(AX)) 
    # # nice rotate
    bpy.data.objects['Suzanne'].rotation_euler = (AX, AY, AZ)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
    time.sleep(0.1)

def accel_merge (input_val):
    input_val_old = input_val
    return input_val_old

def func():
    print("Running...")
    
    mqttc.on_message=on_message

def my_timer():
    from threading import Timer
    t = Timer(4, my_timer)
    t.start()
    func()

# inicializace
mqttc= mqtt.Client()
mqttc.on_message=on_message
mqttc.connect("YOURIP",1883,10)
mqttc.subscribe("M5STACK", 0)
mqttc.loop_forever()

my_timer()
