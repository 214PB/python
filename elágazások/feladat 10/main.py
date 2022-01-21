print("x=")
x: int=int(input())

if(x%2==0 and x%3==0):
    print("ZIZI")
elif(x%3==0):
    print("BAZ")
elif(x%2==0):
    print("BIZ")
else:
    print("X nem osztható se 2-vel se 3-al.")