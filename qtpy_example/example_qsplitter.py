# -*- encode:utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QSlider, QLabel, QApplication, QHBoxLayout, QFrame,\
    QSplitter
from PyQt5.QtCore import Qt
##分割框对某些主题不显示。。
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        hbox = QHBoxLayout(self)
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setGeometry(0,0,100,100)
        topright.setStyleSheet('QWidget { background-color : red }')
        
        topright.setFrameShape(QFrame.StyledPanel)                

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
                                
        self.setGeometry(300, 300, 400, 200)        
        self.show()
        
    def changeValue(self, value):
        if value == 0:
            self.lable.setText("00000")
        else:
            self.lable.setText(value)

                
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
