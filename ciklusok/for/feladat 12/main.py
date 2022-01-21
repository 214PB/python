harommalOszthatoSzamokSzama: int=0

print("kezdő érték: ")
kezdoErtek: int=int(input())

print("vég érték: ")
vegErtek: int=int(input())

for i in range (kezdoErtek, vegErtek, 1):
    if(i % 3 == 0):
        harommalOszthatoSzamokSzama += 1

print(harommalOszthatoSzamokSzama)
