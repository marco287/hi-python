import random
def ordinateur():
    
    INTERVAL_MAX=11
    INTERVAL_MIN=1
    choix_aleatoire=random.randrange(INTERVAL_MIN,INTERVAL_MAX)
    return choix_aleatoire

def utilisateur():
    a=int(input("Devine le nombre: "))
    return a

def comparaison(nbr1,nbr2):
    if (nbr1==nbr2):
        print("Vous avez gagne")
    else:  
        print("Vous avez perdu") 

nombre_recherche=ordinateur()
while True:
    essai=utilisateur()
    comparaison(nombre_recherche,essai)
    q= input("Voulez vous rejouer(o/n)?")
    if q=="n":
        break


        