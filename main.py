from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Nhận diện biển số"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 400
        self.InitWindow()
        self.setStyleSheet("background-color:#3F3F3F")
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.createLayout()
        self.show()
    def createLayout(self):
        hboxBig = QHBoxLayout()
        hbox = QHBoxLayout()

        #Button Image
        self.openImage = QPushButton("Open")
        self.openImage.setStyleSheet("Background-color:none;border: 1px solid white;border-radius:10px;height:30%;width:25%;color:white")
        self.openImage.clicked.connect(self.getImage)

        hbox.addWidget(self.openImage,1)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        # Image
        self.lblImage = QLabel()
        self.lblImage.setFixedSize(500,500)
        self.lblImage.setStyleSheet("border:1px solid white;")
        defaulImage = QPixmap('image/noimg.png')
        scaledefaulImage = defaulImage.scaled(50,50)
        self.lblImage.setPixmap(scaledefaulImage)
        self.lblImage.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.lblImage)
        vbox.setAlignment(Qt.AlignCenter)

        hboxBig.addLayout(vbox)

        # Show Image Plate
        lblImagePlate = QLabel()
        lblanhBienso = QLabel()
        lblanhBienso.setText("Ảnh biển số")
        lblanhBienso.setStyleSheet("color:white")
        lblImagePlate.setFixedSize(200,100)
        lblImagePlate.setStyleSheet("border:1px solid white;")
        vboxRight = QVBoxLayout()
        vboxRight.setAlignment(Qt.AlignTop)
        vboxRight.addWidget(lblanhBienso,1)
        vboxRight.addWidget(lblImagePlate,1)
        hboxBig.addLayout(vboxRight)

        # Show Plate
        lblPlate = QLabel()
        lblBienso = QLabel()
        lblBienso.setText("Biển số")
        lblBienso.setStyleSheet("color:white")
        lblPlate.setText("75C1 - 02128")
        lblPlate.setStyleSheet("font-size:25px;color:white")
        vboxRight.addWidget(lblBienso, 1)
        vboxRight.addWidget(lblPlate, 1)
        vboxRight.addStretch(9)
        hboxBig.addLayout(vboxRight)

        self.setLayout(hboxBig)
    def getImage(self):
        path_img = QFileDialog.getOpenFileName(self,'OpenFile','./','Image Files(*.png *.jpg *.bmp)')
        imagePath = path_img[0]
        pixmap = QPixmap(imagePath)
        if (pixmap.width() > pixmap.height()):
            scaled = pixmap.scaledToWidth(self.lblImage.width(), Qt.SmoothTransformation)
            self.lblImage.setPixmap(QPixmap(scaled))
        if (pixmap.width() < pixmap.height()):
            scaled = pixmap.scaledToHeight(self.lblImage.height(), Qt.SmoothTransformation)
            self.lblImage.setPixmap(QPixmap(scaled))
        else:
            scaled = pixmap.scaledToWidth(self.lblImage.width(), Qt.SmoothTransformation)
            self.lblImage.setPixmap(QPixmap(scaled))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())