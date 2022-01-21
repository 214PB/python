print("kezdő érték: ")
kezdoErtek: int=int(input())

print("vég érték: ")
vegErtek: int=int(input())

if(vegErtek % 2 != 0):
    vegErtek-=1

for i in range (vegErtek, kezdoErtek, -2):
    print(i)
