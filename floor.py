from math import fabs
from random import randint
from baseitem import BaseItem
from baseitem import ItemType
from rocket import Rocket
from spring import Spring


class Floor(BaseItem):
    lastHeight = 0

    def __init__(self, windowX: int, windowY: int, width=120, height=30,
                 isNew=False, isMoving=False, imagePath='images/floor.png'):
        super().__init__(imagePath, windowX, windowY, width, height)

        self.__isMoving = isMoving  # 地板是否左右移动

        currHeight = Floor.lastHeight + randint(70, 90)
        self._rect.x = randint(0, windowX - width)
        self._rect.y = 50 if isNew else windowY - currHeight
        Floor.lastHeight = currHeight

        # 板子上面的东西：火箭 弹簧 怪物 等...
        self.__itemOn = None
        if randint(0, 100) < 50:
            self.__itemOn = Spring(windowX, windowY)
            self.__itemOn.attachTo(self)
        if randint(0, 100) < 5:
            self.__itemOn = Rocket(windowX, windowY, self.getLeft(), self.getTop())
            self.__itemOn.attachTo(self)

    def draw(self, screen):
        screen.blit(self._image, self._rect)
        if self.__itemOn is not None:
            self.__itemOn.draw(screen)


    def getItemOn(self):
        return self.__itemOn

    def isDoodleLandOn(self, x: int, y: int, deltaY=0) -> bool:
        if x < self.getLeft() or x > self.getRight():
            return False
        if self.isDoodleLandOnItemOn(x, y):
            return True
        if deltaY < 0:
            return False
        if fabs(y - self.getCenterY()) < 3:
            return True
        if fabs(y + deltaY - self.getCenterY()) < 3:
            return True
        return False

    def isDoodleLandOnItemOn(self, x: int, y: int) -> bool:
        if self.__itemOn is not None:
            if self.__itemOn.getLeft() < x < self.__itemOn.getRight() \
                    and self.__itemOn.getBottom() < y < self.__itemOn.getTop():
                return True
        return False

    def getLandOnItemType(self) -> ItemType:  # 获取涂鸦跳到此地板上的东西
        if self.__itemOn is not None:
            return self.__itemOn.getType()
        return ItemType.FLOOR

    def getType(self) -> ItemType:
        return ItemType.FLOOR


    @staticmethod
    def setLastHeight(newLastHeight):
        Floor.lastHeight = newLastHeight
