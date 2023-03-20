#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 117
# 60276 Beatriz Santos
# 60283 Alexandra Santos

import datetime
import scheduling
import readingFromFiles




def writeScheduleFile(schedule, header, fileName):
    """
    Writes a collection of scheduled cruises into a file.
    Requires:
    schedule is a list with the structure as in the output of
    scheduling.updateSchedule representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the cruises in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the cruises as ordered head to tail in schedule.
    """
    header = readingFromFiles.readHeader(fileName)
    time = header[5]
    date = header[3]
    hours, minutes = map(int, time.split(':'))
    minutes += 30

    if minutes >= 60:
        hours += 1
        minutes -= 60

    if hours >= 20:
        hours = 8
        day, month, year = map(int, date.split(':'))
        date = datetime.datetime(year, month, day)
        date += datetime.timedelta(days=1)
        date = date.strftime('%d:%m:%Y')

    fileName = f'schedule{hours:02d}h{minutes:02d}.txt'

    with open(fileName, 'w') as inFile:
        header = str(header)
        header.strip('\n')
        inFile.write(header)
        schedule = str(schedule)
        inFile.write(schedule)
    return inFile




def writeSkippersFile(skippers, header, fileName):
    """
    Writes a collection of sckippers cruises into a file.
    Requires:
    Skippers is a list with the structure as in the output of
    skipper.updateSkipper«+ representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the cruises in skippers,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the cruises as ordered head to tail in skippers.
    """
    header = readingFromFiles.readHeader(fileName)
    time = header[5]
    date = header[3]
    hours, minutes = map(int, time.split(':'))
    minutes += 30

    if minutes >= 60:
        hours += 1
        minutes -= 60

    if hours >= 20:
        hours = 8
        day, month, year = map(int, date.split(':'))
        date = datetime.datetime(year, month, day)
        date += datetime.timedelta(days=1)
        date = date.strftime('%d:%m:%Y')

    fileName = f'skippers{hours:02d}h{minutes:02d}.txt'

    with open(fileName, 'w') as inFile:
        header = str(header)
        header.strip('\n')
        inFile.write(header)
        skippers = str(skippers)
        inFile.write(skippers)
    return inFile

