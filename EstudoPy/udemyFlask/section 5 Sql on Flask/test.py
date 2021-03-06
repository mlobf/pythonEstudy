import sqlite3
from sqlite3.dbapi2 import connect

#-------------------------------------------------------------------------
#Create an connection
connection = sqlite3.connect("data.db")
#Create an cursor
cursor = connection.cursor()
# Bellow follows schema to create an table, table's Users.
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

#-------------------------------------------------------------------------
# Inserting one user by time
user = (1, "jose", "asdf")

insert_query = "INSERT INTO users VALUES (?,?,?)"

cursor.execute(insert_query, user)

#-------------------------------------------------------------------------
# Inserting many users at one time.
users = [
    (1, "jose", "asdf"),
    (2, "maria", "asdf"),
    (3, "josezinho", "asdf"),
    (4, "joao", "asdf"),
    (5, "carlos", "asdf"),
    (6, "eduardo", "asdf"),
    (7, "flavio", "asdf"),
    (8, "cardoso", "asdf"),
    (9, "manuel", "asdf"),
    (10, "jair", "asdf"),
    (11, "pablo", "asdf"),
    (12, "marcelo", "asdf"),
    (13, "fabiane", "asdf"),
    (14, "fabiana", "asdf"),
    (15, "fabio", "asdf"),
    (15, "sacifufu", "asdf"),
    (16, "cleide", "asdf"),
]

cursor.executemany(insert_query, users)
#-------------------------------------------------------------------------
#Retrive information form table
select_query = "SELECT * FROM users"
# select_query = "SELECT id FROM users"
# select_query = "SELECT username FROM users"

for row in cursor.execute(select_query):
    print(row)


#-------------------------------------------------------------------------
#Closing commitin and  connection.
connection.commit()

connection.close()
