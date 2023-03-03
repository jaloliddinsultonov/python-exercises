# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 17:17:48 2022

@author: Jaloliddin
"""

# Foydalanuvchidan buyurtma qabul qiluvchi dastru yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

royxat = []
n = 1
print("Mahsulotlar nomini kiriting.")
while True:
    savol = input(f"{n}-mahsulotni kiriting: ") 
    nom = savol
    royxat.append(nom)
    takrorlash = input("Yana mahsulot kiritishni xohlaysizmi? (ha/yo'q)")
    n+=1
    if takrorlash != 'ha':
        break
print("Kiritilgan mahsulotlar:")
for q in royxat:
    print(q)

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

print("Mahsulotlar va ularning narxlarini saqlaymiz")
mahsulotlar = {}
ishora = True
while ishora:
    nom = input("Mahsulot nomini kiriting: ")
    narx = input("Mahsulot narxini kiriting: ")
    mahsulotlar[nom] = float(narx)
    takrorlash = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
    if takrorlash != 'ha':
        ishora = False

for nom, narx in mahsulotlar.items():
    print(f"{nom} {narx} so'm")

# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
