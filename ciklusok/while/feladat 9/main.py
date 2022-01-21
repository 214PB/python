#Kérjünk be egy 3 jegyű  számot és állapítsuk meg, hogy osztható e 7-el. Addig ismételjük a bekérést, amíg nem 3 jegyű a megadott szám.

haromjegyuSzam: int=None
temp: str=""

while(haromjegyuSzam==None or haromjegyuSzam<100 or haromjegyuSzam>999):
    temp=input("Kérem adjon meg egy háromjegyű számot!")
    if(temp.replace("-", "").isnumeric()):
        haromjegyuSzam=int(temp)
        
        if(haromjegyuSzam<100 or haromjegyuSzam>999):
            print("Nem háromjegyű számot adott meg!")


if(haromjegyuSzam%7==0):
    print(f"{haromjegyuSzam} osztható 7-el.")
else:
    print(f"{haromjegyuSzam} nem osztható 7-el.")