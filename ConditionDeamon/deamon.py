from pyTemperature import *
from pypH import *
import MySQLdb


db = MySQLdb.connect("localhost", "root", "aquarium", "AQUARIUMdb")
curs=db.cursor()


for i in range(1) :

	pH=readpH()
	Temp = readtemperature()

	print pH,Temp
	sqlcmd ="""INSERT INTO tempdat (date,time,comments,temperature,pH,Relay1,Relay2) values(CURRENT_DATE(), NOW(), ' ',%f,%f,0,0)"""%(Temp,pH)
	print sqlcmd
	curs.execute (sqlcmd)
	db.commit()
