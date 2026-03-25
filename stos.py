# Zadanie - Stos w Python

stos = []
save = []

while True:
  print ("Program czyta literał znaków i wykonuje rozkazy.\n")
  print ("Dowolny znak - operacja umieszczenia,\nGwiazdka (*) - pobranie elementu ze stosu.")
  print ("Polecenie 'exit' (bez cudzysłowu) zamyka program.\n")
  string = input ("Wprowadź literał znaków: ")
  strlen = len (string)
  if string == "exit":
    exit()
  for i in range (strlen):
    if string[i] == "*" and len (stos) > 0:
      save.append (stos.pop())
    else:
      stos.append (string[i])
  print (save)
  save = []
