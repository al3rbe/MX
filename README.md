# SSD Plate Detection System

This project is designed to detect vehicle plates using the SSD (Single Shot MultiBox Detector) method. It captures images from a camera, detects plates, and then uses OCR (Optical Character Recognition) to read the plate numbers. Detected plates are then checked against an allowed list, and notifications are sent via Telegram. Additionally, the system integrates with a GPS module to provide the location of detected vehicles.
![PHOTO-2023-08-20-03-42-43 3](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-20-03-42-43%203.jpg?raw=true)

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
![PHOTO-2023-08-07-23-59-12](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-07-23-59-12.jpg?raw=true)

1. **Clone the Repository**: 
   Clone the repository or download the project files to your Jetson Nano.

2. **Navigate to the Project Directory**:
```bash
cd ssd-plate_detection
```
![PHOTO-2023-08-09-23-09-15](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-09-23-09-15.jpg?raw=true)

3. **Run the Detection Script**:
   
   To run the detection script, copy and paste the following command into your terminal:

   ```bash
   python test.py

## Troubleshooting

If you encounter any permission errors related to the serial port, you can grant the necessary permissions using the following command:

```bash
sudo chmod 777 /dev/ttySH1
```
![PHOTO-2023-08-09-23-09-22](https://github.com/al3rbe/MX/blob/main/pic/PHOTO-2023-08-09-23-09-22.jpg?raw=true)

**Note**: You might be prompted for the password for the Jetson Nano. The password is `1111`.

## Additional Information

- The system uses a pre-trained model located in the `model` directory.
- Detected plates are saved in the `plates` directory.
- The list of allowed cars is stored in `allowed_cars.csv`.
- The system uses the Plate Recognizer API for additional plate recognition. Ensure you have set up the API key in the environment variables.

