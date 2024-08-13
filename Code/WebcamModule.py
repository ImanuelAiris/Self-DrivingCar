import cv2

 
def getImg(display= False):
    success, img = cap.read()
    if cv2.waitKey(1) and 0xFF == ord('q'):
        return 0
    if display:
        cv2.imshow('IMG',img)
    return img
 
if __name__ == '__main__':
    size=[480,240]
    cap = cv2.VideoCapture(0)
    cap.set(3, size[0])
    cap.set(4, size[1])
    while True:
        img = getImg(True)