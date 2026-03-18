# Program "Ruletka" (pełna wersja, z podpunktami 4 i 5)
# Ten kod nie ma komentarzy, bo jestem leniwy. Potem to zrobię, ok?

from random import randint

m = 100
u = None
q = 0

print ("Masz 100 zł.")

while m > 0:
    print ("Wybierz rodzaj zakładu:")
    wybor = int (input ("1 -- numer pojedynczy,\n2 -- kolumna,\n3 -- tuziny,\n4 -- połowy,\n5 -- parzyste/nieparzyste,\n6 -- czarne/czerwone\n"))
    match wybor:
        case 1:
            q = 35
            u = int (input ("Wprowadź liczbę (0-36): "))
            if u < 0 or u > 36:
                print ("Błąd.")
                exit ()
        case 2:
            q = 2
            u = int (input ("Wprowadź numer kolumny (1-3): "))
            if u < 1 or u > 3:
                print ("Błąd.")
                exit ()
        case 3:
            q = 2
            u = int (input ("Wprowadź tuzin (1-3): "))
            if u < 1 or u > 3:
                print ("Błąd.")
                exit ()
        case 4:
            q = 1
            u = int (input ("Wprowadź numer połowy (1-2): "))
            if u < 1 or u > 2:
                print ("Błąd.")
                exit ()
        case 5:
            q = 1
            u = int (input ("0 -- parzyste, 1 -- nieparzyste: "))
            if u < 0 or u > 1:
                print ("Błąd.")
                exit ()
        case 6:
            q = 1
            u = int (input ("0 -- czarne, 1 -- czerwone: "))
        case _:
            print ("Błąd.")
            exit ()
    stawka = float (input("Wprowadź wysokość stawki [zł]: "))
    if stawka > m:
        print ("Niewystarczająca ilość pieniędzy.")
        exit ()

# Losowanie liczby:
    i = randint (0, 36)
    print ("Wylosowana liczba to:", i)

    if i % 2 == 0:
        print ("Liczba jest parzysta.")
    elif i != 0:
        print ("Liczba nie jest parzysta.")
    
    tuzin = 0
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

    polowa = 0
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
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9 or i == 12 or i == 14 or i == 16 or i == 18 or i == 19 or i == 21 or i == 23 or i == 25 or i == 27 or i == 30 or i == 32 or i == 34 or i == 36:
        czerwona = True
    if czerwona and i != 0:
        print ("Czerwona.")
    elif i != 0:
        print ("Czarna.")

    win = False
    match wybor:
        case 1:
            if u == i:
                win = True
        case 2:
            if u == kolumna:
                win = True
        case 3:
            if u == tuzin:
                win = True
        case 4:
            if u == polowa:
                win = True
        case 5:
            if i % 2 == u:
                win = True
        case 6:
            if u == 0 and czerwona == False:
                win = True
            elif u == 1 and czerwona == True:
                win = True
    if win:
        m = m + q * stawka
        print ("Wygrana!")
    else:
        print ("Przegrana!")
        m = m - stawka
    print ("Masz", m, "zł.")
