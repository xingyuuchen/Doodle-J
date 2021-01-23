from baseitem import BaseItem
from baseitem import ItemType
from pygame import font


class Doodle(BaseItem):

    def __init__(self, imagePath: str, playerName, windowX, windowY, scaleX, scaleY):
        super().__init__(imagePath, windowX, windowY, scaleX, scaleY)

        self._rect = self._rect.move(windowX / 2, windowY - 400)

        self.__playerName = playerName
        self.__isAlive = True

        self.__speedHorizontal = 3
        self.__initSpeedY = -6      # 弹一下的起始y速度
        self.__speedY = self.__initSpeedY
        self.__speedX = 0
        self.__accelerationX = 0.03
        self.__accelerationY = 0.05

        self.__movingDir = 0  # -1左 0不动 1右

        self.__font = font.SysFont("Courier New", 35)
        self.__baseText = "Score: "
        self.__score = 0
        self.__scoreText = self.__font.render(self.__baseText + str(self.__score), True, (255, 0, 0))
        self.__scoreRect = self.__scoreText.get_rect()
        self.__scoreRect.x = 10
        self.__scoreRect.y = 10

        self.__isAtMagicLine = False

        self.__rocket = None
        self.__flying_time = 500
        self.__rocketSpeed = -12


    def draw(self, screen):
        screen.blit(self._image, self._rect)
        screen.blit(self.__scoreText, self.__scoreRect)
        if self.__rocket is not None:
            self.__rocket.draw(screen)


    def move(self):
        # y轴方向
        if self.__rocket is None:
            self.__speedY += self.__accelerationY
        else:
            self.__flying_time -= 1
            if self.__flying_time < 0:
                self.leaveRocket()

        self._rect = self._rect.move(self.__speedX, 0 if self.__isAtMagicLine else self.__speedY)

        # x轴方向
        if self.__movingDir == 0:
            if self.__speedX < 0:
                self.__speedX += self.__accelerationX
                if self.__speedX > 0:
                    self.__speedX = 0
            elif self.__speedX > 0:
                self.__speedX -= self.__accelerationX
                if self.__speedX < 0:
                    self.__speedX = 0

        if self.isOutOfScreen():
            self.__isAlive = False
            print("DEAD!!!!!!")


    def landOnFloor(self):
        print("land on floor")
        self.__speedY = self.__initSpeedY

    def landOnSpring(self):
        print("land on spring")
        self.__speedY = -12

    def landOnRocket(self, rocket):
        print("land on rocket")
        self.__speedY = self.__rocketSpeed
        self.__flying_time = 500
        self.__rocket = rocket
        rocket.attachTo(self)

    def leaveRocket(self):
        self.__flying_time = 0
        self.__rocket = None

    def reachMagicLine(self):
        self.__isAtMagicLine = True

    def leaveMagicLine(self):
        self.__isAtMagicLine = False

    def isAtMagicLine(self):
        return self.__isAtMagicLine


    def increaseScore(self):
        self.__score += int(-1 * self.__speedY)
        self.__scoreText = self.__font.render(
            self.__baseText + str(self.__score), True, (255, 0, 0))


    def setMovingDir(self, direction: int):
        self.__movingDir = direction
        if direction != 0:
            self.__speedX = direction * self.__speedHorizontal


    def getSpeedY(self):
        return self.__speedY

    def isAlive(self):
        return self.__isAlive


    def getType(self) -> ItemType:
        return ItemType.DOODLE
