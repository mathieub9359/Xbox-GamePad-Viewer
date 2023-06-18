#!/usr/bin/python3

import XInput
import time
import math 
import pygame
import sys
import os



def buttonPress(buttons_pressed : dict, screen, left_bumper_image, right_bumper_image):
        if buttons_pressed["X"]:
            pygame.draw.circle(screen, (0,0,255), (330, 223), 18)

        if buttons_pressed["A"]:
            pygame.draw.circle(screen, (0,255,0), (363, 253), 18)

        if buttons_pressed["B"]:
            pygame.draw.circle(screen, (255,0,0), (396, 223), 18)

        if buttons_pressed["Y"]:
            pygame.draw.circle(screen, (255,255,0), (363, 191), 18)

        if buttons_pressed["LEFT_SHOULDER"]:
            screen.blit(left_bumper_image, (61,126))

        if buttons_pressed["RIGHT_SHOULDER"]:
            screen.blit(right_bumper_image, (303,126))

        if buttons_pressed["DPAD_UP"]:
            pygame.draw.rect(screen, (0,0,0), (169,263, 25, 32))

        if buttons_pressed["DPAD_LEFT"]:
            pygame.draw.rect(screen, (0,0,0), (145, 285, 35, 24))

        if buttons_pressed["DPAD_RIGHT"]:
            pygame.draw.rect(screen, (0,0,0), (180, 285, 35, 24))

        if buttons_pressed["DPAD_DOWN"]:
            pygame.draw.rect(screen, (0,0,0), (169, 299, 25, 32))

        if buttons_pressed["BACK"]:
            pygame.draw.circle(screen, "green", (207,222), 11)
        
        if buttons_pressed["START"]:
            pygame.draw.circle(screen, "green", (276,222), 11)



def joystickPosition(joysitck_positions : tuple, buttons_pressed, screen):

    #Drawing the right joystick.
    if buttons_pressed["RIGHT_THUMB"]:
        pygame.draw.circle(screen, "red", (303 + joysitck_positions[1][0]*8, 293 - joysitck_positions[1][1]*8), 19)
    else: 
        pygame.draw.circle(screen, "black", (303 + joysitck_positions[1][0]*8, 293 - joysitck_positions[1][1]*8), 19)

    #Drawing the left joystick.
    if buttons_pressed["LEFT_THUMB"]:
        pygame.draw.circle(screen, "red", (121 + joysitck_positions[0][0]*8, 222 - joysitck_positions[0][1]*8), 19)
    else:
        pygame.draw.circle(screen, "black", (121 + joysitck_positions[0][0]*8, 222 - joysitck_positions[0][1]*8), 19)

def triggerPress(trigger_data : tuple, screen):
    initial_left_trigger = pygame.draw.rect(screen, "grey",(81, 16, 63, 105))
    initial_right_trigger = pygame.draw.rect(screen, "grey", (335, 16, 63, 105))

    left_trigger = pygame.Surface((63, 105))
    right_trigger = pygame.Surface((63, 105))
    
    left_trigger.set_alpha(255*trigger_data[0])
    right_trigger.set_alpha(255*trigger_data[1])

    left_trigger.fill("black")
    right_trigger.fill("black")

    screen.blit(left_trigger, (81, 16))
    screen.blit(right_trigger, (335, 16))

def joystickLayout(joysitck_positions : tuple, screen):
    pygame.draw.circle(screen, "black", (650,223), 140, width=3)
    pygame.draw.circle(screen, "red", (650 + joysitck_positions[0][0]*138, 223 - joysitck_positions[0][1]*138), 5)



def display():
    pygame.init()

    cwd = os.getcwd()
    
    screen = pygame.display.set_mode((800,446))
    pygame.display.set_caption("Controller Inputs")

    image = pygame.image.load(cwd+ "/Images/controller.png")
    left_bumper_image = pygame.image.load(cwd + "/Images/left_bumper.png")
    right_bumper_image = pygame.image.load(cwd+ "/Images/right_bumper.png")
    
    clock = pygame.time.Clock()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill("white")
    
        screen.blit(image, (0,0))

        controller = XInput.get_state(0)
        buttons_pressed = XInput.get_button_values(controller)
        joystick_positions = XInput.get_thumb_values(controller)
        trigger_data = XInput.get_trigger_values(controller)

        buttonPress(buttons_pressed, screen, left_bumper_image, right_bumper_image)
        joystickPosition(joystick_positions, buttons_pressed, screen)
        triggerPress(trigger_data, screen)

        joystickLayout(joystick_positions, screen)

        pygame.display.update()
        clock.tick(30)


def main():
    print(sys.path)
    display()
 

if __name__ == "__main__":
    main()