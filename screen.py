import pygame
from floor import Floor
from baseitem import ItemType


class Screen:

    def __init__(self, bgFilePath: str):
        raw_bg = pygame.image.load(bgFilePath)
        raw_bg_size = raw_bg.get_rect().size    # 原始图片大小
        self.__ratio = raw_bg_size[1] / raw_bg_size[0]
        self.__windowX = 500
        self.__windowY = int(self.__windowX * self.__ratio)
        self.__bg = pygame.transform.scale(raw_bg, (self.__windowX, self.__windowY))
        self.__screen = pygame.display.set_mode((self.__windowX, self.__windowY))
        pygame.display.set_caption("PiePie Jump")

        self.__screen.blit(self.__bg, (0, 0))

        self.__doodle = None
        self.__floors = set()


        for i in range(10):
            flr = Floor(self.getWindowX(), self.getWindowY())
            self.addFloor(flr)

        self.__magicLine = 500


    def addFloor(self, floor: Floor):
        self.__floors.add(floor)
        floor.draw(self.__screen)
        pygame.display.update()


    def setDoodle(self, doodle):
        self.__doodle = doodle
        self.__doodle.draw(self.__screen)
        pygame.display.update()


    def step(self):
        self.__doodle.move()

        if self.__doodle.getTop() <= self.__magicLine:
            if self.__doodle.getSpeedY() < 0:
                self.__doodle.reachMagicLine()
                self.__doodle.increaseScore()
            else:
                self.__doodle.leaveMagicLine()

        if self.__doodle.isAtMagicLine():
            for floor in self.__floors:
                floor.moveY(-self.__doodle.getSpeedY())

        for floor in list(self.__floors):
            if floor.isDoodleLandOn(self.__doodle.getCenterX(), self.__doodle.getBottom(), self.__doodle.getSpeedY()):
                # 看看是掉到了什么东西上
                if floor.getLandOnItemType() == ItemType.ROCKET:
                    self.__doodle.landOnRocket(floor.getItemOn())
                elif floor.getLandOnItemType() == ItemType.SPRING:
                    self.__doodle.landOnSpring()
                elif floor.getLandOnItemType() == ItemType.FLOOR:
                    self.__doodle.landOnFloor()
            if floor.isOutOfScreen():
                self.__floors.remove(floor)
                self.__floors.add(Floor(self.getWindowX(), self.getWindowY(), isNew=True))

        self.drawAll()
        pygame.display.update()



    def drawAll(self):
        self.__screen.blit(self.__bg, (0, 0))

        if self.__doodle is not None:
            self.__doodle.draw(self.__screen)
        for floor in self.__floors:
            # pygame.draw.line(self.__screen, (255, 0, 0),
            #                  (0, floor.getHeight()), (self.__windowX, floor.getHeight()), 3)
            floor.draw(self.__screen)
        # pygame.draw.line(self.__screen, (255, 0, 0), (0, self.__magicLine), (self.__windowX, self.__magicLine))


    def getWindowX(self) -> int:
        return self.__windowX


    def getWindowY(self) -> int:
        return self.__windowY

    def getSurface(self):
        return self.__screen


    @staticmethod
    def getFps() -> int:
        return 90

