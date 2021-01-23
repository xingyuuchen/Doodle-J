from baseitem import BaseItem
from baseitem import ItemType
from random import randint


class Spring(BaseItem):

    def __init__(self, windowX: int, windowY: int, width=50, height=40,
                 imagePath='images/spring.png'):
        super().__init__(imagePath, windowX, windowY, width, height)

        self.__offset = randint(10, 90)
        self.__mainBody = None  # 依附主体：板子还是doodle


    def getType(self) -> ItemType:
        return ItemType.SPRING


    def draw(self, screen):
        if self.__mainBody is not None:     # 坐标依附到主体
            self._rect.left = self.__mainBody.getLeft() + self.__offset
            self._rect.bottom = self.__mainBody.getTop()
        screen.blit(self._image, self._rect)


    def attachTo(self, sth):  # 依附在板子上
        self.__mainBody = sth
