from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QRadioButton,QPushButton,QMessageBox
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1000,800)
        self.setWindowTitle("QRadio Button")
        self.start()
        self.show()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",15))
        obj.move(x,y)
    def start(self):
        self.text = QLabel("Which of the followings are compiler programming language?",self)
        self.font(self.text,50,50)
        self.answer1 = QRadioButton("C programming language",self)
        self.font(self.answer1,100,100)
        self.answer2 = QRadioButton("Python programming language",self)
        self.font(self.answer2,100,150)
        self.answer3 = QRadioButton("Java programming language",self)
        self.font(self.answer3,100,200)
        self.answer4 = QRadioButton("JavaScript programming language",self)
        self.font(self.answer4,100,250)
        self.check = QPushButton("Check",self)
        self.font(self.check,50,300)
        self.check.clicked.connect(self.checkIt)
    def checkIt(self):
        win = QMessageBox(self)
        if self.answer1.isChecked():
            win.setText("You are CORRECT,C is compiler programming language")
        elif not(self.answer1.isChecked()) and not(self.answer2.isChecked()) and not(self.answer3.isChecked()) and not(self.answer4.isChecked()):
            win.setText("Please select an option")
        else:
            win.setText("You are WRONG")
        win.show()
window = Window()
sys.exit(app.exec_())