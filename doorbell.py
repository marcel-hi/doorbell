import RPi.GPIO as GPIO
import pygame

# config the setmode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO-pin for the doorbell botton
drukknop_pin = 12

# Config the GPIO-pin for ibput
GPIO.setup(drukknop_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initilize the pygame mixer
pygame.mixer.init()

# function that play's the sound
def knop_ingedrukt(channel):
    print("Drukknop ingedrukt")
    # Speel het geluidsbestand af
    pygame.mixer.music.load("deurbel.mp3")
    pygame.mixer.music.play()

# Detect the button with interrupt
GPIO.add_event_detect(drukknop_pin, GPIO.FALLING, callback=knop_ingedrukt, bouncetime=300)

# run the script forever. 
while True:
    pass
