# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 20:20:56 2021

@author: Jaloliddin
"""

#Foydalanuvchi kiritgan sonning kvadrati va kubini  konsolga chiqaruvchi dastur

son = float(input("Istalgan son kiriting:\n>>>"))
print(son, " ning kvadrati ", son**2, " ga teng")
print(son, " ning kubi ", son**3, " ga teng")

# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur

yosh = int(input("Yoshingiz nechchida?\n>>>"))
print("Siz ", 2021 - yosh, " da tug'ilgansiz")
#alternative way
print("Siz " + str(2021-yosh) + " da tug'ilgansiz")

# Foydalanuvchidan ikki son kiritishni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

birinchi_son = float(input("Birinchi sonni kiriting:"))
ikkinchi_son = float(input("Ikkinchi sonni kiriting:"))
print(birinchi_son, "+", ikkinchi_son, "=", birinchi_son + ikkinchi_son)
print(birinchi_son, "-", ikkinchi_son, "=", birinchi_son - ikkinchi_son)
print(birinchi_son, "*", ikkinchi_son, "=", birinchi_son * ikkinchi_son)
print(birinchi_son, "/", ikkinchi_son, "=", birinchi_son / ikkinchi_son)

