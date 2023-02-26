# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:31:35 2022

@author: Jaloliddin
"""

# Foydalanuvchidan juft son kiritishni so'rang. Agar fordalanuvchi juft son kiritsa "Rahmat", agar toq son kiritsa juft emas" degan xavabarni chiqaring.

son = int(input("Juft son kiriting?\n>>>"))
if son % 2 == 0:
    print("Rahmat")
else:
    print("Bu juft son emas")

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar = ["suv", "non", "tuxum", "go'sht", "yog'", 'shokolad', 'banan', 'olma', 'qovun', 'nok']
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting:"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
       print("Mahsulot do'konimizda bor")
    else:
       print("Mahsulot do'konimizda yo'q") 
 
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:  Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul #Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm #Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

yosh = int(input("Yoshingizni kiriting:\n>>>"))
if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh <= 18:
    narh = 10000
else:
    narh = 20000
print(f"Sizga chipta narxi {narh} so'm")

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

son = int(input("Birinchi son kiriting: "))
son1 = int(input("Ikkinchi son kiriting: "))
if son > son1:
    print(f"{son} soni, {son1} dan  katta ekan")
elif son < son1:
    print(f"{son1} soni, {son} dan  katta ekan")
else:
   print("sonlar teng")

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.


mahsulotlar = ["suv", "non", "tuxum", "go'sht", "yog'", 'shokolad', 'banan', 'olma', 'qovun', 'nok']
savat = []
bor_mahsulotlar = []
mavjud_emas = []
print("Beshta mahsulot kiriting")
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting:"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
       bor_mahsulotlar.append(mahsulot)
    else:
       mavjud_emas.append(mahsulot)
for n in mavjud_emas:
 if len(mavjud_emas) == 0:
    print("Siz so'ragan barcha mahsulotlar do'kinimizda bor")
 else:
     print(f"Quyidagi mahsulotlar do'konimizda yo'q: {n}")

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar = ["Jaloliddin", "Humoyun", "Doniyor", "Nodirbek", "Shoxrux"]
login = input("Yangi login kiriting: ")
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibisiz", login)

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

son = int(input("Butun son kiriting: "))
for n in range(2,11):
    if son%n == 0:
        print(f"{son} {n} ga qoldiqsiz bo'linadi")































    