import funkcje
import time
print ("Co chcesz zrobić?")
sel = int (input("1 -- suma, 2 -- średnia arytmetyczna,\n3 -- element maksymalny, 4 -- element minimalny,\n5 -- różnica między największym i najmniejszym,\n6 -- liczby parzyste, 7 -- liczby nieparzyste. "))
print ()
match sel:
    case 1:
        print (funkcje.suma ())
    case 2:
        print (funkcje.srar ())
    case 3:
        print (funkcje.maks ())
    case 4:
        print (funkcje.mini ())
    case 5:
        print (funkcje.rozn ())
    case 6:
        print (funkcje.parz ())
    case 7:
        print (funkcje.niep ())
time.sleep (5)
