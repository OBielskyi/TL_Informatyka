import random

slownik = {
    "computer": "komputer",
    "mouse": "mysz",
    "keyboard": "klawiatura",
    "monitor": "monitor",
    "printer": "drukarka",
    "screen": "ekran",
    "file": "plik",
    "folder": "folder",
    "network": "sieć",
    "internet": "internet",
    "password": "hasło",
    "user": "użytkownik",
    "system": "system",
    "server": "serwer",
    "database": "baza danych",
    "processor": "procesor",
    "memory": "pamięć",
    "disk": "dysk",
    "application": "aplikacja",
    "program": "program"
}

Lista_Haseł = {
    "zamek": ["castle", "lock", "zipper"],
    "klucz": ["key", "wrench"],
    "pokój": ["room", "peace"],
    "bieg": ["run", "race", "gear"],
    "stan": ["state", "condition", "status"],
    "rada": ["advice", "council", "board"],
    "akt": ["act", "document", "deed"],
    "sprawa": ["case", "matter", "issue"],
    "widok": ["view", "sight", "scene"],
    "droga": ["road", "way", "path"],
    "strona": ["page", "side", "party"],
    "rząd": ["government", "row"],
    "karta": ["card", "map"],
    "linia": ["line", "queue", "boundary"]
}

for pol, eng in Lista_Haseł.items():
    print(pol, "-", eng)

print('\n   SŁOWNIK ANGIELSKO - POLSKI')

while True:
    print('\n---------     MENU     ---------')
    print(' 1.Tłumacz angielski --> polski  ')
    print(' 2.Tłumacz polski --> angielski  ')
    print(' 3.Dodaj nowe słowo              ')
    print(' 4.Wyświetl cały słownik         ')
    print(' 5.Quiz                          ')
    print(' 0.Wyjście                       ')
    
    wybór = int(input('Wybierz opcję(0-5): '))

    if wybór == 1:
        slowo = input('\nWpisz słowo po angielsku:\n')
        if slowo in slownik:
            print(slowo, 'po polsku znaczy:', slownik[slowo])
        else:
            print('\nNie ma takiego słowa w słowniku')
    
    elif wybór == 2:
        slowo = input('\nWpisz słowo po polsku:\n')
        znalezione = 0
        for eng, pol in slownik.items():
            if pol == slowo:
                znalezione = 1
                print(slowo, 'po angielsku znaczy:', eng)

    elif wybór == 3:
        eng = input('\nWpisz słowo po angielsku: ')
        pol = input('\nWpisz słowo po polsku: ')
        slownik[eng] = pol
        print('\nDodano słowo do słownika')
    
    elif wybór == 4:
        print('\nWyświetlam cały słownik:')
        for eng, pol in slownik.items():
            print(eng, '-', pol)

    elif wybór == 0:
        print('Koniec słownika')
        break

    elif wybór == 5:
        print('Informacje na temat Quizu:')
        print('Quiz ma 3 pytania.')
        print('Program wylosuje słowo po polsku, a Ty wpisujesz angielskie tłumaczenie.')
        print('Za poprawną odpowiedź jest 1 punkt.\n')
        
        lista_do_Quizu = list(slownik.items())
        random.shuffle(lista_do_Quizu)
        
        pytania = 0
        punkty = 0

        for eng, pol in lista_do_Quizu:
            odpowiedz = input(pol + ': ')
            if odpowiedz == eng:
                print('Prawidłowa odpowiedź')
                punkty += 1
            else:
                print('Błędna odpowiedź')
            
            pytania += 1
            if pytania == 3:
                print('\nKoniec Quizu')
                print('Wynik:', punkty)
                break

    else:
        print('\nZły wybór')
