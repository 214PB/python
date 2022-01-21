print("x=")
x: int=int(input())

if(x>=0 and x<=9):
    print("X egyjegyű szám.")
elif(x>=10 and x<=99):
	print("X kétjegyű szám.")
elif(x>=100 and x<=999):
	print("X háromjegyű szám.")
elif(x<0):
	print("X negatív szám.")
else:
	print("X több mint 3 jegyű.")