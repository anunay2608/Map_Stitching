# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:13:47 2020

@author: MOHAN
"""
import cv2
import os
import numpy as np
import glob
import pickle
from collections import deque
import imutils

xpath = r'D:\MAP STITCHING'
os.chdir(xpath)
n = 0
cam_mat_in = open(r'C:\Users\MOHAN\Desktop\Final\camera_matrix.pickle','rb')
cam = pickle.load(cam_mat_in)
           
dist_c_in = open(r'C:\Users\MOHAN\Desktop\Final\distortion_coeffs.pickle', 'rb')
dist = pickle.load(dist_c_in)
    
img_path = r'D:\MAP STITCHING\*.jpg'
images = glob.glob(img_path)
img_list = deque(maxlen=(5))
images_ = []

stitcher = cv2.Stitcher_create()
cap = cv2.VideoCapture(0)

while 1:
    n +=1
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480), interpolation = cv2.INTER_AREA)
        #cv2.imshow('real', frame)
    h, w = frame.shape[ : 2]
    new_cam_mat, roi = cv2.getOptimalNewCameraMatrix(cam, dist, (w,h), 1, (w,h))
    un_dist = cv2.undistort(frame, cam, dist, None, new_cam_mat)
    x, y, w, h = roi
    un_dist = un_dist[y:y+h, x: x+w]
    cv2.imshow('Undistort', un_dist)
    cv2.waitKey(1000)
    img_list.append(un_dist)
        
    if len(img_list) == 5 :
        status, stitched = stitcher.stitch(img_list)
        if status == 0:
            stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0, 0, 0))
            gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
            something, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
              
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            c = max(cnts, key=cv2.contourArea)
            mask = np.zeros(thresh.shape, dtype="uint8")
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
                  
            minRect = mask.copy()
            sub = mask.copy()
                
            while cv2.countNonZero(sub) > 0:
                minRect = cv2.erode(minRect, None)
                sub = cv2.subtract(minRect, thresh)
                   
            cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            c = max(cnts, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(c)
                    
            stitched = stitched[y:y + h, x:x + w]
                    
        cv2.imshow('Stitched', stitched)
        cv2.imwrite(str(n) + '.jpg', stitched)
        cv2.waitKey(1)
        img_list.clear()
        continue
                
        if cv2.waitKey(1000) == ord('f') :
            if len(img_list) == 5 :
                status, stitched = stitcher.stitch(img_list)
                if status == 0:
                    stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0, 0, 0))
                    gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
                    something, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
              
                    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    cnts = imutils.grab_contours(cnts)
                    c = max(cnts, key=cv2.contourArea)
                    mask = np.zeros(thresh.shape, dtype="uint8")
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
                          
                    minRect = mask.copy()
                    sub = mask.copy()
                
                    while cv2.countNonZero(sub) > 0:
                        minRect = cv2.erode(minRect, None)
                        sub = cv2.subtract(minRect, thresh)
                        
                    cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    cnts = imutils.grab_contours(cnts)
                    c = max(cnts, key=cv2.contourArea)
                    (x, y, w, h) = cv2.boundingRect(c)
                    
                    stitched = stitched[y:y + h, x:x + w]
                    
                cv2.imshow('Stitched', stitched)
                cv2.imwrite(str(n) + '.jpg', stitched)
                cv2.waitKey(1)
                img_list.clear()
            break


stitcher = cv2.Stitcher_create()
img_path = 'D:\MAP STITCHING\*.jpg'
images = glob.glob(img_path)
    #img_list = deque(maxlen=(5))
images_ = []
for image in images:
    img = cv2.imread(image)
    images_.append(img)
    
x_status, x_stitched = stitcher.stitch(images_)
if x_status == 0:
    cv2.imshow('Final' , x_stitched)
    cv2.waitKey(1000)
else:
    print("Nahi hua!")
cv2.destroyAllWindows()   