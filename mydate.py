#mydate.py
import tkinter as tk
import datetime
from datetime import date

def ddmmyy(dt):
    dtstr=d1.strftime("%d-%m-%y")
    return dtstr

def endofmonth(dt):
    x=31
    m=dt.month
    y=dt.year
    edate=dt
    if m == 1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        edate=datetime.date(y,m,31)
        return enddate
    if m == 4 or m==6 or m==9 or m==11 :
        edate=datetime.date(y,m,30)
        return edate
    if m==2 :
        if y%4 ==0:
            edate=datetime.date(y,m,29)
            return edate
        else:
            edate=datetime.date(y,m,28)
            return edate

def endofQuarter(dt):
    m=dt.month
    y=dt.year
    edate=dt
    if m == 1 or m==2 or m==3:
        edate=datetime.date(y,3,31)
        return edate
    if m == 4 or m==5 or m==6:
        edate=datetime.date(y,6,30)
        return edate
    if m == 7 or m==8 or m==9:
        edate=datetime.date(y,9,30)
        return edate
    if m == 10 or m==11 or m==12:
        edate=datetime.date(y,12,31)
        return edate


def dtstr2Cordt(dtstr,begdate,enddate):
    #depending on begdate and enddate it will correct year
    #dd.mm.yy  or dd/mm/yy
    #vb code is given in remark below
    return corstr


def dateadd(dt,dmystr,num):
    #dmystr="d"  "m" "y"
    return dt

def datediff(dt1,dt2):
    return days

#following is vb code which intelligently fills yy according to begdate and enddate
#Public Function dtadjust(tdt As Date,begdate as date,enddate as date) As Date
#Dim dd As Integer, mm As Integer, yyyy As Integer
#If Year(begdate) <> Year(enddate) Then
#    dd = Day(tdt)
#    mm = Month(tdt)
#    yyyy = Year(tdt)
#    'begdate='01/04/08'  enddate='3103/09'
#    'if month chnged to 1,2,3 then change year to 09
#    If tdt < begdate Then
#        dtadjust = DateSerial(yyyy + 1, mm, dd)
#    End If
#    'if month changed to 4 to 12 change year to 08
#    If tdt > enddate Then
#        dtadjust = DateSerial(yyyy - 1, mm, dd)
#    End If
#Else
#    dtadjust = tdt
#End If
#End Function


root=tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
d1=datetime.datetime.now()
root.grid()
label1=tk.Label(root,text="todays date").grid(row=0,column=0)
label2=tk.Label(root,text=d1).grid(row=0,column=1)
#label3=tk.Label(root,text="weekday,short").grid(row=1,column=0)
#label3a=tk.Label(root,text=d1.strftime("%a")).grid(row=1,column=1)
#label4=tk.Label(root,text="weekday,full").grid(row=2,column=0)
#label4a=tk.Label(root,text="d1.strftime(%A)" +d1.strftime("%A")).grid(row=2,column=1)
#label4B=tk.Label(root,text="WEEKDAY NUM    %w"+d1.strftime("%w")).grid(row=3,column=0)
#label4B=tk.Label(root,text="day of month NUM    %d"+d1.strftime("%d")).grid(row=4,column=0)
#label4B=tk.Label(root,text="month mmm    %b"+d1.strftime("%b")).grid(row=5,column=0)
#label4B=tk.Label(root,text="month fullnm    %B"+d1.strftime("%B")).grid(row=6,column=0)
#label4B=tk.Label(root,text="month NUM    %m"+d1.strftime("%m")).grid(row=7,column=0)
#label4B=tk.Label(root,text="year yy    %y"+d1.strftime("%y")).grid(row=8,column=0)
#label4B=tk.Label(root,text="year yyyy    %Y"+d1.strftime("%Y")).grid(row=9,column=0)
#d2=d1+5
#label4B=tk.Label(root,text="d1+5="+str(d2)).grid(row=10,column=0)
d3=date.today()
label4B=tk.Label(root,text=date.today()).grid(row=11,column=0)
label4B=tk.Label(root,text=d3.day ).grid(row=12,column=0)
label4B=tk.Label(root,text=d3.month ).grid(row=12,column=1)
label4B=tk.Label(root,text=d3.year ).grid(row=12,column=2)
dtstr=d1.strftime("%I:%M:%S %p")
label4B=tk.Label(root,text=dtstr ).grid(row=13,column=0)
dtstr=d1.strftime("%d-%m-%y")
label4B=tk.Label(root,text=dtstr ).grid(row=13,column=1)
dtstr=ddmmyy(d1)
label4B=tk.Label(root,text=dtstr ).grid(row=13,column=2)
label4B=tk.Label(root,text="end of month " ).grid(row=14,column=0)
d4=endofmonth(d1)
label4B=tk.Label(root,text=d4 ).grid(row=14,column=1)
label4B=tk.Label(root,text="end quarter" ).grid(row=15,column=0)
d4=endofQuarter(d1)
label4B=tk.Label(root,text=d4 ).grid(row=15,column=1)
label4B=tk.Label(root,text="https://www.w3schools.com/python/python_datetime.asp").grid(row=19,column=0)
#https://www.guru99.com/date-time-and-datetime-classes-in-python.html
root.mainloop()
