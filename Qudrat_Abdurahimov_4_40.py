# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:13:00 2022

@author: Jaloliddin
"""

# Har besh misolda """ qilingan


#1
print("P = 4 * a")
a = int(input("a = "))
P = 4 * a
print(f"P={P}")

#2
print("S=a^2")
a = int (input("a = "))
S = a**2
print(f"S={S}")

#3
print("S=a*b  P=2*(a+b)")
a = int(input("a="))
b = int(input("b="))
P = 2 * (a + b)
S = a * b
print(f"P={P}, S={S}")

#4
print("L=pi*d, pi = 3.14")
d = int(input("d="))
PI = 3.14
print(f"L={PI*d}")

#5
print("V = a^3, S = 6 * a^2")
a = int(input("a="))
V = a**3
S = 6 * (a**2)
print("V=", V, "    S=", S)

#6
print("V=a*b*c    S=2*(a*b+b*c+a*c)")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
V = a * b * c
S = 2*(a * b + b * c + a * c)
print(f"V={V},  S={S}")

#7
print("L=2*pi*R,   S = pi*R^2")
R = int(input("R="))
PI = 3.14
L = 2 * PI * R
S = PI * (R**2)
print(f"L={L},   S={S}")

#8
print("(a+b)/2")
a = int(input("a="))
b = int(input("b="))
arif = (a+b) / 2
print(f"arif={arif}")

#9
print("√ a * b")
a = int(input("a="))
b = int(input("b="))
geo = ((a**(1/2))*(b**(1/2)))
print("geo=", geo)

#10
print("a≠0  b≠0   a+b, a*b, a^2, b^2")
a = int(input("a="))
b = int(input("b="))
summa = a + b
mult = a * b
a_kv = a**2
b_kv = b**2
print(f"a+b={summa}\na*b={mult}\na^2={a_kv}\nb^2={b_kv}")

#11
print("a≠0, b≠0, a+b,  a*b, |a|, |b|")
a = int(input("a= "))
b = int(input("b= "))
summa = a+b
mult = a*b
mod_a = abs(a)
mod_b = abs(b)

#12
print("c = sqrt(a^2 + b^2), P=a+b+c")
a = float(input("a="))
b = float(input("b="))
c = ((a**2) + (b**2))**(1/2)
P = a + b + c
print(f"c={c}, P={P}")

#13
print("R1, R2, (R1>R2), S1=pi*R1, S2=pi*R2, S3=pi(R1-R2")
PI = 3.14
r1 = float(input("R1="))
r2 = float(input("R2="))
s1 = PI * r1
s2 = PI * r2
s3 = PI * (r1 - r2)
print(f"S1={s1}, S2={s2}, S3={s3}")

#14
print("L=2*pi*R, S=pi*R^2")
PI = 3.14
l = int(input("L="))
r = l / (2 * PI)
s = PI * (r**2)
print(f"R={r}, S={s}")


















