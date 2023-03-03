# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:56:15 2022

@author: Jaloliddin
"""

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.

user = "Yaxshi ko'rgan kitoblaringizni kiriting:"
user += "(agar dasturni to'xtatmoqchi bo'lsangiz, 'stop' so'zini yozing)\n"
qiymat = ''
while qiymat != 'stop':
    qiymat = input(user)
    if qiymat == 'stop':
       break
print("Siz dasturni to'xtatdingiz rahmat")

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

banner = "0-7 yosh - 2000 so'm \n7-18 yosh - 3000 so'm\n18-65 yosh - 10000 so'm \n65-∞ yosh bepul \nP.S.(Dasturni yopish uchun 'exit' yoki 'quit' deb yozing)"
banner += "\nYoshingiz nechchida:"
ishora = True
while ishora:
  yosh = (input(banner))
  if yosh == 'exit' or yosh == 'quit':
    ishora = False 
  else:          
        raqam = int(yosh)
        if raqam < 7:
            print(f"Siz {yosh} yoshdasiz, chipta 2000 so'm")
        elif 7<=raqam<18:
            print(f"Siz {yosh} yoshdasiz, chipta 3000 so'm")
        elif 18<=raqam<65:
            print(f"Siz {yosh} yoshdasiz, chipta 10000 so'm")
        else:
            print(f"Siz {yosh} yoshdasiz, sizga tekin")          

# Yuqoridagi dastruni turli usullarda youzib ko'ring(break, ishora, yoki shart tekshirish)    
            
banner = "0-7 yosh - 2000 so'm \n7-18 yosh - 3000 so'm\n18-65 yosh - 10000 so'm \n65-∞ yosh bepul \nP.S.(Dasturni yopish uchun 'exit' yoki 'quit' deb yozing)"
banner += "\nYoshingiz nechchida:"
while True:
  yosh = (input(banner))
  if yosh == 'exit' or yosh == 'quit':
    break
  else:          
        raqam = int(yosh)
        if raqam < 7:
            print(f"Siz {yosh} yoshdasiz, chipta 2000 so'm")
        elif 7<=raqam<18:
            print(f"Siz {yosh} yoshdasiz, chipta 3000 so'm")
        elif 18<=raqam<65:
            print(f"Siz {yosh} yoshdasiz, chipta 10000 so'm")
        else:
            print(f"Siz {yosh} yoshdasiz, sizga tekin")

# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
'''
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
'''

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")


























                          