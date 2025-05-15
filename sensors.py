from naoqi import ALProxy
import time

def wait_for_head_tap(NAO_IP, NAO_PORT):
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)
    
    tts.say("If you are ready to start your exercises, tap my head.")
    
    while True:
        head_touch = memory.getData("Device/SubDeviceList/Head/Touch/Front/Sensor/Value")
        head_touch += memory.getData("Device/SubDeviceList/Head/Touch/Middle/Sensor/Value")
        head_touch += memory.getData("Device/SubDeviceList/Head/Touch/Rear/Sensor/Value")
        
        if head_touch > 0.5:
            print("Head was tapped")
            break
        time.sleep(0.2)
