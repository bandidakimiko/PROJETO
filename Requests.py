#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 77
# 60276 Beatriz Santos
# 60243 Beatriz Deus

import constants


class Requests:

    def _init_(self,name,languages,category,specialization,duration):
        '''
        
        Requires:
        Ensures:
        '''
        self._name=name
        self._languages=languages
        self._category=category
        self._specialization=specialization
        self._duration=duration

    def getName_Requests(self):
        '''

        Requires:
        Ensures:
        '''

        return self._name
    
    def setName_Requests(self,name):
        '''
        
        Requires:
        Ensures:
        '''

        self._name=name

    def getLanguages_Requests(self):
        '''
        
        Requires:
        Ensures:
        '''

        return self._languages

    def setLanguages_Requests(self,languages):
        '''
        
        Requires
        Ensures:
        '''

        self._languages=languages

    def getCategory_Requests(self):
        '''
        
        Requires:
        Ensures:
        '''

        return self._category
    
    def setCategory_Requests(self,category):
        '''
        
        Requires:
        Ensures:
        '''

        self._category=category

    def getSpecialization_Requests(self):
        '''
        
        Requires:
        Ensures:
        '''

        return self._specialization
    
    def setSpecialization_Requests(self,specialization):
        '''
        
        Requires:
        Ensures:
        '''

        self._specialization=specialization

    def getDuration_Requests(self):
        '''
        
        Requires:
        Ensures:
        '''

        return self._duration
    
    def setDuration_Requests(self,duration):
        '''
        
        Requires:
        Ensures:
        '''

        self._duration=duration

    def _str_(self):
        '''
        
        Requires:
        Ensures:
        '''
        return f"Request's name: {self._name}, languages: {self._languages}, category: {self._category}, specialization: {self._specialization}, duration: {self._duration}"


    def removeHeader_Request(self, fileName):
        """
        Remove the header of a file
        Requires:
        Ensures: 
        """

        without_header = []
        with open(fileName) as f:
            for i, line in enumerate(f):
                if i>=7:
                    without_header.append([elem.strip(')').strip('(') for elem in line.strip().split(',')])
        return without_header


