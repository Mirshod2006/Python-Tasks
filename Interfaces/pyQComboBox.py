from PyQt5.QtWidgets import QLabel,QComboBox,QApplication,QWidget,QPushButton
from PyQt5.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCombo Box")
        self.setGeometry(200,200,1000,800)
        self.start()
        self.show()

    def font(self,obj,x,y):
        obj.setFont(QFont("Times",15))
        obj.move(x,y)

    def start(self):
        self.text = QLabel("Which programming specialty that you are choosing?",self)
        self.font(self.text,50,50)
        self.combo = QComboBox(self)
        self.font(self.combo,50,100)
        self.combo.addItems(["","Front-end","Back-end","DevOps","Machine Learning","Game Development"])
        self.next = QPushButton("Next",self)
        self.font(self.next,50,150)
        self.next.clicked.connect(self.next_page)
        self.back = QPushButton("<--",self)
        self.font(self.back,10,10)
        self.back.clicked.connect(self.back_page)
        self.back.hide()
    def next_page(self):
        self.next.hide()
        if self.combo.currentText() !="":
            self.text.setText("I am going to learn "+self.combo.currentText()+",\nand I hope I will find myself in this field!")
            self.text.adjustSize()
        else:
            self.text.setText("Please choose a specialty!")
        self.combo.hide()
        self.back.show()

    def back_page(self):
        self.next.show()
        self.combo.show()
        self.text.setText("Which programming specialty that you are choosing?")
        self.text.adjustSize()
        self.back.hide()

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())