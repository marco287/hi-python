import random

MOTS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
mot = random.choice(MOTS)
mot_choisi = mot
mot_masque = mot_choisi[0:-1]+"_"
chance=3
while chance>0:
  
    print(f"Le mot choisi est  {mot_masque} ") 
    devinette=input("Trouver la derniere lettre: ")
 
    if (devinette == mot_choisi[-1]):
        print("Bravo! Vous avez bien trouve la lettre qui termine cette phrase")
        break
     
    else:
    
        chance-=1
        print(f"desole vous avez perdu , il vous reste {chance} chance(s)")
        

    
    