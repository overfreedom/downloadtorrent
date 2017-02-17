from PyQt5.QtWidgets import QApplication, QCheckBox, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        hbox = QHBoxLayout()
        pixmap = QPixmap('web.png')
        lb = QLabel()
        lb.setPixmap(pixmap)
        hbox.addWidget(lb)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 400, 200)
        self.show()


        
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
