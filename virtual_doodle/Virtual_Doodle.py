# import autopy
# import time
# from PIL import Image, ImageOps



def v_doodle():
    import cv2
    import numpy as np
    from . import HandTracks as ht

    # Defining parameters for image processing
    width, height = 1000, 1000
    frame_rate = 100
    smooth = 7

    # Defining some aesthetic characteristics
    radius = 10
    c_colour = (153, 50, 204)

    # Preparing the Canvas.
    canvas = np.zeros((500, 500, 3), dtype='uint8')
    # Set Background Colour as White
    canvas[:] = (255, 255, 255)

        # Turn on Camera and set resolution
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    # Using mediapipe to locate hands
    hand_map = ht.detect_hands(hand_count=1)
    # finger tip ids
    tips = [4, 8, 12, 16, 20]
    # Capture Image
    ini_x, ini_y = 0, 0
    while True:
        success, frames = cap.read()
        frame = cv2.flip(frames, 1)
        #frame = cv2.resize(frame, (500,500))
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
            if up_fingers[1] and up_fingers[2] == 0:
                if ini_x == ini_y == 0:
                    ini_x, ini_y = index_x, index_y
                cv2.line(canvas, (ini_x, ini_y), (index_x, index_y), c_colour, 20)
            ini_x, ini_y = index_x, index_y           

                # Clear canvas if Index, Middle and Ring Fingers are up
            if up_fingers[1] and up_fingers[2] and up_fingers[3] == 1:
                l1, img1 = hand_map.calc_dis(tips[1], tips[2], frame)    # distance between index and middle
                l2, img2 = hand_map.calc_dis(tips[2], tips[3], img1)    # distance between middle and ring
                # If the three fingers are close together, clear canvas
                if l1 < 40 and l2 < 40:
                    canvas[:] = (255, 255, 255)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.imshow('Hand Tracker', frame)
        cv2.imshow('Canvas', canvas)
    cv2.imwrite('Doodle.png', canvas)
    cap.release()
    cv2.destroyAllWindows()      
