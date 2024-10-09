from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtWidgets import QMessageBox,QCheckBox,QPushButton
from PyQt5.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox")
        self.setGeometry(200,200,1000,800)
        self.start()
        self.show()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",15))
        obj.move(x,y)
    def start(self):
        self.text = QLabel("Which programming languages do you know?",self)
        self.font(self.text,50,50)
        self.v1 = QCheckBox("I know C programming language!",self)
        self.font(self.v1,100,150)
        self.v2 = QCheckBox("I know Python programming language!",self)
        self.font(self.v2,100,200)
        self.v3 = QCheckBox("I know Java programming language!",self)
        self.font(self.v3,100,250)
        self.v4 = QCheckBox("I know C++ programming language!",self)
        self.font(self.v4,100,300)
        self.next = QPushButton("Next",self)
        self.font(self.next,50,400)
        self.next.clicked.connect(self.choices)
        self.back = QPushButton("<--",self)
        self.font(self.back,10,10)
        self.back.hide()
        self.back.clicked.connect(self.backing)
    def backing(self):
        self.text.setText("Which programming languages do you know?")
        self.text.adjustSize()
        self.v1.show()
        self.v2.show()
        self.v3.show()
        self.v4.show()
        self.next.show()
        self.back.hide()
    def choices(self):
        self.text.setText("Programming languages that I know:\n")
        if self.v1.isChecked():
            self.text.setText(self.text.text() + self.v1.text()+"\n")
        if self.v2.isChecked():
            self.text.setText(self.text.text() + self.v2.text()+"\n")
        if self.v3.isChecked():
            self.text.setText(self.text.text() + self.v3.text()+"\n")
        if self.v4.isChecked():
            self.text.setText(self.text.text() + self.v4.text()+"\n")
        if not(self.v1.isChecked()) and not(self.v2.isChecked()) and not(self.v3.isChecked()) and not(self.v4.isChecked()):
            self.text.setText("I do NOT know any Programming Language!")
        self.v1.hide()
        self.v2.hide()
        self.v3.hide()
        self.v4.hide()
        self.text.adjustSize()
        self.next.hide()
        self.back.show()
app=QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
