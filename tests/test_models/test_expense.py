from datetime import datetime

import pytest

from bookkeeper.repository.sqlite_repository import SqliteRepository
from bookkeeper.models.expense import Expense


@pytest.fixture
def repo():
    return SqliteRepository()


def test_create_with_full_args_list():
    e = Expense(name='test', total=100, category='food', expense_date=datetime.now(),
                comment='test', pk=1)
    assert e.total == 100
    assert e.category == 'food'


def test_create_brief():
    e = Expense('test', 100, 'food')
    assert e.name == 'test'
    assert e.total == 100
    assert e.category == 'food'

def test_default_velues():
    e = Expense('test', 100)
    assert e.category == 'Undefined'
    assert e.comment == ''

# def test_can_add_to_repo(repo):
#     e = Expense('test', 100)
#     pk = repo.add(e)
#     assert e.pk == pk


def test_sql_formatting():
    date_ = datetime.now()
    e = Expense(name='test', total=100, category='food', expense_date=date_,
                comment='test', pk=1)
    sql_format = {"expense":"test", "total":100, "category": "food", 'comment':'test', "date": date_.strftime("%Y-%m-%d") }
    print(sql_format, e.sql_format())
    assert sql_format == e.sql_format()