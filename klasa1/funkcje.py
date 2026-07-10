# Program "Funkcje"
'''
Program wczytuje 10 liczb (int) i realizuje działania za pomocą funkcji:
suma (suma), średnia arytmetyczna (srar),
największa (maks) i najmniesza (mini) liczba,
różnica pomiędzy maks a mini (rozn),
liczby parzyste (parz) i nieparzyste (niep).
'''

# Wczytujemy liczby
int1 = int (input ("Wprowadź liczbę 1 (int): "))
int2 = int (input ("Wprowadź liczbę 2: "))
int3 = int (input ("Wprowadź liczbę 3: "))
int4 = int (input ("Wprowadź liczbę 4: "))
int5 = int (input ("Wprowadź liczbę 5: "))
int6 = int (input ("Wprowadź liczbę 6: "))
int7 = int (input ("Wprowadź liczbę 7: "))
int8 = int (input ("Wprowadź liczbę 8: "))
int9 = int (input ("Wprowadź liczbę 9: "))
int10 = int (input ("Wprowadź liczbę 10: "))

# Definiujemy funkcje
def suma (): return int1+int2+int3+int4+int5+int6+int7+int8+int9+int10
def srar (): return (suma () // 10)
# Funkcja maks () ma chujowy (nieczytelny) kod, jeśli wiesz jak naprawić, to proszę to zrobić.
def maks ():
    if not ((int2 > int1) or (int3 > int1) or (int4 > int1) or (int5 > int1) or (int6 > int1) or (int7 > int1) or (int8 > int1) or (int9 > int1) or (int10 > int1)):
        return int1
    elif not ((int1 > int2) or (int3 > int2) or (int4 > int2) or (int5 > int2) or (int6 > int2) or (int7 > int2) or (int8 > int2) or (int9 > int2) or (int10 > int2)):
        return int2
    elif not ((int1 > int3) or (int2 > int3) or (int4 > int3) or (int5 > int3) or (int6 > int3) or (int7 > int3) or (int8 > int3) or (int9 > int3) or (int10 > int3)):
        return int3
    elif not ((int1 > int4) or (int2 > int4) or (int3 > int4) or (int5 > int4) or (int6 > int4) or (int7 > int4) or (int8 > int4) or (int9 > int4) or (int10 > int4)):
        return int4
    elif not ((int1 > int5) or (int2 > int5) or (int3 > int5) or (int4 > int5) or (int6 > int5) or (int7 > int5) or (int8 > int5) or (int9 > int5) or (int10 > int5)):
        return int5
    elif not ((int1 > int6) or (int2 > int6) or (int3 > int6) or (int4 > int6) or (int5 > int6) or (int7 > int6) or (int8 > int6) or (int9 > int6) or (int10 > int6)):
        return int6
    elif not ((int1 > int7) or (int2 > int7) or (int3 > int7) or (int4 > int7) or (int5 > int7) or (int6 > int7) or (int8 > int7) or (int9 > int7) or (int10 > int7)):
        return int7
    elif not ((int1 > int8) or (int2 > int8) or (int3 > int8) or (int4 > int8) or (int5 > int8) or (int6 > int8) or (int7 > int8) or (int9 > int8) or (int10 > int8)):
        return int8
    elif not ((int1 > int9) or (int2 > int9) or (int3 > int9) or (int4 > int9) or (int5 > int9) or (int6 > int9) or (int7 > int9) or (int8 > int9) or (int10 > int9)):
        return int9
    else:
        return int10
# Ten sam problem z funkcją mini (), jest prawie nieczytelna (działa jak odwrócona maks ()).
def mini ():
    if not ((int2 < int1) or (int3 < int1) or (int4 < int1) or (int5 < int1) or (int6 < int1) or (int7 < int1) or (int8 < int1) or (int9 < int1) or (int10 < int1)):
        return int1
    elif not ((int1 < int2) or (int3 < int2) or (int4 < int2) or (int5 < int2) or (int6 < int2) or (int7 < int2) or (int8 < int2) or (int9 < int2) or (int10 < int2)):
        return int2
    elif not ((int1 < int3) or (int2 < int3) or (int4 < int3) or (int5 < int3) or (int6 < int3) or (int7 < int3) or (int8 < int3) or (int9 < int3) or (int10 < int3)):
        return int3
    elif not ((int1 < int4) or (int2 < int4) or (int3 < int4) or (int5 < int4) or (int6 < int4) or (int7 < int4) or (int8 < int4) or (int9 < int4) or (int10 < int4)):
        return int4
    elif not ((int1 < int5) or (int2 < int5) or (int3 < int5) or (int4 < int5) or (int6 < int5) or (int7 < int5) or (int8 < int5) or (int9 < int5) or (int10 < int5)):
        return int5
    elif not ((int1 < int6) or (int2 < int6) or (int3 < int6) or (int4 < int6) or (int5 < int6) or (int7 < int6) or (int8 < int6) or (int9 < int6) or (int10 < int6)):
        return int6
    elif not ((int1 < int7) or (int2 < int7) or (int3 < int7) or (int4 < int7) or (int5 < int7) or (int6 < int7) or (int8 < int7) or (int9 < int7) or (int10 < int7)):
        return int7
    elif not ((int1 < int8) or (int2 < int8) or (int3 < int8) or (int4 < int8) or (int5 < int8) or (int6 < int8) or (int7 < int8) or (int9 < int8) or (int10 < int8)):
        return int8
    elif not ((int1 < int9) or (int2 < int9) or (int3 < int9) or (int4 < int9) or (int5 < int9) or (int6 < int9) or (int7 < int9) or (int8 < int9) or (int10 < int9)):
        return int9
    else:
        return int10
def rozn ():
    return maks()-mini()
# Kod funkcji parz () jest w miarę czytelny, ale wydaje mi się, że można go trochę skrócić.
def parz ():
    licznik = 0
    if (int1 % 2) == 0:
        licznik += 1
    if (int2 % 2) == 0:
        licznik += 1
    if (int3 % 2) == 0:
        licznik += 1
    if (int4 % 2) == 0:
        licznik += 1
    if (int5 % 2) == 0:
        licznik += 1
    if (int6 % 2) == 0:
        licznik += 1
    if (int7 % 2) == 0:
        licznik += 1
    if (int8 % 2) == 0:
        licznik += 1
    if (int9 % 2) == 0:
        licznik += 1
    if (int10 % 2) == 0:
        licznik += 1
    return licznik
def niep ():
    return 10 - parz()

# Menu
print ()
print ("Co chcesz zrobić?")
sel = int (input("1 -- suma, 2 -- średnia arytmetyczna,\n3 -- element maksymalny, 4 -- element minimalny,\n5 -- różnica między największym i najmniejszym,\n6 -- liczby parzyste, 7 -- liczby nieparzyste. "))
match sel:
    case 1:
        print (suma ())
    case 2:
        print (srar ())
    case 3:
        print (maks ())
    case 4:
        print (mini ())
    case 5:
        print (rozn ())
    case 6:
        print (parz ())
    case 7:
        print (niep ())
