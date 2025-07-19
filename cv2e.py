import cv2
img = cv2.VideoCapture(0)

Truee = True

while Truee:
    ret, cap = img.read()

    cv2.imshow('Camera', cap)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

img.release()
cv2.destroyAllWindows()

