import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.btn1.clicked.connect(self.open_theme1)
        self.btn2.clicked.connect(self.open_theme2)
        self.btn3.clicked.connect(self.open_theme3)
        self.btn4.clicked.connect(self.open_theme4)
        self.btn5.clicked.connect(self.open_theme5)
        self.btn1_ab.clicked.connect(self.instruction)
        self.btn_te.clicked.connect(self.open_tests_e)
        self.btn_to.clicked.connect(self.open_tests_o)

    def open_theme1(self):
        self.theme1 = Theme1(self, "Тема 1")
        self.theme1.show()

    def open_theme2(self):
        self.theme2 = Theme2(self, "Тема 2")
        self.theme2.show()

    def open_theme3(self):
        self.theme3 = Theme3(self, "Тема 3")
        self.theme3.show()

    def open_theme4(self):
        self.theme4 = Theme4(self, "Тема 4")
        self.theme4.show()

    def open_theme5(self):
        self.theme5 = Theme5(self, "Тема 5")
        self.theme5.show()

    def instruction(self):
        self.instruction = Instruction(self, "Инструкция")
        self.instruction.show()

    def open_tests_e(self):
        self.tests_E = Tests_E(self, 'Тесты ЕГЭ')
        self.tests_E.show()

    def open_tests_o(self):
        self.tests_O = Tests_O(self, 'Тесты ОГЭ')
        self.tests_O.show()


class Theme1(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('theme1.ui', self)


class Theme2(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('theme2.ui', self)


class Theme3(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('theme3.ui', self)


class Theme4(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('theme4.ui', self)


class Theme5(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('theme5.ui', self)


class Instruction(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('instruction.ui', self)


class Tests_E(QWidget):
    def __init__(self, *args):
        super.__init__()
        uic.loadUi('instruction.ui', self)

class Tests_O(QWidget):
    def __init__(self, *args):
        super.__init__()
        uic.loadUi('instruction.ui', self)


def except_hook(cls, exceprion, traceback):
    sys.__excepthook__(cls, exceprion, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
