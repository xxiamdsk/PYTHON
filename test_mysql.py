import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="123456")
print(db)