isim=input("Kullanici adini gir:").lower()
yasakli_isimler=["admin","root","administrator"]

if isim in yasakli_isimler:
        print("Supheli kullanici tespit edildi.")
        with open("supheli_log.txt","a") as dosya:
            dosya.write(f"\n{isim} supheli giris yapti.\n")
            
else:
     print(f"{isim} giris yapti")