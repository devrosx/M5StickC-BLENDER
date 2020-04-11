Experimental conection between M5StickC and Blender. With this you can use gyroscope or Angle sensor values and move/rotate object in Blender. Script should work with M5stack and M5stackFire devices (untested).


## How to use
Choose sensor folder you want to use.
# Flash M5StickC with latest UIFlow
# Configure mqqt server
Use rshell to connect M5StickC serial port
Configure WIFI and MQQT server in main.py file...
Upload boot.py main.py with rshell command
``` 
rshell -p (your serial port)
cp boot.py /flash
cp main.py /flash

```

# Install blender (tested on 2.7b)
install Paho for system
```
pip install paho-mqtt
```
install Paho for blender
Navigate to blender python folder (on my OSX /Applications/blender.app/Contents/Resources/2.79/python/bin)
```
./python3.7m  -m ensurepip
./python3.7m -m pip install paho-mqtt
```
You have to install Paho for Blender python and your system python separately.
# Edit scripts with your MQQT adress

Now you can test debug.py
(you should see some output when you press A button on M5StickC)
If it works you can try rotation.blend file
on OSX is recomended to run from terminal (/Applications/blender.app/Contents/MacOS/blender on my machine)
to see python output...

# BUGS
Rotation with angle sensor is not perfect, but it works...