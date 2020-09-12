#!/bin/bash

### darknet original weights

# mkdir -p weights && cd weights

# wget -c https://pjreddie.com/media/files/yolov3.weights
# wget -c https://pjreddie.com/media/files/yolov3-tiny.weights
# wget -c https://pjreddie.com/media/files/yolov3-spp.weights

### darknet53 weights (first 75 layers only)

# wget -c https://pjreddie.com/media/files/darknet53.conv.74

### ultralytics google drive folder

## contains pjreddie's original weights, their pytorch versions,
## and new ultralytics pytorch weights

# https://drive.google.com/drive/folders/1uxgUBemJVw9wZsdpboYbzUN4bcRhsuAI

### new method (for ultralytics google drive folder)

## possible choices are present in models.py (line ~459)

python3 -c "from models import *;
attempt_download('weights/yolov3.pt');
attempt_download('weights/yolov3-spp.pt');
"
