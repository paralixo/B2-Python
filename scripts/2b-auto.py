#!/usr/bin/python3.6
# Nom: 2b-auto
# Description: resolution jeu du plus ou moins dans un fichier
# Auteur: Florian Lafuente
# Date: 23/10/2018

# Gestion des regex
import re

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

max = 100
min = 0
nb = 50
fin = False
while fin is False:
  contenu = lire()

  if contenu == 'Victoire!':
    fin = True
    continue
  
  # On vérifie le contenu du fichier
  if re.match(r"^[0-9]+$", contenu):
    continue
  
  # On écrit dans le fichier
  else:
    if contenu == 'Plus grand':
      min = nb
    elif contenu == 'Plus petit':
      max = nb
    nb = min+int((max - min)/2)
    ecrire(str(nb))
    
