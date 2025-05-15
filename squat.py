from naoqi import ALProxy
import time


def squat(NAO_IP="172.18.16.31", NAO_PORT=9559):
    """
    Implements a safer and more stable squat exercise for the NAO robot
    with ultra-gradual transitions between arm and knee movements.
    """
    try:
        # Initialize proxies
        motion = ALProxy("ALMotion", NAO_IP, NAO_PORT)
        posture = ALProxy("ALRobotPosture", NAO_IP, NAO_PORT)
        tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)

        # Check if robot is sitting and stand it up if needed
        try:
            current_posture = posture.getPosture()
            if current_posture == "Sit" or current_posture == "Crouch":
                tts.say("I need to stand up first.")
                motion.wakeUp()  # This should bring the robot to a standing position
                time.sleep(2)
        except:
            # If getPosture fails, just make sure the robot is standing
            motion.wakeUp()
            time.sleep(2)

        # Make sure the robot is fully stable before starting
        tts.say("Preparing for squat exercise.")
        posture.goToPosture("Stand", 0.3)  # Very slow movement to Stand
        time.sleep(3)  # Give extra time to stabilize

        # Set appropriate stiffness
        motion.setStiffnesses("Body", 0.7)  # Lower stiffness for more natural movement
        time.sleep(1)


        tts.say("I'll adjust my posture slightly.")


        arm_names = ["LShoulderPitch", "RShoulderPitch"]


        motion.setAngles(arm_names, [0.9, 0.9], 0.1)
        time.sleep(2)

        motion.setAngles(arm_names, [0.7, 0.7], 0.1)
        time.sleep(2)


        motion.setAngles(arm_names, [0.5, 0.5], 0.1)
        time.sleep(3)


        tts.say("Stabilizing.")
        time.sleep(2)


        tts.say("I will now demonstrate a very gentle knee bend.")

        knee_names = ["LKneePitch", "RKneePitch"]


        motion.setAngles(knee_names, [0.05, 0.05], 0.05)
        time.sleep(2)


        motion.setAngles(knee_names, [0.1, 0.1], 0.05)
        time.sleep(2)


        motion.setAngles(knee_names, [0.15, 0.15], 0.05)
        time.sleep(2)


        motion.setAngles(knee_names, [0.2, 0.2], 0.05)
        time.sleep(2)


        tts.say("Holding this position. This is a gentle squat.")
        time.sleep(3)


        tts.say("Now I'll stand back up.")


        motion.setAngles(knee_names, [0.15, 0.15], 0.05)
        time.sleep(2)


        motion.setAngles(knee_names, [0.1, 0.1], 0.05)
        time.sleep(2)


        motion.setAngles(knee_names, [0.05, 0.05], 0.05)
        time.sleep(2)


        posture.goToPosture("Stand", 0.2)
        time.sleep(2)


        tts.say("Now it's your turn to try a squat.")
        tts.say("Stand with your feet shoulder-width apart.")
        time.sleep(2)
        tts.say("Slowly bend your knees while keeping your back straight.")
        time.sleep(3)
        tts.say("Lower yourself as if sitting in a chair, but only go as far as comfortable.")
        time.sleep(3)
        tts.say("Hold for three seconds.")
        time.sleep(3)
        tts.say("Now slowly stand back up.")
        time.sleep(3)


        tts.say("Let's do two more repetitions.")

        for i in range(2):

            tts.say("Repetition " + str(i + 2) + ". Squat down slowly.")
            time.sleep(3)
            tts.say("Hold this position.")
            time.sleep(3)
            tts.say("Now stand back up.")
            time.sleep(3)

        tts.say("Great job! You've completed the squat exercise.")

        posture.goToPosture("Stand", 0.2)
        motion.setStiffnesses("Body", 0.5)

    except Exception as e:
        print("Error in squat exercise:", str(e))
        try:
            tts.say("I'm having some difficulty with this exercise.")
            try:

                motion.setStiffnesses("Body", 0.8)
                posture.goToPosture("Stand", 0.1)
            except:
                motion.rest()
                print("Reverted to rest position due to error")
        except:
            print("Could not recover from error")

    return