#Fisheye effect roemoval 

import cv2
import numpy as np
import pickle
import os

#HERE WE HAV CLICKED AROUND 500 IMAGES OF A CHESSBOARD PRINTOUT TAKEN ON AN A4 SIZE SHEET, AND THEN STORED IT IN FOLDER NAMED CHESSBOX

img_names = []
for i in os.listdir("/home/anunay/Desktop/chessbox"):
	img_path = "/home/anunay/Desktop/chessbox" + "/" + i
	img_names.append(img_path)

term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)#30 and 0.1 are the threshhold value for the count of chessbox corners found and epsilon value. 
scale_h = scale_w = img_points_scale = 5#taken randomly...

pattern_size=(9,6)
itrs = ([0], range(pattern_size[1]), range(pattern_size[0]))
pattern_points = np.array(list(product(*itrs)), np.float32)[:,::-1]
pattern_points_lst = []
img_points_lst = []
shape_old = None



for fn in img_names:
	img = cv2.imread(fn)
    img = np.array(img, dtype = np.float32)
    shape = img.shape[:2]
    hh, ww = shape

    found, corners = cv2.findChessboardCorners(img, pattern_size)
    if found:
        corners_fine = corners.copy() * img_points_scale
        cv2.cornerSubPix(img, corners_fine, (5, 5), (-1, -1), term)

        img_points_lst.append(corners_fine.reshape(-1, 2))
        pattern_points_lst.append(pattern_points)

    else:
        print('chessboard not found')
        continue

if len(pattern_points_lst) > 0:
    print("calibrateCamera")

    size = (int(round(ww*scale_w)), int(round(hh*scale_h)))
    flags = cv2.CALIB_RATIONAL_MODEL
    rms, camera_matrix, distortion_coeffs, rvecs, tvecs = \
            cv2.calibrateCamera(pattern_points_lst,
                                img_points_lst,
                                size,
                                None,
                                None, None,
                                None,
                                flags,
                                term)

   	camera_matrix_file = open("/home/anunay/Desktop/camera_matrix", wb)
   	coeffs_file = open("/home/anunay/Desktop/distortion_coeff", wb)

   	pickle.dump(camera_matrix, camera_matrix_file)
   	camera_matrix_file.close()

   	pickle.dump(distortion_coeffs, coeffs_file)
   	coeffs_file.close()
