import sqlite3

conn = sqlite3.connect("reviews.db")

class Database:
    def __init__(self,path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS review(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone_number TEXT,
            rate INTEGER,
            text TEXT                       
            )          
            ''')

            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS store (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name_product TEXT,
                               size TEXT,
                               price TEXT,
                               photo TEXT,
                               product_id TEXT
                           )
                       """)

            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS products_details (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               product_id INTEGER,
                               category TEXT,
                               info_product TEXT
                           )
                       """)

            conn.commit()

    def add_complaint(self,data:dict):
        print(data)
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO review (name,phone_number,rate,text) VALUES(?,?,?,?)     
            ''',
                (data["name"],data["phone_number"],data["rate"],data["text"]),
                        )
            conn.commit()

