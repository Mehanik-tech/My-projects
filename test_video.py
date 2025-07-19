from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
media = QMediaPlayer()
media.setVideoOutput()
vid = QMediaContent('WIN_20250125_17_15_51_Pro.mp4')

vid.media.setMedia(vid)
vid.media.play()