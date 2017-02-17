from PyQt5.QtWidgets import QApplication,QCheckBox,QWidget, QSlider
from PyQt5.QtCore import Qt
import sys
from PyQt5.Qt import QLabel
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        sld = QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30,40,100,30)
        sld.valueChanged[int].connect(self.valueChanged)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('web.png'))
        self.label.setGeometry(160,40,80,30)

        self.setGeometry(300,300,280,70)
        self.setWindowTitle("slider")                
        self.show()

    def valueChanged(self,value):
        self.label.setGeometry(value,40,80,30)
        
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())