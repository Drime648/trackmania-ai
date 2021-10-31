import cv2 as cv
import numpy as np
from PIL import ImageGrab

def screen_record():
    while(True):
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800, 400)))
        processed_img = cv.cvtColor(printscreen, cv.COLOR_RGB2GRAY)
        processed_img = cv.GaussianBlur(processed_img, (3, 3), cv.BORDER_DEFAULT)
        processed_img = cv.Canny(processed_img, threshold1=200, threshold2=300)
        cv.imshow('window',processed_img)
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break

screen_record()

