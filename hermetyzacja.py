# Oleksandr Bielskyi, 2Ic
# Zadanie na hermetyzację

# Kocham Tomka ponad wszystko


class Temperatura:
    tcheck = False
    while not tcheck:
        try:
            __Celsjusz = float(
                input("Podaj temperaturę w stopniach Celsjusza: ")
            )  # musi być > -273.15
        except ValueError, KeyboardInterrupt:
            print("Błąd: Proszę wprowadzić liczbę.")
            quit()
        if __Celsjusz <= -273.15:
            print(
                "Błąd: Wprowadzono temperaturę mniejszą lub równą absolutnemu zeru (-273.15 stopni Celsjusza)."
            )
        else:
            tcheck = True

    def wyswietl(self):
        print(self.__Celsjusz)

    def wczytaj(self, i):
        self.__Celsjusz = i

    def fahrenheit(self):
        print(round((self.__Celsjusz * 1.8 + 32), 2))

    def kelwin(self):
        print(round((self.__Celsjusz + 273.15), 2))

    def reamur(self):
        print(round((self.__Celsjusz * 0.8), 2))


temperatura = Temperatura()
while True:
    try:
        sel = input(
            "[wy]świetl   [w]czytaj   [f]ahrenheit   [k]elwin   [r]eamur   [z]amknij: "
        )
    except Exception, KeyboardInterrupt:
        "Błąd."
        quit()
    match sel:
        case "wy":
            temperatura.wyswietl()
        case "w":
            tcheck = False
            while not tcheck:
                try:
                    temp = float(input("Podaj temperaturę w stopniach Celsjusza: "))
                except ValueError, KeyboardInterrupt:
                    print("Błąd: Proszę wprowadzić liczbę.")
                if temp <= -273.15:
                    print(
                        "Błąd: Wprowadzono temperaturę mniejszą lub równą absolutnemu zeru (-273.15 stopni Celsjusza)."
                    )
                else:
                    break
            temperatura.wczytaj(temp)
        case "f":
            temperatura.fahrenheit()
        case "k":
            temperatura.kelwin()
        case "r":
            temperatura.reamur()
        case "z":
            quit()
        case _:
            print("Błąd: Proszę wybrać jedną z dostępnych opcji.")
