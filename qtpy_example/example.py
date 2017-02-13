from PyQt5.QtWidgets import QApplication,QWidget 
from PyQt5.QtGui import QIcon 
import sys
class Example (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.resize(500,500)
        self.move(300,300)
        self.setWindowTitle("have icon app")
        self.setWindowIcon(QIcon("web.png"))
        self.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    win = Example()
    sys.exit(app.exec_())
        