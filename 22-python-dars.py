# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 09:46:20 2022

@author: Jaloliddin
"""

# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def kopaytma(*sonlar):
    a = 1
    for son in sonlar:
        a *= son
    return a
print(kopaytma(2,3,4,45,5))        

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_malumot(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar

talaba1 = talaba_malumot("Jaloliddin", "Sultonov", yosh = 20, mutaxasisligi = 'computer engineering', imtiyozlar = "yo'q")
print(talaba1)    
        