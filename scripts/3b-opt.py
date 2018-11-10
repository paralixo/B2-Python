#!/usr/bin/python3.6
# Nom: 3b-opt
# Description: script 3a-save avec choix de répertoire et une aide
# Auteur: Florian Lafuente
# Date: 11/11/2018

# Imports
import shutil
import gzip
import os
import sys
import signal

sys.stdout.write("Répertoire de sauvegarde (data) :")
dst = input()
sys.stdout.write("Répertoire à sauvegarder :")
src = input()
filename = src.split("/")
filename = filename[len(filename)-1]

#filename = "bidon"
#src = "/tmp/pyscripts/B2-Python/scripts/" + filename
#dst = "/tmp/pyscripts/B2-Python/scripts/data"

# Fonction gestion signal
def quit(*args):
  try:
    os.remove(src + ".tar.gz")
    sys.stdout.write("Sauvegarde annulé.")
  except:
    sys.stdout.write("Au revoir !")
  exit(0)

signal.signal(signal.SIGINT, quit)

# On archive le répertoire choisi
shutil.make_archive(src, 'gztar', src)
filename += ".tar.gz"

# L'archive existe-t-elle déjà dans le dossier data ?
isAlreadyHere = False
for file in os.listdir(dst):
  if file == filename:
    isAlreadyHere = True
    sys.stdout.write("Fichier déjà présent. Je vérifie si il y a une différence entre les fichiers. \n")
    break;

# Si l'archive est déjà présente, le contenu est-t-il différent ?
isFileDifferent = False
if isAlreadyHere:
  new_file = gzip.open(src + ".tar.gz").read()
  current_file = gzip.open(dst + "/"  + filename).read()
  if new_file == current_file:
    sys.stdout.write("Pas de différences. On annule la sauvegarde. \n")
  else:
    isFileDifferent = True
    sys.stdout.write("Différences détectés. On déplace l'archive. \n")

# Déplacement du fichier
if (isAlreadyHere and isFileDifferent) or isAlreadyHere == False:
  shutil.move(src + ".tar.gz", dst + "/" + filename)

os.remove(src + ".tar.gz")
