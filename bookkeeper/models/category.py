"""
Модель категории расходов
"""
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterator





@dataclass
class Category:
    
    name: str
    description: str
    pk: int = 0
    


    def sql_format(self):
        return {"category":self.name, "description":self.description}







