from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QToolTip 
import sys
from PyQt5.Qt import QFont, QAction
from PyQt5.QtCore import pyqtSignal,QCoreApplication,pyqtSlot    

class Example(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.initWin()
    def initWin(self):
        self.resize(500,300)
        self.move(300,300)
        QToolTip.setFont(QFont("SansSerif",10))
        self.setToolTip("this is Qwidget tooltips")
        
        btn = QPushButton("Button",self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.close)
        btn.move(100,100)
              
        
        btn.setToolTip("this is pushbutton tooltips")        
        self.show()

    

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    e =Example()
    sys.exit(app.exec_())        