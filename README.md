# Map_Stitching
Map Stitching or Mosaicing is a task of composing and stitching multiple images with narrow but overlapping fields of aerial views to create a larger image with a wider field of view covering a large area in a single RGB image.
The process of map stitching involves following tasks : 
  1) Finding the common feature points between two images, from where the two images are to be stitched.
  2) Checking the stitching condition, i.e. find if the features found are greater than the minimum number of features to be extracted.
  3) Stitching the two images from the common feature points line as a single image.
  4) At last it includes the cropping and final finishing part which includes the removal of additional black background from the final image to make it a attractive final image.

