#Olvassunk be egy életkort 0-99 között. Addig ismételjük amíg nem lesz jó a bevitel! Adjuk meg hogy melyik korosztályba esik az illető!
#0-6: gyerek, 7-18: iskolás, 19-65: dolgozó, 65- nyugdíjas)

eletkor: int= 100
temp: str=""

while(eletkor>99 or eletkor<0):
    temp= input("Kérem adja meg az életkorát!")
    if(temp.isnumeric()):
        eletkor=  int(temp)

if(eletkor>=0 and eletkor<=6):
    print("Ön gyerek.")
elif(eletkor>=7 and eletkor<=18):
    print("Ön iskolás.")
elif(eletkor>=19 and eletkor<=65):
    print("Ön dolgozó")
elif(eletkor>65):
    print("Ön nyugdíjas.")