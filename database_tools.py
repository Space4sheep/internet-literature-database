import sqlite3

import pandas as pd

books = pd.read_csv('StarylevLib.csv')

conn = sqlite3.connect('db.sqlite3')
#c = conn.cursor()

#c.execute('''CREATE TABLE books (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title text, author text, url text)''')

books.to_sql('main_book', conn, if_exists='append', index=False)
