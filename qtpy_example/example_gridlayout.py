from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QTextEdit, QGridLayout
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()
        
    def initWindow(self):
        self.setGeometry(300, 300, 500, 200)
        title = QLabel("Title")
        author = QLabel("Author")
        review = QLabel("Review")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewTextEdit = QTextEdit()

        glayout = QGridLayout()
        glayout.addWidget(title, 1, 0)
        glayout.addWidget(titleEdit, 1, 1)
        glayout.addWidget(author, 2, 0)
        glayout.addWidget(authorEdit, 2, 1)
        glayout.addWidget(review, 3, 0)
        glayout.addWidget(reviewTextEdit, 3, 1,6,3)

        self.setLayout(glayout)

        self.show()

if __name__ == "__main__":        
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
