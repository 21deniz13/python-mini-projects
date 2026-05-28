kullanici=input("Kullanici adinizi giriniz:")
dosya=open("log.txt","a")
dosya.write(f"{kullanici} sisteme giris yapti")
dosya.close
dosya=open( "log.txt","r")
icerik=dosya.read()
print(icerik)
dosya.close()
print("Log kaydi olusturuldu.")
#import os 
#os.remove("log.txt")  text dosyasını siler 
#if os.path.exists("log.txt") bu da böyle bir dosya var mı diye kontrol eder
dosya=open("log.txt","w")
dosya.write("Yeni veri")
dosya.close()