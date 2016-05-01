import os
#os.system("source /home/pi/root/bin/thisroot.sh")
from plotter import * 
from ROOT import THttpServer,TGraph
from time import sleep

os.setuid(1000)

server = THttpServer("""http:8080""")

grT = TGraph(1000000)
grpH = TGraph(1000000)
grT24 = TGraph(1000000)
grpH24 = TGraph(1000000)

grT.SetName("Temperature")
grpH.SetName("pH")
grT24.SetName("Temperature 24H")
grpH24.SetName("pH 24H") 

UpdatePlots(grT,grpH,grT24,grpH24)
server.Register("/",grT)
server.Register("/",grpH)
server.Register("/",grT24)
server.Register("/",grpH24)
while 1 :
	UpdatePlots(grT,grpH,grT24,grpH24)	
	sleep(60)
	#print "Alive!!!!"

