from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QBoxLayout, QApplication, QVBoxLayout
import sys
from PyQt5.QtCore import Qt
class Example(QWidget):
    def __init__(self):
        
        super().__init__()
  
        self.initWindow()

    def initWindow(self):
        self.setGeometry(300,300,400,200)
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)
 
        vbox = QVBoxLayout()
         
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        sld.setMaximum(100)
        sld.valueChanged.connect(lcd.display)
#         lcd.display("hea")
        self.setLayout(vbox)
        self.show()

if __name__ == "__main__":        
    app = QApplication(sys.argv)
    print("main")
    ex = Example()
    
    sys.exit(app.exec_())