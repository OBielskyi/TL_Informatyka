# Oleksandr Bielskyi, 1Ic
# Zadanie 2: Czyszczenie numerów telefonów

import re

def cleaning(tekst):
  to_remove = re.findall("\D", tekst)
  result = re.sub(to_remove, tekst)
  if len(result) > 0:
    return result
  else:
    return 1

while True:
  to_print = cleaning(input("Wprowadź tekst: "))
  if to_print != 1:
    print(to_print)
  res = input("0 -- zakończ, dowolny inny znak -- kontynuuj: ")
  if res == "0":
    quit()
