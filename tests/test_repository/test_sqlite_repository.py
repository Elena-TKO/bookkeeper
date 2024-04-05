from bookkeeper.repository.sqlite_repository import SqliteRepository
import pytest
from datetime import datetime


def test_get_total_per_period():
    repo = SqliteRepository()
    total_spend = repo.get_expenses_per_period('Month', datetime.now().strftime("%Y-%m-%d"))
    print(total_spend)
    assert isinstance(total_spend, float|int)

