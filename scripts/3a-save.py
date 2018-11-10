#!/usr/bin/python3.6
# Nom: 3a-save
# Description: archive et compresse un répertoire vers le répertoire 'data'
# Auteur: Florian Lafuente
# Date: 06/11/2018

# Imports
import shutil
import gzip
import os
import sys
import signal

src = "/tmp/pyscripts/B2-Python/scripts/bidon"
filename = "bidon"
dst = "/tmp/pyscripts/B2-Python/scripts/data"

# On archive le répertoire choisi
shutil.make_archive(src, 'gztar')
filename += ".tar.gz"

# L'archive existe-t-elle déjà dans le dossier data ?
isAlreadyHere = False
for file in os.listdir(dst):
  if file == filename:
    isAlreadyHere = True
    print("Fichier déjà présent")
    break;

# Si l'archive est déjà présente, le contenu est-t-il différent ?
if isAlreadyHere:
  new_file = gzip.open(src + ".tar.gz").read()
  current_file = gzip.open(dst + "/"  + filename).read()
  if new_file == current_file:
    print("Fichiers identiques ! ")
  else:
    print("Déplacement du fichier")
    shutil.move(src + ".tar.gz", dst + "/" + filename)
