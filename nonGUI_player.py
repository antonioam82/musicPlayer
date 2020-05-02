import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import sys
import os

app=C.QCoreApplication(sys.argv)

direc = input("Ruta: ")
os.chdir(direc)
audio = input("Introduce audio: ")
url= C.QUrl.fromLocalFile(audio)
content= M.QMediaContent(url)
player = M.QMediaPlayer()
player.setMedia(content)
player.play()

player.stateChanged.connect( app.quit )
app.exec()
