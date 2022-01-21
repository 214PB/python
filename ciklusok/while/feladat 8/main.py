#8 – Keszítsünk automata menüt ahol egy szám egy üdítőt jelent. 
# A felhasználónak választania kell üdítőt, de csak azokból amelyek a kínálatban vannak. 
# Amennyiben nem azt választjuk nem kapunk üdítőt.

udito: int=None
temp: str=""


while(udito==None):
    temp=input("Kérem válasszon egy üdítőt! 1-9-ig")
    if(temp.isnumeric()):
        udito=int(temp)

if(udito==1):
    print("A választott üdítő: narancslé")
elif(udito==2):
    print("A választott üdítő: kóla")
elif(udito==3):
    print("A választott üdítő: szőlőlé")
elif(udito==4):
    print("A választott üdítő: tej")
elif(udito==5):
    print("A választott üdítő: kávé")
elif(udito==6):
    print("A választott üdítő: kakaó")
elif(udito==7):
    print("A választott üdítő: limonádé")
elif(udito==8):
    print("A választott üdítő: forrócsoki")
elif(udito==9):
    print("A választott üdítő: szivárvány unikornis")
else:
    print("Nem a kínálatból választott")      