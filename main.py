with open("liczby.txt") as f:
    tab = f.read().splitlines()

tab2 = []
for i in tab:
    print(i.split(" "))
    for j in i.split(" "):
        tab2.append(int(j))
print(tab2)
wynik = []
wynik2 = 0
for x in range(1, 43):
    wynik.append(str(x) + " " + str(tab2.count(x)))
    wynik2 += tab2.count(x)
print(wynik)
print(wynik2)

for i in range(0, len(wynik)-1):
    for j in range(0, len(wynik)-i-1):
        a = wynik[j].split(" ")[1]
        b = wynik[j+1].split(" ")[1]
        if a > b:
            wynik[j], wynik[j+1] = wynik[j+1], wynik[j]
print(wynik[-6:])
