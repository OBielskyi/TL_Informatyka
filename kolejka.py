# Program "Kolejka"
# Symuluje działanie kolejki w sklepie

from time import sleep
from os import system

kolejka = []
active = True
while (active):
  print ("MENU")
  print ("1 -- dodaj klienta do kolejki\n2 -- obsłuż klienta\n3 -- pokaż pierwszą osobę w kolejce\n4 -- wyświetl całą kolejkę\n5 -- sprawdź długość kolejki\n6 -- zakończ")
  choice = int (input ("Wybierz opcję: "))
  match choice:
    case 1:
      kolejka.append (input("Wprowadź imię klienta: "))
    case 2:
      if len(kolejka)>0:
        print ("Obsłużono klienta:", kolejka.pop())
      else:
        print ("Kolejka jest pusta.")
    case 3:
      print ("Pierwsza osoba w kolejce to:", kolejka [0])
    case 4:
      print ("Cała kolejka:", kolejka)
    case 5:
      print ("Długość kolejki wynosi:", len(kolejka))
    case 6:
      active = False
  sleep (1)
  system ("clear||cls")
