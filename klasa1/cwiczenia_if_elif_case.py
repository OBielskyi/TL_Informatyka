# Ćwiczenie 1
print ("Ćwiczenie 1")
print ("-------------------------------------------------------")\

punkty = int (input ("Wprowadź liczbę punktów (maksymalnie 100): "))
match punkty:
    case punkty if punkty >= 100:
        print ("Celujący")
    case punkty if punkty >= 90:
        print ("Bardzo dobry")
    case punkty if punkty >= 70:
        print ("Dobry")
    case punkty if punkty >= 50:
        print ("Dostateczny")
    case punkty if punkty >= 40:
        print ("Dopuszczający")
    case punkty if punkty >= 0:
        print ("Niedostateczny")
    case _:
        print ("Blędna liczba punktów")
        
print ("-------------------------------------------------------")
print ()

# Ćwiczenie 2
print ("Ćwiczenie 2")
print ("-------------------------------------------------------")

dzien = int (input ("Wprowadź dzień: "))
miesiac = int (input ("Wprowadź miesiąc: "))
rok = int (input ("Wprowadź rok: "))
dzien_ok = (dzien >= 1) and (dzien <= 31)
miesiac_ok = (miesiac >= 1) and (miesiac <= 12)
rok_przestepny = (rok % 4) == 0
dzien_ok_luty = None
match miesiac:
    case miesiac if (miesiac == 2) and (rok_przestepny):
        if (dzien_ok) and (dzien <= 29):
            dzien_ok_luty = True
        else:
            dzien_ok_luty = False
    case miesiac if miesiac == 2:
        if (dzien_ok) and (dzien <= 28):
            dzien_ok_luty = True
        else:
            dzien_ok_luty = False
match dzien_ok_luty:
    case None:
        if (dzien_ok) and (miesiac_ok):
            print ("Data jest poprawna.")
        else:
            print ("Niepoprawna data.")
    case True:
        print ("Data jest poprawna.")
    case False:
        print ("Niepoprawna data.")
print ("-------------------------------------------------------")
print ()

# Ćwiczenie 3
print ("Ćwiczenie 3")
print ("-------------------------------------------------------")

liczba1 = float (input ("Wprowadź liczbę 1: "))
liczba2 = float (input ("Wprowadź liczbę 2: "))
liczba3 = float (input ("Wprowadź liczbę 3: "))
warunek = None
if (liczba1 > 100) and (liczba2 <= 100) and (liczba3 <= 100):
    warunek = True
elif (liczba2 > 100) and (liczba1 <= 100) and (liczba3 <= 100):
    warunek = True
elif (liczba3 > 100) and (liczba1 <= 100) and (liczba2 <= 100):
    warunek = True
else:
    warunek = False
if warunek:
    print ("Dokładnie jedna z tych liczb jest większa od 100.")
print ("-------------------------------------------------------")
print ()

# Ćwiczenie 4
print ("Ćwiczenie 4")
print ("-------------------------------------------------------")

znak = input ("Wprowadź jeden znak z klawiatury: ")
match znak:
    case 'a'|'e'|'i'|'o'|'u'|'y':
        print ("Samogłoska")
    case 'b'|'c'|'d'|'f'|'g'|'h'|'j'|'k'|'l'|'m'|'n'|'p'|'q'|'r'|'s'|'t'|'v'|'w'|'x'|'z':
        print ("Spółgłoska")
print ("-------------------------------------------------------")
