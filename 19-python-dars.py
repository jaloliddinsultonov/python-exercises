# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:19:24 2022

@author: Jaloliddin
"""

# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

def ism_t_yil(ism):
    """Foydalanuvchi ismi va yoshini so'rab,
      uning tug'ilgan yilini hisoblaydigan funksiya."""
    yosh = int(input("Necha yoshdasiz: ")) 
    print(f"{ism.title()} {2022 - yosh}-yilda tavallud topgan")

ism_t_yil('Jaloliddin')

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kv_kub():
    """Foydalanuvchidan son olib, uning kvadrati
    va kubini konsolga chiqaruvchi funksiya"""
    son = int(input("Son kiriting: "))
    print(f"{son} ning kvadrati {son**2}, kubi esa {son**3} ga teng")
    
kv_kub()

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

def juft_toq():
    """Foydalanuvchidan son olib, son juft 
    yoki toqligini konsolga chiqaruvchi funksiya"""
    son = int(input("Butun son kiriting: "))
    if son%2==0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")
juft_toq()

# 2-usul
def juft_toq(son):
    if son%2!=0:
        print("toq")
    else:
        print("juft")
juft_toq(23)

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def bolshe_menshe():
    """Foydalanuvchidan ikkita son olib,
    ulardan kattasini konsolga chiqaruvchi funksiya.
    Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqariladi"""
    son1 = float(input("Birinchi sonni kiriting:"))
    son2 = float(input("Ikkinchi sonni kiriting:"))
    if son1 > son2:
        print(f"{son1}>{son2}")
    elif son1 < son2:
        print(f"{son1}<{son2}")
    else:
        print(f"{son1}={son2}")
bolshe_menshe()

# Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
def qiymat_oshirgich():
    """Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya"""
    x = float(input("x ni kiriting:"))
    y = float(input("y ni kiriting:"))
    print(f"x^y = {x**(y)}")
qiymat_oshirgich()

# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
def qiymat_oshirgich(x, y = 2):
    print(f"x^y={x**(y)}")
qiymat_oshirgich(3)

# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def ability():
    son = float(input("Son kiriting:"))
    for n in range(2, 11):
        if son%n==0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
ability()












