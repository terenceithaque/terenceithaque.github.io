from random import randrange
from tkinter import *






def jeu(mots, essais = 5):
  print(essais)
  # mots = ["amour", "république", "amitié", "moeurs", "facilité", "mérite"]
  a = mots[randrange(len(mots))]

  print(a)
  
  while essais > 0:
    print("Essayez de trouver n'importe quel mot ayant le même nombre de caractères que celui affiché")
    reponse = input()
    if len(reponse) < len(a):
      essais = essais - 1
      print("Mot trop court ! Vous perdez 1 essai ! Essais restants :", essais)
    elif len(reponse) > len(a):
      essais = essais - 1 
      print("Mot trop long! Vous perdez 1 essai. Essais restants :", essais)
     # reponse = input("Essayez de trouver n'importe quel mot ayant le même nombre de caractères que celui affiché")
    elif reponse == a:
      essais = essais - 1
      print("Vous avez rentré le même mot que celui proposé. Vous perdez 1 essai. Essais restants :", essais)
    elif len(reponse) == len(a):
      print("Bravo ! Vous avez gagné !")
      break

  if essais == 0:
    print("Vous avez perdu tous vos essais. GAME OVER")
  


jeu(["amour", "république", "amitié", "moeurs", "facilité", "mérite", "valide", "démentiel", "fleur", "cuisine", "vipère", "autocratie", "village"])



    
