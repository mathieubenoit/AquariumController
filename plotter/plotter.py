import MySQLdb
from ROOT import TGraph,TCanvas,gROOT
import datetime 
from dateutil import parser
from time import mktime
def convertTime(day,time): 
	date_object =datetime.datetime(day.year, day.month, day.day) + time
	return mktime(date_object.timetuple())

def UpdatePlots(grT,grpH):
#gROOT.SetStyle("Pub")

    db = MySQLdb.connect("localhost", "root", "aquarium", "AQUARIUMdb")
    curs=db.cursor()


    sqlcmd = "SELECT * FROM tempdat"

    curs.execute(sqlcmd)
    data=curs.fetchall()


    grT .Set(len(data))	
    grpH.Set(len(data))

    for i,col in enumerate(data) : 

        Time=convertTime(col[0],col[1])
        #print col[0],col[1],col[3],col[4],Time
        grT.SetPoint(i,Time,col[3])
        grpH.SetPoint(i,Time,col[4])

    grT.GetXaxis().SetTimeDisplay(1)
    grpH.GetXaxis().SetTimeDisplay(1)
    grpH.GetXaxis().SetNdivisions(8)
    grT.GetXaxis().SetNdivisions(8)
    grT.GetXaxis().SetTimeFormat("%d-%m-%Y %H:%M");
    grpH.GetXaxis().SetTimeFormat("%d-%m-%Y %H:%M");
    grT.GetXaxis().SetTimeOffset(3600)
    grpH.GetXaxis().SetTimeOffset(3600)

    grT.GetXaxis().SetLabelSize(0.02)
    grpH.GetXaxis().SetLabelSize(0.02)
    grT.GetYaxis().SetLabelSize(0.025)
    grpH.GetYaxis().SetLabelSize(0.025)

    grT.GetYaxis().SetTitleOffset(1.3)


    grT.SetMarkerSize(0.01)
    grpH.SetMarkerSize(0.01)

    grT.SetLineColor(2)
    grpH.SetLineColor(3)

    grT.GetYaxis().SetTitle("Temperature (C)")
    grT.GetYaxis().SetRangeUser(25,30)

    grpH.GetYaxis().SetTitle("pH")
    
    grT.SetTitle("Aquarium water temperature")
    grpH.SetTitle("Aquarium water pH")
    
    
    
   # return grT,grpH

    #can.Divide(2)
    #can.cd(1)
    #grT.Draw("AC*")
    #can.cd(2)
    #grpH.Draw("AC*")




