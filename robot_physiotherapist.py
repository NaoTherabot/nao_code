import naoqi
import time
from naoqi import ALProxy
from speech_functions import recognize_name, get_knee_status, choose_exercise, ask_mood, provide_affirmation, breathing_exercise
from sensors import wait_for_head_tap
from logic import perform_exercise

NAO_IP = "172.18.16.31" 
NAO_PORT = 9559

if __name__ == "__main__":
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
    recog = ALProxy("ALSpeechRecognition", NAO_IP, NAO_PORT)
    memory = ALProxy("ALMemory", NAO_IP, NAO_PORT)

    tts.say("Hello, my name is Nao, your interactive physiotherapy and mental support assistant. I'm here to help you with rehabilitation and to lift your spirits.")

    # Recognize patient name
    patient_name = recognize_name(tts, recog, memory)
    tts.say("Hi, {}. It's nice to meet you.".format(patient_name or ""))
    time.sleep(3)

    # Check patient's mood
    mood = ask_mood(tts, recog, memory)
    if mood:
        tts.say("Thank you for sharing. It's okay to feel " + mood + ". I'm here to support you.")
    else:
        tts.say("Thank you for letting me know.")

    time.sleep(2)
    provide_affirmation(tts)

    # Breathing exercise
    breathing_exercise(tts)

    # Check knee status
    knee_status = get_knee_status(tts, recog, memory)
    if knee_status:
        tts.say("Thank you for letting me know. You said your knee feels " + knee_status + ".")
    else:
        tts.say("Thank you for letting me know")
    
    wait_for_head_tap(NAO_IP, NAO_PORT)
    time.sleep(5)

    # Exercise selection
    exercise_number = choose_exercise(tts, recog, memory)
    exercises = ["Squats", "Leg raises", "Lunges", "Heel slides", "Ankle rotations", "Calf raises", "Seated knee flexion",
                 "Arm circles"]

    if exercise_number:
        selected_exercise = exercises[exercise_number - 1]
        tts.say("You selected " + selected_exercise + ". Let's get started!")
    else:
        selected_exercise = "Squats"
        tts.say("Let's start with the first exercise, Squats")

    # Perform the selected exercise
    perform_exercise(selected_exercise, patient_name, tts, recog, memory)

    tts.say("Great job, {}! Remember, you're doing amazing. Take care and see you next time.".format(patient_name or ""))
                        