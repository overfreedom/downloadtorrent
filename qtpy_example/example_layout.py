from PyQt5.QtWidgets import QApplication,QPushButton,QBoxLayout,QMainWindow, QHBoxLayout,\
    QVBoxLayout,QWidget
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.initWindow()
        except Exception as e:
            print(e)
            
    def initWindow(self):
                
        self.okButton = QPushButton("OK")
        self.okButton.resize(self.okButton.sizeHint())
        self.cancelButton = QPushButton("cancel")
         
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.okButton)
        self.hbox.addWidget(self.cancelButton)
         
        self.vbox =QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
          
        self.setLayout(self.vbox)
        self.setGeometry(300,300,500,200)
#         self.setCentralWidget(self.vbox)
        self.show()
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#  
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#  
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#          
#         self.setLayout(vbox)   
#          
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('Buttons')   
#         self.show()
        
if __name__ == "__main__":
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())