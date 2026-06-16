# Real-Time-Hand-Gesture-Recognition-Using-Deep-Learning
 Real-Time Hand Gesture Recognition Using Deep Learning is a system that detects and classifies hand gestures from a live video feed using a webcam. It uses Convolutional Neural Networks (CNNs) and OpenCV to recognize gestures like thumbs up, stop, or peace in real time. 

# Gesture Dataset Collection Script
This script is used to collect hand gesture images through a webcam for training a computer vision or gesture recognition model. It captures images from a predefined Region of Interest (ROI) and saves them into a dataset folder corresponding to a specific gesture class.

## Features

* Captures real-time video using OpenCV.
* Defines a fixed Region of Interest (ROI) where the user should place their hand gesture.
* Automatically creates a dataset folder for the selected gesture ID.
* Saves captured gesture images in JPEG format.
* Displays the number of images collected during the capture process.
* Allows manual image capture for better dataset quality.

## Working

1. The webcam is initialized using OpenCV.

2. A rectangular ROI is displayed on the screen.

3. The user places their hand gesture inside the ROI.

4. Press the **'c'** key to capture and save an image.

5. Images are stored in the directory:

   ```
   dataset/<gesture_id>/
   ```

6. The process continues until the required number of images is collected or the user presses **'q'** to quit.

## Controls

| Key | Action                                 |
| --- | -------------------------------------- |
| c   | Capture and save current gesture image |
| q   | Quit dataset collection                |

## Parameters

* `gesture_id` : Unique identifier for the gesture class.
* `num_images` : Total number of images to collect.
* `save_path` : Directory where captured images are stored.

## Output

The script generates a structured dataset where each gesture has its own folder containing captured images. This dataset can later be used for training gesture recognition models using machine learning or deep learning techniques.

## Requirements

* Python 3.x
* OpenCV (`cv2`)
* Webcam

## Example

For `gesture_id = 6`, the captured images will be saved in:

```
dataset/6/
```

with filenames:

```
0.jpg
1.jpg
2.jpg
...
299.jpg
```

This script is an important first step in building a hand gesture recognition system, ensuring consistent and organized data collection for model training.
