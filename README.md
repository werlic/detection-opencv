# Implementation Object Detection with Own Cascade in OpenCV

Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

This repository is implementation object detection using haar feature cascade from method/algorithm Viola Jones.

Package required: *OpenCV*

Before running program, you must have own cascade trained with dataset.
1. Test image
2. Own Cascade file
<br>
### change value in this variable with own path to image file :
```
img_path = '<path_to_your_img>'
```
<br>
### change value in this variable with own path to cascade :
```
cascade_path = '<path_to_your_cascade>'
```

## Running Program
```
python detect.py
```