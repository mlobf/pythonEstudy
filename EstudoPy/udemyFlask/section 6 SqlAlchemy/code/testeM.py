import sqlite3
from sqlite3.dbapi2 import connect
from flask_restful import Resource, reqparse
import user

username =  "jose"

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


query = "SELECT * FROM users WHERE username=?"
result = cursor.execute(query, (username,))
if result:
    print('Y')

row = result.fetchone()


""":
for linha in row:
    print(row)
"""

print(row)

