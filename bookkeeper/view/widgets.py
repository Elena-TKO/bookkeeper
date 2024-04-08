import sys
import random

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget,
    QTableWidgetItem, QDockWidget, QFormLayout,
    QLineEdit, QWidget, QPushButton, QSpinBox,
    QMessageBox, QToolBar, QMessageBox,QHBoxLayout
)
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidget


data = [row.split('|') for row in '''
2023-01-09 15:09:00|7.49|хозтовары|пакет на кассе
2023-01-09 15:09:00|104.99|кефир
2023-01-09 15:09:00|129.99|хлеб
2023-01-09 15:09:00|239.98|сладости|пряники
2023-01-09 15:09:00|139.99|сыр
2023-01-09 15:09:00|82.99|сметана
2023-01-06 20:32:02|5536.00|книги|книги по Python и PyQt
2023-01-05 23:01:38|478.00|телефон
2023-01-03 14:18:00|78.00|продукты
2023-01-03 14:18:00|1112.00|рыба
2023-01-03 14:18:00|1008.00|рыба
2023-01-03 14:18:00|156.00|рыба
2023-01-03 14:18:00|168.00|сладости
2023-01-03 14:18:00|236.73|фрукты
2023-01-03 14:18:00|16.00|хозтовары
2023-01-03 13:59:00|259.73|книги
2023-01-03 13:59:00|119.86|хлеб
2023-01-03 13:59:00|159.82|крупы
2023-01-03 13:59:00|79.91|макароны
2023-01-03 13:59:00|479.48|овощи
'''.strip().splitlines()]

class Table_expenses(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = self.expenses_table = QTableWidget(self, 4, 20)
        self.window.setWindowTitle('Table')
        # self.window.resize(300, 200)


        self.expenses_table.setColumnCount(4)
        self.expenses_table.setRowCount(20)
        self.expenses_table.setHorizontalHeaderLabels(
            "Дата Сумма Категория Комментарий".split())

        self.header = self.expenses_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.expenses_table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.expenses_table.verticalHeader().hide()


    def add_data(self, data):
        self.expenses_table.setRowCount(len(data)+3)
        for i, row in enumerate(data):
            for j, x in enumerate(row):
                self.expenses_table.setItem(
                    i, j,
                    QTableWidgetItem(x.capitalize())
                )


class Table_budget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = self.table = QTableWidget(self)
        self.window.setWindowTitle("Бюджет")
        # self.window.resize(300, 300)

        self.table.setColumnCount(2)
        self.table.setRowCount(3)
        self.table.setHorizontalHeaderLabels(
            "Сумма Бюджет".split())
        self.table.setVerticalHeaderLabels(
            "День Неделя Месяц".split()
        )

        self.header = self.table.horizontalHeader()
        self.header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.table.setEditTriggers(
                    QtWidgets.QAbstractItemView.NoEditTriggers)
        
        
    def add_data(self, data):
            for i, row in enumerate(data):
                for j, x in enumerate(row):
                    self.table.setItem(
                        i, j,
                        QTableWidgetItem(x.capitalize())
                    )
        
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.table1 = Table_expenses()
        self.table2 = Table_budget()

        self.widget = QWidget()
        self.layout = QtWidgets.QVBoxLayout()

        self.layout.addWidget(QtWidgets.QLabel(f'Расходы'))
        
        self.layout.addWidget(self.table1.window)
        self.layout.addWidget(QtWidgets.QLabel(f'Бюджет'))
        self.layout.addWidget(self.table2.window)

        self.widget_l1 = QWidget()
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.addWidget(QtWidgets.QLabel(f'Сумма'))
        self.h_layout.addWidget(QtWidgets.QLineEdit())
        self.widget_l1.setLayout(self.h_layout)

        self.layout.addWidget(self.widget_l1)
 
        self.widget_l2 = QWidget()
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.addWidget(QtWidgets.QLabel(f'Категория'))
        self.combo_box = QtWidgets.QComboBox()
        [self.combo_box.addItem(i) for i in 'hello']
        self.h_layout.addWidget(self.combo_box)
        self.h_layout.addWidget(QtWidgets.QPushButton("Добавить категорию"))
        self.widget_l2.setLayout(self.h_layout)

        self.layout.addWidget(self.widget_l2)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.resize(700, 800)


    def update_expenses(self, data):
        self.table1.add_data(data)

    def update_budget(self, data):
        self.table2.add_data(data)
        
    





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_table = MainWindow()
    # window_table.setWindowTitle('Повторное использование')
    # window_table.resize(700, 800)
    window_table.update_expenses(data)
    window_table.show()
    sys.exit(app.exec())