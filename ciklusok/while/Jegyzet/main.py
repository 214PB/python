#pip3 import keyboard

#csomagok importálása
import os
#import keyboard
import time

#változók definiálása
#a szám amit be kell olvasni
    #kezdőértéke None, mivel a while ciklusban ki tudom ezt használni ismétlés vizsgálatára 
    #mindaddig futtatja a ciklust, míg a numbernek nem lesz értéke
number: int=None
    #segéd változó, a beolvasott értéket fogja tárolni
data: str= ""

#while ciklus mindaddig fog futni, amíg a number változó nem kap értéket, nem None lesz
while(number==None):
    #beolvasás, annak eltárolása a data változóban
    data=input("Kérem a számot:")
    #megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható-e
    #mindegy hogy int vagy float
    #isdigit() -> bool típusú változó
    if(data.isdigit()):
        #ha az isdigit() függvény értéke igaz, akkor számot írt be a fölhasználó, amit BIZTOS át tudunk alatítani szám típusúvá
        number=int(data)
    #az isdigit() függvény értéke hamis, a fölhasználó nem számot írt be
    #a number változó None marad
    #ciklus ismétlődik
    else:
        print("/nNem számot adott meg!")
        #a programot futtató szálat (therd) elaltatjuk 3 másodpercre
        time.sleep(3)
        #letöröljük a képernyőt
        os.system("cls")
#        print("/nA folytatáshoz nyomja meg az enter billentyűt!")
        #egy végtelen while ciklust írunk, mivel arra várunk, hogy a fölhasználó lenyomja a kért billentyűt
#        while(True):
            #figyeljük, hogy a fölhasználó lenyomta-e az enter gombot
#            if(keyboard.is_pressed('enter')):
                #letöröljük a képernyőt
#                os.system("cls")
            #kilépünk a belső ciklusból
#            break
#kiírjuk a beolvasott számot
print(f"A beolvasott szám {number}")
