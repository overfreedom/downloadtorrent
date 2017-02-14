from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QMessageBox
import sys

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMain()
        
    def initMain(self):
        self.resize(500,300)
        self.move(300,300)
        
        btn = QPushButton("btn",self)
        btn.resize(btn.sizeHint())
        btn.move(100,100)
        btn.clicked.connect(self.showMessage)
        self.show()

    def showMessage(self):
#         print('helll world')
        msg = QMessageBox.question(self, "message", "are you sure to quit", QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if msg == QMessageBox.Yes :
            self.close()

if __name__ == "__main__" :            
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())