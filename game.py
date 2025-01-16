import sys
from random import randint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(568, 424)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "start"))


class Git(Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.flag = False
        self.sps = []

    def initUI(self):
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        if self.flag:
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.flag = False

    def draw_flag(self, qp):
        x, y = randint(0, 560), randint(0, 420)
        r = randint(0, 200)
        h, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        self.sps.append((x, y, r, h, g, b))
        for i in self.sps:
            qp.setBrush(QColor(i[3], i[4], i[5]))
            qp.drawEllipse(i[0], i[1], i[2], i[2])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Git()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())