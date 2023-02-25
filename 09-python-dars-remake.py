# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:01:32 2022

@author: Jaloliddin
"""

# Kamida 5 ta elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

ismlar = ["Jaloliddin", "Humoyunmirzo","Nodirbek", "Doniyor", "Shoxrux"]
for ism in ismlar:
    print(f"{ism} iltimos kvartira to'lovini o'z vaqtida to'lab qo'ying")
    
# Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

ismlar = ["Jaloliddin", "Humoyunmirzo","Nodirbek", "Doniyor", "Shoxrux"]
for ism in ismlar:
    print(f"{ism} iltimos kvartira to'lovini o'z vaqtida to'lab qo'ying")
print("Kod", len(ismlar), "marta bajarildi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

toq_sonlar = list(range(11,100,2))
sonlar_kubi = []
for son in toq_sonlar:
    sonlar_kubi.append(son**3)
print(toq_sonlar)
print(sonlar_kubi)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.

kinolar = []
print("5 ta eng sevimli kinolaringizni kiriting")
for kino in range(5):
    kinolar.append(input(f"{kino+1}-kinoni kiriting:"))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

insonlar = []
n = input("Necha kishi bilan bugun uchrashdingiz?")
n = int(n)
print(f"Siz {n} ta kishi bilan uchrashibsiz, ularni ismini birma-bir yozib chiqing")
for ism in range(n):
    insonlar.append(input(f"{ism+1}-chi inson ismini kiriting:"))
print(insonlar)
