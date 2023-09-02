import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QWidget
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtGui import QIcon

from Settings.Editor.EditorIni import editor_settings
from UI.GameWindow.GameWindow import GameWindow
from Engine.Engine import Engine
        

class EditorWindow(QMainWindow):
    _engine = None
    
    def __init__(self, engine, parent=None):
        super().__init__()
        self._engine = engine
        self._init_menubar()
        self._init_GameWindow()
        
    def _init_menubar(self):
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
        
    def _init_GameWindow(self):
        self.setCentralWidget(GameWindow(self.engine))
        
    @property
    def engine(self):
        return self._engine


def start_editor():
	engine = Engine()
	app = QApplication(sys.argv)
	w = EditorWindow(engine)
	w.show()
	app.exec_()
