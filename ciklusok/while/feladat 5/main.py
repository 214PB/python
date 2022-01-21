probalkozasokSzama: int=0
osszeg: int=0
szam: int=0
temp: str=""
hatarErtek: int=0

while(hatarErtek < 100):
    temp=input("Írjon be egy határértéket:")
    if(temp.replace("-", "").isnumeric()):
        hatarErtek = int(temp)

temp=""

while(osszeg < hatarErtek):
    temp=input("Adjon meg egy számot:")
    
    if(temp.replace("-", "").isnumeric()):
        szam=int(temp)
        osszeg += szam
        probalkozasokSzama += 1
        print(f"Összeg: {osszeg}")

print(f"{probalkozasokSzama} próbálkozással elérte a(z) {hatarErtek} értéket.")