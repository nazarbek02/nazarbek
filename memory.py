from turtle import update
from pygame import *
from random import randint 
from time import time as timer
 
window = display.set_mode((700, 500)) 
display.set_caption('Shooter') 
background = transform.scale(image.load('galaxy.jpg'), (700, 500)) 
 
mixer.init() 
mixer.music.load('space.ogg') 
mixer.music.play() 
 
clock = time.Clock() 
 
 
