#!/usr/bin/python3.6
# Nom: 1d-mol
# Description: Jeu du plus ou moins
# Auteur: Florian Lafuente
# Date: 23/10/2018

# Gestion du random, des regex et gestion des signals
from random import randint
import re
import signal

# Fonction d'au revoir + affichage de la solution
def bye(*args):
  global x
  print("\nAu revoir!\nLa solution était: " + str(x))
  exit()

# Gestion signals
signal.signal(signal.SIGINT, bye)
signal.signal(signal.SIGTERM, bye)

x = randint(0,100)
fin = False

while fin is False:
  nb = input("Veuillez saisir un nombre entier (entre 0 et 100): ")

  # On vérifie l'entrée utilisateur
  if re.match(r"^[0-9]+$", nb):
    nb = int(nb)
    if nb > 100:
      continue
    
    if nb < x:
      print("Plus grand")
    elif nb > x:
      print("Plus petit")
    else:
      print ("Victoire!")
      fin = True
  
  elif nb == 'q':
    bye()  

  else:
    continue
