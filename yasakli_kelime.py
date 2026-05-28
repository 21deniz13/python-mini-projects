yasakli_kelimeler=["hack","attack","admin"]
isim=input("İnput giriniz:")
if isim in yasakli_kelimeler:
    print("Tehlikeli icerik tespit edildi.")
else:
    print("Dogru giris.")