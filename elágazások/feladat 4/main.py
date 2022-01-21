print("x=")
x: int=int(input())

print("y=")
y: int=int(input())

if(x==y):
    print("A két beolvasott szám egyenlő")
elif(x<y):
    print(f"{y}")
else:
    print(f"{x}")
