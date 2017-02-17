from PyQt5.QtWidgets import QApplication, QCheckBox, QWidget, QHBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt
import sys
from builtins import str


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        hbox = QHBoxLayout()
        hbox.setStretch(1,1)
        self.lb = QLabel()
        hbox.addWidget(self.lb,1)
        hbox.setStretch(1,2)
        ledit = QLineEdit()
        ledit.textChanged[str].connect(self.textChanged)
        hbox.addWidget(ledit,2)
        
        self.setLayout(hbox)
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def textChanged(self,text):
        self.lb.setText(text)

        
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
