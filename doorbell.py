import RPi.GPIO as GPIO
import pygame
import time

# config the setmode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO-pin for the doorbell botton
button_pin = 12

# Config the GPIO-pin for input
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the pygame mixer
pygame.mixer.init()

# function that plays the sound
def button_pressed():
    print("Button pressed")
    # Play the sound file
    pygame.mixer.music.load("deurbel.mp3")
    pygame.mixer.music.play()

# Detect the button with interrupt
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_pressed, bouncetime=300)

# run the script forever. 
while True:
    time.sleep(0.1)
