import cv2 
import numpy as np
from display import Display
from matplotlib import pyplot as plt
from extractor import Extractor
import time
W = 1920//2
H = 1080//2

disp = Display(W,H)
 

fe = Extractor()
def process_frame(img):

    img = cv2.resize(img,(W, H)) 
    kp = fe.extract(img)
    if matches is None:
        return

    for p in kp:
        u,v = map(lambda x: int(round(x)), p.pt)
        cv2.circle(img, (u,v), color=(0,255,0),radius=3)
    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture('test.mp4')

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
    
        
