# simple ellipse or rectangle for buttons

class SimpleButton:

    def __init__(self, width=30, height=30):
        self.posX = 200
        self.posY = 200
        self.width = width
        self.height = height

    def move(self, x, y):
        self.posX = x
        self.posY = y

    def draw(self):
        pass

    def isInside(self, x: int, y: int):
        if self.posX < x and x < (self.posX + self.width):
            if self.posY < y and y < (self.posY + self.height):
                return True
        return False
        

class RectButton(SimpleButton):

    def __init__(self, width, height):
        super().__init__(width, height)

    def draw(self, painter):
        painter.save()
        painter.translate(self.posX - self.width/2, self.posY - self.height/2)
        painter.drawRect(0, 0, self.width, self.height)
        painter.restore()


class EllipseButton(SimpleButton):

    def __init__(self, width, height):
        super().__init__(width, height)

    def draw(self, painter):
        painter.save()
        painter.translate(self.posX - self.width/2, self.posY - self.height/2)
        painter.drawEllipse(0, 0, self.width, self.height)
        painter.restore()
