from pyTemperature import *
from pypH import *
import MySQLdb
from time import sleep

db = MySQLdb.connect("localhost", "root", "aquarium", "AQUARIUMdb")
curs=db.cursor()


for i in range(1) :

	pH=readpH()
	
	Temp=0
	for i in range(10):
		Temp += readtemperature()
		sleep(5)
	Temp/=10	
	print pH,Temp
	sqlcmd ="""INSERT INTO tempdat (date,time,comments,temperature,pH,Relay1,Relay2) values(CURRENT_DATE(), NOW(), ' ',%f,%f,0,0)"""%(Temp,pH)
	print sqlcmd
	curs.execute (sqlcmd)
	db.commit()
