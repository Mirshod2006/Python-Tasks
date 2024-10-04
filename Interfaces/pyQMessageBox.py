from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox
from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")
        self.setGeometry(200,200,800,1000)
        self.start()
        self.show()

    def font(self,obj,x,y):
        obj.setFont(QFont("Times",24))
        obj.move(x,y)

    def start(self):
        number1=QLabel("First number = ",self)
        self.font(number1,50,50)
        number2=QLabel("Second number = ",self)
        self.font(number2,50,125)
        self.num1 = QLineEdit(self)
        self.font(self.num1,350,50)
        self.num2 = QLineEdit(self)
        self.font(self.num2,400,125)
        plus = QPushButton("+",self)
        self.font(plus,100,200)
        minus = QPushButton("-",self)
        self.font(minus,200,200)
        multiply = QPushButton("*",self)
        self.font(multiply,300,200)
        divide = QPushButton("/",self)
        self.font(divide,400,200)
        plus.clicked.connect(self.run1)
        minus.clicked.connect(self.run2)
        multiply.clicked.connect(self.run3)
        divide.clicked.connect(self.run4)
        self.window1 = QMessageBox(self)

    def run1(self):
        number1 = int(self.num1.text())
        number2 = int(self.num2.text())
        self.window1.setText(str(number1)+" + "+str(number2)+" = " + str(number1 + number2))
        self.window1.setWindowTitle("Adding two numbers!")
        self.window1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Reset)
        self.window1.show()
    def run2(self):
        number1 = int(self.num1.text())
        number2 = int(self.num2.text())
        self.window1.setText(str(number1)+" - "+str(number2)+" = " + str(number1 - number2))
        self.window1.setWindowTitle("Subtracting two numbers!")
        self.window1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Reset)
        self.window1.show()

    def run3(self):
        number1 = int(self.num1.text())
        number2 = int(self.num2.text())
        self.window1.setText(str(number1)+" * "+str(number2)+" = " + str(number1 * number2))
        self.window1.setWindowTitle("Multiplying two numbers!")
        self.window1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Reset)
        self.window1.show()

    def run4(self):
        number1 = int(self.num1.text())
        number2 = int(self.num2.text())
        if number2 != 0:
            self.window1.setText(str(number1)+" / "+str(number2)+" = " + str(number1 / number2))
            self.window1.setWindowTitle("Dividing two numbers!")
            self.window1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Reset)
        else:
            self.window1.setText("Dividing by zero number is prohibited in General Math!")
            self.window1.setWindowTitle("Dividing two numbers!")
            self.window1.setDetailedText("""Dividing by zero may possible in the other courses of math,
but general math does not support dividing by zero!""")
            self.window1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Reset)
        self.window1.show()

window = Window()
sys.exit(app.exec_())
