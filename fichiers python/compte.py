from turtle import *
#from tkinter import *
#def close() :
       #root = Tk()
       #root.geometry("200x100")

      # close_button = Button(root, text="Arrêter le processus", command = exit())
    
       #close_button.pack(pady = 20)


       #root.mainloop()
def compte_nombres():
    compte = 0
    nombre = 0
    while compte < 20:
        nombre = nombre + 1
        print(nombre)
        compte = compte + 1
    print("Il y a", nombre, "nombres")
    print(nombre, "divisé par 2 est égal à", nombre / 2)
    print("Le carré de", nombre, "est égal à", nombre * nombre)
    forward(nombre)
    left(nombre)
    back(nombre)
    print("Il y a", nombre, "cotés dans cette figure")



#close()        
compte_nombres()

    





