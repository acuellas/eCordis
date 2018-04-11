import pymssql

# server    
# user      
# password  
# database  
conn = pymssql.connect('CHEN-PC\MSSQLSERVERNA', 'sa', '123', 'TestPython')

cursor = conn.cursor()

# CREATE TABLE AND INSERT
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])

conn.commit()

# SELECT METHOD
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

# 
# for row in cursor:
#     print("ID=%d, Name=%s" % (row[0], row[1]))

# CLOSE CONNECTION
conn.close()