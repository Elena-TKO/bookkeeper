from models.budget import Budget
from models.category import Category
from models.expense import Expense
from models.view import View

from repository.sqlite_repository import SqliteRepository

import sys
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget,
    QTableWidgetItem, QDockWidget, QFormLayout,
    QLineEdit, QWidget, QPushButton, QSpinBox,
    QMessageBox, QToolBar, QMessageBox,QHBoxLayout
)
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidget



class Bookkeeper():
    def __init__(self) -> None:
        self.hello = "hello"
        self.view = View()
        self.budget = Budget(0,0,0)
        self.repo = SqliteRepository() 
        self.expenses = []
        for row in self.repo.get_table("Expenses"):
            self.expenses.append(Expense(
                pk=row[0],
                name=row[1],
                category=row[2],
                comment=row[3], 
                total=row[4],
                expense_date=row[5]
            ))
        self.categories = []
        for row in self.repo.get_table("Categories"):
            self.categories.append(Category(
                pk=row[0],
                name=row[1],
                description=row[2]
            ))
        
        
    def count_budget(self):
        new_budget = []
        print(datetime.now())
        now_date = datetime.now().strftime('%Y-%m-%d')
        for period in ['Day', 'Week', 'Month']:
            b = self.repo.get_expenses_per_period(period, '2022-10-01')  
            new_budget.append(float(b))
        self.new_budget = Budget(*new_budget  )
          

    def run(self):
        
        self.count_budget()
        # self.limit_budget = list(map(str, (self.budget.day, self.budget.week, self.budget.month)))
        
        up_b = [a for a in zip(list(map(str, (self.new_budget.day, self.new_budget.week, self.new_budget.month))),
                  list(map(str, (self.budget.day, self.budget.week, self.budget.month))))]
    
        self.view.update_expenses([[exp.expense_date, str(exp.total), exp.name, exp.comment] for exp in self.expenses])
        self.view.update_budget(up_b)
        print('-_________')
    
            
    def add_expense_to_db(self, expense_class):
        self.repo.add("Expenses", expense_class.sql_format())


    def add_category_to_db(self, category_class):
        self.repo.add("Categories", category_class.sql_format())




    # def add_category(self, name, parent):
    #     if name in [c.name for c in self.cats]:
    #         raise ValidationError(
    #         f'Категория {name} уже существует')
    #     cat = Category(name, parent)
    #     self.category_repository.add(cat)
    #     self.cats.append(cat)
    #     self.view.set_category_list(self.cats)
    
    
if __name__ == "__main__":
    # v = View()
    app = QtWidgets.QApplication(sys.argv)
    bk = Bookkeeper()
    bk.run()
    print('hello')
    sys.exit(app.exec())
