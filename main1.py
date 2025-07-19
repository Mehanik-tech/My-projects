import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, \
    QColorDialog, QSlider, QLineEdit
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen
from PyQt5.QtCore import Qt
class EasyEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image = None
        self.drawing = False
        self.last_point = None
        self.pen_color = Qt.red
        self.brightness = 0
        self.contrast = 1.0
        self.text = ""


    def initUI(self):
        self.setWindowTitle('not is CAPCUT.balabol')
        self.setGeometry(100,100,800,600)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        self.btn_open = QPushButton('Open images')
        self.btn_open.clicked.connect(self.open_image)

        self.btn_save = QPushButton('Save')
        self.btn_save.clicked.connect(self.save_image)

        self.btn_draw = QPushButton('Drawing')
        self.btn_draw.clicked.connect(self.enable_drawing)

        self.btn_clear = QPushButton('Clear drew')
        self.btn_clear.clicked.connect(self.clear_drawing)

        self.btn_filter = QPushButton('Filter (c/b)')
        self.btn_filter.clicked.connect(self.apply_filter)


        self.btn_rotate = QPushButton('Rotate 90`')
        self.btn_rotate.clicked.connect(self.rotate_image)

        self.btn_color = QPushButton('Color change')
        self.btn_color.clicked.connect(self.change_color)

        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText('Enter text: ')
        self.text_input.textChanged.connect(self.set_text)

        self.brightnrss_slider = QSlider(Qt.Horizontal)
        self.brightnrss_slider.setRange(-100, 100)
        self.brightnrss_slider.setValue(0)
        self.brightnrss_slider.valueChanged.connect(self.update_image)

        self.contrast_slider = QSlider(Qt.Horizontal)
        self.contrast_slider.setRange(1,300)
        self.contrast_slider.setValue(100)
        self.contrast_slider.valueChanged.connect(self.update_image)

        lay = QVBoxLayout()
        lay.addWidget(self.label)

        control = QHBoxLayout()
        control.addWidget(self.btn_open)
        control.addWidget(self.btn_save)
        control.addWidget(self.btn_draw)
        control.addWidget(self.btn_clear)
        control.addWidget(self.btn_filter)
        control.addWidget(self.btn_rotate)
        control.addWidget(self.btn_color)

        lay.addWidget(control)
        lay.addWidget(self.text_input)
        lay.addWidget(QLabel('Яскравість'))
        lay.addWidget(self.brightnrss_slider)
        lay.addWidget(QLabel('Контраст'))
        lay.addWidget(self.contrast_slider)

        self.setLayout(lay)

    def open_image(self):
        filename, = QFileDialog.getOpenFileNames(self, 'Open image', "", "Image (*.png *,jpg *.jpeg)")
        if filename:
            self.image = cv2.imread(filename)
            self.display_image()

    def save_image(self):
        filename, = QFileDialog.getOpenFileNames(self, 'Open image', "", "Image (*.png *,jpg *.jpeg)")
        if filename and self.image is not None:
            cv2.imwrite(filename, self.image)

    def display_image(self):
        if self.image is not None:
            img = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytes_per_line = ch * w
            q_img = QImage(img.data, w, h, bytes_per_line, QImage.Format_BGR888)
            self.label.setPixmap(QPixmap.fromImage(q_img))

    def apply_filter(self):
        if self.image is not None:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
            self.display_image()


    def rotate_image(self):
        if self.image is not None:
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
            self.display_image()

    def enable_drawing(self):
        self.drawing = not self.drawing

    def mousePressEvent(self, event):
        if self.drawing and self.image is not None:
            self.last_point = event.pos()


    def mouseMoveEvent(self, event):
        if self.drawing and self.last_point is not None and self.image is not None:
            painter = QPainter(self.label.pixmap())
            pen = QPen(self.pen_color, 3, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            painter.end()
            self.last_point = event.pos()
            self.update()


    def clear_drawing(self):
        self.display_image()

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen_color = color


    def set_text(self, text):
        self.text = text
        self.update_image()

    def update_image(self):
        if self.image is not None:
            img = self.image.copy()
            self.brightness = self.brihtrness_slider.value()
            self.contrast = self.contrast_slider.value() / 100.0
            img = cv2.convertScaleAbs(img, alpha=self.contrast, beta=self.brihtrness)
            if self.text:
                cv2.putText(img, self.text, (50,50,), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            self.image = img
            self.display_image()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    edit = EasyEditor()
    edit.show()
    sys.exit(app.exec_())
