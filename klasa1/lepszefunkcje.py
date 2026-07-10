liczby_calk = []


print("-" * 30)
print("\nWpisz 10 liczb całkowitych\n")
print("-" * 30)


for i in range(10):
    while True:
        liczba = int(
            input("\nPodaj liczbe:")
        )  ### wypisywanie z klawiatury liczb całkowitych
        liczby_calk.append(liczba)
        break


def Suma_liczb_calk(liczby_calk):
    return sum(liczby_calk)  ### suma


def srd_arytm(liczby_calk):
    return Suma_liczb_calk(liczby_calk) / len(liczby_calk)  ### średnia arytmetyczna


def mediana(liczby_calk):
    liczby_sorted = sorted(liczby_calk)
    return liczby_sorted[4]  ### mediana


# Tu medianą będzie 5 element z 10


def elem_max(liczby_calk):
    return max(liczby_calk)  ### element maksymalny


def elem_min(liczby_calk):
    return min(liczby_calk)  ### element minimalny


def rozn_najw_najmn(liczby_calk):
    return elem_max(liczby_calk) - elem_min(
        liczby_calk
    )  ### różnica największej od najmniejszej


def liczba_liczb_parz(liczby_calk):
    parzyste = 0
    for i in liczby_calk:
        if i % 2 == 0:  ### liczby parzyste
            parzyste += 1
    return parzyste


def liczba_liczb_nieparz(liczby_calk):
    nieparzyste = 0
    for i in liczby_calk:
        if i % 2 != 0:  ### Liczby nieparzyste
            nieparzyste += 1
    return nieparzyste


print("-" * 30)
print("\nSuma tych liczb wynosi:", Suma_liczb_calk(liczby_calk))
print("-" * 30)
print("\nŚrednia arytmetyczna liczb wynosi:", srd_arytm(liczby_calk))
print("-" * 30)
print("\nmediana tych liczb wynosi:", mediana(liczby_calk))
print("-" * 30)
print("\n element maksymalny liczb to :", elem_max(liczby_calk))
print("-" * 30)
print("\n element minimalny liczb to :", elem_min(liczby_calk))
print("-" * 30)
print(
    "\n różnica między największym i najmniejszym elementem to :",
    rozn_najw_najmn(liczby_calk),
)
print("-" * 30)
print("\n liczba liczb parzystych wynosi:", liczba_liczb_parz(liczby_calk))
print("-" * 30)
print("\n liczba liczb nieparzystych wynosi:", liczba_liczb_nieparz(liczby_calk))
print("-" * 30)
