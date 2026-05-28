#isdigit string içinde rakam olup olmadıgını kontrol eder metin.isdigit()
sifre=input("Sifre giriniz:")
sayi_var_mi=False
if len(sifre)<8:
    print("Sifre kisa!")
    
else:
    for char in sifre:
       if char.isdigit():
         sayi_var_mi=True
    if sayi_var_mi==False:
      print("Sayi icermeli.")
    else:
      print(f"Sifre basarili.Sifreniz: {sifre}")

