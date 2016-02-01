
import pygame, os, sys, random
from pygame.locals import *

directions = ('north', 'west', 'south', 'east')

def load_image(direction = 0):
    image = pygame.image.load('bird.jpg')
    image = pygame.transform.scale(image, (30,40))
    image = pygame.transform.rotate(image, 90 * direction)
    imgRect = image.get_rect()
    return image, imgRect

def get_flock():
    corners = [
        (int(480*.25), int(480*.25)),  # 0: top left
        (int(480*.75), int(480*.25)),  # 1: top right
        (int(480*.25), int(480*.75)),  # 2: bottom left
        (int(480*.75), int(480*.75))]  # 3: bottom right
    center = (int(480*.50),)*2  # shorthand: (n,)*3 == (n,n,n)
    flock = pygame.Surface((480,480))
    for i in corners:
        image, imgRect = load_image()
        imgRect.center = i
        flock.blit(image, imgRect)
    flock = pygame.transform.rotate(flock, 90* random.randint(0,3)) # rotates flock
    direction = random.randint(0,3)
    image, imgRect = load_image(direction)
    imgRect.center = center
    flock.blit(image, imgRect)
    return flock, directions[direction]

def quit():
    pygame.quit()
    sys.exit()

def check_event(event):
    if event.type == QUIT:
        quit()
    elif event.type == KEYDOWN:
        if event.key in (K_UP, K_w):
            return 'north'
        elif event.key in (K_RIGHT, K_d):
            return 'east'
        elif event.key in (K_DOWN, K_s):
            return 'south'
        elif event.key in (K_LEFT, K_a):
            return 'west'
        else: return None
    else: return None

def check_answer(inputDirection, centerDirection):
    print(inputDirection)
    print(centerDirection)
    return inputDirection == centerDirection















