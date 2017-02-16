from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton, QDesktopWidget
from PyQt5.QtCore import QRect
import sys
from PyQt5.Qt import QAction, QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()
        
    def initWindow(self):
        self.setGeometry(150,150,500,200)
        self.statusBar().showMessage("Ready!")

        exitAction = QAction(QIcon("exit.png"),'&Exit',self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)        

        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)

        
        self.btn = QPushButton("button",self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.setCenter)
        self.show()
        
    def setCenter(self):
        try:
            qr = self.frameGeometry()
#         print('hh')        
            cp = QDesktopWidget().availableGeometry().center()                                                
            qr.moveCenter(cp)
            self.move(qr.topLeft())
            qrbtn = QRect(self.frameGeometry().x()+self.frameGeometry().width()/2,
                          self.frameGeometry().y()+self.frameGeometry().height()/2,30,30)            
            self.btn.move(qrbtn.topLeft())
        except Exception as e:
            print(e)
            self.close()

if __name__ == "__main__":          
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())