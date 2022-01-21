#Írjunk programot, amely bekéri a nevünket, és ha azt megadtuk, akkor üdvözlő szöveggel üdvözli a felhasználót.

#név nem lehet üres string
#szóközöket aad meg (1 vagy több)
#név hossza

import os
import time

nev: str=""

while(nev=="" or nev.isspace() or len(nev) <3):
    nev= input("Kérem a nevét!")
    if(nev==""):
        print("Nem adott meg nevet!")
        time.sleep(3)
        os.system("cls")
    elif(nev.isspace()):
        print("Nem nevet adott meg!")
        time.sleep(3)
        os.system("cls")
    elif(len(nev)<3 ):
        print("Nem megfelelő nevet adott meg!")
        time.sleep(3)
        os.system("cls")

print(f"Üdvözlöm kedves {nev}")