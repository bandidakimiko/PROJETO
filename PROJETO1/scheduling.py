#-*- coding: utf-8 -*-

# 2022-2023 Programação 1 (LTI)
# Grupo 117
# 60276 Beatriz Santos
# 60283 Alexandra Santos


import readingFromFiles
import dateTime
import constants
import numpy as np
import datetime

skippers = readingFromFiles.readSkippersFile('skippers18h00.txt')
schedule = readingFromFiles.readScheduleFile('schedule18h00.txt')
requests = readingFromFiles.readRequestsFile('requests18h00.txt')
previousDate = readingFromFiles.readDate('skippers18h00.txt')
previousHour = readingFromFiles.readTime('skippers18h00.txt')

# The next function returns the same list of scheduled cruises without the ones that have already been done.

def get_cruises(sch,d,h):
	"""
	Creates a list of scheduled cruises without the ones that have aleadry been done
	Requires:sch is a list, d have to be date and h is a hour
	Ensures:returns the list of scheduled cruises without the ones that have aleadry been done
	"""
	my_array = []
	for i in range(len(sch)):
		if dateTime.DateToInt(sch[i][0]) > dateTime.DateToInt(d):
			my_array.append(sch[i])
		elif dateTime.DateToInt(sch[i][0]) == dateTime.DateToInt(d):
			if dateTime.hourToInt(sch[i][1]) > dateTime.hourToInt(h):
				my_array.append(sch[i])
			elif dateTime.hourToInt(sch[i][1]) == dateTime.hourToInt(h):
				if dateTime.minutesToInt(sch[i][1]) >= dateTime.minutesToInt(h):
					my_array.append(sch[i])

	return my_array




# The next function separates the languages of a element in a list

def sep_languages(string1, string2):
    """
    Creates a list and separates the languages of an element
    Requires: string1 and string2 has to be a string
    Ensures:returns a list with the languages of an element
    """

    flag1 = False
    string1 = str(string1)
    string2 = str(string2)
    array1=[]
    array2=[]

    array1 = string1.rstrip(")").lstrip("(").split("; ")
    array2 = string2.rstrip(")").lstrip("(").split("; ")

    if len(array2)>len(array1):
        b=array1
        a=array2
    else:
        a=array1
        b=array2

    flag1 = np.any(np.in1d(a, b))
    return flag1


# The next function gives a list with the clients and skippers 

def get_skippers(req,skip):
    """
    Creats a list with the clients and skippers 
    Requires: req and skip has to be a list
    Ensures:returns a list of the clients and the skippers
    """

    skp = []
    skippers_list = []
    client_list = []
    flag = 0

    for line in range(len(req)):
        for element in range(len(skip)):
            if sep_languages(req[line][constants.LANGUAGE_IDX], skip[element][constants.LANGUAGE_IDX]) == True:
                if req[line][constants.CATEGORY_IDX] == skip[element][constants.CATEGORY_IDX]:
                    if req[line][constants.SPECIALIZATION_REQ_IDX] == skip[element][constants.SPECIALIZATION_SKP_IDX]:
                        if int(skip[element][constants.HOURSDONE_SKP_IDX]) + int(req[line][constants.REQUESTEDHOURS_IDX]) <= int(skip[element][constants.HOURSCANDO_SKP_IDX]):
                            skp.append(skip[element])
                            skp.sort(key = lambda skp: (skp[constants.TIME_SKP_IDX], skp[constants.PRICE_SKP_IDX], skp[constants.HOURSDONE_SKP_IDX], skp[constants.SKIPPER_NAME_IDX]))
                        else:
                            flag += 1 
                    else:
                        flag += 1 
                else:
                    flag += 1             
            else:
                flag += 1 
        
        if flag == len(skip):
            skippers_list.append(constants.NOT_ASSIGNED)
        else:
            skippers_list.append(skp[constants.SKIPPER_NAME_IDX])

        client_list.append(req[line][constants.CLIENT_NAME_IDX])

        flag = 0  
        skp = []             
    
    return skippers_list, client_list




def updateSchedule(skippers, requests, schedule, previousDate, previousHour):
    """
    Update cruises' schedule assigning the cruises requested given
    to the skippers given taking into account a previous schedule.
    Requires:
    skippers is a list of lists with the structure as in the output of
	readingFromFiles.readSkipersFile concerning the previous update time;
	schedule is a list of lists with the structure as in the output of
	readingFromFiles.readScheduleFile concerning the previous update time;
	requests is a list of lists with the structure as in the output of 
	readingFromFiles.readRequestsFile concerning the current update time;
	date is string in format DD:MM:YYYY with the previous update date;
	hour is string in format HH:MN: with the previous update hour;
    Ensures:
    a list of cruises, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	(omitted here for the sake of readability).
    """
    updatedScheduleCruises = []
    newCruises = []
    updatedScheduleCruises += get_cruises(schedule, previousDate, previousHour)
    sk_list = get_skippers(requests,skippers)[0]
    cl_list = get_skippers(requests,skippers)[1]
    i = 0
    for line in range(len(sk_list)):
        newlist = []
        if sk_list[line] == constants.NOT_ASSIGNED:
            date = previousDate.strip('\n')
            newlist.append(date)
            newlist.append(sk_list[line])
            newlist.append(cl_list[line])
            newCruises.append(newlist)
            i += 1
        else:
            date = str(sk_list[line][constants.DATE_SKP_IDX])
            hour = str(sk_list[line][constants.TIME_SKP_IDX])
            if dateTime.hourToInt(hour) >= dateTime.hourToInt('20:00'):
                hour = dateTime.intToTime(8, 00)
                hour = hour.rstrip(')')
                date = date.lstrip('(')
                date = dateTime.DateToInt(date)
                date = date + 1
                date = dateTime.intToDateFormat(date)
            else:
                date = date
                hour = hour.rstrip(')')
                date = date.lstrip('(')
                hour = dateTime.TimeToInt(hour)
                hour += 30
                hour = str(hour)
                time = datetime.datetime.strptime(hour, '%H%M').time()
                hour = time.strftime('%H:%M')

            price = int(requests[line][constants.REQUESTEDHOURS_IDX]) * int(sk_list[line][constants.PRICE_SKP_IDX])
            newlist.append(date)
            newlist.append(hour)
            newlist.append(requests[line][constants.REQUESTEDHOURS_IDX])
            newlist.append(sk_list[line][constants.SKIPPER_NAME_IDX])
            newlist.append(price)
            newlist.append(cl_list[line])
            newCruises.append(newlist)
            i += 1
    updatedScheduleCruises += newCruises
    updatedScheduleCruises.sort(key = lambda updatedScheduleCruises: updatedScheduleCruises[1] == constants.NOT_ASSIGNED)
    updatedScheduleCruises.sort(key = lambda updatedScheduleCruises: updatedScheduleCruises[0])
    updatedScheduleCruises.sort(key = lambda updatedScheduleCruises: updatedScheduleCruises[1])
    updatedScheduleCruises.sort(key = lambda updatedScheduleCruises: updatedScheduleCruises[2])

    return  updatedScheduleCruises




def updateSkippers(skippers, schedule):
    '''
    A list with the list of skippers updated
    Requires: 
    skippers is a list of lists with the structure as in the output of
	readingFromFiles.readSkipersFile concerning the previous update time;
	schedule is a list of lists with the structure as in the output of
	readingFromFiles.readScheduleFile concerning the previous update time;
	requests is a list of lists with the structure as in the output of 
	readingFromFiles.readRequestsFile concerning the current update time
    Ensures: 
    a list of skippers, representing the previous list updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	(omitted here for the sake of readability).
    '''
    updatedSkippers = []
    new_list = []
    
    for line in skippers:

        skippers_name = line[constants.SKIPPER_NAME_IDX]
        skippers_language = line[constants.LANGUAGE_IDX]
        skippers_category = line[constants.CATEGORY_IDX]
        skippers_price = line[constants.PRICE_SKP_IDX]
        skippers_specialization = line[constants.SPECIALIZATION_SKP_IDX]
        skippers_totalHours = line[constants.HOURSCANDO_SKP_IDX]
        skippers_hoursDone = line[constants.HOURSDONE_SKP_IDX]

        new_list.append(skippers_name) 
        new_list.append(skippers_language) 
        new_list.append(skippers_category) 
        new_list.append(skippers_price)
        new_list.append(skippers_specialization) 
        new_list.append(skippers_totalHours) 
        new_list.append(skippers_hoursDone) 
        updatedSkippers.append(new_list)

        new_list = []

    for line in range(len(skippers)):
        skippers_lastcruise = schedule[line][0]
        new_list.append(skippers_lastcruise)

        if line in schedule != constants.NOT_ASSIGNED:
            skippers_lastcruisehour = line[1]  
            new_list.append(skippers_lastcruisehour)

        updatedSkippers.append(new_list)

    return updatedSkippers
    
