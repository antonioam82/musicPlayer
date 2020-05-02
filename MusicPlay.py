from PyQt5.QtWidgets import *
import PyQt5.QtMultimedia as M
import sys
import os


class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.w = QWidget()
        self.resize(600,300)
        self.move(300,300)
        self.setWindowTitle("Audio Player")
        btnSel=QPushButton("SELLECT AUDIO",self)
        btnSel.move(10,0)
        btnSel.clicked.connect(self.play)

    def play(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.mp3)")   

if __name__== '__main__':

    app = QApplication(sys.argv)
    
    w = MusicPlayer()
    w.show()
    app.exec_()
