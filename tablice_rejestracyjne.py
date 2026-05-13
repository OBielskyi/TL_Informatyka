# Oleksandr Bielskyi, 1Ic
# Zadanie 1: Walidacja tablic rejestracyjnych

import re

def waliduj_tablice(tekst):
  match = re.search("[A-Z][A-Z][A-Z]?\s\w\w\w\w\w*", tekst)
  return match
  
while True:
  result = waliduj_tablice(input("Proszę wprowadzić ciąg znaków: "))
  if result:
    print("Tablica rejestracyjna jest poprawna.")
  else:
    print("Tablica rejestracyjna jest niepoprawna!")
  sel = input("0 -- zakończ, dowolny inny znak -- kontynuuj: ")
  if sel == 0:
    quit()
