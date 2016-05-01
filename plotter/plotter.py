import MySQLdb
from ROOT import TGraph,TCanvas,gROOT
import datetime 
from dateutil import parser
from time import mktime
def convertTime(day,time): 
	date_object =datetime.datetime(day.year, day.month, day.day) + time
	return mktime(date_object.timetuple())

def UpdatePlots(grT,grpH,grT24,grpH24):
#gROOT.SetStyle("Pub")

    db = MySQLdb.connect("localhost", "root", "aquarium", "AQUARIUMdb")
    curs=db.cursor()


    sqlcmd = "SELECT * FROM tempdat"

    curs.execute(sqlcmd)
    data=curs.fetchall()
    
    sqlcmd = "SELECT * FROM tempdat WHERE TIMESTAMP(date, time)  >= (now() - INTERVAL 1 DAY) ;"
    curs.execute(sqlcmd)
    data24 = curs.fetchall()
    #print data24
    
    grT .Set(len(data))	
    grpH.Set(len(data))
    
    grT24 .Set(len(data24))	
    grpH24.Set(len(data24))
    formattedData_pH = [[],[]]    
    for i,col in enumerate(data) : 

        Time=convertTime(col[0],col[1])
        #print col[0],col[1],col[3],col[4],Time
        formattedData_pH[0].append(Time)
        formattedData_pH[1].append(col[4])       
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
    formattedData24_pH = [[],[]]    
    for i,col in enumerate(data24) : 

        Time=convertTime(col[0],col[1])
        #print col[0],col[1],col[3],col[4],Time
        formattedData24_pH[0].append(Time)
        formattedData24_pH[1].append(col[4])
        grT24.SetPoint(i,Time,col[3])
        grpH24.SetPoint(i,Time,col[4])

    grT24.GetXaxis().SetTimeDisplay(1)
    grpH24.GetXaxis().SetTimeDisplay(1)
    grpH24.GetXaxis().SetNdivisions(8)
    grT24.GetXaxis().SetNdivisions(8)
    grT24.GetXaxis().SetTimeFormat("%d-%m-%Y %H:%M");
    grpH24.GetXaxis().SetTimeFormat("%d-%m-%Y %H:%M");
    grT24.GetXaxis().SetTimeOffset(3600)
    grpH24.GetXaxis().SetTimeOffset(3600)

    grT24.GetXaxis().SetLabelSize(0.02)
    grpH24.GetXaxis().SetLabelSize(0.02)
    grT24.GetYaxis().SetLabelSize(0.025)
    grpH24.GetYaxis().SetLabelSize(0.025)

    grT24.GetYaxis().SetTitleOffset(1.3)


    grT24.SetMarkerSize(0.01)
    grpH24.SetMarkerSize(0.01)

    grT24.SetLineColor(2)
    grpH24.SetLineColor(3)

    grT24.GetYaxis().SetTitle("Temperature (C)")
    grT24.GetYaxis().SetRangeUser(25,30)

    grpH24.GetYaxis().SetTitle("pH")
    
    grT24.SetTitle("Aquarium water temperature")
    grpH24.SetTitle("Aquarium water pH")    
    
    return formattedData_pH

    #can.Divide(2)
    #can.cd(1)
    #grT.Draw("AC*")
    #can.cd(2)
    #grpH.Draw("AC*")




