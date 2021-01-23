import pygame
from enum import Enum


class ItemType(Enum):
    DOODLE = 1
    FLOOR = 2
    MONSTER = 3
    SPRING = 4
    ROCKET = 5



class BaseItem:

    def __init__(self, imagePath: str, windowX: int,
                 windowY: int, width, height):
        img = pygame.image.load(imagePath)
        self._image = pygame.transform.scale(img, (width, height))
        self._rect = self._image.get_rect()

        self._windowX = windowX
        self._windowY = windowY

    def getType(self) -> ItemType:
        raise NotImplementedError('you must impl getType() when subclassing BaseItem.')

    def draw(self, screen):
        raise NotImplementedError('you must impl draw() when subclassing BaseItem.')


    def getRect(self):
        return self._rect

    def moveY(self, y):
        self._rect.y += y

    def getLeft(self):
        return self._rect.left

    def getRight(self):
        return self._rect.right

    def getCenterY(self):
        return self._rect.centery

    def getCenterX(self):
        return self._rect.centerx

    def getWidth(self):
        return self._rect.width

    def getHeight(self):
        return self._rect.height

    def getBottom(self):
        return self._rect.bottom

    def getTop(self):
        return self._rect.top

    def getX(self):
        return self._rect.x

    def getY(self):
        return self._rect.y

    def isOutOfScreen(self):
        if self._rect.bottom > self._windowY or self._rect.top < 0:
            return True
        return False
