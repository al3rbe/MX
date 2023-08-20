# SSD Plate Detection System: Robotic License Plate Verification in Parking Lots

This repository contains the project "Design and Development of a Robotic System for License Plate Verification in Parking Lots using a Single Shot Detector and ArduRover" by Ascandar Alfort and Mohammed Alhubail, submitted to King Fahd University of Petroleum and Minerals, College of Engineering and physics, Department of Control & Instrumentation Engineering.

![Project Image](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-20-03-42-43%203.jpg?raw=true)

## Abstract

The project presents an innovative robotic system designed to enhance parking lot management through automated license plate detection and authorization verification. It employs advanced image processing techniques, the Single Shot Detector (SSD) algorithm for accurate license plate recognition, and an autonomous navigation system using ArduoRover. The system aims to streamline parking operations and improve security by preventing unauthorized parking.

## Introduction

With the rise in urbanization and technological advancements, managing parking facilities has become a challenge. This project focuses on developing a robotic system to address modern parking lot management complexities. The system aims to detect license plates accurately and verify if a parked car is authorized to occupy a designated parking space. The integration of image processing techniques, the SSD algorithm, and ArduoRover technology offers a comprehensive solution for parking lot management.

## Literature Review

### License Plate Detection and Image Processing:

License plate detection is crucial for vehicle identification and parking management. With advancements in deep learning and image processing, techniques like convolutional neural networks (CNNs) have shown significant results in detecting license plates within complex scenes.

### Single Shot Detector (SSD) Algorithm:

The SSD algorithm, known for balancing speed and accuracy, is suitable for detecting license plates, which can vary in size due to distance and angle.

### Autonomous Navigation Using ArduoRover:

ArduoRover, an open-source platform for rover-type robots, provides a framework for implementing autonomous navigation systems. It uses sensor data, GPS information, and preconfigured maps to ensure safe movement within dynamic environments.

## Prerequisites

- OpenCV (cv2)
- NumPy
- requests
- csv
- os, sys, time
- telepot (for Telegram integration)
- PIL (Python Imaging Library)
- pytesseract (for OCR)
- serial (for GPS integration)
- pynmea2 (for parsing NMEA sentences from GPS)

## Setup

1. **Clone the Repository**: 
   Clone the repository or download the project files to your Jetson Nano.

2. **Navigate to the Project Directory**:
```bash
cd ssd-plate_detection
```
3. **Run the Detection Script**:
   To run the detection script, copy and paste the following command into your terminal:
```bash
python test.py
```
## Troubleshooting
If you encounter any permission errors related to the serial port, you can grant the necessary permissions using the following command:
```bash
sudo chmod 777 /dev/ttyTHS1
```
**NOTE**
You might be prompted for the password for the Jetson Nano. The password is '1111'.

## Additional Information
1. The system uses a pre-trained model located in the model directory.
2. Detected plates are saved in the plates directory.
3. The list of allowed cars is stored in allowed_cars.csv.
4. The system uses the Plate Recognizer API for additional plate recognition. Ensure you have set up the API key in the environment variables.
