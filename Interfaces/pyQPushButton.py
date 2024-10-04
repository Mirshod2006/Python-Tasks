from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My third application")
        self.setGeometry(100,100,800,600)
        self.start()
        self.show()

    def font(self,obj,x,y):
        obj.setFont(QFont("Times",25))
        obj.move(x,y)

    def start(self):
        self.text1 = QLabel("Output Infos",self)
        self.font(self.text1,50,120)
        self.input = QLineEdit(self)
        self.font(self.input,50,50)
        ok = QPushButton("Ok!",self)
        self.font(ok,50,200)
        ok.clicked.connect(self.run)
    def run(self):
        self.text1.setText(self.input.text())
        self.text1.adjustSize()
window = Window()
sys.exit(app.exec_())