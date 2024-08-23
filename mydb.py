import pymysql

dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="Tamunodein@18"
)

cursorObj = dataBase.cursor()

cursorObj.execute("CREATE DATABASE mydb")

print("Done!")