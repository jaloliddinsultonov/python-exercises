# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:00:28 2021

@author: Jaloliddin
"""

# Copying
mevalar = ["olma", "anjir", "shaftoli", "o'rik"]
narhlar = [1000, 1222, -32232.32, 32331]
sonlar = ["bir", "ikki", 3, 4, 5]
ismlar = []
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])
print("Birinchi meva: ", mevalar[0].upper())
print("Uchinchi meva: ", mevalar[2].title())
print(narhlar[2] + narhlar[1])
cars = ["Toyota", "Mersedes", "Skoda", "Hyundai", "GM", "Volvo"]
print(cars[-1])  #eng ohirgi elementni ko'rsatadi. shows the last element
mevalar.append("tarvuz")
print(mevalar)
usa = []
usa.append("Ielts")
usa.append("SAT")
usa.append("Luck")
print(usa)
usa.insert(0, "strong desire")
print(usa)
del usa[-1]
print(usa)
usa.remove('Ielts')
bozorlik = mevalar.pop(3)
print(bozorlik)

# Exercises

# Ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizni ismini kiriting

ismlar = ["Asadbek", "Yahyobek", "Muhammadqodir", "Allayar"]
print("Salom ", ismlar[0], "aka, bugun Shohruza osh qilib beradimi?")
print(ismlar[1] + ", choyxonaga boramizmi?")
print(ismlar[2], " a bu ashna ashnagarchilik qayerda qoldi?")
print("Qpraqalpoq tinchmi, ", ismlar[-1])

# Sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang(musbat, manfiy, butun, o'nlik)

sonlar = [1000, 3223, -2313, 133.13]
print(sonlar)
sonlar[0] = sonlar[0] + 2000
print(sonlar) 
print(sonlar[2] + sonlar[1])
print(sonlar[0] * sonlar[3])

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingizga eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizning tirik bo'lgan shaxslarning ismini kiriting.

t_shaxslar = ["Amir Temur", "Abu Rayhon Beruniy"]
t_shaxslar.append("Abu Ali Ibn Sino")
t_shaxslar.append("Alisher Navoiy")
z_shaxslar = ["Mark Zuckerberg", "Bill Gates", "Elon Mask", "Hans Zimmer", "Jackie Chan"]
print("Men tarixiy shaxslardan ", t_shaxslar.pop(2), " bilan, zamonaviy shaxslardan esa", z_shaxslar.pop(1), " bilan suhbat qilishni istar edim")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
friends.append("Po")
friends.append("Ugvey")
friends.append("Taylung")
friends.append("Shi'fu")
friends.append("Kay")
print(friends)
friends.remove("Po")
friends.remove('Shi\'fu')
friends.insert(0, "Kong")
friends.insert(-1, "Tiger")
friends.insert(2, "Vachchach")
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))



















