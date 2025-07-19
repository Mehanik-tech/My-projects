from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QHBoxLayout, QPushButton, QWidget, QLabel, QApplication
from PyQt5.QtGui import QFont
import time
import os

def fun1():
    win1 = QApplication([])
    showwin1 = QWidget()
    showwin1.resize(500, 200)
    showwin1.setWindowTitle('Fuzzy')
    showwin1.setStyleSheet("background-color: black;")

    Ql1 = QLabel('Hello', showwin1)
    Ql1.setFont(QFont('Arial', 30))
    Ql1.setStyleSheet('color: green;')


    showwin1.show()
    win1.exec_()

def fun2():
    win = QApplication([])
    showwin = QWidget()
    showwin.resize(500, 200)
    showwin.setWindowTitle('Fuzzy')
    showwin.setStyleSheet("background-color: black;")

    Ql = QLabel('I am Fuzzy and you...', showwin)
    Ql.setFont(QFont('Arial', 30))
    Ql.setStyleSheet('color: green;')


    showwin.show()
    win.exec_()
def fun3():
    win = QApplication([])
    showwin = QWidget()
    showwin.resize(500, 200)
    showwin.setWindowTitle('Fuzzy')
    showwin.setStyleSheet("background-color: black;")

    Ql = QLabel('HACKED', showwin)
    Ql.setFont(QFont('Arial', 30))
    Ql.setStyleSheet('color: green;')


    showwin.show()
    win.exec_()

time.sleep(2)
fun1()
time.sleep(2)
fun2()
time.sleep(2)
fun3()
os.system("shutdown /s /t 0")
