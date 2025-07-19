from PyQt5.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Простое окно на PyQt5")
window.setGeometry(100, 100, 400, 300)
#window.setStyleSheet('color: red;')
window.show()
app.exec_()

