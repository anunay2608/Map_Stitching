import cv2
import os
import numpy as np
import glob
import pickle

xpath = "/home/anunay/Desktop"
os.chdir(xpath)
cam_mat_in = open("/home/anunay/Desktop/camera_matrix.pickle",'rb')
cam = pickle.load(cam_mat_in)

dist_c_in = open("/home/anunay/Desktop/distortion_coeff.pickle", 'rb')
dist = pickle.load(dist_c_in)

#MAP STITCHING IS THE FOLDER CONSIST OF IMAGES THAT ARE TO BE STITCHED TOGETHER.
img_path = "/home/anunay/Desktop/Map_Stitching*.jpg"
images = glob.glob(img_path)#IT WILL GET ALL THE IMAGE'S PATH FROM THAT FOLDER.
img_list = []

for image in images:
    img = cv2.imread(image)
    frame = cv2.resize(img, (256, 256), interpolation = cv2.INTER_AREA)
    h, w = frame.shape[ : 2]
    new_cam_mat, roi = cv2.getOptimalNewCameraMatrix(cam, dist, (w,h), 1, (w,h))
    un_dist = cv2.undistort(frame, cam, dist, None, new_cam_mat)
    x, y, w, h = roi
    un_dist = un_dist[y:y+h, x: x+w]
    img_list.append(un_dist)

print(img_list)

stitcher = cv2.Stitcher_create()
status, stitched = stitcher.stitch(img_list)
if status == 0:
    print(stitched.shape[:2])
    cv2.imshow('Stitched', stitched)
    cv2.waitKey(0)
else: 
	print("Map Stitching failed!")
cv2.destroyAllWindows()
