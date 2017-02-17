from PyQt5.QtWidgets import QApplication,QCheckBox,QWidget, QPushButton, QFrame
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        try :
            self.initWindow()
        except Exception as e:
            print(e)
    def initWindow(self):
        self.setGeometry(300,300,400,200)
        self.col = QColor(0,0,0)

        redb = QPushButton('RED',self)
        redb.setCheckable(True)
        redb.move(10,10)
        redb.clicked[bool].connect(self.setColor)

        blueb = QPushButton("BLUE",self)
        blueb.setCheckable(True)
        blueb.move(10,30)
        blueb.clicked[bool].connect(self.setColor)
         
        greenb = QPushButton("GREEN",self)
        greenb.setCheckable(True)
        greenb.move(10,50)
        greenb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(200,10,50,50)
        self.square.setStyleSheet("QWidget { background-color : %s }" % self.col.name())
                
        self.show()
    def setColor(self,pressed):
        try:
            soure = self.sender()
            if pressed:
                val = 255
            else:
                val = 0
    
            if soure.text() == 'RED':
                self.col.setRed(val)
                
            if soure.text() == 'GREEN':
                self.col.setGreen(val)
                
            if soure.text() == 'BLUE':    
                self.col.setBlue(val)
    
            self.square.setStyleSheet('QFrame { background-color : %s}' % self.col.name() )
        except Exception as e :
            print(e)
        

    

        
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())