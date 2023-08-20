# SSD Plate Detection System: Robotic License Plate Verification in Parking Lots

This repository contains the project 
**Design and Development of a Robotic System for License Plate Verification in Parking Lots using a Single Shot Detector and ArduRover** by

1. **Mohammed Alhubail**
2. **Ascandar Alfort**

Submitted to King Fahd University of Petroleum and Minerals, College of Engineering and physics, Department of Control & Instrumentation Engineering.

![Project Image](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-20-03-42-43%203.jpg?raw=true)

## Abstract

The project presents an innovative robotic system designed to enhance parking lot management through automated license plate detection and authorization verification. It employs advanced image processing techniques, the Single Shot Detector (SSD) algorithm for accurate license plate recognition, and an autonomous navigation system using ArduoRover. The system aims to streamline parking operations and improve security by preventing unauthorized parking.

## Introduction

With the rise in urbanization and technological advancements, managing parking facilities has become challenging. This project focuses on developing a robotic system to address modern parking lot management complexities. The system aims to detect license plates accurately and verify if a parked car is authorized to occupy a designated parking space. The integration of image processing techniques, the SSD algorithm, and ArduoRover technology offer a comprehensive solution for parking lot management.
![PHOTO-2023-08-09-23-09-22](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-09-23-09-22.jpg?raw=true)

## Literature Review

### License Plate Detection and Image Processing:

License plate detection is crucial for vehicle identification and parking management. With advancements in deep learning and image processing, techniques like convolutional neural networks (CNNs) have shown significant results in detecting license plates within complex scenes.

### Single Shot Detector (SSD) Algorithm:

The SSD algorithm, known for balancing speed and accuracy, is suitable for detecting license plates, which can vary in size due to distance and angle.
![1-s2.0-S1077314219301328-gr2.jpg](https://github.com/al3rbe/MX/blob/main/pic/1-s2.0-S1077314219301328-gr2.jpg?raw=true)

### Autonomous Navigation Using ArduoRover:

ArduoRover, an open-source platform for rover-type robots, provides a framework for implementing autonomous navigation systems. It uses sensor data, GPS information, and preconfigured maps to ensure safe movement within dynamic environments.

![mp_mission_planning.jpeg](https://github.com/al3rbe/MX/blob/main/pic/mp_mission_planning.jpeg?raw=true)

mp_mission_planning.jpeg

## ROS Integration

The project integrates with the Robot Operating System (ROS) to manage the robotic components and ensure seamless communication between different parts of the system. ROS provides tools, libraries, and conventions to simplify the task of creating complex and robust robot behavior across a wide variety of robotic platforms.

### Setting up ROS:

1. **Install ROS**:
   Follow the official ROS installation guide for your specific operating system.

2. **Create a ROS Workspace**:
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```
3. **Clone the Repository into the ROS Workspace:**
```bash
cd ~/catkin_ws/src/
git clone https://github.com/al3rbe/MX
```
4. **Build the Project:**
```bash
cd ~/catkin_ws/
catkin_make
```
5. **Source the Workspace:**
```bash
source devel/setup.bash
```
6. **Launch the Robotic System:**
```bash
   roslaunch SSD-tank mxproject.launch
```
![PHOTO-2023-08-02-22-43-22](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-02-22-43-22.jpg?raw=true)
![PHOTO-2023-08-02-22-43-22 2](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-02-22-43-22%202.jpg?raw=true)

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
  
![PHOTO-2023-08-07-23-59-12](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-07-23-59-12.jpg?raw=true)

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
![PHOTO-2023-08-16-22-09-59](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-16-22-09-59.jpg?raw=true)
## Additional Information
1. The system uses a pre-trained model located in the model directory.
2. Detected plates are saved in the plates directory.
3. The list of allowed cars is stored in allowed_cars.csv.
4. The system uses the Plate Recognizer API for additional plate recognition. Ensure you have set up the API key in the environment variables.
