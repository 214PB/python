probalkozasokSzama: int=0
osszeg: int=0
szam: int=0
temp: str=""

while(osszeg<100):
    temp=input("Adjon meg egy számot:")
    if(temp.replace("-", "").isnumeric()):
        szam=int(temp)
        osszeg+=szam
        probalkozasokSzama +=1
        print(f"{probalkozasokSzama}. probálkozás, összeg: {osszeg}")
