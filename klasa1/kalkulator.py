# Kalkulator

from os import system
# Pokazujemy menu
print ("KALKULATOR")
ex = input ("Kliknij [Enter] by kontynuować, wprowadź coś innego by zamknąć program")
if len(ex)!=0:
  quit()
print("Ten kalkulator obsługuje tylko 4 operacje: dodawanie, odejmowanie, mnożenie i dzielenie.\nWczytuje 2 liczby.")
l1=1.0
l2=1.0
op = ""
res=1.0
try:
  l1 = float(input("Wprowadź pierwszą liczbę: "))
except Exception:
  print("Nieoczekiwany błąd -- musisz wprowadzić liczbę. Zamykam program...")
  quit()
try:
  l2 = float(input("Wprowadź drugą liczbę: "))
except Exception:
  print("Nieoczekiwany błąd -- musisz wprowadzić liczbę. Zamykam program...")
  quit()
try:
  op = input("Wprowadź operacje (znak): ")
except Exception:
  print("Nieoczekawiny błąd. Zamykam program...")
  quit()
match op:
  case "+":
    res=l1+l2
    print("Wynik:",res)
  case "-":
    res=l1-l2
    print("Wynik:",res)
  case "*":
    res=l1-l2
    print("Wynik:",res)
  case "/":
    try:
      res=l1/l2
      print("Wynik:",res)
    except Exception:
      print("Błąd -- niepoprawna operacja. Zamykam program...")
      quit()
