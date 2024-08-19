# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 23:18:45 2024

@author: furka
tas_kagit_makas_FURKAN_YERGÖK
Bu kod Furkan Yergök tarafından Bootcamp için yazıldı.
Lütfen terminale tas_kagit_makas_FURKAN_YERGOK() yazarak oyunu çağırınız.
"""
import random
print("Lutfen terminale tas_kagit_makas_FURKAN_YERGOK() yazarak oyunu çağırınız.\n")
def tas_kagit_makas_FURKAN_YERGOK():
    print("Taş kağıt makas oyununa hoş geldiniz!")
    print("Bu oyun 3 turdan oluşmaktadır.\nHer oyun sonunda size ve bilgisayara oyunu oynayıp oynamak istemediği sorulacaktır. Eğer iki taraf da oyunu oynamak isterse oyun tekrar başlayacaktır.")
    print("P1: 1. Oyuncu, P2: 2. Oyuncu(bilgisayar)\n")
    ct = 1
    p1_puan=0
    p2_puan=0
    draw=0
    while ct<4:
        choices = ["tas","kagit","makas"]
        while True:
            p1 = str(input("tas, kagit veya makas arasından birini seçiniz:\n"))
            if p1 in choices:
                break
            print("Geçersiz bir seçim yaptınız.")
        p2 = random.choice(choices)
        print(f"\nP1'in seçimi:{p1}!\nP2'nin seçimi:{p2}!")
        if p1 == "tas" and p2=="makas":
            p1_puan+=1
            print(f"P1 {ct}. roundu kazandı!")
        elif p1 == "tas" and p2=="kagit":
            p2_puan+=1
            print(f"P2 {ct}. roundu kazandı!")
        elif p1 == "tas" and p2=="tas":
            draw+=1
            print(f"Round berabere!")
        elif p1 == "makas" and p2=="tas":
            p2_puan+=1
            print(f"P2 {ct}. roundu kazandı!")
        elif p1 == "makas" and p2=="kagit":
            p1_puan+=1
            print(f"P1 {ct}. roundu kazandı!")
        elif p1 == "makas" and p2=="makas":
            draw+=1
            print(f"Round berabere!, P1:{p1}, P2:{p2}")
        elif p1 =="kagit" and p2 =="tas":
            p1_puan+=1
            print(f"P1 {ct}. roundu kazandı!")
        elif p1 =="kagit" and p2 == "makas":
            p2_puan+=1
            print(f"P2 {ct}. roundu kazandı!")
        elif p1 =="kagit" and p2 =="kagit":
            print(f"Round berabere!, P1:{p1}, P2:{p2}")
        ct+=1
    print("Oyun sona erdi!\n")
    if p1_puan>p2_puan:
        print(f"Oyunun kazananı, {p1_puan} puan ile: 1. Oyuncu(P1)!")
    elif p1_puan<p2_puan:
        print(f"Oyunun kazananı: {p2_puan} puan ile 2. Oyuncu(P1)!")
    else:
        print("Oyun berabere!")
    print(f"P1: {p1_puan} round kazandı!\nP2: {p2_puan} round kazandı!\n{draw} oyun berabere bitti!")
    replay = str(input("Tekrar oynamak isterseniz y yazınız."))
    computer = ["y","n"]
    cc = random.choice(computer)
    if cc == replay and cc == "y":
        tas_kagit_makas_FURKAN_YERGOK()
        return
    elif replay == cc and cc!="y":
        print("Oyun tekrar oynanmayacak. İki taraf da oynamayı reddetti.")
    elif replay =="y":
        print("Oyun tekrar oynanmayacak. 1. Oyuncu oynamayı reddetti.")
    elif cc == "n":
        print("Oyun tekrar oynanmayacak. Bilgisayar oynamayı reddetti. :(")

    
    
    