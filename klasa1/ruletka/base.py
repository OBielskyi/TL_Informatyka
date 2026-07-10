# Program "Ruletka" (krótka wersja)

from random import randint    # Program ten potrzebuje randint z modułu random dla generacji losowych liczb

# Losowanie liczby
i = randint (0, 36)
print ("Wylosowana liczba to:", i)

if i % 2 == 0:
    print ("Liczba jest parzysta.")
elif i != 0:
    print ("Liczba nie jest parzysta.")
    
tuzin = 0    # Jeśli tuzin pozostanie 0, to i jest 0, czyli nie należy do żadnego tuzina
match i:
    case i if i >= 1 and i <= 12:
        tuzin = 1
    case i if i >= 13 and i <= 24:
        tuzin = 2
    case i if i >= 25 and i <= 36:
        tuzin = 3
match tuzin:
    case 1:
        print ("Liczba należy do 1 tuzina.")
    case 2:
        print ("Liczba należy do 2 tuzina.")
    case 3:
        print ("Liczba należy do 3 tuzina.")

polowa = 0    # Analogicznie do zmiennej tuzin
if i >= 1 and i <=18:
    polowa = 1
elif i >= 18 and i <= 36:
    polowa = 2
if polowa == 1:
    print ("Liczba należy do 1 połowy liczb koła ruletki.")
elif polowa == 2:
    print ("Liczba należy do 2 połowy liczb koła ruletki.")

kolumna = 0
match i:
    case i if i % 3 == 1:
        kolumna = 1
    case i if i % 3 == 2:
        kolumna = 2
    case i if i % 3 == 3:
        kolumna = 3

if kolumna != 0:
    print ("Liczba należy do", kolumna, "kolumny.")

czerwona = False
# Kod poniżej sprawdza, czy liczba jest czerwoną (według tabelki). Ten warunek jest długi w chuj, ale chyba nie da się tego zrobić inaczej.
if i == 1 or i == 3 or i == 5 or i == 7 or i == 9 or i == 12 or i == 14 or i == 16 or i == 18 or i == 19 or i == 21 or i == 23 or i == 25 or i == 27 or i == 30 or i == 32 or i == 34 or i == 36:
    czerwona = True
if czerwona and i != 0:
    print ("Czerwona.")
elif i != 0:
    print ("Czarna.")
