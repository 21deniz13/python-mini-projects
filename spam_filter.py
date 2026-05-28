mesaj=input("Mesajinizi giriniz:")
yasakli_kelimeler=["free","win","money"]
for kelimeler in yasakli_kelimeler:
    if kelimeler in mesaj:
        print("Spam mesaji tespit edildi!")
        break
else:
        print("Dogru giris!")
        



#lower ve upper mantığı
kelime1="DenIz"
kelime2="tonus"
print(kelime1.lower())
print(kelime2.upper())