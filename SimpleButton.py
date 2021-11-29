# simple clickable buttons, sliders, etc


class CollisionRect:

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
        if (self.posX - self.width/2) < x and x < (self.posX + self.width/2):
            if (self.posY - self.height/2) < y and y < (self.posY + self.height/2):
                return True
        return False
        

class RectButton(CollisionRect):

    def __init__(self, width, height):
        super().__init__(width, height)

    def draw(self, painter):
        painter.save()
        painter.translate(self.posX - self.width/2, self.posY - self.height/2)
        painter.drawRect(0, 0, self.width, self.height)
        painter.restore()


class EllipseButton(CollisionRect):

    def __init__(self, width, height):
        super().__init__(width, height)

    def draw(self, painter):
        painter.save()
        painter.translate(self.posX - self.width/2, self.posY - self.height/2)
        painter.drawEllipse(0, 0, self.width, self.height)
        painter.restore()

class PassiveSlider(CollisionRect):

    def __init__(self, width=150, height=30):
        self.position = 0
        self.max = width
        super().__init__(width=width, height=height)

    def setPosition(self, pos):
        '''pos: int  a 0.0->1.0 value for the slider position'''
        self.position = int(pos * self.max)

    def draw(self, painter):
        gap = 1 # tooths' gap
        tooth_w = 10
        painter.save()
        painter.translate(self.posX - self.width/2, self.posY - self.height/2)
        painter.drawLine(0, self.height/2, self.width, self.height/2)
        painter.drawRect(0 + self.position - gap - tooth_w, 0 + self.height/2,
                         tooth_w, self.height
                         )
        painter.drawRect(0 + self.position + gap, 0 + self.height/2,
                         tooth_w, self.height
                         )
        painter.restore()
