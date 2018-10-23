#!/usr/bin/python3.6
# Nom: 1c-moy
# Description: Affiche la moyenne des notes et un top 5
# Auteur: Florian Lafuente
# Date: 15/10/2018

# Pour la regex
import re

# fonction qui retourne les prenoms des eleves associés à leur note
def notes():
  dict = {}
  
  while True:
    prenom = input('Veuillez saisir un prenom: ')    
    if prenom == 'q':
      break
    
    elif re.match(r"^([a-z]|[A-Z]|-|é|ï)+$", prenom):
      note = input('Veuillez saisir un note pour ' + prenom + ': ')
      try:
        note = int(note)
        if note >= 0 and note <= 20:
          dict[prenom] = note
        else:
          print('Veuillez saisir un nombre compris entre 0 et 20')
      except ValueError:
        print('Veuillez saisir un entier valide')
    
    else:
      print('Veuillez saisir un prénom valide')


  return dict

# Retourne la moyenne des notes saisies
def getMoyenne(dict):
  somme = 0
  for key in dict:
    somme += dict[key]
  moyenne = somme / len(dict)
  moyenne = round(moyenne, 2)
  return str(moyenne)

# Affiche le top 5 des notes
def getTop5(dict):
  print('Les meilleures notes: ')

  sortDict = sorted(dict.items(), key=lambda x: x[1])
  top = len(dict)-1
  limit = top-5
  for i in range(top, limit, -1):
    if i >= 0:
      prenom = sortDict[i][0]
      note = sortDict[i][1]
      print(str(top - i + 1) + ': ' + prenom + ' avec ' + str(note) + '/20')

# On récupère les prénoms et les notes
dict = notes()

# On calcule puis affiche la moyenne des notes
moyenne = getMoyenne(dict)
print('Moyenne: ' + moyenne)

# On affiche le top 5
getTop5(dict)

