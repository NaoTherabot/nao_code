# -*- coding: utf-8 -*-


import socket
import time
import random
from naoqi import ALProxy

# --- Setup NAO Proxies ---
tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
motion = ALProxy("ALMotion", "127.0.0.1", 9559)
posture = ALProxy("ALRobotPosture", "127.0.0.1", 9559)
recog = ALProxy("ALSpeechRecognition", "127.0.0.1", 9559)
memory = ALProxy("ALMemory", "127.0.0.1", 9559)

# --- UDP Server Setup ---
UDP_IP = "172.18.16.31"  # Replace with your NAO's IP
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("NAO is waiting for client...")

# --- Wait for Client Signal ---
while True:
    data, addr = sock.recvfrom(1024)
    if data.strip() == b"start":  # bytes check
        break

# --- Functions ---

def say_with_gestures(text):
    speed = 0.2
    # Raise right arm gently before speaking
    motion.post.setAngles("RShoulderPitch", 0.3, speed)
    motion.post.setAngles("RShoulderRoll", -0.2, speed)
    motion.post.setAngles("RElbowYaw", 0.5, speed)
    motion.post.setAngles("RElbowRoll", 1.0, speed)

    # Speak (blocking call)
    tts.say(text)

    # Return right arm to resting position after speaking
    motion.setAngles("RShoulderPitch", 1.5, speed)
    motion.setAngles("RShoulderRoll", 0.0, speed)
    motion.setAngles("RElbowYaw", 0.0, speed)
    motion.setAngles("RElbowRoll", -0.5, speed)

def recognize_name(tts, recog, memory):
    name_list = ["Manoj", "Sherwin", "Nazim"]  # Add more names if needed

    try:
        recog.setLanguage("English")
        recog.pause(True)
        recog.setVocabulary(name_list, False)
        recog.pause(False)
        
        say_with_gestures("Hello, I am your therapy assistant. Before we start may I know your name please?")
        recog.subscribe("NameRecognition")
        time.sleep(5)

        word = memory.getData("WordRecognized")
        recog.unsubscribe("NameRecognition")

        if word and word[1] > 0.4:
            return word[0]
        else:
            say_with_gestures("Sorry, I couldn't hear your name clearly.")
            return None

    except Exception as e:
        print("Error during name recognition:", e)
        return None

def breathing_exercise():
    say_with_gestures("Let's do a simple breathing exercise to relax.")
    say_with_gestures("Take a deep breath in... hold it... and exhale slowly.")
    time.sleep(5)
    say_with_gestures("Let's do it one more time. Inhale... hold... and exhale.")
    time.sleep(5)

def slow_stretch():
    speed = 0.1  # Very slow and safe

    # Raise both arms slowly
    motion.setAngles(["LShoulderPitch", "RShoulderPitch"], [0.5, 0.5], speed)
    time.sleep(3)

    # Stretch arms to side slowly
    motion.setAngles(["LShoulderRoll", "RShoulderRoll"], [0.3, -0.3], speed)
    time.sleep(3)

    # Gently rotate shoulders in and out
    motion.setAngles(["LElbowYaw", "RElbowYaw"], [-1.0, 1.0], speed)
    time.sleep(3)
    motion.setAngles(["LElbowYaw", "RElbowYaw"], [0.5, -0.5], speed)
    time.sleep(3)

    # Return to neutral
    motion.setAngles(["LShoulderPitch", "RShoulderPitch"], [1.5, 1.5], speed)
    motion.setAngles(["LShoulderRoll", "RShoulderRoll"], [0.0, 0.0], speed)
    motion.setAngles(["LElbowYaw", "RElbowYaw"], [-0.5, 0.5], speed)
    time.sleep(2)

def provide_affirmation():
    affirmations = [
        "You are doing great! Keep going.",
        "Remember, every step forward is progress.",
        "You are stronger than you think.",
        "Take a deep breath. You got this."
    ]
    say_with_gestures(random.choice(affirmations))

def moderate_exercise():
    speed = 0.1  # Keep it slow for safety
    
    # Raise both arms above the head slowly
    motion.setAngles(["LShoulderPitch", "RShoulderPitch"], [0.0, 0.0], speed)
    time.sleep(3)
    
    # Stretch arms up and slightly backward
    motion.setAngles(["LShoulderRoll", "RShoulderRoll"], [-0.3, 0.3], speed)
    time.sleep(3)
    
    # Slowly bend elbows to touch head (like a stretch)
    motion.setAngles(["LElbowRoll", "RElbowRoll"], [-1.2, 1.2], speed)
    time.sleep(3)
    
    # Return arms slowly to rest position
    motion.setAngles(["LShoulderPitch", "RShoulderPitch"], [1.5, 1.5], speed)
    motion.setAngles(["LShoulderRoll", "RShoulderRoll"], [0.0, 0.0], speed)
    motion.setAngles(["LElbowRoll", "RElbowRoll"], [-0.5, 0.5], speed)
    time.sleep(2)
def safe_minimal_exercise():
    import time

    speed = 0.05  # Very slow
    posture.goToPosture("StandInit", 0.6)

    # 1. Gently sway hips left and right using HipRoll
    try:
        print("Swaying hips gently...")
        motion.setAngles("LHipRoll", 0.1, speed)
        motion.setAngles("RHipRoll", 0.1, speed)
        time.sleep(2)

        motion.setAngles("LHipRoll", -0.1, speed)
        motion.setAngles("RHipRoll", -0.1, speed)
        time.sleep(2)

        motion.setAngles("LHipRoll", 0.0, speed)
        motion.setAngles("RHipRoll", 0.0, speed)
        time.sleep(1)

        # 2. Raise right arm gently forward and hold, then back
        print("Raising right arm slowly...")
        motion.setAngles("RShoulderPitch", 0.5, speed)
        time.sleep(2)

        print("Lowering right arm slowly...")
        motion.setAngles("RShoulderPitch", 1.4, speed)
        time.sleep(2)

    except Exception as e:
        print("Error during exercise:", e)

    # Return to safe standing posture
    posture.goToPosture("StandInit", 0.6)


# --- Main Interaction ---

# 1. Recognize Name
name = recognize_name(tts, recog, memory)
if not name:
    name = "friend"

say_with_gestures("Nice to meet you, " + name + "! Let's start with a small breathing exercise.")

# 2. Breathing Exercise
breathing_exercise()

# 3. Main Physiotherapy Stretching
say_with_gestures("Now we will do a slow stretching exercise. Please follow me!")

# Move to StandInit
posture.goToPosture("StandInit", 0.6)

slow_stretch()

say_with_gestures("Great job, " + name + "! You followed the movements really well.")

provide_affirmation()

say_with_gestures("Now let's try a slightly more challenging exercise, but we will do it slowly and carefully.")

moderate_exercise()

say_with_gestures("Well done! You did excellent, " + name + ". Remember to stay relaxed and keep practicing.")

provide_affirmation()

posture.goToPosture("Stand", 0.6)

say_with_gestures("Now let's try a slightly more challenging exercise with your lower body, but we will do it slowly and carefully.")

safe_minimal_exercise()

say_with_gestures("Well done! You did excellent, " + name + ". Remember to stay relaxed and keep practicing.")

say_with_gestures("So this is it for today, hope you liked the session, don't forget to leave a review")
