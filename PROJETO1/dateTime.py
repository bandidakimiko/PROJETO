#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 117
# 60276 Beatriz Santos
# 60283 Alexandra Santos


def hourToInt(time):
    """
    Splits the hours and minutes and returns the hours as an integer
    Requires: time has to be a string
    Ensures: returns the hours as an integer
    """
    t = str(time)
    t = t.split(":")
    return int(t[0])



def minutesToInt(time):
    """
    Splits the hours and minutes and returns the minutes as an integer
    Requires: time has to be a string
    Ensures: returns the minutes as an integer
    """
    t = str(time)
    t = t.split(":")
    return int(t[-1])



def intToTime(hour, minutes):
    """
    Changes the hours and minutes into a time format.
    Requires: hours and minutes have to be strings
    Ensures: returns the time
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m
    return h + ":" + m 

def TimeToInt(time): #Transforms the minutes and hours into an integer number, returning the time as an integer 
    """
    Turns the time into an integer
    Requires: time has to be a string
    Ensures: returns the time as an integer
    """
    t = str(time)
    t = t.split(':')
    hour = int(t[0])   
    min = int(t[1])     
    return min + hour * 100



def dayToInt(date): #Splits the date and returns just the day as an integer
    """
    Splits the date and returns the day as an integer
    Requires: date has to be a string
    Ensures: returns the day as an integer
    """
    d = str(date)
    d = d.split(":")
    return int(d[0])



def monthToInt(date): #Splits the date and returns just the month as an integer
    """
    Splits the date and returns the month as an integer
    Requires: date has to be a string
    Ensures: returns the month as an integer
    """
    m = str(date)
    m = m.split(":")
    return int(m[1])



def yearToInt(date): #Splits the date and returns just the year as an integer
    """
    Splits the date and returns the year as an integer
    Requires: date has to be a string
    Ensures: returns the year as an integer
    """
    y = str(date)
    y = y.split(":")
    return int(y[2])


def DateToInt(date): #Transforms the date into an integer and transforms it to the date format YYYYMMDD
    """
    Turns the date into an integer
    Requires: date has to be a string
    Ensures: returns the date as an integer in the format YYYYMMDD
    """
    d = str(date)
    d = d.split(':')
    print(d)
    day = int(d[0])   
    month = int(d[1])   
    year = int(d[2])   
    print(day, month, year)
    return day + month * 100 + year * 10000




def intToDate(day, month, year): #Changes the day, month and year into a date format DD:MM:YYYY.
    """
    Changes the day, month and year into a date format DD:MM:YYYY.
    Requires: day, month and year have to be strings
    Ensures: returns the date
    """
    d = str(day)
    m = str(month)
    y = str(year)

    if day < 10:
        d = "0" + d

    if month < 10:
        m = "0" + m
    
    if year < 10:
        y = "0" + y
    return d + ":" + m + ":" + y 


def intToDateFormat(date):
    """
    Turns a date in the format DD:MM:YYYY
    Requires: date has to be an integral
    Ensures: returs a string with the date
    """
    date = str(date)
    day = date[-2:]
    month = date[-4:-2]
    year = date[:-4]
    date = day + ':' + month + ':' + year
    return date

def updatedatetime(time, date): 
    """
    Returns the time and date
    Requires:time and date have to be strings
    Ensures:returns the time and the date
    """
    h = hourToInt(time)
    min = minutesToInt(time)
    day = dayToInt(date)
    month = monthToInt(date)
    year = yearToInt(date)

    if h < 8:
        h = 8
        min = 0

    elif h>20:
        h = 8
        min = 0
        if day == 30:
            day = 1
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        else:
            day +=1

    elif min >= 0 and min < 30: 
        min= 30

    elif min >= 30 and min <= 59:
        h += 1
        min = 0
    
    return intToTime(h,min), intToDate(day, month, year)

 








