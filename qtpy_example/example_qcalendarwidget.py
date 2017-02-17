from PyQt5.QtWidgets import QApplication,QCheckBox,QWidget, QCalendarWidget, QLabel
from PyQt5.QtCore import Qt, QDate
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.setGeometry(300,300,400,300)
        cd = QCalendarWidget(self)
        date = cd.selectedDate()
        cd.clicked[QDate].connect(self.showDate)
        cd.setGridVisible(True)
        cd.setGeometry(200,100,200,100)
        
        self.label = QLabel(date.toString(),self)
        self.label.setGeometry(20,50,100,30)
        self.show()

    def showDate(self,date):
        self.label.setText(date.toString())
        
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())