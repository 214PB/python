print("Kérem adja meg a kedvenc filmjét!")
film: str=str(input())

print("Kérem adja meg ennek a megjelenési évét!")
ev: int=int(input())

print("Kérem adja meg ennek a rendezőjét!")
rendezo: str=str(input())

print("Kérem adja meg a főszereplő nevét!")
foszereplo: str=str(input())

print(f"{ev}-ban/-ben {rendezo} rendezésében megjelent a/az {film} című film {foszereplo} főszereplésével!")