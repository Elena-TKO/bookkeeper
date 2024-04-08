"""
Описан класс, представляющий расходную операцию
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Expense:
    """
    Расходная операция.
    amount - сумма
    category - id категории расходов
    expense_date - дата расхода
    added_date - дата добавления в бд
    comment - комментарий
    pk - id записи в базе данных
    """
    
    name: str
    total: int
    category: str = field(default='Undefined')
    comment: str = field(default='')
    expense_date: datetime = field(default_factory=datetime.now)
    # added_date: datetime = field(default_factory=datetime.now)
    pk: int = 0
    


    def sql_format(self):

        date_format = datetime.strftime(self.expense_date, "%Y-%m-%d")
        return {'expense':self.name, 'total':self.total, 'category':self.category,
                'comment':self.comment, 'date':date_format}
