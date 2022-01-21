#7 – Kérjünk be egy számot és egy másikat úgy, hogy nagyobb legyen az elsőnél. 
# Számoljunk visszafelé a nagyobbik számtól a kisebbik felé. 
# (A feladat kiegészíthető azzal, hogy bekérjük a lépésközt is, ami kisebb kell legyen a két szám különbségénél.)

kezdoertek: int=None
vegertek: int=None
temp: str=""

while(kezdoertek==None):
    temp=input("Kérem adja meg a kezdőértéket!")
    if(temp.replace("-", "").isnumeric()):
        kezdoertek=int(temp)

while(vegertek==None or kezdoertek<=vegertek):
    temp=input("Kérem adja meg a végértéket!")
    if(temp.replace("-", "").isnumeric()):
        vegertek=int(temp)

for i in range(kezdoertek, vegertek, -1):
    print(i)