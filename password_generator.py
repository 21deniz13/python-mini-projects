import random
import string
karakterler=string.ascii_letters+string.digits+string.punctuation
uzunluk=int(input("Sifre uzunlugu giriniz:"))
sifre=[]
for i in range(0,uzunluk):
    sifre.append(random.choice(karakterler))
print(f"Olusturulan sifre:{sifre}")
print("".join(sifre))

