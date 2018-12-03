# -*- coding: utf-8 -*-
from picamera.array import PiRGBArray
from picamera import PiCamera
import sys
import argparse
import warnings
import datetime
import time
import cv2
import numpy as np
import os
import imutils

Kernel_size=15
low_threshold=5
high_threshold=10

rho=1
threshold=10
theta=np.pi/180
minLineLength=0
maxLineGap=0

#Initialize camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(640, 480))

for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # CAPTURE FRAME-BY-FRAME
    frame = f.array
    time.sleep(0.1)
    #frame = imutils.resize(frame, width=500)
    #Convert to Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Blur image to reduce noise. if Kernel_size is bigger the image will be more blurry
    blurred = cv2.GaussianBlur(gray, (Kernel_size, Kernel_size), 0)
    
    #Perform canny edge-detection.
    #If a pixel gradient is higher than high_threshold is considered as an edge.
    #if a pixel gradient is lower than low_threshold is is rejected , it is not an edge.
    #Bigger high_threshold values will provoque to find less edges.
    #Canny recommended ratio upper:lower  between 2:1 or 3:1
    edged = cv2.Canny(blurred, low_threshold, high_threshold)
    #Perform hough lines probalistic transform
    lines = cv2.HoughLinesP(edged,rho,theta,threshold,minLineLength,maxLineGap)
    
    #Draw cicrcles in the center of the picture
    cv2.circle(frame,(320,240),20,(0,0,255),1)
    cv2.circle(frame,(320,240),10,(0,255,0),1)
    cv2.circle(frame,(320,240),2,(255,0,0),2)
    
    #With this for loops only a dots matrix is painted on the picture
##    for y in range(0,480,20):
##            for x in range(0,640,20):
##                cv2.line(frame,(x,y),(x,y),(0,255,255),2)
    
    #With this for loops a grid is painted on the picture
    for y in range(0,480,40):
            cv2.line(frame,(0,y),(640,y),(255,0,0),1)
            for x in range(0,640,40):
                cv2.line(frame,(x,0),(x,480),(255,0,0),1)
                
    #Draw lines on input image
    # if ( len(lines) != 0 )
    #print(lines);
    if(lines is not None):
        x=0
        y=0
        for line in lines:
            for x1,y1,x2,y2 in line:
                x=x+x1+x2
                y=y+y1+y2
                cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2) 
            cv2.putText(frame,'lines_detected',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
        xa=x/(2*len(lines[0])*len(lines))
        ya=y/(2*len(lines[0])*len(lines))
        cv2.circle(frame,(int(xa),int(ya)),5,(255,255,255),1)
        cv2.imshow("line detect test", frame)
        print(xa,ya)       
    else:
        cv2.putText(frame,'lines_undetected',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
        cv2.imshow("line detect test", frame)
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
 
# When everything is done, release the capture

#video_capture.release()
cv2.destroyAllWindows()
