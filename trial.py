import sqlite3
import time
conn = sqlite3.connect('a.sqlite')
cursor = conn.cursor()
start = time.time()
a=cursor.execute('select * from user')
print(time.time()-start)