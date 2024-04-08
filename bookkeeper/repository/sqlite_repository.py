import os.path
import sqlite3
from datetime import datetime, date
from bookkeeper.repository.test_data import *
import calendar



## COMMON FUNCTIONS
def prepare_data( input: list) -> str:
    new_input = []
    for el in input:
        if isinstance(el, str):
            el = "'" + el + "'"
        new_input.append(str(el))
    return ','.join(new_input)


def make_sql_type_data(input: dict) -> dict:
    new_input = {}
    for k,v in input.items():
        if isinstance(v, str):
            v = "'" + v + "'"
        new_input[k] = str(v)
    return new_input


def weekdays(input_day:str) -> list[str]:
    year, month, day = map(int, input_day.split('-'))
    my_day = date(year, month, day)
    c = calendar.Calendar()
    for week in c.monthdatescalendar(year, month):
        if my_day in week:
            return[weekday.strftime("%Y-%m-%d") for weekday in week]

class SqliteRepository():
    def __init__(self, **table_classes):
        ## table_classes: {"Table1": [{col1:val1,col2:val2}], "Table2": [{col1:val1},{col1:val2}, {col1:val3}]}
        self.dbname = 'database.db'
        self.table_names = [key for key in table_classes]
        self.table_data = table_classes
        #TODO: добавить автоматическую обработку таблиц
        self.table_columns = {"Expenses": ['title', 'category', 'total', 'date'], "Categories": ['category', 'description']}
        self.limits = {
            "Day":1000, "Week": 3000, "Month": 20000
        }
        self.table_ids = {"Expenses":"expense_id", "Categories":"category_id"}


        if not os.path.exists('database.db'):
            print("Creating database...")
            db = sqlite3.connect('database.db')
            c = db.cursor()
            # Создание таблицы

            c.execute("""CREATE TABLE Expenses (
                expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense TEXT,
                category TEXT,
                comment TEXT,
                total FLOAT,
                date DATE
            )""")
            c.execute("""CREATE TABLE Categories (
                    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT,
                    description TEXT
                )""")
            db.close()


    # def watch_database():
    #     db = sqlite3.connect('database.db')
    #     c = db.cursor()
    #     # TODO: write
    #     db.close()

    def watch_table(self, table_name:str):
        db = sqlite3.connect(self.dbname)
        c = db.cursor()
        print(f"Table: {table_name}")
        c.execute(f"""SELECT * FROM {table_name}""")
        table_data = c.fetchall()
        if table_data == []:
            print("No data")
        else:
            
            for line in table_data:
                print(line)
        db.close()
        
    
    def get_table(self, table_name:str):
        db = sqlite3.connect(self.dbname)
        c = db.cursor()
        print(f"Table: {table_name}")
        c.execute(f"""SELECT * FROM {table_name}""")
        table_data = c.fetchall()
        if table_data == []:
            print("No data")
        else:
            return table_data
        db.close()


    def get_row(self, table_name:str, row_id:int):
        db = sqlite3.connect(self.dbname)
        c = db.cursor()

        id_name = self.table_ids[table_name]
        c.execute(f"""
                SELECT * FROM {table_name}
                WHERE {id_name} = {row_id}
        """)
        res = c.fetchall()[0]
        db.close()
        res_dict = {}
        for i,el in enumerate(res):
            if i == 0:
                column = id_name
            else:
                column = self.table_columns[table_name][i-1]
            value = res[i]
            res_dict[column] = value
        return res_dict

    def get_expenses_per_period(self, period:str, date:str):
        """
        date: "2000-10-01"
        period: "Day"/"Week"/"Month"
        """

        db = sqlite3.connect('database.db')
        c = db.cursor()

        today = datetime.strptime(date, "%Y-%m-%d")

        today_dict = {
            "Year" : today.year,
            "Month" : today.month,
            "Day" : today.day
        }
        year, month, day = today_dict['Year'], today_dict['Month'], today_dict['Day']
        today_sql_format = f"{today_dict['Year']}-{today_dict['Month']}-{today_dict['Day']}"
        # date = datetime.strptime(today, "%Y-%m-d")
        if True:
            if period == 'Day':
                condition = f"date = '{today_sql_format}'"

            if period == 'Week':
                current_week_days = weekdays(today_sql_format)
                current_week_days_sql = ','.join([f"'{el}'" for el in current_week_days])
                condition = f"date IN ({current_week_days_sql})"

            if period == "Month":
                condition = f"Month = '{month}' and Year = '{year}' "

            query = f"""
                        SELECT SUM(period_sum) FROM
                                            (
                                                        SELECT SUM(total) as period_sum, strftime('%d', date) as Day, strftime('%m', date) as Month, strftime('%Y', date) as Year
                                                        FROM Expenses
                                                        WHERE {condition}
                                                        GROUP BY  Year, Month, Day
                                            )
                                            """

            c.execute(query)
            res = c.fetchall()
            db.close()

            if res == [] or res[0][0] == None:
                return 0
            else:
                return res[0][0]



    def add(self, table_name:str, row_to_add:dict):
        db = sqlite3.connect('database.db')
        c = db.cursor()

        #TODO: add checking
        values = prepare_data(row_to_add.values())
        columns = prepare_data(row_to_add.keys())
        c.execute(f"""
                        INSERT INTO {table_name} ({columns}) VALUES
                        ({values})
                    """)
        db.commit()
        db.close()

    def update(self, table_name:str, table_updates:dict, condition:dict):
        db = sqlite3.connect('database.db')
        c = db.cursor()

        table_updates = make_sql_type_data(table_updates)
        print(table_updates)
        query_set = [  ' = '.join([k,v])  for k,v in table_updates.items()]
        query_set = ','.join(query_set)

        row_id, id_ = [(k,v) for k,v in condition.items()][0]
        query = f"""UPDATE {table_name} 
                    SET {query_set} 
                    WHERE  {row_id} = {id_}"""
        print("""UPDATE Categories 
                    SET category = 'dog', description = 'its a dog' 
                    WHERE  category_id = 1;""")
        #TODO: add query for WHERE {}
        c.execute(query)

        db.commit()
        db.close()

    def delete(self, table_name:str, row_to_delete:dict):
        db = sqlite3.connect('database.db')
        c = db.cursor()

        row_to_delete = make_sql_type_data(row_to_delete)
        column, name = [(k, v) for k, v in row_to_delete.items()][0]
        c.execute(f"""DELETE FROM {table_name} WHERE {column} = {name}""")

        db.commit()
        db.close()

    def get_expenses_per_period_old(self, period)->int:
        db = sqlite3.connect('database.db')
        c = db.cursor()

        patterns = {"Day, Month, Year":'%Y-%m-%d','Month, Year':'%Y-%m', "Year": '%Y'}
        date_dict = {}
        for p, pattern in patterns.items():
            try:
                date = datetime.strptime(period, pattern)
                sql_period = p
                date_dict['Day'] = date.day
                date_dict['Month'] = date.month
                date_dict['Year'] = date.year
            except:
                continue

        new_date_dict = date_dict.copy()
        for el in date_dict:
            if el not in sql_period:
                new_date_dict.pop(el)

        date_condition = ' and '.join([ f"{el} = '{new_date_dict[el]}'"    for el in new_date_dict])
        # print(date, date_condition)
        query = f"""
                SELECT period_sum FROM 
                (
                SELECT SUM(total) as period_sum, strftime('%d', date) as Day, strftime('%m', date) as Month, strftime('%Y', date) as Year
                FROM Expenses
                WHERE {date_condition}
                GROUP BY {sql_period}
                )
        """
        c.execute(query)
        res = c.fetchall()
        db.close()

        if res == []:
            raise ValueError("No such date in database...")
        if len(res) != 1:
            raise ValueError("Something truly wrong...")

        return res[0][0]







def create_test_categories(repo):
    for category, desc in test_categories.items():
        repo.add("Categories",  {"category":category, "description":desc})


def create_test_expenses(repo):
    for expense in test_expenses:
        repo.add("Expenses", expense)




# Добавление данных

# Удаление данных
# c.execute("DELETE FROM articles WHERE avtor = 'Admin'")

# Изменение данных
# c.execute("UPDATE articles SET avtor = 'Admin', views = 1 WHERE title = 'Amazon is cool!'")
#
# # Выборка данных
# c.execute("SELECT rowid, * FROM articles WHERE rowid < 5 ORDER BY views")
# items = c.fetchall()
# print(items)
# # print(c.fetchmany(1))
# # print(c.fetchone()[1])
#
# # for el in items:
# #     print(el[1] + "\n" + el[4])
#
# db.commit()



## CATEGORIES
def add_categories(rows:list[dict]):
        ## rows: [{'category':'name1', 'description':'desc1'}, {}....]
        db = sqlite3.connect('database.db')
        c = db.cursor()

        c.execute("SELECT category FROM Categories")
        categories = c.fetchall()
        print(categories)
        for row in rows:
            c.execute("""
                INSERT INTO Categories VALUES
                (?, ?, ?)
            """, ('', {row['category']}, {row['description']}))
        db.close()

def update_categories(renamer:dict):
    ## renamer: {old_category: [new_category,new_description], ....}
    db = sqlite3.connect('database.db')
    c = db.cursor()
    for category in renamer:
        new_name = renamer[category][0]
        new_description= renamer[category][1]
        if new_description:
            c.execute(f"UPDATE Categories SET description = (?) WHERE category = (?)",
                      (new_description, category ))
        if renamer[category][0] != category:
            c.execute(f"UPDATE Categories SET category = (?) WHERE category = (?)",
                      (new_name, category))
    db.close()


## EXPENSES

def add_expense(title, category, total, date):
    db = sqlite3.connect('database.db')
    c = db.cursor()
    c.execute(f"""INSERT INTO Expenses VALUES
     ({title}, {category}, {total}, {date})""")
    db.close()





if __name__ == "__main__":
    repo = SqliteRepository()
    # repo.add("Categories", {"category":"cat", "description":"it is a cat"})

    # repo.update('Categories', {'category':'dog', 'description':"it is a dog"}, {'category_id':1})
    # repo.delete('Categories', {'category':'cat'})
    # create_test_expenses(repo)
    # create_test_categories(repo)

    # total_per_period = repo.get_expenses_per_period('Month', '2022-10-01')
    # print(total_per_period)
    # print(repo.get_row('Categories', 4))

