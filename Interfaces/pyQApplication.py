from PyQt5.QtWidgets import QApplication,QWidget
import sys
app = QApplication(sys.argv)
faced = QWidget()
faced.setWindowTitle("My First Python Application")
faced.setGeometry(150,150,400,400)#(x,y,width,height)
faced.setFixedSize(1000,800)
faced.show()
sys.exit(app.exec_())