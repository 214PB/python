parosSzamokOsszege: int=0
paratlanSzamokSzorzata: int=1

print("kezdő érték: ")
kezdoErtek: int=int(input())

print("vég érték: ")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    if (i % 2 == 0):
        parosSzamokOsszege + i
    else:
        paratlanSzamokSzorzata * i 

print(f"{parosSzamokOsszege}")
print(f"{paratlanSzamokSzorzata}")
