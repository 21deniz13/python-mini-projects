from datetime import datetime


kullanici=input("Kullanici adinizi giriniz:\n")
if kullanici=="exit":
    print("Program kapatildi.")
else:
 with open("mesaj.txt","a") as dosya:
    simdi=datetime.now()
    dosya.write(f"{simdi} oldugu anda {kullanici} merhaba dedi .")
 print("Mesaj kaydedildi.")


