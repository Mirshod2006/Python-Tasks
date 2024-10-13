from PyQt5.QtWidgets import  QWidget,QPushButton,QLabel,QLineEdit,QApplication,QMessageBox
from PyQt5.QtGui import  QFont
import sys
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Mironshoh",
    password="02072021Imron!",
    database = 'chat_db'
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS whatsapp(login TEXT,parol TEXT,chat TEXT)")
# mycursor.executemany("INSERT INTO whatsapp(login,parol,chat) VALUES (%s,%s,%s)",[
#     ('Admin','12345',""),
#     ('User','54321',"")])
# mydb.commit()

app = QApplication(sys.argv)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1000,750)
        self.setWindowTitle("Login")
        self.start()
        self.show()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",15))
        obj.move(x,y)

    def start(self):
        self.login = QLabel("LOGIN",self)
        self.font(self.login,400,100)
        self.parol = QLabel("PASSWORD",self)
        self.font(self.parol,400,200)
        self.login_input = QLineEdit(self)
        self.font(self.login_input,400,150)
        self.parol_input = QLineEdit(self)
        self.font(self.parol_input,400,250)
        self.enter = QPushButton("Enter",self)
        self.font(self.enter,400,300)
        self.enter.clicked.connect(self.send_data)
        self.back = QPushButton("Back",self)
        self.font(self.back,50,50)
        self.back.clicked.connect(self.back_page)
        self.back.hide()
        self.sending_input = QLineEdit(self)
        self.font(self.sending_input,400,150)
        self.sending_input.hide()
        self.received_message = QLineEdit(self)
        self.font(self.received_message,400,250)
        self.received_message.hide()
        self.receiver = QLineEdit(self)
        self.font(self.receiver,400,350)
        self.receiver.hide()
        self.sending = QLabel("SENDING MESSAGE",self)
        self.font(self.sending,400,100)
        self.sending.hide()
        self.received = QLabel("RECEIVED MESSAGE",self)
        self.font(self.received,400,200)
        self.received.hide()
        self.receiver_label = QLabel("RECEIVER",self)
        self.font(self.receiver_label,400,300)
        self.receiver_label.hide()
        self.send = QPushButton("Send",self)
        self.font(self.send,400,400)
        self.send.hide()
        self.send.clicked.connect(self.update_chat)
    def update_chat(self):
        receiver = self.receiver.text() or ""  # Pythonic way of checking for None or empty string
        query = "UPDATE whatsapp SET chat = %s WHERE login = %s"
        mycursor.execute(query, (self.sending_input.text(), receiver))  # Values should be passed as a tuple
        mydb.commit()
        self.sending_input.clear()
        self.receiver.clear()

    def send_data(self):
        query = "SELECT login,parol,chat FROM whatsapp WHERE login=%s"
        role = self.login_input.text() if self.login_input.text()!=None else ""
        mycursor.execute(query, (role,))
        result = mycursor.fetchone()
        print(result)
        login,parol,chat = result if result!=None else ("","","")
        print(*chat)
        # print(parol)
        # print(login)
        if self.parol_input.text()==parol and parol!="":
            self.login.hide()
            self.login_input.hide()
            self.parol.hide()
            self.parol_input.hide()
            self.enter.hide()
            self.send.show()
            self.sending_input.show()
            self.receiver.show()
            self.received_message.setText(chat)
            self.received_message.show()
            self.sending.show()
            self.receiver_label.show()
            self.received.show()
            self.back.show()
        else:
            self.message = QMessageBox(self)
            self.message.setText("Please, check login and password!")
            self.message.setWindowTitle("Login Error!")
            self.message.exec_()

    def back_page(self):
        self.login.show()
        self.login_input.show()
        self.parol.show()
        self.parol_input.show()
        self.enter.show()
        self.send.hide()
        self.sending_input.hide()
        self.receiver.hide()
        self.received_message.hide()
        self.sending.hide()
        self.receiver_label.hide()
        self.received.hide()
        self.back.hide()

window = Window()
sys.exit(app.exec_())
