import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction
from PyQt5.QtGui import QIcon

from Settings.Editor.EditorIni import editor_settings


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
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
        #button = QPushButton(editor_settings["name"])

        # Set the central widget of the Window.
        #self.setCentralWidget(button)


def start_editor():
	app = QApplication(sys.argv)

	window = MainWindow()
	#window.show()

	app.exec()
	return app
	
if __name__ == "__main__":
	start_editor()