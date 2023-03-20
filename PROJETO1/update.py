#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 117
# 60276 Beatriz Santos
# 60283 Alexandra Santos


import sys
import readingFromFiles
import dateTime
import writingToFiles
import scheduling

 

def assign(skippersFileName, scheduleFileName, requestsFileName):
    """
    Runs the enjoyTagus application.

    Requires:
    skippersFileName is a str with the name of a .txt file containing a list
    of skippers, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of cruises assigned to skippers as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested;
    these input files concern the same company, date and time.
    Ensures:
    writing of two .txt files containing the updated list of cruises assigned
    to skippers and the updated list of skippers, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, scheduleXXhYY.txt and
    skippersXXhYY.txt, where XXhYY represents the time and date 30 minutes
    after the time and date indicated in the files skippersFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """   
    skippers = readingFromFiles.readSkippersFile(skippersFileName)
    schedule = readingFromFiles.readScheduleFile(scheduleFileName)
    requests = readingFromFiles.readRequestsFile(requestsFileName)

    skpheader = readingFromFiles.readHeader(skippersFileName)
    schheader = readingFromFiles.readHeader(scheduleFileName)


    previousDate = readingFromFiles.readDate(scheduleFileName)
    previousHour = readingFromFiles.readTime(scheduleFileName)
    
    date = dateTime.intToDateFormat(previousDate)
    hour = previousHour.strip('\n')
    

    updatedschedule = scheduling.updateSchedule(skippers, schedule, requests, date, hour )
    updatedskippers = scheduling.updateSkippers(skippers, updatedschedule)

    output1 = writingToFiles.writeSkippersFile(updatedschedule, skpheader, updatedschedule)
    output2 = writingToFiles.writeScheduleFile(updatedskippers, schheader, updatedskippers)

    return output1, output2


print(len(sys.argv))




    