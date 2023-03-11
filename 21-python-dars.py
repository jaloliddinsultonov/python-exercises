# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 09:23:46 2022

@author: Jaloliddin
"""

# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 

def katta_harf(nomlar):
    katta = []
    while nomlar:
        nom = nomlar.pop()
        katta.append(nom.title())
    return katta

nomlar = ['jalol', 'gulnoza', 'humoyun', 'arthur']
a = katta_harf(nomlar)
print(a)

# Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring
       
def katta_harf(nomlar):
    katta = []
    while nomlar:
        nom = nomlar.pop()
        katta.append(nom.title())
    return katta

nomlar = ['jalol', 'gulnoza', 'humoyun', 'arthur']
a = katta_harf(nomlar[:])
print(a)  
print(nomlar) 

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def bahola(ismlar):
    baholar = {}
    for n in ismlar:
        baho = input(f"Talaba {n.title()} ning bahosini kiriting: ")
        baholar[n] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
b = bahola(talabalar)
print(b)
            