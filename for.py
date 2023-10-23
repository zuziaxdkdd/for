# 1. Wyświetl liczby od 1 do 10.
# 2. Oblicz sumę liczb od 1 do 100.
# 3. Wyświetl wszystkie parzyste liczby od 1 do 50.
# 4. Oblicz iloczyn liczb od 1 do 5.
# 5. Wyświetl odwróconą wersję napisu "Hello World!".
# 6. Wyświetl wszystkie litery z podanego słowa.
# 7. Oblicz sumę elementów listy liczb.
# 8. Wyświetl wszystkie liczby od 20 do 30, które są podzielne przez 3.
# 9. Znajdź największą liczbę w liście.
# 10. Wyświetl wszystkie liczby od 1 do 100, które są podzielne jednocześnie przez 3 i 5.
# 11. Oblicz średnią arytmetyczną z listy liczb.
# 12. Wyświetl wszystkie litery z podanego zdania, pomijając spacje.
# 13. Oblicz silnię liczby podanej przez użytkownika.
# 14. Wyświetl tabliczkę mnożenia (od 1 do 20).
# 15. Sprawdź, czy podane słowo jest palindromem.
# 16. Zamień wszystkie litery w podanym napisie na wielkie litery.
# 17. Wyświetl liczby od 1 do 10 w odwrotnej kolejności.


# 1. Wyświetl liczby od 1 do 10.

for el in range(10):
    print(el)



# 2. Oblicz sumę liczb od 1 do 100.

suma = 0

for el in range(100):
    el += 1
    suma += el

print(suma)

# a tak w odpoweidziach:

suma = 0

for el in range(100):
    suma += 1

print(suma)


# 3. Wyświetl wszystkie parzyste liczby od 1 do 50.

for el in range(51):
    if el % 2 == 0:
        print(el)


# 4. Oblicz iloczyn liczb od 1 do 5.

iloczyn = 1

for i in range(1,6,1):
    iloczyn *= i

print(iloczyn)

print(1*2*3*4*5)


# 5. Wyświetl odwróconą wersję napisu "Hello World!".

napis = "Hello World!"
napis2 = ""

for el in napis:
    napis2 = el + napis2

print(napis2)


# 6. Wyświetl wszystkie litery z podanego słowa.

slowo = "słowo"

for el in slowo:
    print(el)


# 7. Oblicz sumę elementów listy liczb.

lista = [1,1,1,1,1,1,7]

suma = 0

for el in lista:
    suma += 1

print(suma)


# 8. Wyświetl wszystkie liczby od 20 do 30, które są podzielne przez 3.

for el in range(20,31,1):
    if el % 3 == 0:
        print(el)


# 9. Znajdź największą liczbę w liście.

lista = [1,2,3,10,8,5]

najwieksza = lista[0]

for el in lista:
    if el > najwieksza:
        najwieksza = el

print(najwieksza)


# 10. Wyświetl wszystkie liczby od 1 do 100, które są podzielne jednocześnie przez 3 i 5.

for el in range(100):
    if el % 3 == 0:
        if el % 5 == 0:
            print(el)



#11. Oblicz średnią arytmetyczną z listy liczb.

lista = [2,4,6,8,10]

srednia = 0
iloscliczb = 0

for el in lista:
    srednia += el

for el in lista:
    iloscliczb += 1

print(srednia % iloscliczb)

# w odp:

lista = [2,5]
suma = 0
for number in lista:
    suma += number
print(suma/len(lista))


# 12. Wyświetl wszystkie litery z podanego zdania, pomijając spacje.

zdanie = "litery z podanego zdania"

for el in zdanie:
    if el != " ":
        print(el)


# 18. Wyświetl liczby od 1 do 10 w odwrotnej kolejności.

for el in range(10,0,-1):
    print(-el)




# reszta to pomoc z odpowiedziami


# 13. Oblicz silnię liczby podanej przez użytkownika.


inp = int(input())
silnia = 1
for i in range(1,inp+1):
    silnia *= i
print(silnia)


# 14. Wyświetl tabliczkę mnożenia (od 1 do 20).


for i in range(1,21):
    for j in range(1,21):
        res = i * j
        print(f" {res:3} ", end=" ")
    print("\n")


# 15. Sprawdź, czy podane słowo jest palindromem.


inp = input()
palindromem = True
for i in range(len(inp)//2):
    if inp[i] != inp[-i - 1]:
        palindromem = False
        break
print(palindromem)


# 16. Zamień wszystkie litery w podanym napisie na wielkie litery.


inp = input()
text = ""
for el in inp:
    text += el.upper()
print(text)
