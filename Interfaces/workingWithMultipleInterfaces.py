from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Window")
        self.setGeometry(50,200,1000,800)
        self.start()
        self.show()

    def font(self,obj,x,y):
        obj.setFont(QFont("Times",15))
        obj.move(x,y)
    def start(self):
        login = QLabel("Login:",self)
        self.font(login,50,50)
        password = QLabel("Password:",self)
        self.font(password,50,100)
        input_login = QLineEdit(self)
        self.font(input_login,300,50)
        input_password = QLineEdit(self)
        self.font(input_password,300,100)
        input_login.setPlaceholderText("Enter your login...")
        input_password.setPlaceholderText("Enter your password...")
        sign_in = QPushButton("Sign In",self)
        self.font(sign_in,50,150)
        sign_up = QPushButton("Sign Up",self)
        self.font(sign_up,300,150)
        sign_in.clicked.connect(self.signIn)
        sign_up.clicked.connect(self.signUp)


    def signUp(self):
        self.second = Window2()
        self.second.show()


    def signIn(self):
        
        self.close()

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.setGeometry(600,200,1000,800)
        self.start()
        self.show()

    def font(self,obj,x,y):
        obj.setFont(QFont("Times",15))
        obj.move(x,y)
    def start(self):
        self.back = QPushButton("<--",self)
        self.font(self.back,10,10)
        self.back.clicked.connect(self.backToFirst)
    def backToFirst(self):
        self.close()



window = Window1()
sys.exit(app.exec_())