import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QWidget
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtGui import QIcon

import pygame

from Settings.Editor.EditorIni import editor_settings

class ImageWidget(QWidget):
    def __init__(self,surface,parent=None):
        super(ImageWidget,self).__init__(parent)
        w=surface.get_width()
        h=surface.get_height()
        self.data=surface.get_buffer().raw
        self.image=QImage(self.data,w,h,QImage.Format_RGB32)

    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        qp.drawImage(0,0,self.image)
        qp.end()
        
# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self, surface,parent=None):
        super().__init__()
        
        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu('File')
        helpMenu=mainMenu.addMenu('Help')
        exitButton=QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        self.show()

        self.setWindowTitle(editor_settings["name"])
        
        self.setCentralWidget(ImageWidget(surface))


def start_editor():
	#app = QApplication(sys.argv)
	#window = MainWindow()
	#app.exec()
	#return app
	pygame.init()
	s=pygame.Surface((640,480))
	s.fill((64,128,192,224))
	pygame.draw.circle(s,(255,255,255,255),(100,100),50)
	app=QApplication(sys.argv)
	w=MainWindow(s)
	w.show()
	app.exec_()
	
if __name__ == "__main__":
	start_editor()