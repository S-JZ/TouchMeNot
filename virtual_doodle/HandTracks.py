import cv2
import mediapipe as mp
import math
#import numpy as np
#import time

class detect_hands():
    def __init__(self, hand_count=2, mode=False, detect_confi=0.5, track_confi=0.5):
        self.mode = mode
        self.hand_count = hand_count
        self.detect_confi = detect_confi
        self.track_confi = track_confi
        self.hand_skeleton = mp.solutions.hands
        self.hands = self.hand_skeleton.Hands(
            self.mode, self.hand_count, self.detect_confi, self.track_confi)
        self.draw_hand_nodes = mp.solutions.drawing_utils
        self.fingertips = [4, 8, 12, 16, 20]

    def locate_hands(self, image, circuit=True):
        img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.hand_print = self.hands.process(img_RGB)
        if self.hand_print.multi_hand_landmarks:
            for hand_marks in self.hand_print.multi_hand_landmarks:
                self.draw_hand_nodes.draw_landmarks(
                    image, hand_marks, self.hand_skeleton.HAND_CONNECTIONS)
        return image

    def find_finger_positions(self, image, hand_id):
        self.lmarks = []
        if self.hand_print.multi_hand_landmarks:
            hand = self.hand_print.multi_hand_landmarks[hand_id]
            for tip_id, node in enumerate(hand.landmark):
                img_h, img_w, img_c = image.shape
                scaled_x, scaled_y = int(node.x * img_w), int(node.y * img_h)
                self.lmarks.append([tip_id, scaled_x, scaled_y])
        return self.lmarks

    def many_fingers_up(self):
        tot_fingers = []
        # Thumb detection
        if self.lmarks[self.fingertips[0]][1] > self.lmarks[self.fingertips[0] - 1][1]:
            tot_fingers.append(1)
        else:
            tot_fingers.append(0)
        for tipid in range(1, 5):
            if self.lmarks[self.fingertips[tipid]][2] < self.lmarks[self.fingertips[tipid] - 2][2]:
                tot_fingers.append(1)
            else:
                tot_fingers.append(0)
        return tot_fingers

    def calc_dis(self, node1, node2, image, circuit=True, radius=10, thick=3):
        n1_x, n1_y = self.lmarks[node1][1:]
        n2_x, n2_y = self.lmarks[node2][1:]
        if circuit:
            cv2.circle(image, (n1_x, n1_y), radius, (255, 0, 255), cv2.FILLED)
            cv2.circle(image, (n2_x, n2_y), radius, (255, 0, 255), cv2.FILLED)
            cv2.line(image, (n1_x, n1_y), (n2_x, n2_y), (0, 0, 255), thick)
        return math.hypot((n2_x - n1_x), (n2_y - n1_y)), image
