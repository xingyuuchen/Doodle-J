import sys
import os
import pygame
from doodle import Doodle
from screen import Screen
from floor import Floor


def mainLoop(photoPath='images/cxy.png'):
    Floor.setLastHeight(0)

    screen = Screen('images/bg.jpg')
    X = screen.getWindowX()
    Y = screen.getWindowY()
    doodle = Doodle(photoPath, 'piepie', X, Y, 180, 250)

    screen.setDoodle(doodle)

    clock = pygame.time.Clock()
    while True:
        clock.tick(Screen.getFps())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exit game.")
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    doodle.setMovingDir(-1)
                    print("left")
                elif event.key == pygame.K_RIGHT:
                    doodle.setMovingDir(1)
                    print("right")
            elif event.type == pygame.KEYUP:
                doodle.setMovingDir(0)

        screen.step()

        if not doodle.isAlive():
            return True



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('\nusage: python main.py {your photo file path}')
        exit()
    avatarPath = sys.argv[1]
    if not os.path.isfile(avatarPath):
        print('\nyour file does NOT exists: ' + avatarPath)
        exit()

    pygame.init()
    while True:
        print("new game")
        if not mainLoop(avatarPath):
            break
