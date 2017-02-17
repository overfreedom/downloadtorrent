from PyQt5.QtWidgets import QApplication,QCheckBox,QWidget, QSlider, QProgressBar, QPushButton
from PyQt5.QtCore import Qt, QTimer, QBasicTimer
import sys
from PyQt5.Qt import QLabel
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.timer = QBasicTimer()
        self.pb = QProgressBar(self)
        self. step = 0
        self.btn = QPushButton("start",self)
        self.pb.setGeometry(10,40,200,20)
        self.btn.clicked.connect(self.doAction)
        
        self.btn.setGeometry(10,5,70,20)
        self.setGeometry(300,300,280,70)
                        
        self.show()

        

    def timerEvent(self,e):
        if self.step >= 100:
            self.btn.setText("finished")
            self.timer.stop()
            return

        self.step +=1
        self.pb.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.btn.setText("start")
            self.timer.stop()

        else:
            self.timer.start(100,self)
            self.btn.setText("stop")
            
        
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())