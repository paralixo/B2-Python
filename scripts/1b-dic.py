#!/usr/bin/python3.6
# Nom: 1b-dic
# Description: Retourne une liste de prenoms dans l'ordre alphabétique
# Auteur: Florian Lafuente
# Date: 15/10/2018

# Pour que la regex fonctionne
import re

# fonction qui retourne les prenoms demandés à l'utilisateur
def prenoms():
  list = []
  continueWhile = True
  
  while continueWhile:
    prenom = input('Veuillez sasir un prénom: ')
    if prenom == 'q':
      continueWhile = False
    elif re.match(r"^([a-z]|[A-Z]|-|é|ï)+$", prenom):
      list.append(prenom)
    else:
      print('Veuillez saisir un prénom valide')

  return list

list = prenoms()

# Trie alphabétique
sortedList = sorted(list)
print(sortedList)
