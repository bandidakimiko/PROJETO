#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 77
# 60276 Beatriz Santos
# 60243 Beatriz Deus



class Skippers:
    
    def __init__(self, name, languages, category, price, specialization, duration, hours, lastCruiseDate, lastCruiseHour, fileName):
        '''
        
        Requires:
        Ensures:
        '''

        self._name = name
        self._languages = languages
        self._category = category
        self._price = price
        self._specialization = specialization
        self._duration = duration
        self._hours = hours
        self._lastCruiseDate = lastCruiseDate
        self._lastCruiseHour = lastCruiseHour
        self._fileName = fileName


    def getName(self):
        '''
        The name of the skipper.
        '''

        return self._name
    
    def setName(self, name):
        '''
        
        Requires:
        Ensures:
        '''

        self._name = name



    def getLanguages(self):
        '''
        The languages spoken by the skipper.
        '''

        return self._languages
    
    def setLanguages(self, languages):
        '''
        
        Requires:
        Ensures:
        '''

        self._languages = languages


    def getCategory(self):
        '''
        The category of the skipper's navigation chart.
        '''

        return self._category
    
    def setCategory(self, category):
        '''
        
        Requires:
        Ensures:
        '''

        self._category = category


    def getPrice(self):
        '''
        The price charged by the skipper
        '''

        return self._price
    
    def setPrice(self, price):
        '''
        
        Requires:
        Ensures:
        '''

        self._price = price


    def getSpecialization(self):
        '''
        The specialization of the skipper (confort, price or speed)
        '''

        return self._specialization
    
    def setSpecialization(self, specialization):
        '''
        
        Requires:
        Ensures:
        '''

        self._specialization = specialization


    def getDuration(self):
        '''
        The number of hours a skipper agrees to do without taking two days off.
        '''

        return self._duration
    
    def setDuration(self, duration):
        '''
        
        Requires:
        Ensures:
        '''

        self._duration = duration


    def getHours(self):
        '''
        Sum of the number of hours the skipper has scheduled.
        '''

        return self._hours
    
    def setHours(self, hours):
        '''
        
        Requires:
        Ensures:
        '''

        self._hours = hours

    
    def getLastCruiseDate(self):
        '''
        The date and hour of the last cruise scheduled for that skipper.
        '''

        return self._lastCruiseDate
    
    def setLastCruiseDate(self, lastCruiseDate):
        '''
        
        Requires:
        Ensures:
        '''

        self._lastCruiseDate = lastCruiseDate

    def getLastCruiseHour(self):
        '''
        The date and hour of the last cruise scheduled for that skipper.
        '''

        return self._lastCruiseHour
    
    def setLastCruiseHour(self, lastCruiseHour):
        '''

        '''

        self._lastCruiseHour = lastCruiseHour

    def getFileName(self):
        """
        
        """
        return self._fileName
    
    def setFileName(self, fileName):
        """
        
        """
        self._fileName = fileName


    def removeHeader_Skipper(self, fileName):
        """
        Remove the header of a file
        Requires:
        Ensures: 
        """

        without_header = []
        with open(fileName, 'r') as f:
            for i, line in enumerate(f):
                if i>=7:
                    without_header.append([elem.strip('(') for elem in line.strip().split(',')])
        return without_header

    def __str__(self):
        """
        
        Requires:
        Ensures:
        """
        return f"Skipper's name: {self._name}, languages: {self._languages}, category: {self._category}, price: {self._price}, specialization: {self._specialization}, duration {self._duration}, hours: {self._hours}, Date of the last cruise scheduled: {self._lastCruiseDate}, Time of the last cruise scheduled: {self._lastCruiseHour}"
    




