#11 – Írjunk programot amely a felhasználótól bekér egy páros majd egy tőlle nagyobb páratlan számot. 
# A következő lépésben generáljunk egy véletlen számot e két érték közt és határozzuk meg mely szám 
# (páros vagy páratlan) van messzebb a véletlen számunktól.
#	 Számítsuk ki a két bekért érték közti átlagot is.
#	 Számoljuk meg a 4-el osztható számok számát is.

import random 

paros: int=None
paratlan: int=None
temp: str=""

while(paros==None or paros%2 != 0):
    temp=input("Kérem adjon meg egy számot, amely páros!")
    if(temp.replace("-", "").isnumeric()):
        paros=int(temp)

while(paratlan==None or paros>=paratlan or paratlan%2==0):
    temp=input(f"Kérem adjon meg egy számot, amely páratlan és nagyobb mint {paros}!")
    if(temp.replace("-", "").isnumeric()):
        paratlan=int(temp)

rnd=random.randint(paros, paratlan)

if(abs(rnd-paros) > abs(paratlan-rnd)):
    print(f"A(z) {paros} van messzebb a véletlen számtól.")
elif(rnd-paros < paratlan-rnd):
    print(f"A(z) {paratlan} van messzebb a véletlen számtól.")

#print(f"A random szám {rnd}")

#atlag számítás
atlag: int=(paros+paratlan)/2

print(f"{paros} és {paratlan} átlaga {atlag}")

neggyelOszthato: int=0
for i in range(paros, paratlan +1, 1):
    if(i%4==0):
        neggyelOszthato+=1

print(f"{paros} és {paratlan} között {neggyelOszthato} 4-el osztható szám van.")