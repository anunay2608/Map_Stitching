Examples and images are yet to be added....
# Map_Stitching
Map Stitching or Mosaicing is a task of composing and stitching multiple images with narrow but overlapping fields of aerial views to create a larger image with a wider field of view covering a large area in a single RGB image.
The process of map stitching involves following tasks : 
  1) Finding the common feature points between two images, from where the two images are to be stitched.
  2) Checking the stitching condition, i.e. find if the features found are greater than the minimum number of features to be extracted.
  3) Stitching the two images from the common feature points line as a single image.that produces strong visual distortion intended to create a wide panoramic or hemispherical image. 
  4) At last it includes the cropping and final finishing part which includes the removal of additional black background from the final image to make it a attractive final image.

## Fisheye :
We have created the fisheye file to remove the FISHEYE effect which is most commonly seen in approximately all cameras, resulting in the strong visual distortion intended to create a wide panoramic or hemispherical image. For doing the same we have to click the variable images of the chessboard printout taken on any A4 size sheet and then running the code Fisheye.py for the same. Fisheye.py returns 2 pickle file consisting of Camera Matrix and the Distortion Coefficient values hich perticularly depends on the camera itself.

## Stitcher : 
Stitcher.py is the code which stitches the images given to it. It extracts the images from the given folder and then undistort each and every image using the previously calculated Camera Matrix and Distortion Coefficients and then follows the complete Map_Stitching procedure to stitch all the given images to each other and outputs a single RGB image by composing all the multiple images.
[HERE YOU HAVE TO SPECIFY THE PATH TO THE CAM_MATRIX, DISTORTIO_COEFF PATH AND THE IMAGES FOLDER PATH, AND HENCE RECIEVES A SINGLE STITCHED IMAGE.]

## Real Time Map_Stitching : 
This code represents the real time map stitching task, which includes the controlling of a camera using python code and then stitching the 5 consecutive frames which is done because of space constraints. Since stitching task performed on the complete video will lead to a larger space consumption hence we stitched 5(can be variable, let "n") alternate frames and stored them into a folder. This basically reduces the computation power and the space consumotion by factor of "n". Then we can stitch the saved folder by the same concept as discussed in Map_Stitching and coded in Stitcher.py                                                   [HERE TOO WE HAVE TO INPUT THE CAMERA_MATRIX AND DISTORTION_COEFFICIENT PICKLE FILE AND THE FOLDER IN WHICH THE "N" ALTERNATIVE STITCHED FRAMES ARE TO BE STITCHED] and it outputs the stitched tiles and also the Single Stiched RGB Image.                    
## Requirements 
The following python libraries are necessary to run the Map Stitching code:
  1) OpenCV
  2) Glob
  3) Numpy
  4) OS
  5) Pickle
  6) Connections
  7) Imutils
