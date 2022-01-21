import random

#változók definiálása
tipp: int = 0
rnd: int = 0
tippekSzama: int = 1
temp: str = ""

rnd=random.randint(0,9)

#eltaláltuk e a számot és elértük e a max tippszámot
while(tipp != rnd and tippekSzama <= 5):
    temp = ""
    #ellenőrizzük hogy számot írt e be
    while(temp == "" or temp.isspace() or not temp.isnumeric()):
        temp=input(f"Kérem a(z) {tippekSzama}. tippet!")
        if(temp.isnumeric()):
            tipp = int(temp)
            tippekSzama += 1
        else:
            print("Nem számot adott meg")

if(tipp == rnd):
    print(f"Gratulálunk, eltalálta a számot: {rnd}")

else:
    print(f"Sajnos nem találta el a számot: {rnd}")