import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

#vi = int(input('Вибери відео 1 чи 2: '))

#if vi == 1:
 #   v = '13001673_3840_2160_30fps.mp4'
#elif:
 #   v = 'WIN_20250125_17_15_51_Pro.mp4'
#else:
 #   e = QMessageBox()

    #e.exec_()
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Video player')
        self.setGeometry(100,100,800,600)


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.videoNidegt = QVideoWidget(self)
        layout.addWidget(self.videoNidegt)


        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.videoNidegt)

        video = '13001673_3840_2160_30fps.mp4'   # 'WIN_20250125_17_15_51_Pro.mp4'
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile(video)))
        self.media.play()
#хогвартс в облості програмування
if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Widget()
    s.show()
    sys.exit(app.exec_())













