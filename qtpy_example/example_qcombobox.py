import sys
from PyQt5.QtWidgets import QMainWindow, QSlider, QLabel, QApplication, QComboBox
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.label = QLabel('aaa',self)
        self.label.move(20,20)
        self.label.adjustSize()
        
        combobox = QComboBox(self)
        combobox.addItem('aaa')
        combobox.addItem('bbbb')
        combobox.addItem('ccccc')
        combobox.addItem('dddddd')
        combobox.move(20,50)
        combobox.adjustSize()
        print(combobox.currentText())
        combobox.currentTextChanged[str].connect(self.changeValue)
        self.setGeometry(300,300,400,200)
        self.show()
        
    def changeValue(self,value):
        
        self.label.setText(value)
        self.label.adjustSize()
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())