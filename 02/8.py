import sqlite3

connect = sqlite3.connect("starships.sqlite")

cursor = connect.cursor()

cursor.execute(
    "SELECT name FROM ships WHERE NOT passenger = '0';"
)

print(cursor)
for i in cursor:
    print(i)


connect.commit()
connect.close()
