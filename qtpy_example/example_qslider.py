import sys
from PyQt5.QtWidgets import QMainWindow, QSlider, QLabel, QApplication
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.setGeometry(300,300,400,200)
        sld = QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(20,20,200,10)
        sld.valueChanged[int].connect(self.changeValue)

        self.lable = QLabel(self)
        self.show()
        
    def changeValue(self,value):
        if value == 0:
            self.lable.setText("00000")
        else:
            self.lable.setText(value)

                
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())