# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:23:38 2022

@author: Jaloliddin
"""

# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

class User:
    def __init__(self, ism, familiya, tyil, email, tel):
        self.name = ism
        self.surname = familiya
        self.date_of_birth = tyil
        self.email = email
        self.tel = tel
        
    def tanishtiruv(self):
        print(f"{self.name} {self.surname}. Date of birth: {self.date_of_birth}.\nemail:{self.email} \ntel:{self.tel}")
            
user1 = User("Jaloliddin", "Sultonov", 2002, "sultonovjaloliddin07@gmail.com", 733677206)   
print(user1.tanishtiruv())
    
# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).

class User:
    def __init__(self, ism, familiya, tyil, email, tel):
        self.name = ism
        self.surname = familiya
        self.date_of_birth = tyil
        self.email = email
        self.tel = tel
     
    def get_info(self):
        return f"{self.name} {self.surname}. Date of birth: {self.date_of_birth}.\nemail:{self.email} \ntel:{self.tel}"
    
    # def tanishtiruv(self):
    #     print(f"{self.name} {self.surname}. Date of birth: {self.date_of_birth}.\nemail:{self.email} \ntel:{self.tel}")
user2 = User("Jake", 'Barboza', 1989, "jakebarboza@gmail.com", 7383829293)
print(user2.get_info())

# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.

class User:
    def __init__(self, ism, familiya, tyil, email, tel):
        self.name = ism
        self.surname = familiya
        self.date_of_birth = tyil
        self.email = email
        self.tel = tel
     
    def get_info(self):
        return f"{self.name} {self.surname}. Date of birth: {self.date_of_birth}.\nemail:{self.email} \ntel:{self.tel}"
    
    # def tanishtiruv(self):
    #     print(f"{self.name} {self.surname}. Date of birth: {self.date_of_birth}.\nemail:{self.email} \ntel:{self.tel}")
user2 = User("Jake", 'Barboza', 1989, "jakebarboza@gmail.com", 7383829293)
print(user2.get_info())
user3 = User("Mashal", "Latifi", 2000, "sjael@yahoo.com", 188929999)
print(user3.name)
print(user3.get_info())
print(user3.tel)