import sys

from PySide6 import QtWidgets


class LabeledInput(QtWidgets.QWidget):
    def __init__(self, text, placeholder, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel(text)
        self.input = QtWidgets.QLineEdit(placeholder)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)

        self.setLayout(self.layout)

    def text(self):
        return self.input.text()


class XYInput(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.x_input = LabeledInput('x:', '0')
        self.y_input = LabeledInput('y:', '0')
        self.submit_button = QtWidgets.QPushButton('Отправить')
        self.submit_button.clicked.connect(self.submit)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.x_input)
        self.vbox.addWidget(self.y_input)
        self.vbox.addWidget(self.submit_button)

        self.setLayout(self.vbox)

    def submit(self):
        print(self.x_input.text(), self.y_input.text())


app = QtWidgets.QApplication(sys.argv)
window = XYInput()
window.setWindowTitle('Повторное использование')
window.resize(350, 150)
window.show()
sys.exit(app.exec())