# Sortowanie liczb

import time


def insertion_sort(lista, visual=True):
    for i in range(1, len(lista)):
        curel = lista[i]
        j = i - 1
        while j >= 0 and curel < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
            if visual:
                print(lista)
        lista[j + 1] = curel
        if visual:
            print(lista)


def bubble_sort(lista, visual=True):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                if visual:
                    print(lista)


def quick_sort(lista, low, high, visual=True):
    if low < high:
        piv = lista[high]
        i = low - 1
        for j in range(low, high):
            if lista[j] < piv:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
                if visual:
                    print(lista)
        lista[i + 1], lista[high] = lista[high], lista[i + 1]
        if visual:
            print(lista)

        pi = i + 1
        quick_sort(lista, low, pi - 1, visual)
        quick_sort(lista, pi + 1, high, visual)


def benchmark(lista):
    test_lista = lista[:]
    start = time.perf_counter()
    insertion_sort(test_lista, visual=False)
    print(f"Insertion Sort: {(time.perf_counter() - start) * 1000:.3f} ms")

    test_lista = lista[:]
    start = time.perf_counter()
    bubble_sort(test_lista, visual=False)
    print(f"Bubble Sort: {(time.perf_counter() - start) * 1000:.3f} ms")

    test_lista = lista[:]
    start = time.perf_counter()
    quick_sort(test_lista, 0, len(test_lista) - 1, visual=False)
    print(f"Quick Sort: {(time.perf_counter() - start) * 1000:.3f} ms")


def main():
    user_input = input("Wprowadź liczby int oddzielone spacjami: ")
    data = [int(x) for x in user_input.split()]

    print("\n1. Insertion Sort\n2. Bubble Sort\n3. Quick Sort\n4. Benchmark")
    sel = input("Wybór: ")

    match sel:
        case "1":
            insertion_sort(data[:])
        case "2":
            bubble_sort(data[:])
        case "3":
            quick_sort(data[:], 0, len(data) - 1)
        case "4":
            benchmark(data)
        case _:
            print("Nieprawidłowy wybór.")


if __name__ == "__main__":
    main()
