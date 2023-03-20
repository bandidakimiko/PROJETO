#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 77
# 60276 Beatriz Santos
# 60243 Beatriz Deus

from Skippers import Skippers



class ReadingFromFiles:

    def __init__(self, filename):
        """
        """
        self._fileName = filename


    def getFileName(self):
        """
        
        """
        return self._fileName
    
    def setFileName(self, fileName):
        """
        
        """
        self._fileName = fileName


    def read_header(self, fileName):
        """
        
        Requires:
        Ensures: 
        """

        without_header = []
        with open(self._fileName) as f:
            for i, line in enumerate(f):
                if i>=7:
                    without_header.append([elem.strip(')').strip('(') for elem in line.strip().split(',')])
        return without_header
