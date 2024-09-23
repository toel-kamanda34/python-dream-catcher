import sqlite3

CONN = sqlite3.connect('dreams.db')
CURSOR = CONN.cursor()