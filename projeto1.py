#-*- coding: utf-8 -*-

# 2022-2023 Programação 2 (LTI)
# Grupo 77
# 60276 Beatriz Santos
# 60243 Beatriz Deus


from Skippers import Skippers



file = 'skippers17h00.txt'

SkWithoutHeader = Skippers.removeHeader_Skipper(file, file)

print(SkWithoutHeader)





###NOTA: podemos manter o modulo do DateTime, fazer um modulo update.py e manter o ficheiro de constantes

