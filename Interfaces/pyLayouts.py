from PyQt5.QtWidgets import QWidget,QLabel,QHBoxLayout,QVBoxLayout,QPushButton,QApplication
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout and QVBoxLayout")
        self.setGeometry(100,100,1000,800)
        self.start()
        self.show()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",15))
        obj.move(x,y)

    def start(self):
        self.ok = QPushButton("Ok",self)
        self.font(self.ok,100,100)
        self.cancel = QPushButton("Cancel",self)
        self.font(self.cancel,200,200)
        # horizon_layout = QHBoxLayout(self)
        # horizon_layout.addStretch()
        # horizon_layout.addWidget(self.ok)
        # horizon_layout.addWidget(self.cancel)
        vertical_layout = QVBoxLayout(self)
        vertical_layout.addStretch()
        vertical_layout.addWidget(self.ok)
        vertical_layout.addWidget(self.cancel)
window = Window()
sys.exit(app.exec_())