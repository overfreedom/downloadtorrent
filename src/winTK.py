'''
Created on 2017年2月10日

@author: Administrator
'''

from PyQt5.QtWidgets import QApplication,QWidget
import sys
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle("simple app")
    w.show()

    sys.exit(app.exec_())
    