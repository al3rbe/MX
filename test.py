import cv2 as cv
import numpy as np
import requests
import csv
import os
import sys
import time
import telepot
from PIL import Image
from pytesseract import image_to_string
import serial
import pynmea2
from datetime import datetime, date

# Assign the provided values
pbtxt_path = "model/graph.pbtxt"
model_path = "model/frozen_inference_graph.pb"
allowed_cars_csv = "allowed_cars.csv"
telegram_token = "5936642927:AAEZfbb9P8kWIVYPM24Gm7ESJcXNnXrKJy4"
security_chat_id = "5489923654"
serial_port = "/dev/ttyTHS1"

# Initialize constants
LABELS = ["null", "plate"]
API_URL = "https://api.platerecognizer.com/v1/plate-reader/"
os.environ['PLATE_RECOGNIZER_API_KEY'] = "7eec2921af56967a9076aaf25c107267c07a881d"

# Initialize the Telegram bot
bot = telepot.Bot(telegram_token)

# Initialize the GPS
baud_rate = 9600
gps_serial = serial.Serial(serial_port, baud_rate, timeout=5)

# Read the allowed cars list
allowed_cars = []
with open(allowed_cars_csv, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        allowed_cars.append({
            "plate": row[0],
            "expiry_date": datetime.strptime(row[1], '%d/%m/%Y'),
            "chat_id": row[2],
        })

# Initialize the plate detector
cvNet = cv.dnn.readNetFromTensorflow(model_path, pbtxt_path)

# Initialize the camera
cap = cv.VideoCapture(0)

# Initialize the last known GPS location
last_known_location = None

def parse_gps_data(line):
    global last_known_location
    try:
        if line.startswith("$GPGGA"):
            msg = pynmea2.parse(line)
            latitude = msg.latitude
            longitude = msg.longitude
            google_maps_link = create_google_maps_link(latitude, longitude)
            last_known_location = google_maps_link
            return google_maps_link
    except pynmea2.ParseError:
        print("Error parsing GPS data.")
    except Exception as e:
        print("Error: {}".format(e))
    return last_known_location

def send_telegram_message(chat_id, message, image_path):
    with open(image_path, 'rb') as f:
        bot.sendPhoto(chat_id, f, caption=message)

def create_google_maps_link(latitude, longitude):
    return "https://maps.google.com/maps?q={:.6f},{:.6f}".format(latitude, longitude)

while True:
    try:
        # Capture frame-by-frame
        ret, img = cap.read()
        rows = img.shape[0]
        cols = img.shape[1]
        cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
        cvOut = cvNet.forward()

        for detection in cvOut[0, 0, :, :]:
            score = float(detection[2])
            if score > 0.5:
                # Crop the detected plate
                left = int(detection[3] * cols)
                top = int(detection[4] * rows)
                right = int(detection[5] * cols)
                bottom = int(detection[6] * rows)
                cropped_plate = img[top:bottom, left:right]

                # Draw bounding box on the original image
                cv.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

                # Save the cropped plate image
                plate_filename = "plates/{}{}{}_{}.png".format(left, top, right, bottom)
                cv.imwrite(plate_filename, cropped_plate)

                # Apply OCR on the cropped plate
                plate_image = Image.open(plate_filename)
                ocr_result = image_to_string(plate_image, lang='eng')

                # Send the cropped plate to the API
                with open(plate_filename, 'rb') as f:
                    response = requests.post(
                        API_URL,
                        files=dict(upload=f),
                        headers={'Authorization': 'Token ' + os.environ['PLATE_RECOGNIZER_API_KEY']}
                    )

                # Check if the API response contains the expected data
                if 'results' in response.json() and len(response.json()['results']) > 0:
                    # Parse the API response
                    api_result = response.json()['results'][0]['plate']
                    api_confidence = response.json()['results'][0]['score']

                    allowed = False
                    owner_chat_id = None
                    expiry_date = None
                    for car in allowed_cars:
                        if car["plate"] == api_result:
                            allowed = date.today() <= car["expiry_date"].date()
                            owner_chat_id = car["chat_id"]
                            expiry_date = car["expiry_date"].strftime('%d/%m/%Y')
                            break

                    # Get GPS location
                    location = parse_gps_data(gps_serial.readline().decode('utf-8').strip())

                    # Create a message with the image and information
                    security_message = "API result: {}\nAPI confidence: {:.2f}%\nOCR result: {}\nPlate detection confidence: {:.2f}%\nAllowed: {}\nLocation: {}".format(
                        api_result, api_confidence * 100, ocr_result, score * 100, allowed, location)
                    
                    owner_message = "Your car {} is no longer authorized to park here. It was authorized up to {}. Location: {}".format(api_result, expiry_date, location)

                    # Send the cropped plate image with the information to the security
                    send_telegram_message(security_chat_id, security_message, plate_filename)

                    # Send a message to the owner if the car is not allowed
                    if not allowed and owner_chat_id is not None:
                        send_telegram_message(owner_chat_id, owner_message, plate_filename)

        # Display the resulting frame
        cv.imshow('frame', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print("Error: {}".format(e))

cap.release()
cv.destroyAllWindows()
import cv2 as cv
import numpy as np
import requests
import csv
import os
import sys
import time
import telepot
from PIL import Image
from pytesseract import image_to_string
import serial
import pynmea2
from datetime import datetime, date

# Assign the provided values
pbtxt_path = "model/graph.pbtxt"
model_path = "model/frozen_inference_graph.pb"
allowed_cars_csv = "allowed_cars.csv"
telegram_token = "5936642927:AAEZfbb9P8kWIVYPM24Gm7ESJcXNnXrKJy4"
security_chat_id = "5489923654"
serial_port = "/dev/ttyTHS1"

# Initialize constants
LABELS = ["null", "plate"]
API_URL = "https://api.platerecognizer.com/v1/plate-reader/"
os.environ['PLATE_RECOGNIZER_API_KEY'] = "7eec2921af56967a9076aaf25c107267c07a881d"

# Initialize the Telegram bot
bot = telepot.Bot(telegram_token)

# Initialize the GPS
baud_rate = 9600
gps_serial = serial.Serial(serial_port, baud_rate, timeout=5)

# Read the allowed cars list
allowed_cars = []
with open(allowed_cars_csv, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        allowed_cars.append({
            "plate": row[0],
            "expiry_date": datetime.strptime(row[1], '%d/%m/%Y'),
            "chat_id": row[2],
        })

# Initialize the plate detector
cvNet = cv.dnn.readNetFromTensorflow(model_path, pbtxt_path)

# Initialize the camera
cap = cv.VideoCapture(0)

# Initialize the last known GPS location
last_known_location = None

def parse_gps_data(line):
    global last_known_location
    try:
        if line.startswith("$GPGGA"):
            msg = pynmea2.parse(line)
            latitude = msg.latitude
            longitude = msg.longitude
            google_maps_link = create_google_maps_link(latitude, longitude)
            last_known_location = google_maps_link
            return google_maps_link
    except pynmea2.ParseError:
        print("Error parsing GPS data.")
    except Exception as e:
        print("Error: {}".format(e))
    return last_known_location

def send_telegram_message(chat_id, message, image_path):
    with open(image_path, 'rb') as f:
        bot.sendPhoto(chat_id, f, caption=message)

def create_google_maps_link(latitude, longitude):
    return "https://maps.google.com/maps?q={:.6f},{:.6f}".format(latitude, longitude)

while True:
    try:
        # Capture frame-by-frame
        ret, img = cap.read()
        rows = img.shape[0]
        cols = img.shape[1]
        cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
        cvOut = cvNet.forward()

        for detection in cvOut[0, 0, :, :]:
            score = float(detection[2])
            if score > 0.5:
                # Crop the detected plate
                left = int(detection[3] * cols)
                top = int(detection[4] * rows)
                right = int(detection[5] * cols)
                bottom = int(detection[6] * rows)
                cropped_plate = img[top:bottom, left:right]

                # Draw bounding box on the original image
                cv.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

                # Save the cropped plate image
                plate_filename = "plates/{}{}{}_{}.png".format(left, top, right, bottom)
                cv.imwrite(plate_filename, cropped_plate)

                # Apply OCR on the cropped plate
                plate_image = Image.open(plate_filename)
                ocr_result = image_to_string(plate_image, lang='eng')

                # Send the cropped plate to the API
                with open(plate_filename, 'rb') as f:
                    response = requests.post(
                        API_URL,
                        files=dict(upload=f),
                        headers={'Authorization': 'Token ' + os.environ['PLATE_RECOGNIZER_API_KEY']}
                    )

                # Check if the API response contains the expected data
                if 'results' in response.json() and len(response.json()['results']) > 0:
                    # Parse the API response
                    api_result = response.json()['results'][0]['plate']
                    api_confidence = response.json()['results'][0]['score']

                    allowed = False
                    owner_chat_id = None
                    expiry_date = None
                    for car in allowed_cars:
                        if car["plate"] == api_result:
                            allowed = date.today() <= car["expiry_date"].date()
                            owner_chat_id = car["chat_id"]
                            expiry_date = car["expiry_date"].strftime('%d/%m/%Y')
                            break

                    # Get GPS location
                    location = parse_gps_data(gps_serial.readline().decode('utf-8').strip())

                    # Create a message with the image and information
                    security_message = "API result: {}\nAPI confidence: {:.2f}%\nOCR result: {}\nPlate detection confidence: {:.2f}%\nAllowed: {}\nLocation: {}".format(
                        api_result, api_confidence * 100, ocr_result, score * 100, allowed, location)
                    
                    owner_message = "Your car {} is no longer authorized to park here. It was authorized up to {}. Location: {}".format(api_result, expiry_date, location)

                    # Send the cropped plate image with the information to the security
                    send_telegram_message(security_chat_id, security_message, plate_filename)

                    # Send a message to the owner if the car is not allowed
                    if not allowed and owner_chat_id is not None:
                        send_telegram_message(owner_chat_id, owner_message, plate_filename)

        # Display the resulting frame
        cv.imshow('frame', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print("Error: {}".format(e))

cap.release()
cv.destroyAllWindows()
