def navigate():
    import time
    import pyautogui
    import random
    import cv2
    import numpy as np
    import time
    from . import HandTracks as ht

    def hover_and_click(status, click, x, y):
        if status:
            pyautogui.moveTo(x, y, duration=0.05) 
            #time.sleep(random.uniform(0.001, 0.003))
        if click:
            pyautogui.click(x=x, y=y, clicks=1, button='left')



    def standard_scroll(key='down'):
        if key == 'down':
            pyautogui.scroll(-20)
        else:
            pyautogui.scroll(20)



    # Defining parameters for image processing
    width, height = 1000, 1000
    fr = 100
    smooth = 7

    # Defining some aesthetic characteristics
    radius = 10
    c_colour = (153, 50, 204)
    #Screen size
    global wScr
    wScr, hScr = pyautogui.size()
    wCam, hCam = 640, 480
    # Turn on Camera and set resolution
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    # Using mediapipe to locate hands
    hand_map = ht.detect_hands(hand_count=1)
    # finger tip ids
    tips = [4, 8, 12, 16, 20]
    status = True
    X, Y = cX, cY = 0, 0
    # Capture Image
    t1 = time.time()
    while True:
        #print ("Current position: " + str(mouse.position))
        success, frames = cap.read()
        frame = cv2.flip(frames, 1)
        frame = cv2.resize(frame,(int(wScr), int(hScr)))   #(
        # Draw hand landmarks
        frame = hand_map.locate_hands(frame)
        # Find Landmarks on hand
        landmarks = hand_map.find_finger_positions(frame, 0)
        if len(landmarks) != 0:  # If Hand Detected
            # Index Finger's coordinates
            index_x, index_y = landmarks[1][1:]
            # Middle Finger's coordinates
            middle_x, middle_y = landmarks[2][1:]
            # To check the fingers that are up
            up_fingers = hand_map.many_fingers_up()
            # Draw Gesture : Index Finger must be up and middle finger must be down
            if up_fingers[1] == 1 and up_fingers[2] == 0:
                hover_and_click(True, False, index_x, index_y)
            if up_fingers[1] == 1 and up_fingers[2] == 1:
                if time.time() - t1 > 2:
                    hover_and_click(True, True, index_x, index_y)
                    t1 = time.time()
            l1, img1 = hand_map.calc_dis(tips[0], tips[1], frame)
            if l1 < 15:
                status = False
            if not status:
                if up_fingers[0] == up_fingers[1] == up_fingers[2] == up_fingers[3] == up_fingers[4] == 1:
                    status = True
                else:
                    l2, img2 = hand_map.calc_dis(tips[0], tips[1], frame)
                    if l2 > 40:
                        standard_scroll()
                    else:
                        standard_scroll('up')

        cv2.imshow('Hand Tracker', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()