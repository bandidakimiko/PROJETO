#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 117
# 60276 Beatriz Santos
# 60283 Alexandra Santos

from constants import NUM_HEADER_LINES
from constants import DATE_LINE
from constants import TIME_LINE


def removeHeader(fileName): #reads the header and ignores it and therefore returns the file without the header
    """
    Reads the lines after the header of the file
    Requires: fileName is str with the name of a .txt file
    Ensures: reads the file  without the header
    """    
    with open(fileName, 'r') as inFile:
        for _ in range(NUM_HEADER_LINES):
            inFile.readline()
        return inFile.readlines()


def readHeader(fileName): #reads the header and returns it in a list
    """
    Read the header of the file
    Requires:fileName is str with the name of a .txt file
    Ensures:returns the header as a list
    """
    inFile = open(fileName, 'r')
    header = []
    header = [next(inFile) for x in range(NUM_HEADER_LINES)]
    return header



def readSkippersFile(fileName):
    """
    Reads a file with a list of skippers into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a skipper listed in
    the file fileName (with all the info pieces belonging to that skipper),
    following the order provided in the lines of the file.
    """
    inFile = removeHeader(fileName)      

    skippersList = [] 

    for line in inFile:
        skippersData = line.rstrip().split(", ")
        skippersList.append(skippersData)
    return skippersList




def readRequestsFile(fileName):
    """
    Reads a file with a list of requested cruises with a given file name into a collection.
    Requires: 
    fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification.
    Ensures: 
    list of lists where each list corresponds to a request listed in
    the file fileName (with all the info pieces belonging to that skipper),
    following the order provided in the lines of the file.
    """
    inFile = removeHeader(fileName)      

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)
    return requestsList




def readScheduleFile(fileName): #reads the schedule file and creates a list of cruises scheduled
    """
    Reads a file with a list of schedule cruises with a given file name into a collection.
    Requires: 
    fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification.
    Ensures: 
    list of lists where each list corresponds to a schedule listed in
    the file fileName (with all the info pieces belonging to that skipper),
    following the order provided in the lines of the file.
    """
    inFile = removeHeader(fileName)

    scheduleList = [] 
    for line in inFile:
        scheduleData = line.rstrip().split(", ")
        scheduleList.append(scheduleData)
    return scheduleList

def readDate(fileName): #reads the file and returns only the date of the cruises
    """
    Reads a file and return the line that contains the date
    Requires: fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification.
    Ensures:the line that contains the date
    """
    with open(fileName, 'r') as inFile:
        for _ in range(DATE_LINE):
            inFile.readline()
        return inFile.readline()

def readTime(fileName): #reads the file and returns only the time of the cruises
    """
    Reads a file and return the line that contains the time
    Requires: fileName is str with the name of a .txt file containing
    a list of skippers organized as in the examples provided in
    the general specification.
    Ensures:the line that contains the time
    """
    with open(fileName, 'r') as inFile:
        for _ in range(TIME_LINE):
            inFile.readline()
        return inFile.readline()


