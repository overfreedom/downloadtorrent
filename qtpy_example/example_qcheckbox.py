from PyQt5.QtWidgets import QApplication,QCheckBox,QWidget
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.setGeometry(300,300,400,200)
        cb = QCheckBox("show title",self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        self.setWindowTitle("Qcheck box")
        self.show()

    def changeTitle(self,state):
        if state == Qt.Checked :
            self.setWindowTitle("Qcheck box")
            return 

        self.setWindowTitle("")

        
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())