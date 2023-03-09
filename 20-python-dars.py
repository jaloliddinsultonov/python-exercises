# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:13:27 2022

@author: Jaloliddin
"""

# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

def info(ismi, familiyasi, t_yili, t_joyi, emaili = '', teli = ''):
    malumot = {
        'ism':ismi,
        'familiya': familiyasi,
        't_yil': t_yili,
        't_joy': t_joyi,
        'email': emaili,
        'tel': teli
        }
    return malumot

#odam1 = info('Jaloliddin', 'Sultonov', 2002, 'Xatirchi tumani', 'sj@gmail.com', '+48 777 777 777')
#print(odam1)

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

print("Foydalanuvchi haqida ma'lumot kiriting: ")
foydalanuvchilar = []
while True:
    ismi = input("Ismi: ")
    familiyasi = input("Familiyasi: ")
    t_yili = int(input("Tug'ildan yili: "))
    t_joyi = input("Tug'ilgan joyi: ")
    emaili = input("email: ")
    teli = input("Tel raqami: ")
    foydalanuvchilar.append(info(ismi, familiyasi, t_yili, t_joyi))
    javob = input("Davom etasizmi? (yes/no): ")
    if javob == 'no':
        break
print("Foydalanuvchilar ro'yxati")
for foydalanuvchi in foydalanuvchilar:
    print(foydalanuvchi)

# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

def comparer():
    son1 = float(input("Birinchi son kiriting: "))
    son2 = float(input("Ikkinchi son kiriting: "))
    son3 = float(input("Uchinchi son kiriting: "))
    son = max(son1, son2, son3)
    print(f"Uchta son orasida eng kattasi {son}")
    return son
s = comparer()
print(s)

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

def computer(radiusi, diametri, perimetri, yuzini):
    yechim = {
        'radius': radiusi,
        'diametr': diametri,
        'perimetr': perimetri,
        'yuzi' : yuzini
        }
    return yechim
malumot = []
PI = 3.14
radiusi = float(input("Aylana radiusini kiriting: "))
diametri = 2 * radiusi
perimetri = 2 * PI * radiusi
yuzini = PI * radiusi * radiusi
malumot.append(computer(radiusi, diametri, perimetri, yuzini))
print(malumot)

# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def tub_sonlar(min, max):
    tub_son = []
    for n in range(min, max+1):
        tub = True
        if (n==1):
            tub = False
        elif (n==2):
            tub = True
        else:
            for x in range(2, n):
                if(n%x == 0):
                    tub = False
        if tub:
            tub_son.append(n)
    return tub_son
print(tub_sonlar(1, 78))

# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

def fibonachchi(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
print(fibonachchi(100))
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

