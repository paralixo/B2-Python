#!/usr/bin/python3.6
# Nom: 2a-mol
# Description: Jeu du plus ou moins dans un fichier
# Auteur: Florian Lafuente
# Date: 23/10/2018

# Gestion du random, des regex et gestion des signals
from random import randint
import re
import signal

# Fonction d'au revoir + affichage de la solution
def bye(*args):
  global x
  ecrire("Au revoir!\nLa solution était: " + str(x))
  exit(0)

# Gestion signals
signal.signal(signal.SIGINT, bye)
signal.signal(signal.SIGTERM, bye)

# Ecrire dans un fichier
def ecrire(message):
  fichier = open("plusmoins.txt", "w")
  fichier.write(message)
  fichier.close()

# Lecture du fichier
def lire():
  fichier = open("plusmoins.txt", "r")
  message = fichier.read()
  fichier.close()
  return message

x = randint(0,100)
fin = False

ecrire("Bienvenue dans le jeu du plus ou moins!\n Veuillez saisir des nombres entiers compris entre 0 et 100\n")
while fin is False:
  nb = lire()

  # On vérifie l'entrée utilisateur
  if re.match(r"^[0-9]+$", nb):
    nb = int(nb)
    if nb > 100:
      continue
    
    if nb < x:
      ecrire("Plus grand")
    elif nb > x:
      ecrire("Plus petit")
    else:
      ecrire("Victoire!")
      fin = True
  
  elif nb == 'q' or nb == 'q\n':
    bye()  

  else:
    continue
