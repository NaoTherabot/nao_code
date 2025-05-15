from naoqi import ALProxy
import time
from exercises.squat import squat
from exercises.leg_raises import leg_raises
from exercises.lunge import lunge
from exercises.heel_slide import heel_slide
from exercises.ankle_rotations import ankle_rotations
from exercises.calf_raises import calf_raises
from exercises.seated_knee_flexion import seated_knee_flexion
from exercises.arm_circles import arm_circles


def perform_exercise(exercise_name, patient_name, tts, recog, memory):
    try:
        tts.say("Starting the " + exercise_name + " exercise.")

        if exercise_name == "Squats":
            squat()
        elif exercise_name == "Leg raises":
            leg_raises()
        elif exercise_name == "Lunges":
            lunge()
        elif exercise_name == "Heel slides":
            heel_slide()
        elif exercise_name == "Ankle rotations":
            ankle_rotations()
        elif exercise_name == "Calf raises":
            calf_raises()
        elif exercise_name == "Seated knee flexion":
            seated_knee_flexion()
        elif exercise_name == "Arm circles":
            arm_circles()
        else:
            tts.say("Exercise not recognized.")

        tts.say("Great job! You've completed the " + exercise_name + " exercise.")

    except Exception as e:
        print("An error occurred while performing the exercise:", e)
        tts.say("There was an issue while performing the exercise. Let's try again later.")
