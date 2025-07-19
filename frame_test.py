import cv2
import time
import keyboard
import webbrowser as web


threshold = 3      
cooldown = 1        

cap = cv2.VideoCapture(0)
time.sleep(2)

ret, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

last_trigger_time = 0

while True:
    ret, frame2 = cap.read()
    if not ret:
        break
 
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    delta = cv2.absdiff(frame1_gray, gray)
    thresh = cv2.threshold(delta, threshold, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) > 1500:
            motion_detected = True
            break

    if motion_detected and (time.time() - last_trigger_time > cooldown):
        
        web.open("http://www.google.com")

        last_trigger_time = time.time()

    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break

    frame1_gray = gray

cap.release()
cv2.destroyAllWindows()