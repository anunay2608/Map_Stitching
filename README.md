# Map_Stitching
Map Stitching or Mosaicing is a task of composing and stitching multiple images with narrow but overlapping fields of aerial views to create a larger image with a wider field of view covering a large area in a single RGB image.
The process of map stitching involves following tasks : 
  1) Finding the common feature points between two images, from where the two images are to be stitched.
  2) Checking the stitching condition, i.e. find if the features found are greater than the minimum number of features to be extracted.
  3) Stitching the two images from the common feature points line as a single image.that produces strong visual distortion intended to create a wide panoramic or hemispherical image. 
  4) At last it includes the cropping and final finishing part which includes the removal of additional black background from the final image to make it a attractive final image.

## Fisheye :
  We have created the fisheye file to remove the FISHEYE effect which is most commonly seen in approximately all cameras, resulting in the strong visual distortion intended to create a wide panoramic or hemispherical image. For doing the same we have to click the variable images of the chessboard printout taken on any A4 size sheet and then running the code Fisheye.py for the same. Fisheye.py returns 2 pickle file consisting of Camera Matrix and the Distortion Coefficient values hich perticularly depends on the camera itself.

# Stitcher : 
  
# Requirements 
The following python libraries are necessary to run the Map Stitching code:
  1) OpenCV
  2) Glob
  3) Numpy
  4) OS
  5) Pickle

