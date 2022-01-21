x: int=None
temp: str=""

while(x==None):
    temp=input("Adjon meg egy számot!")
    if(temp.isnumeric()):
        x=int(temp)

for i in range (0, x, 1):
    if(i>1):
        for j in range(2, i, 1):
            if(i%j==0):
                break
            else:
                print(i)