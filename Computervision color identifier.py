import cv2
import numpy as np
import pyautogui

capture = cv2.VideoCapture(0)
blue_low = np.array([100, 150, 0])
blue_up = np.array([140, 255, 255])
prev_y = 0

while True:
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, blue_low, blue_up)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            x, y, w, h= cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if y < prev_y:
                pyautogui.press('space')
            prev_y = y

    cv2.imshow("Camera", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(10) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
