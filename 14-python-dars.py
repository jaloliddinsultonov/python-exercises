# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 19:00:55 2022

@author: Jaloliddin
"""

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

otam = {}
otam = {
    'ism': 'sattorov yoqub',
    'yosh': 47,
    't_yil': 1975,
    't_joy': 'xatirchi',
    "kasb": "o'qituvchi"
        }
print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda, {otam['t_joy'].title()} tumanida tug'ilgan. Hozir {otam['yosh']} yoshdalar va {otam['kasb']} lavozimida ishlab kelmoqdalar.")


# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

taom = {'otam': "sho'rva", 'onam': "shashlik", 'dazl': 'tort', 'shox': "go'sht", 'men' : 'osh'} 
print(f"otamning sevimli taomi {taom['otam']}")
print(f"onamning sevimli taomi {taom['onam']}")
print(f"Fazliddinning sevimli taomi {taom['dazl']}")
print(f"Shoxjahonning sevimli taomi {taom['shox']}")


# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

python = {
    'int':'integer numbers: 1,2, 53, -323',
    'float':'float numbers: 1/3, 34.32',
    'string':'words',
    'bool':"true, false",
    'if':"hard to explain:)"
    }
print(python)


# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

uz_en = {
    'non':'bread',
    'olma':'apple',
    'telefon':"phone",
    'daftar':'notebook',
    'noutbuk':'laptop'
    }
translator = uz_en.get('non', 'Bunday so\'z mavjud emas')
print(translator)


# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

kalit = input("Kalit so'z kiriting:")
uz_en = {
    'non':'bread',
    'olma':'apple',
    'telefon':"phone",
    'daftar':'notebook',
    'noutbuk':'laptop'
    }
translator = uz_en.get(kalit)
if translator == None:
    print("bunday so'z mavjud emas") 
else:
    print(f"{kalit} so'zi, {translator} deb tarjima qilinadi")
