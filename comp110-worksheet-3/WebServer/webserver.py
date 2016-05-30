#!/usr/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()

print("Content-Type: text/html; charset=utf-8\n\n")

import cgi
form = cgi.FieldStorage()
if 'user' not in form:
  print ("Something Went Wrong")
else:
  print ("Hello" + str(form.getvalue("user")))

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='HighScores',
    user='root',
    passwd='',
    host='localhost')
c = conn.cursor()

my_first_int = 2
my_first_str = 'Two'

# Insert some example data.
c.execute("INSERT INTO High_Score VALUES (Caught, '2')")
c.execute("INSERT INTO High_Score VALUES (Lost, '3')")
c.execute("INSERT INTO High_Score VALUES (ID, '1')")
# c.execute("INSERT INTO users VALUES (" + my_first_int + ", '" + my_first_str +$
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM High_Score")
c.execute("SELECT * FROM High_Score")
print([(r[0], r[1]) for r in c.fetchall()])
