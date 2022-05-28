from turtle import *

nombre_cote = 20
i = 0
while i < nombre_cote :
    forward(100)
    left(360/nombre_cote)
    i = i + 1

def compte_cote() :
    print("Cette figure contient", nombre_cote, "cotés")

compte_cote()    


#    color("orange")

#up()

#while nombre_cote < 7 :
#    forward(50)
#    right(90)
#    nombre_cote = nombre_cote + 1


    
