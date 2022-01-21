#18 – A felhasználótól kérjünk be egy intervallumot (kezdő és vég értéket). Az első elemet adjuk hozzá az összeghez, 
#a másodikat vonjuk ki, a harmadikat újra adjuk hozzá az összeghez, a negyediket vonjuk ki az összegből … és így tovább.

elojelValto: int=1
osszege: int=0

print("Kezdőérték=")
kezdoErtek: int=int(input())

print("Végérték=")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek, + 1, 1):
    osszeg= osszeg+i *elojelValto
    elojelValto= elojelValto* (-1)

print(osszeg)