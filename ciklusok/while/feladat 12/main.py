#12 - Van egy kis megtakarított pénzem (min 10.000, max 50.000).
#  Arra vagyok kíváncsi, hogy hány hónap múlva éri el ez az összeg a bankban a 100 000 Ft-ot, ha havi 2%-os kamattal számolhatok?

penz: float=None
temp: str=""
honapok: int=0

while(penz==None or penz<10000 or penz>50000 ):
    temp=input("Kérem adja meg a pénzének az összegét!")
    if(temp.isnumeric()):
        penz=int(temp)

while(penz<100000):
    penz=penz*1.02
    honapok+=1

print(f"{honapok} hónap alatt éri el a 100.000 Ft-t a pénze a bankban.")
