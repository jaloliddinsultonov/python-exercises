# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:47:57 2022

@author: Jaloliddin
"""

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'maryam':'huawei p30',   
    'jaloliddin':'iphone 11',
    'fazliddin':'oppo 2',
    'shoxjahon':'realme g2 neo',
    'abdurahmon':'iphone 13 pro max',
    'gulnoza':'sony'
    }
for n in sorted(telefonlar):
    print(n)

# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

countries = {
    'Poland':'Warsaw',
    'USA':'Washington D.C',
    'Uzbekistan':'Tashkent',
    'Australia':'Canberra',
    'Egypt':'Cairo',
    'Germany':'Berlin',
    'France':'Paris'
    }
for n in sorted(countries):
    print(n)
print("\n")
for m in sorted(countries.values()):
    print(m)

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

user = input("Istalgan davlat nomini kiriting: ").title()
countries = {
    'Poland':'Warsaw',
    'USA':'Washington D.C',
    'Uzbekistan':'Tashkent',
    'Australia':'Canberra',
    'Egypt':'Cairo',
    'Germany':'Berlin',
    'France':'Paris'
    }
n = countries.get(user)
if n !=None:
    print(n)
else:
    print("Bizda bunday ma'lumot yo'q")

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
        'osh':50,
        "sho'rva":15,
        'lavash':20,
        'kabob':30,
        'norin':100,
        'manti':65,
        'chuchvara':50,
        'shashlik':10,
        'somsa':7,
        'non':5       
        }
zakaz = []
for q in range(3):
    zakaz.append(input(f"{q+1}-buyurtmani kiriting\n>>>"))

for n in zakaz:
    if n in menu:
         print(f"{n}ning narxi {menu[n]}")
    else:
         print('Bizda bunday taom yoq')


























    