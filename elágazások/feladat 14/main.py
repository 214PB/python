print("x=")
x: int=int(input())

print("y=")
y: int=int(input())

print("z=")
z: int=int(input())

if(x%y==0 and x%z==0):
    print("X osztható y-al és z-vel.")
elif(x%y==0):
    print("X osztható y-al.")
elif(x%z==0):
    print("X osztható z-vel.")
else:
    print("X nem osztható se y-al, se z-vel.")