#!/usr/bin/python3.6
# Nom: 1a-add
# Description: retourne la somme de deux nombres demandés à l'utilisateur
# Auteur: Florian Lafuente
# Date: 15/10/2018

# Fonction qui retourne la somme de deux nombres
def somme(a, b):
  return a+b

# Saisi utilisateur
nb1 = input('Veuillez saisir un nombre: ')
nb2 = input('Veuillez saisir un deuxième nombre: ')

# Conversion en int
try:
  nb1 = int(nb1)
  nb2 = int(nb2)
except ValueError:
  print('Vous n'avez pas saisi des nombres entiers')
  exit()

# Affichage du résultat
print('Résultat: ' + somme(nb1, nb2))
