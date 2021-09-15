import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="rail",port=3306)
print("Connection done")
mycursor=mydb.cursor()
mycursor.execute("create table traindetail(tname char(50) default null,tnum int(10) default null,ac1 int(20) default null,ac2 int(20) default null,ac3 int(20)default null,slp int(20) default null)")
mycursor.execute("create table passengers(pname char(50) default null,age int(10) default null,trainno int(20) default null,noofpas int(20) default null,cls varchar(200) default null,amt int(20) default null,status char(50) default null,pnrno int(20) default null)")
mydb.close()


