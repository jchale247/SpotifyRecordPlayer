import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

#try to write url to rfid tag
try:
    text = input('Spotify URL: ')
    print("place tag above reader")
    reader.write(text)
    print("Written Successfully")
finally:
    GPIO.cleanup()
