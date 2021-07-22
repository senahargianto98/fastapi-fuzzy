import sqlite3

conn = sqlite3.connect('blog.db')
print('Connected to database successfully.')

cur = conn.cursor()
rows = cur.execute("select * from fuzzy")
for row in rows:
   print(str(row[1]))