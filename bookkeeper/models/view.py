from bookkeeper.view.widgets import *


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






data = [row.split('|') for row in '''
2023-01-09 15:09:00|7.49|хозтовары|пакет на кассе
2023-01-09 15:09:00|104.99|кефир
2023-01-09 15:09:00|129.99|хлеб
2023-01-09 15:09:00|239.98|сладости|пряники
'''.strip().splitlines()]



class View():
    def __init__(self) -> None:
        
        self.table_expences = Table_expenses()
        self.table_budget = Table_budget()
        self.main_window = MainWindow()
        self.main_window.show()
        
        

        
        
    def update_categories(self, cats):
        self.main_window.update_categories(cats)
    
    def update_expenses(self, data):
        self.main_window.update_expenses(data)
        self.expenses_in_view = data
        
        
    def update_budget(self, data):
        self.main_window.update_budget(data)
        self.budget_in_view = data
    
    
    

    
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    test_view = View()
    test_view.update_expenses(data)
    test_view.main_window.show()
     
    sys.exit(app.exec())
    
    