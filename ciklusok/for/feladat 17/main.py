szamokSzama: int=0
szamokOsszege: int=0
atlag: int=0

print("Kezdő érték=")
kezdoErtek: int=int(input())

print("Végérték=")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek + 1, 1):
    szamokOsszege+:i
    szamokSzama+=1

atlag= szamokOsszege / szamokSzama

print(atlag)