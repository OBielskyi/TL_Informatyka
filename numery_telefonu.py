# Oleksandr Bielskyi, 1Ic
# Zadanie 2: Czyszczenie numerów telefonów

import re

def clearing(tekst: str) -> list[str]:
    wzorzec = r'(?<!\d)\+?(?:[\(\)]*\d[\(\)]*[\s\-]*){8,}[\(\)]*\d(?!\d)'
    dopasowania = re.findall(wzorzec, tekst)
    lista_numerow = []
    
    for dopasowanie in dopasowania:
        cyfry = re.sub(r'\D', '', dopasowanie)
        
        if len(cyfry) >= 9:
            numer_dobry = cyfry[-9:]
            lista_numerow.append(numer_dobry)
            
    return lista_numerow

while True:
    result = clearing(input("Wprowadź tekst zawierający numer(y) telefonu: "))
    for i in result:
        print(i)
    sel = input("0 -- zakończ, dowolny inny znak -- kontynuuj: ")
    if sel == "0":
      quit()
