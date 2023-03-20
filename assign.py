#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 77
# 60276 Beatriz Santos
# 60243 Beatriz Deus

from Skippers import Skippers
from Requests import Requests

class Assign:

    def __innit__(self, fileName):
        """
        
        """
        SkWithoutHeader = Skippers.removeHeader_Skipper(fileName, fileName)
        RqWithoutHeader = Requests.removeHeader_Request(fileName, fileName)
        return SkWithoutHeader and RqWithoutHeader

    def match(SkWithoutHeader, RqWithoutHeader):
        """
        
        """
        
