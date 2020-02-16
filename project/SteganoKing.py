from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox, QFileDialog, QWidget, QAction, QInputDialog, QTextEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image
import sqlite3
import time
import datetime
import sys

class login(QMainWindow):
    def __init__(self):
        super(login,self).__init__()

        self.title = "SteganoKing"
        self.top = 50
        self.left = 100
        self.width = 1000
        self.height = 650
        self.setStyleSheet("background-color: #151414;")
        self.dialogs = list()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.label = QLabel("Stegano king",self)
        self.label.setStyleSheet('color:red;font-family: Veni;font-size: 70px')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(300,30)
        self.label.adjustSize()

        self.icon_label = QLabel(self)
        self.icon_label.setPixmap(QPixmap('bg_icon.png'))
        self.icon_label.move(350,180)
        self.icon_label.adjustSize()

        self.Login_button = QPushButton("Login",self)
        self.Login_button.move(466,520)
        self.Login_button.setStyleSheet('color:white;font-family: psKampen-Bold;font-size: 30px')
        self.Login_button.adjustSize()
        self.Login_button.clicked.connect(self.clicked)
        
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def clicked(self):
        dialog = First()
        self.dialogs.append(dialog)
        dialog.show()

class Second(QMainWindow):
    def __init__(self,fname,tname):
        super(Second, self).__init__()

        self.title = tname
        self.left = 0
        self.top = 0
        self.width = 1400
        self.height = 750
        self.fname = fname
        #self.setStyleSheet("background-color: #303030;")
        
        oImage = QImage("bg.png")
        sImage = oImage.scaled(QSize(2000,700))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)
        self.InitWindow()

    def InitWindow(self):

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(100,100,600,400)
        self.openFile()

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def openFile(self):
            f = open(self.fname,'r')

            with f:
                data = f.read()
                self.textedit.setText(data)

class First(QMainWindow):
    def __init__(self):
        super(First,self).__init__()

        self.title = "SteganoKing"
        self.left = 0
        self.top = 0
        self.width = 1400
        self.height = 750
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.location = ""
        self.text = ""
        self.newimg_name = ""
        self.flag = 0
        self.fname = ""
        self.tname = ""
        #self.setStyleSheet("background-color: #151414;")
        
        oImage = QImage("bg.png")
        sImage = oImage.scaled(QSize(1600,750))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)
        self.dialogs = list()
        self.dialogs1 = list()
        self.dialogs2 = list()
        self.InitWindow()

        self.conn = sqlite3.connect('History.db')
        self.c = self.conn.cursor()

    def clicked(self):
        dialog = Second(self.fname,self.tname)
        self.dialogs.append(dialog)
        dialog.show()

    def InitWindow(self):
        #self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        Mainmenu = self.menuBar()
        Mainmenu.setStyleSheet('color:black;font-family: psKampen-Bold;font-size: 15px')
        fileMenu = Mainmenu.addMenu("File")
        helpMenu = Mainmenu.addMenu("Help")
        aboutMenu = Mainmenu.addMenu("About")

        exitbutton = QAction("Exit",self)
        exitbutton.setShortcut("Ctrl+Q")
        exitbutton.setStatusTip("Exit Application")
        exitbutton.triggered.connect(self.close_req)
        fileMenu.addAction(exitbutton)

        shortcuts = QAction("Shortcuts",self)
        shortcuts.setStatusTip("Shows all shortcuts")
        steps_e = QAction("Encoding Steps",self)
        steps_e.setStatusTip("How to encode?")
        steps_d = QAction("Decoding Steps",self)
        steps_d.setStatusTip("How to decode?")
        helpMenu.addAction(shortcuts)
        helpMenu.addAction(steps_e)
        helpMenu.addAction(steps_d)
        shortcuts.triggered.connect(self.shortcuts_set_value)
        steps_e.triggered.connect(self.encode_set_value)
        steps_d.triggered.connect(self.decode_set_value)

        stego = QAction("Steganography",self)
        stego.setStatusTip("What is Steganography?")
        us = QAction("About US",self)
        us.setStatusTip("Developers")
        aboutMenu.addAction(stego)
        aboutMenu.addAction(us)
        stego.triggered.connect(self.stego_set_value)
        us.triggered.connect(self.us_set_value)

        #self.title_Label = QLabel("<B><font color = 'red' font size = 30>SteganoKing</font></B>",self)
        self.title_label = QLabel("Stegano King",self)
        self.title_label.setStyleSheet('color:red;font-family: Veni;font-size: 70px')
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.move(450,50)
        #self.title_label.setGeometry(QtCore.QRect(270,50,300,60))
        self.title_label.adjustSize()

        self.icon_label = QLabel(self)
        self.icon_label.setPixmap(QPixmap('bg_icon1.png'))
        self.icon_label.move(900,100)
        self.icon_label.adjustSize()

        self.LineEdit = QLineEdit(self)
        self.LineEdit.move(120,210)
        self.LineEdit.resize(380,40)
        self.LineEdit.setStyleSheet('font-family: Century Gothic; color:black')

        self.browse_button = QPushButton("Browse",self)
        self.browse_button.move(560,212)
        #self.browse_button.setToolTip("Browse Image")
        self.browse_button.clicked.connect(self.selectFile)
        self.browse_button.setShortcut("Ctrl+B")
        self.browse_button.setStyleSheet('color:black;font-family: psKampen-Bold;font-size: 20px')

        self.encode_button = QPushButton("Encode",self)
        self.encode_button.move(180,280)
        self.encode_button.setToolTip("Encode Image")
        self.encode_button.setShortcut("Ctrl+E")
        self.encode_button.setStyleSheet('color:black;font-family: psKampen-Bold;font-size: 20px')
        self.encode_button.clicked.connect(self.encode_call)

        self.decode_button = QPushButton("Decode",self)
        self.decode_button.move(350,280)
        self.decode_button.setToolTip("Decode Image")
        self.decode_button.setShortcut("Ctrl+D")
        self.decode_button.setStyleSheet('color:black;font-family: psKampen-Bold;font-size: 20px')
        self.decode_button.clicked.connect(self.decode_call)

        self.save_button = QPushButton("Save",self)
        self.save_button.move(120,354)
        self.save_button.setToolTip("Save Changes")
        self.save_button.setShortcut("Ctrl+S")
        self.save_button.setStyleSheet('color:black;font-family: psKampen-Bold;font-size: 20px')
        self.save_button.clicked.connect(self.save_condition)

        self.reset_button = QPushButton("Reset",self)
        self.reset_button.move(261,354)
        self.reset_button.setToolTip("Reset Changes")
        self.reset_button.setStyleSheet('color:black;font-family: psKampen-Bold;font-size: 20px')
        self.reset_button.clicked.connect(self.reseter)
        self.reset_button.setShortcut("Ctrl+R")

        self.close_button = QPushButton("Close",self)
        self.close_button.move(400,354)
        self.close_button.setToolTip("Close Application")
        self.close_button.setStyleSheet('color:black;font-family: psKampen-Bold;font-size: 20px')
        self.close_button.clicked.connect(self.close_req)
        self.close_button.setShortcut("Ctrl+Q")

        self.bottom_Label = QLabel("<h2>Your Text will Appear here:<\h3>",self)
        self.bottom_Label.setGeometry(QtCore.QRect(120,412,300,40))

        self.text_Label = QLabel(self)
        #self.text_Label.setGeometry(QtCore.QRect(120,425,600,100))
        self.text_Label.move(120,450)
        self.text_Label.adjustSize()

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        #self.showMaximized()
    
    def save_condition(self):
        if self.location!="" and self.text!="":
            self.create_table()
            self.dynamic_data_entry()
            self.flag = 2
            self.display_dialog()


    def shortcuts_set_value(self):
        self.fname = "Shortcuts.txt"
        self.tname = "Help"
        self.clicked()
    
    def encode_set_value(self):
        self.fname = "Encode.txt"
        self.tname = "Help"
        self.clicked()

    def decode_set_value(self):
        self.fname = "Decode.txt"
        self.tname = "Help"
        self.clicked()

    def stego_set_value(self):
        self.clicked2()

    def us_set_value(self):
        self.clicked1()

    def clicked1(self):
        dialog = about()
        self.dialogs1.append(dialog)
        dialog.show()

    def clicked2(self):
        dialog = stego()
        self.dialogs2.append(dialog)
        dialog.show()

    def selectFile(self):
        filter = "Images (*.png)"
        fname = QFileDialog.getOpenFileName(self,"Open Image","Image",filter)
        #print(fname)
        #print(type(fname))
        self.location = str(fname[0])
        self.LineEdit.setText(self.location)
        
    def reseter(self):
        self.LineEdit.clear()
        self.location = ""
        self.text_Label.clear()
        self.text = ""

    def createInputDialog_text(self):
        if len(self.location)>0:
            text, ok = QInputDialog.getText(self,"Encode text","Enter the text")
            if ok:
                self.text = str(text)
                self.text_Label.setText("<h2>"+self.text+"<\h2>")
                self.text_Label.adjustSize()

    def display_dialog(self):
        if self.flag==1:
            reply1 = QMessageBox.question(self, "Status", "Image Successfully Encoded", QMessageBox.Ok)
        elif self.flag==0:
            reply1 = QMessageBox.question(self, "Status", "Image Successfully Decoded ", QMessageBox.Ok)
        else:
            reply1 = QMessageBox.question(self, "Status", "Data Successfully Stored ", QMessageBox.Ok)

    def encode_call(self):
        if self.location == "":
            reply2 = QMessageBox.question(self, "No image selected", "Select Image first ", QMessageBox.Ok)
            reply2.setStyleSheet('color:white;font-family: psKampen-Bold;font-size: 20px')
        else:
             self.createInputDialog_text()
             self.encode()

    def decode_call(self):
        if self.location == "":
            reply2 = QMessageBox.question(self, "No image selected", "Select Image first ", QMessageBox.Ok)
        else:
             self.decoder_text()
             self.display_dialog()

    def decoder_text(self):
        if len(self.location)>0:
            self.text = self.decode()
            self.text_Label.setText("<h2>"+self.text+"<\h2>")

    def close(self):
        QCoreApplication.instance().quit()

    def close_req(self):
        reply = QMessageBox.question(self, "Close Window", "Are you sure to close the Application", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
    
    def genData(self, data):
        newd = [] 
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modPix(self, pix, data):
     
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
    
        for i in range(lendata):
            pix = [value for value in imdata.__next__()[:3] +
                                      imdata.__next__()[:3] +
                                      imdata.__next__()[:3]]         
            for j in range(0, 8):
                if (datalist[i][j]=='0') and (pix[j]% 2 != 0):
                    if (pix[j]% 2 != 0):
                        pix[j] -= 1
                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
 
    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)
        
        for pixel in self.modPix(newimg.getdata(), data):
        
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def encode(self):
        self.flag = 1
        img = self.location
        image = Image.open(img, 'r')
        
        data = self.text
        if (len(data) == 0):
            reply3 = QMessageBox.question(self, "No Text Found", "Enter Text first ", QMessageBox.Ok)
        else:   
            newimg = image.copy()
            self.encode_enc(newimg, data)
            img_1, ok = QInputDialog.getText(self,"Create New Image","Enter new image name (with '.png' extension)")
            if ok:
                self.newimg_name = str(img_1)
            if(len(self.newimg_name)==0):
                reply3 = QMessageBox.question(self, "No Text Found", "Enter Image Name first ", QMessageBox.Ok)
            else:
                new_img_name = self.newimg_name
                newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
                self.display_dialog()

    def decode(self):
        self.flag = 0
        img = self.location
        image = Image.open(img, 'r')
        data = ''
        imgdata = iter(image.getdata())
        
        while (True):
            pixels = [value for value in next(imgdata)[:3] +
                                         next(imgdata)[:3] +
                                         next(imgdata)[:3]]
            
            binstr = ''
            
            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'
                    
            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                return data

    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS History (Date TEXT,Time TEXT, ImageLocation TEXT,Type TEXT, Message TEXT)')

    def dynamic_data_entry(self):
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
        time1 = str(datetime.datetime.fromtimestamp(unix).strftime('%H:%M:%S'))
        imgname1 = self.location
        message1 = self.text
        if self.flag == 1:
            type1 = "encode"
        else:
            type1 = "decode"
        self.c.execute("INSERT INTO History(Date, Time, ImageLocation, Type, Message) VALUES (?, ?, ?, ?, ?)",(date, time1, imgname1,type1, message1))
        self.conn.commit()

class about(QMainWindow):
    def __init__(self):
        super(about,self).__init__()

        self.title = "About Us"
        self.top = 0
        self.left = 0
        self.width = 1400
        self.height = 750

        
        self.InitWindow()

    def InitWindow(self):

        self.label = QLabel("About US",self)
        self.label.setStyleSheet('color:red;font-family: Veni;font-size: 70px')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(520,30)
        self.label.adjustSize()
        
        self.pic1_label = QLabel(self)
        self.pic1_label.setPixmap(QPixmap('pic1.png'))
        self.pic1_label.move(300,180)
        self.pic1_label.adjustSize()

        self.pic2_label = QLabel(self)
        self.pic2_label.setPixmap(QPixmap('pic2.png'))
        self.pic2_label.move(540,195)
        self.pic2_label.adjustSize()
    
        self.pic3_label = QLabel(self)
        self.pic3_label.setPixmap(QPixmap('pic3.png'))
        self.pic3_label.move(780,195)
        self.pic3_label.adjustSize()

        self.label1 = QLabel("Safir Motiwala\n2175052",self)
        self.label1.setStyleSheet('color:blue;font-family: Veni;font-size: 25px')
        self.label1.move(300,400)
        self.label1.adjustSize()

        self.label2 = QLabel("Rutuja Kalbhor\n2175051",self)
        self.label2.setStyleSheet('color:blue;font-family: Veni;font-size: 25px')
        self.label2.move(540,400)
        self.label2.adjustSize()

        self.label3 = QLabel("Vivek Rote\n2175065",self)
        self.label3.setStyleSheet('color:blue;font-family: Veni;font-size: 25px')
        self.label3.move(790,400)
        self.label3.adjustSize()

        self.label4 = QLabel("Note : ",self)
        self.label4.setStyleSheet('color:red;font-family: Arial;font-size: 25px')
        self.label4.move(100,490)
        self.label4.adjustSize()

        self.label5 = QLabel("This Software is developed only for fair usage or legal purpose. \nThe Software and its developers won't be responsible for any \nillegal/criminal use of the software.",self)
        self.label5.setStyleSheet('color:black;font-family: Arial;font-size: 20px')
        self.label5.move(100,520)
        self.label5.adjustSize()

        self.label6 = QLabel("Date : ",self)
        self.label6.setStyleSheet('color:red;font-family: Arial;font-size: 20px')
        self.label6.move(790,510)
        self.label6.adjustSize()

        self.label7 = QLabel("10 October 2018",self)
        self.label7.setStyleSheet('color:black;font-family: Arial;font-size: 20px')
        self.label7.move(860,510)
        self.label7.adjustSize()

        self.label8 = QLabel("Version : ",self)
        self.label8.setStyleSheet('color:red;font-family: Arial;font-size: 20px')
        self.label8.move(790,540)
        self.label8.adjustSize()

        self.label9 = QLabel("1.0",self)
        self.label9.setStyleSheet('color:black;font-family: Arial;font-size: 20px')
        self.label9.move(870,540)
        self.label9.adjustSize()

        self.label10 = QLabel("Venue : ",self)
        self.label10.setStyleSheet('color:red;font-family: Arial;font-size: 20px')
        self.label10.move(790,570)
        self.label10.adjustSize()

        self.label11 = QLabel("IT - Second Year \nMIT SOE \nMIT ADT University",self)
        self.label11.setStyleSheet('color:black;font-family: Arial;font-size: 20px')
        self.label11.move(870,570)
        self.label11.adjustSize()

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

class stego(QMainWindow):
    def __init__(self):
        super(stego,self).__init__()

        self.title = "Steganography"
        self.top = 0
        self.left = 0
        self.width = 1400
        self.height = 750

        
        self.InitWindow()

    def InitWindow(self):

        self.label = QLabel("What is Steganography?",self)
        self.label.setStyleSheet('color:red;font-family: Veni;font-size: 70px')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(270,30)
        self.label.adjustSize()

        self.label1 = QLabel("Steganography is data hidden within data. \nSteganography is an encryption technique that can \nbe used along with cryptography as an extra-secure \nmethod in which to protect data."+
"Steganography techniques can be applied to images,\na video file or an audio file. \nTypically, however, steganography is written in \ncharacters including hash marking, but its usage "+
"within images is also common. At any rate, \nsteganography protects from pirating copyrighted \nmaterials as well as aiding in unauthorized viewing.",self)
        self.label1.setStyleSheet('color:black;font-family: Veni;font-size: 20px')
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.move(270,200)
        self.label1.adjustSize()
        

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
main = login()
#main.setFixedSize(800,600)
sys.exit(App.exec())