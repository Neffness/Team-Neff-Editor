from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget


class GameWindow(QWidget):
    def __init__(self,surface,parent=None):
        super(GameWindow,self).__init__(parent)
        w=surface.get_width()
        h=surface.get_height()
        self.data=surface.get_buffer().raw
        self.image=QImage(self.data,w,h,QImage.Format_RGB32)

    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        qp.drawImage(0,0,self.image)
        qp.end()