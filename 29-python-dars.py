# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 16:26:13 2022

@author: Jaloliddin
"""

class Avto():
    def __init__(self, model, rang, korobka, narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometer = 0
    
    def get_info(self, kilometer):
        self.kilometer = kilometer
        return f"Model:{self.model} \nRang:{self.rang} \nKorobka:{self.korobka} \nNarh:{self.narh} \nKilometri:{self.kilometer}"
    
    def update_km(self):
        self.kilometer += 10
          
avto1 = Avto("Toyota", "Oq", "Avtomat", 15000)
print(avto1.get_info("12"))

class Avtosalon():
    def __init__(self, salon_nomi, manzil, sotuvdagi_avtomobillar):
        self.salon_nomi = salon_nomi
        self.manzil = manzil
        self.sotuvdagi_avtomobillar = sotuvdagi_avtomobillar
        self.avtos = []
        self.avto_num = 0
        
    def add_avto(self, avto):
        self.avtos.append(avto)
        self.avto_num += 1
        
    def get_avtos(self):
        return [x.get_info() for x in self.avtos]
        
        
        