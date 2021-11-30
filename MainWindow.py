"""Simple pomodoro window with PyQt5."""

import sys

from PyQt5.QtCore import QCoreApplication, QTimer, Qt
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtGui import QMouseEvent, QPaintEvent
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication

import SimpleButton
import PomodoTimer

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__(None, Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        self.dragPosition = None
        self.posx = 700
        self.posy = 500
        self.width = 500
        self.height = 500
        self.title = 'Pomodoro'
        self.background = QPixmap('image/pomodo_bkg_02.png')
        if self.background:
            self.width = self.background.width()
            self.height = self.background.height()

        self.setWindowTitle(self.title)
        self.setGeometry(self.posx, self.posy, self.width, self.height)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # init window assets
        self.stop_button = SimpleButton.RectButton(48, 48)
        self.stop_button.move(176,240)
        self.start_button = SimpleButton.RectButton(48, 48)
        self.start_button.move(336,240)
        self.time_slider = SimpleButton.PassiveSlider()
        self.time_slider.move(256,370)

        # timer
        self.pom_timer = PomodoTimer.PomodoTimer()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(500)

        # add quit to keyboard shortcut
        quitAction = QAction(self.tr("E&xit"), self)
        quitAction.setShortcut(self.tr("Ctrl+Q"))
        quitAction.triggered.connect(QCoreApplication.quit)
        self.addAction(quitAction)

        # add start/stop timer to keyboard shortcut
        startstopAction = QAction(self.tr("S&tart/S&top"), self)
        startstopAction.setShortcut(self.tr("Space"))
        startstopAction.triggered.connect(self.pom_timer.pause)
        self.addAction(startstopAction)

        self.setToolTip("Ctrl-Q for Quit.\nMove tomato with left mouse button.")

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self.dragPosition = a0.globalPos() - self.frameGeometry().topLeft()
            print(a0.localPos())
            if self.time_slider.isInside(a0.localPos().x(), a0.localPos().y()):
                print("paused")
                self.pom_timer.pause()
            if self.stop_button.isInside(a0.localPos().x(), a0.localPos().y()):
                print("Stop.")
                self.pom_timer.stop()
                self.time_slider.setPosition(0.0)
                print(self.pom_timer.state)
            if self.start_button.isInside(a0.localPos().x(), a0.localPos().y()):
                print("Start.")
                self.pom_timer.start()
                print(self.pom_timer.state)
            a0.accept()
        return super().mousePressEvent(a0)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if a0.buttons() & Qt.LeftButton and self.dragPosition:
            self.move(a0.globalPos() - self.dragPosition)
            a0.accept()
        return super().mouseMoveEvent(a0)

    def paintEvent(self, a0: QPaintEvent) -> None:
        # start painting with background image
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        painter.drawPixmap(0, 0, self.background)
        # draw buttons
        painter.setPen(Qt.PenStyle.SolidLine)
        painter.setBrush(QColor(118,22,22))
        self.stop_button.draw(painter)
        painter.setBrush(QColor(118,33,33))
        self.start_button.draw(painter)
        painter.setBrush(QColor(210,200,200))
        self.time_slider.draw(painter)
        return super().paintEvent(a0)

    def update(self):
        super().update()
        self.pom_timer.update()
        self.time_slider.setTimes(self.pom_timer.getElapsedTime(), self.pom_timer.getEndTime())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
