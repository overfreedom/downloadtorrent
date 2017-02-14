from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QAction, QTextEdit
from PyQt5.QtCore import pyqtSignal,pyqtSlot,QObject
from PyQt5.QtGui import QIcon
import sys
class Communicate(QObject):
    closeApp = pyqtSignal()
    

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.te = QTextEdit(self)
        self.setCentralWidget(self.te)
        self.initWin()

    def addAvatar(self):
        print('addAvatar')

    def addAvatarSet(self):
        print('addAvatarSet')

    def addAvatarDecoration(self):
        print('addAvatarDecoration')

    def modifyAvatar(self):
        print('modifyAvatar')

    def modifyAvatarSet(self):
        print('modifyAvatarSet')

    def modifyAvatarDecoration(self):
        print('modifyAvatarDecoration')

    def settingPath(self):
        print('settingPath')

    def homePage(self):
        print('homePage') 
                       
    def initWin(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)                
        self.resize(500,500)
        self.move(300,300)
        self.setWindowTitle("Qmainwindow")
        self.show()
        
        self.addAvatarAct = QAction(QIcon("res/ico/addAvatar.ico"), "&Add Avatar", self, triggered=self.addAvatar)
        self.addAvatarSetAct = QAction(QIcon("res/ico/addAvatarSet.ico"), "&Add AvatarSet", self, triggered=self.addAvatarSet)
        self.addAvatarDecorationAct = QAction(QIcon("res/ico/addAvatarDecoration.ico"), "&Add AvatarDecoration", self, triggered=self.addAvatarDecoration)
        self.modifyAvatarAct = QAction(QIcon("res/ico/modifyAvatar.ico"), "&Modify Avatar or Decoration", self, triggered=self.modifyAvatar)
        self.modifyAvatarSetAct = QAction(QIcon("res/ico/modifyAvatarSet.ico"), "&Modify AvatarSet", self, triggered=self.modifyAvatarSet)
        self.settingAct = QAction(QIcon("res/ico/settingPath.ico"), "&路径", self, triggered=self.settingPath)
        self.homeAct = QAction(QIcon("res/ico/home.ico"), "&首页", self, triggered=self.homePage)
        
        self.addMenu = self.menuBar().addMenu("&添加")
        self.addMenu.addAction(self.addAvatarAct)
        self.addMenu.addAction(self.addAvatarSetAct)
        self.addMenu.addAction(self.addAvatarDecorationAct)
        self.modifyMenu = self.menuBar().addMenu("&修改")
        self.modifyMenu.addAction(self.modifyAvatarAct)
        self.modifyMenu.addAction(self.modifyAvatarSetAct)
        self.settingMenu = self.menuBar().addMenu("&设置")
        self.settingMenu.addAction(self.settingAct)

    def mousePressEvent(self, *args, **kwargs):
        print("close window")
        self.c.closeApp.emit()
        
        
if __name__ == "__main__" :        
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())