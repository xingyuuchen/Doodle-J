from baseitem import BaseItem
from baseitem import ItemType
from random import randint
import pygame


class Rocket(BaseItem):

    def __init__(self, windowX: int, windowY: int, x, y, width=60, height=100,
                 imagePath='images/rocket.png'):
        super().__init__(imagePath, windowX, windowY, width, height)
        self._rect.x = x
        self._rect.y = y

        self.__offset = randint(10, 90)
        self.__mainBody = None  # 依附主体：板子还是doodle


    def getType(self) -> ItemType:
        return ItemType.ROCKET


    def draw(self, screen):
        if self.__mainBody is not None:     # 坐标依附到主体
            self._rect.bottom = self.__mainBody.getBottom()
            if self.__mainBody.getType() == ItemType.DOODLE:
                self._rect.left = self.__mainBody.getLeft()
            else:
                self._rect.left = self.__mainBody.getLeft() + self.__offset
        screen.blit(self._image, self._rect)


    def attachTo(self, sth):  # 依附在板子上或者doodle上
        self.__mainBody = sth
        if sth.getType() == ItemType.DOODLE:
            print("attach to doodle")
            img = pygame.image.load('images/rocket.png')
            self._image = pygame.transform.scale(img, (sth.getWidth(), sth.getHeight()))
            self._rect = self._image.get_rect()


    def getMainBody(self):
        return self.__mainBody
