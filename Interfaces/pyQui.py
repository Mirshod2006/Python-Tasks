from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QLineEdit,QTextEdit
from PyQt5.QtGui import QPainter,QPen,QBrush,QFont
import sys


app = QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My second application")
        self.setGeometry(100,100,800,600)
        self.start()
        self.show()
    

    def start(self):
        write = QLabel("Hello Brothers",self)
        write.move(100,50)
        write.setFont(QFont("Times", 25))
        text = QTextEdit(self)
        text.setText(write.text())
        text.setGeometry(100,200,500,50)
        text.setFont(QFont("Times",25))
        line = QLineEdit(self)
        line.setText(write.text())
        line.setGeometry(100,300,500,50)
        line.setFont(QFont("Times",25))

faced = Window()
sys.exit(app.exec_())
