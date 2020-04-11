import paho.mqtt.client as mqtt
import json
import math
import time

def on_message(client,userdata,msg):
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    try:
        data=json.loads(m_decode)
        angle_x = (data['angle_x'])
        angle_x = scale(angle_x, (0.0, 1024.0), (0, +6.28))
        angle_x = round(angle_x, 2)
        angle_y = 0
        angle_z = 0
    except:
        pass
    try:
        data=json.loads(m_decode)
        angle_y = (data['angle_y'])
        angle_y = scale(angle_y, (0.0, 1024.0), (0, +6.28))
        angle_y = round(angle_y, 2)
        angle_z = 0
        angle_x = 0
    except:
        pass
    try:
        data=json.loads(m_decode)
        angle_z = (data['angle_z'])
        angle_z = scale(angle_z, (0.0, 1024.0), (0, +6.28))
        angle_z = round(angle_z, 2)
        angle_y = 0
        angle_x = 0
    except:
        pass
    print ('X: ' + str(angle_x) + 'Y: ' + str(angle_y) + 'Z: ' + str(angle_z))
    # bpy.data.objects['Suzanne'].rotation_euler = (angle_x, angle_y, angle_z)
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
    time.sleep(0.1)

def scale(val, src, dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def func():
    print("Running...")
    
    mqttc.on_message=on_message

def my_timer():
    from threading import Timer
    t = Timer(4, my_timer)
    t.start()
    func()

mqttc= mqtt.Client()
mqttc.on_message=on_message
mqttc.connect("XXX",1883,10)
mqttc.subscribe("M5STACK", 0)
mqttc.loop_forever()

my_timer()
