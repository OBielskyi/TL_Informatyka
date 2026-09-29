# Klasy i obiekty
# Oleksandr Bielskyi, 2Ic

# Napisz klasę KontoBankowe z atrybutami wlasciciel oraz saldo (początkowo domyślnie 0.0).
# Metody:
# wplac(kwota) - jeśli kwota jest dodatnia, dodaje pieniądze do konta
# wyplac(kwota) - odejmuje pieniądze s konta, o ile na koncie jest wystarczająco środków
# pokaż_saldo() - aktualny stan konta
# Przy tworzeniu obiektu podaj nazwę właściciela

class KontoBankowe:
    def __init__(self,wlasciciel):
        self.wlasciciel = wlasciciel
        self.saldo = 0.0
    def wplac(self, kwota):
        if kwota > 0:
            self.saldo += kwota
        else:
            print("Proszę wprowadzić liczbę dodatnią.")
    def wyplac(self, kwota):
        if kwota > 0 and kwota <= self.saldo:
            self.saldo -= kwota
        elif kwota > self.saldo:
            print("Nie masz wystarczająco środków.")
            
        else:
            print("Proszę wprowadzić liczbę dodatnią.")
    def pokaz_saldo(self):
        print(self.saldo)
nowe_konto = KontoBankowe(input("Podaj nazwę właściciela konta: "))
while True:
    print("1 -- wpłacić kwotę, 2 -- wypłacić kwotę, 3 -- pokaż saldo, 4 -- zakończ")
    try:
        choice = int(input("Proszę wybrać opcję: "))
    except ValueError:
        print("Błąd: proszę wprowadzić liczbę.")
        quit()
    match choice:
        case 1:
            try:
                nowe_konto.wplac(float(input("Ile chcesz wpłacić? ")))
            except ValueError:
                print("Proszę wprowadzić liczbę.")
        case 2:
            try:
                nowe_konto.wyplac(float(input("Ile chcesz wypłacić? ")))
            except ValueError:
                print("Proszę wprowadzić liczbę.")
        case 3:
            nowe_konto.pokaz_saldo()
        case 4:
            quit()
