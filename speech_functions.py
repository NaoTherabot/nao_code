from naoqi import ALProxy
import time
import random
def recognize_name(tts, recog, memory):
    name_list = ["Manoj", "Sherwin", "Nazim"]

    try:
        recog.setLanguage("English")
        recog.pause(True)
        recog.setVocabulary(name_list, False)
        recog.pause(False)

        tts.say("What is your name?")
        recog.subscribe("NameRecognition")
        time.sleep(5)

        word = memory.getData("WordRecognized")
        recog.unsubscribe("NameRecognition")

        if word[1] > 0.4:
            return word[0]
        else:
            tts.say("HI ")
            return None

    except Exception as e:
        print("Error during name recognition", e)
        return None
def get_knee_status(tts, recog, memory):
    knee_status_list = ["good", "bad", "okay"]
    
    try:
        recog.setLanguage("English")
        recog.pause(True)
        recog.setVocabulary(knee_status_list, True)
        recog.pause(False)
        
        tts.say("How is your leg feeling today? Please say 'good', 'bad', or 'okay'.")
        recog.subscribe("KneeStatusRecognition")
        time.sleep(5)
        
        word = memory.getData("WordRecognized")
        recog.unsubscribe("KneeStatusRecognition")
        
        if word[1] > 0.4:
            return word[0]
        else:
            tts.say("Sorry, I didn't catch that. Could you please say how your leg is feeling?")
            return None
    
    except Exception as e:
        print("Error during knee status recognition:", e)
        return None


def ask_mood(tts, recog, memory):
    mood_words = ["happy", "sad", "anxious", "calm", "stressed", "okay"]

    try:
        recog.setLanguage("English")
        recog.pause(True)
        recog.setVocabulary(mood_words, True)
        recog.pause(False)

        tts.say("How are you feeling today?")
        recog.subscribe("MoodCheck")
        time.sleep(5)

        word = memory.getData("WordRecognized")
        recog.unsubscribe("MoodCheck")

        if word[1] > 0.4:
            return word[0]
        else:
            tts.say("I didn't quite hear that")
            return None

    except Exception as e:
        print("Error in mood check", e)
        return None

def choose_exercise(tts, recog, memory):
    exercise_list = ["Squats", "Leg raises", "Lunges", "Heel slides", "Ankle rotations", "Calf raises", "Seated knee flexion", "Arm circles"]
    
    try:
        recog.setLanguage("English")
        recog.pause(True)
        recog.setVocabulary(exercise_list, True)
        recog.pause(False)
        
        tts.say("Please choose an exercise. You can say one of the following: Squats, Leg raises, Lunges, Heel slides, Ankle rotations, Calf raises, Seated knee flexion, Arm circles.")
        recog.subscribe("ExerciseSelection")
        time.sleep(5)
        
        word = memory.getData("WordRecognized")
        recog.unsubscribe("ExerciseSelection")
        
        if word[1] > 0.4:
            return exercise_list.index(word[0]) + 1  # Return the index of the chosen exercise (1-based index)
        else:
            tts.say("Sorry, I didn't catch that. Could you please repeat your exercise choice?")
            return None
    
    except Exception as e:
        print("Error during exercise selection:", e)
        return None

def provide_affirmation(tts):
    affirmations = [
        "You are doing great! Keep going.",
        "Remember, every step forward is progress.",
        "You are stronger than you think.",
        "Take a deep breath. You got this."
    ]
    tts.say(random.choice(affirmations))


def breathing_exercise(tts):
    tts.say("Let's do a simple breathing exercise to relax.")
    tts.say("Take a deep breath in... hold it... and exhale slowly.")
    time.sleep(5)
    tts.say("Let's do it one more time. Inhale... hold... and exhale.")
    time.sleep(5)
