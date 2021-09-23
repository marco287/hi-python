from random import *

INTERVAL_MAX=11
INTERVAL_MIN=1
choix_aleatoire=randrange(INTERVAL_MIN,INTERVAL_MAX)
while True:
    
    nb_utilisateur = int(input("Devine le nombre "))
    if choix_aleatoire<nb_utilisateur:
        print("Le nombre recherche est inferieur")
        
    elif choix_aleatoire>nb_utilisateur:
        print("Le nombre recherche est superieur")  
         
    else:
        print("Bravo, vous avez reussi") 
        break     