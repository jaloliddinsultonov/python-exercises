# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:00:19 2022

@author: Jaloliddin
"""

odam0 = {
    'ism':'Cristiano Ronaldo',
    'tyil': 1885,
    'kasb':"futbolist",
    'daromadi':30_000_000
    }
odam1 = {
    'ism':'Farrux Mannopov',
    'tyil':1997,
    'kasb':'viner, bloger',
    'daromadi':3000
    }
odam2 = {
    'ism':'Anvar Narzullayev',
    'tyil':1978,
    'kasb':"o'qituvchi",
    'daromadi':10000
    }
odam3 = {
    'ism':'Jaloliddin Sultonov',
    'tyil':2002,
    'kasb':'student',
    'daromadi':500
    }
odamlar = [odam0, odam1, odam2, odam3]
for odam in odamlar:
    print(f"{odam['ism']}, {odam['tyil']}-yilda tug'ilgan, "
          f"kasbi {odam['kasb']}. Oylik daromadi {odam['daromadi']}$")
    
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

odam0['asar'] = "Kambag'allikdan boylikkacha"
odam1['asar'] = "Жизнь простых ребят(Секреты успешных вайнеров)"
odam2['asar'] = "Python asoslari"
odam3['asar'] = "Yalqovlik san'ati"

for odam in odamlar:
    print(f"{odam['ism']}, {odam['asar']}")
 
# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.

odam0 = {
    'nodirbek':['The Big Bang Theory', 'Matrix', 'Friends'],
    'humoyun':['Spider-Man', 'Batman', "Superman"],
    'doniyor':['Побег из Шоушенга', 'The Great Getsby', 'Avatar'],
    'shoxrux':['Gotham', 'La casa de papel', 'Peaky Blinders']
    }
for ism, filmlar in odam0.items():
    print(f"\n{ism.title()}ning sevimli filmlari:")
    for film in filmlar:
        print(film.upper())

# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    'Poland':{
        'capital':'Warsaw',
        'population':33_000_000,
        'currency':'zloty',
        'language':'Polish'
        },
    'Uzbekistan':{
        'capital':'Tashkent',
        'population':32_000_000,
        'currency':'sum',
        'language':'Uzbek'
        },
    'USA':{
        'capital':'Washington D.C',
        'population':331_000_000,
        'currency':'dollar',
        'language':'English'
        }
    }
for davlat, info in davlatlar.items():
    print(f"\n{davlat} davlatining poytaxti {info['capital']}. Axolisi {info['population']} kishidan "
          f"iborat bo'lib, valyutasi {info['currency']}. Davlat tili {info['language']}.")

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

user = input("Qaysi davlat haqida ma'lumotga ega bo'lmoqchisiz?\n>>>")
davlatlar = {
    'Poland':{
        'capital':'Warsaw',
        'population':33_000_000,
        'currency':'zloty',
        'language':'Polish'
        },
    'Uzbekistan':{
        'capital':'Tashkent',
        'population':32_000_000,
        'currency':'sum',
        'language':'Uzbek'
        },
    'USA':{
        'capital':'Washington D.C',
        'population':331_000_000,
        'currency':'dollar',
        'language':'English'
        }
    }
if user in davlatlar:
    info = davlatlar[user]
    print(f"\n{user.capitalize()}ning poytaxti {info['capital'].title()}"
          f"\nAholisi: {info['population']}"
          f"\nDavlat tili: {info['language']}"
          f"\nPul birligi: {info['currency']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")







'''
for davlat, info in davlatlar.items():
    print("\n")
for q in user:
   if q in davlat:
        print(print(f"\n{davlat} davlatining poytaxti {info['capital']}. Axolisi {info['population']} kishidan "
          f"iborat bo'lib, valyutasi {info['currency']}. Davlat tili {info['language']}."))
   else:
        print("Bizda bu davlat haqida ma'lumot yo'q")
'''




















