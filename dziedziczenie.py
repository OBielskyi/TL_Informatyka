# Zadanie na dziedziczenie
# Oleksandr Bielskyi, 2Ic

class Zwierze:
	def __init__(self, gatunek, wiek, plec):
		self.gatunek = gatunek
		self.wiek = wiek
		self.plec = plec
	def biegnij(self, s, t):
		if t > 0 and s > 0:
			v = round((s / t), 2)
			print(v, "[m/s]")
		else:
			print("Błąd: Nieprawidłowa wartość.")
			quit()
	def daj_glos(self):
		print("????")
class Pies(Zwierze):
	def daj_glos(self):
		print("Hau!")
class Kot(Zwierze):
	def daj_glos(self):
		print("Miau!")
class Krowa(Zwierze):
	def daj_glos(self):
		print("Muu!")
print("Zwierze\n")
try:
	zwierze = Zwierze(input("Wprowadź nazwę gatunku: "), int(input("Wprowadź wiek: ")), input("Wprowadź płeć: "))
except Exception:
	print("Błąd: Nieprawidłowa wartość.")
	quit()
print("\nPies\n")
try:
	pies = Pies (input("Wprowadź nazwę gatunku: "), int(input("Wprowadź wiek: ")), input("Wprowadź płeć: "))
except Exception:
	print("Błąd: Nieprawidłowa wartość.")
	quit()
print("\nKot\n")
try:
	kot = Kot (input("Wprowadź nazwę gatunku: "), int(input("Wprowadź wiek: ")), input("Wprowadź płeć: "))
except Exception:
	print("Błąd: Nieprawidłowa wartość.")
	quit()
print("\nKrowa\n")
try:
	krowa = Krowa (input("Wprowadź nazwę gatunku: "), int(input("Wprowadź wiek: ")), input("Wprowadź płeć: "))
except Exception:
	print("Błąd: Nieprawidłowa wartość.")
	quit()
print("\nZwierze:")
zwierze.daj_glos()
print("\nPies:")
pies.daj_glos()
print("\nKot:")
kot.daj_glos()
print("\nKrowa:")
krowa.daj_glos()
print("\nBieganie (Zwierze)\n")
try:
	zwierze.biegnij(float(input("Wprowadź drogę [m]: ")), float(input("Wprowadź czas [s]: ")))
except Exception:
	print("Błąd: Nieprawidłowa wartość.")
	quit()
