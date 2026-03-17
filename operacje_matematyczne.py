# !! JEST TO ĆWICZENIE Z 1 OKRESU !!

import math

# Ćwiczenie 1
n = int (input ("Wprowadź liczbę trzycyfrową: "))
print ()
n1 = n % 10
n10 = (n % 100 - n1) // 10
n100 = (n % 1000 - n10 - n1) // 100
nsum = n1 + n10 + n100
print (n,"->",n100,"+",n10,"+",n1,"=",nsum)

# Ćwiczenie 2
print ()
print (n,"->",n1,n10,n100)

# Ćwiczenie 3
print ()
ocena1 = int (input ("Wprowadź ocenę 1: "))
waga1 = int (input ("Wprowadź wagę oceny 1:"))
ocena2 = int (input ("Wprowadź ocenę 2: "))
waga2 = int (input ("Wprowadź wagę oceny 2: "))
ocena3 = int (input ("Wprowadź ocenę 3: "))
waga3 = int (input ("Wprowadź wagę oceny 3: "))
srednia = ((ocena1 * waga1) + (ocena2 * waga2) + (ocena3 * waga3)) / (waga1 + waga2 + waga3)
print ("Średnia ocen wynosi:", srednia)

# Ćwiczenie 4
a = float (input ("Wprowadź długość przyprostokątnej a: "))
b = float (input ("Wprowadź długość przyprostokątnej b: "))
c = math.sqrt (a ** 2 + b ** 2)
print ("Długość przeciwprostokątnej c wynosi:",c)
