# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 19:12:25 2022

@author: Jaloliddin
"""

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["Uzbekistan", "Australia", "Poland", "USA", "Germany", "Saudi Arabia", "Canada"]
print(davlatlar)

print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
print(davlatlar.sort())

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120, 1200, 2))
print(sonlar)
print(sum(sonlar))
print(max(sonlar) - min(sonlar))
print(len(sonlar))
print(sonlar[0:21], sonlar[260:281], sonlar[520:541])

#Taomlar degan ro'yxat yarating va ichiga istalgan 5 ta taomni kiriting

taomlar = ['osh', 'norin', 'somsa', 'shashlik', 'sho\'rva']
print(taomlar)
nonushta = taomlar[:]
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.append('kolbasa')
nonushta.append('choy')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)