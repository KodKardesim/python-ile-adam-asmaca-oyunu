import random
import os

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
--------"""]

kelimeler = ["kiraz", "zencefil", "zerdeçal", "mango", "şans", "narkoz", "timur", "güneysudan", "şampuan", "moderasyon",
             "cebelitarık", "liberya", "palau", "argüman", "operatör"]
flag = True
while flag:
    os.system("cls")
    kelime = random.choice(kelimeler)  # Rastgele bir kelime seçtik.
    tahminSayisi = 6
    bulunanharfler = []  # Bulunan harflerin tutulacağı yer.
    yanlisharfler = []  # Yanlış bulunan harflerin tutulacağı yer.
    harfsayisi = len(kelime)
    z = list('_' * harfsayisi)
    print(resim[0])
    print(' '.join(z), end='\n')
    while tahminSayisi > 0:
        if z == list(kelime):
            print("OYUNU KAZANDIN!!!")
            break
        char = input("Bir harfi veya kelimeyi tahmin edin : ").replace("İ", "i").replace("I", "ı").lower()
        # lower() ile gelen harfleri küçük harfe çevirdik. ancak İ ve I küçültülürken bazı hatalar çıkabiliyor.
        # Bunun için replace ile kendimiz küçülttük.

        if len(char) == 1:
            if char in bulunanharfler:
                os.system("cls")
                print(resim[6 - tahminSayisi])
                print(' '.join(z), end='\n')
                print("Yanlış bulunan harfler : {}".format(yanlisharfler))
                print("Bu harfi zaten buldun!")

            elif char not in kelime:  # girilen harf kelime icinde yoksa eger
                tahminSayisi -= 1
                os.system("cls")
                print(resim[6 - tahminSayisi])
                print(' '.join(z), end='\n')
                yanlisharfler.append(char)
                print("Yanlış bulunan harfler : {}".format(yanlisharfler))
                print("\nYANLIŞ TAHMİN!!! Kalan hakkın : {}".format(tahminSayisi))
            else:
                for i in range(len(kelime)):
                    if char == kelime[i]:
                        os.system("cls")
                        print(resim[6 - tahminSayisi])

                        z[i] = char
                        bulunanharfler.append(char)
                print(' '.join(z), end='\n')
                print("Yanlış bulunan harfler : {}".format(yanlisharfler))
                print("\nDOĞRU TAHMİN!!! Kalan hakkın : {}".format(tahminSayisi))

        elif len(char) > 0:
            if char == kelime:
                print("\nTEBRİKLER!!! Kelimeyi buldunuz.")
                devam = input("Tekrar oynamak ister misiniz? [e/h]")
                if devam == "e" or devam == "E":
                    flag = True
                    break
                else:
                    flag = False
                    break
            else:
                tahminSayisi -= 1
                os.system("cls")
                print(resim[6 - tahminSayisi])
                print(' '.join(z), end='\n')
                print("Yanlış bulunan harfler : {}".format(yanlisharfler))
                print("\nYANLIŞ TAHMİN!!! Kalan hakkın : {}".format(tahminSayisi))

        if tahminSayisi == 0:
            print("\nTahmin hakkiniz kalmadi. Kaybettiniz! Adam Asildi.")
            print(f"Doğru kelime : {kelime}")
            devam = input("Tekrar oynamak ister misiniz? [e/h]")
            if devam == "e" or devam == "E":
                flag = True
            else:
                flag = False
