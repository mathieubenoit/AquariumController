import os
#os.system("source /home/pi/root/bin/thisroot.sh")
from plotter import * 
from ROOT import THttpServer,TGraph
from time import sleep

os.setuid(1000)

server = THttpServer("""http:8080""")

grT = TGraph(1000000)
grpH = TGraph(1000000)
grT.SetName("Temperature")
grpH.SetName("pH")
UpdatePlots(grT,grpH)
server.Register("/",grT)
server.Register("/",grpH)
while 1 :
	UpdatePlots(grT,grpH)	
	sleep(60)
	#print "Alive!!!!"

