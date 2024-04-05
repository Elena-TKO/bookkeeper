import sys

from PySide6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = expenses_table = QtWidgets.QTableWidget(4, 20)
window.setWindowTitle('Table')
window.resize(600, 600)

expenses_table.setColumnCount(4)
expenses_table.setRowCount(20)
expenses_table.setHorizontalHeaderLabels(
    "Дата Сумма Категория Комментарий".split())

header = expenses_table.horizontalHeader()
header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

expenses_table.setEditTriggers(
    QtWidgets.QAbstractItemView.NoEditTriggers)
expenses_table.verticalHeader().hide()

def add_data(data):
    for i, row in enumerate(data):
        for j, x in enumerate(row):
            expenses_table.setItem(
                i, j,
                QtWidgets.QTableWidgetItem(x.capitalize())
            )

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
# add_data(data)

window.show()
sys.exit(app.exec())