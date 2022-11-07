x = float(input("Valor a ser trocado"))
cem: int
cinquenta: int
vinte: int
dez: int
cinco: int
dois: int

cem = x // 100
print(cem, "notas de 100")
x = x - (x // 100)*100

cinquenta = x // 50
print(cinquenta, "notas de 50")
x = x - (x // 50)*50

vinte = x // 20
print(vinte, "notas de 20")
x = x - (x // 20)*20

dez = x // 10
print(dez, "notas de 10")
x = x - (x//10)*10

cinco = x // 5
print(cinco, "notas de 5")
x = x - (x//5)*5

dois = x // 2
print(dois, "notas de 2")
x = x - (x // 2)*2