from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox,QPushButton,QRadioButton
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)

class EnterButton(QPushButton):
    def __init__(self, name,win,x,y):
        super().__init__(name,win)
        self.setFont(QFont("Times",20))
        self.setGeometry(x,y,100,60)
        self.x = x
        self.y = y
    def click(self,fun):
        self.clicked.connect(fun)

class Button(QPushButton):
    def __init__(self, name,win,x,y):
        super().__init__(name,win)
        self.setFont(QFont("Times",20))
        self.setGeometry(x,y,100,100)
        self.x = x
        self.y = y
    def click(self,fun):
        self.clicked.connect(fun)

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Window")
        self.setGeometry(50,200,1000,800)
        self.var = ""
        self.start()
        self.show()

    def font(self,obj,x,y):
        obj.setFont(QFont("Times",25))
        obj.move(x,y)

    def start(self):
        self.version1 = QRadioButton("X",self)
        self.font(self.version1,50,50)
        self.version2 = QRadioButton("O",self)
        self.font(self.version2,120,50)
        self.enter = EnterButton("Enter",self,50,130)
        self.enter.click(self.choose)
        self.b1 = Button("",self,50,50)
        self.b2 = Button("",self,50,150)
        self.b3 = Button("",self,50,250)
        self.b4 = Button("",self,150,50)
        self.b5 = Button("",self,150,150)
        self.b6 = Button("",self,150,250)
        self.b7 = Button("",self,250,50)
        self.b8 = Button("",self,250,150)
        self.b9 = Button("",self,250,250)
        self.b1.click(self.B1)
        self.b2.click(self.B2)
        self.b3.click(self.B3)
        self.b4.click(self.B4)
        self.b5.click(self.B5)
        self.b6.click(self.B6)
        self.b7.click(self.B7)
        self.b8.click(self.B8)
        self.b9.click(self.B9)
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b5.hide()
        self.b6.hide()
        self.b7.hide()
        self.b8.hide()
        self.b9.hide()
    def refresh(self):
        self.b1.setText("")
        self.b2.setText("")
        self.b3.setText("")
        self.b4.setText("")
        self.b5.setText("")
        self.b6.setText("")
        self.b7.setText("")
        self.b8.setText("")
        self.b9.setText("")
    def check(self):
        winner = QMessageBox(self)
        if self.b1.text()!="" and self.b1.text() == self.b2.text() and self.b1.text() == self.b3.text():
            winner.setText("Player " + self.b1.text() + " is WINNER!")
           # winner.setIcon(QMessageBox.critical)
            winner.show()
            self.refresh()
        elif self.b1.text()!="" and self.b1.text() == self.b4.text() and self.b1.text() == self.b7.text():
            winner.setText("Player " + self.b1.text() + " is WINNER!")
           # winner.setIcon(QMessageBox.critical)
            winner.show()
            self.refresh()
        elif self.b1.text()!="" and self.b1.text() == self.b5.text() and self.b9.text() == self.b3.text():
            winner.setText("Player " + self.b1.text() + " is WINNER!")
            #winner.setIcon(QMessageBox.critical)
            winner.show()
            self.refresh()
        elif self.b2.text()!="" and self.b2.text() == self.b5.text() and self.b2.text() == self.b8.text():
            winner.setText("Player " + self.b2.text() + " is WINNER!")
            #winner.setIcon(QMessageBox.critical)
            winner.show()
            self.refresh()
        elif self.b3.text()!="" and self.b3.text() == self.b6.text() and self.b1.text() == self.b9.text():
            winner.setText("Player " + self.b3.text() + " is WINNER!")
            #winner.setIcon(QMessageBox.critical)
            winner.show()
            self.refresh()
        elif self.b4.text()!="" and self.b4.text() == self.b5.text() and self.b4.text() == self.b6.text():
            winner.setText("Player " + self.b4.text() + " is WINNER!")
            #winner.setIcon(QMessageBox.critical)
            winner.show()
            self.refresh()
        elif self.b7.text()!="" and self.b7.text() == self.b8.text() and self.b9.text() == self.b8.text():
            winner.setText("Player " + self.b7.text() + " is WINNER!")
            #winner.setIcon(QMessageBox.critical)
            winner.show()
            self.refresh()
        elif self.b7.text()!="" and self.b7.text() == self.b5.text() and self.b3.text() == self.b7.text():
            winner.setText("Player " + self.b3.text() + " is WINNER!")
            #winner.setIcon(QMessageBox.critical)
            winner.show()
            self.refresh()
        elif (self.b7.text()!="" and self.b6.text() != "" and self.b5.text() != "" and self.b3.text() != "" and self.b4.text() !=""
         and self.b8.text()!="" and self.b9.text() != "" and self.b1.text() != "" and self.b2.text() != ""):
            winner.setText("DRAW!")
            #winner.setIcon(QMessageBox.information)
            winner.show()
            self.refresh()

    def B1(self):
        if self.b1.text()=="":
            self.b1.setText(self.var)
        if self.var == "X":
            self.var = "O"
        else:
            self.var = "X"
        self.check()
    def B2(self):
        if self.b2.text()=="":
            self.b2.setText(self.var)
        if self.var == "X":
            self.var = "O"
        else:
            self.var = "X"
        self.check()
    def B3(self):
        if self.b3.text()=="":
            self.b3.setText(self.var)
        if self.var == "X":
            self.var = "O"
        else:
            self.var = "X"
        self.check()
    def B4(self):
        if self.b4.text()=="":
            self.b4.setText(self.var)
        if self.var == "X":
            self.var = "O"
        else:
            self.var = "X"
        self.check()
    def B5(self):
        if self.b5.text()=="":
            self.b5.setText(self.var)
        if self.var == "X":
            self.var = "O"
        else:
            self.var = "X"
        self.check()
    def B6(self):
        if self.b6.text()=="":
            self.b6.setText(self.var)
        if self.var == "X":
            self.var = "O"
        else:
            self.var = "X"
        self.check()
    def B7(self):
        if self.b7.text()=="":
            self.b7.setText(self.var)
        if self.var == "X":
            self.var = "O"
        else:
            self.var = "X"
        self.check()
    def B8(self):
        if self.b8.text()=="":
            self.b8.setText(self.var)
        if self.var == "X":
            self.var = "O"
        else:
            self.var = "X"
        self.check()
    def B9(self):
        if self.b9.text()=="":
            self.b9.setText(self.var)
        if self.var == "X":
            self.var = "O"
        else:
            self.var = "X"
        self.check()
    

    def choose(self):
        if self.version1.isChecked():
            self.var = "X"
        if self.version2.isChecked():
            self.var = "O"
        self.version1.hide()
        self.version2.hide()
        self.enter.hide()
        self.b1.show()
        self.b2.show()
        self.b3.show()
        self.b4.show()
        self.b5.show()
        self.b6.show()
        self.b7.show()
        self.b8.show()
        self.b9.show()

window = Window1()
sys.exit(app.exec_())