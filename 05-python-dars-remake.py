# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:44:10 2021

@author: Jaloliddin
"""

#
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
print(kocha, "ko'chasi,", mahalla, "mahallasi,", tuman, " tumani,", viloyat, "viloyati")
#
kocha = input("Qaysi ko'cha?")
mahalla = input("Qaysi mahalla?")
tuman = input("Qaysi tuman?")
viloyat = input("Qaysi viloyat?")
print(kocha, "ko'chasi,\n", mahalla, "mahallasi,\n", tuman, "tumani,\n", viloyat, "viloyati")
manzil = f" {kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())
print(manzil.title())
