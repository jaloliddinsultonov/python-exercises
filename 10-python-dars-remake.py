# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 21:13:10 2022

@author: Jaloliddin
"""

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())  

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

admin = 'Jaloliddin'
name = input("Iltimos loginingizni kiriting\n>>>")
if name.lower() == 'jaloliddin':
    print(f"Xush kelibsiz, {name.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {name.title()}")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
x = input("Birinchi sonni kiriting: ")
y = input("Ikkinchi sonnin kiriting: ")
if x == y: 
    print("Sonlar teng")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.

x = int(input("Istalgan son kiriting: "))
if x >= 0:
    print("Musbat son")
else:
    print("Manfiy son")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.

x = int(input("Son kiritin: "))
if x >= 0:
  y = x**(1/2)
  print(f"{x} ning ildizi {y} ga teng")
else:
    print("Musbat son kiriting")
     
    












