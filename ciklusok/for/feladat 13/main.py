parosSzamokOsszege: int=0
paratlanSzamokOsszege: int=0

print("kezdő érték: ")
kezdoErtek: int=int(input())

print("vég érték: ")
vegErtek: int=int(input())

for i in range (kezdoErtek, vegErtek, 1):
    if(i % 2 == 0):
        parosSzamokOsszege+=i
    else:
        paratlanSzamokOsszege+=i

if(parosSzamokOsszege > paratlanSzamokOsszege):
    print(parosSzamokOsszege)
elif(parosSzamokOsszege < paratlanSzamokOsszege):
    print(paratlanSzamokOsszege)
else:
    print("egyenlő")
