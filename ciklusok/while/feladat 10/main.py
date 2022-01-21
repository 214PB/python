#Kérjünk be egy max 2 jegyű, pozitív n számot:
#	Írjuk ki 0 és n közt a páros számokat#
#	Adjuk össze 0 és n közt az 5-el osztható számokat
#	Számoljuk meg, hány szám osztható 0 és n közt 11-el
#	Írjuk ki azon számokat 0 és n közt amelyek 7-el osztva 3-at adnak maradékul

n: int=None
temp: str=""
ottelOszthato: int=0
tizenegyelOszthato: int=0

while(n==None or n>99):
    temp=input("Kérem adjon meg egy pozitív kétjegyű számot!")
    if(temp.isnumeric()):
        n=int(temp)

#paros számok kiírása
print("Páros számok:")
for i in range(0, n + 1, 2):
    print(i, end=" ")

for i in range(0, n + 1, 1):
#0 és n közt az 5-el osztható számok összege
    if(i%5==0):
        ottelOszthato+=i
#11-el osztható számok száma
    if(i%11==0 and i!=0):
        tizenegyelOszthato+=1
    
print(f"5-el osztható számok összege: {ottelOszthato}")

print(f"Tizenegyel osztható számok száma: {tizenegyelOszthato}")

#7-el osztva 3 a maradéka
print("7-el osztva 3-at adnak maradékul:")
for i in range(0, n + 1, 1):
    if(i%7==3 and i>7):
        print(i)
