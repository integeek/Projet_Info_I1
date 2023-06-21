#config
import heros as H
from random import randint
import random

#Affiche les règles du jeu au début de la partie
def afficher_regles():
    print("============================ Règles du jeu ============================")
    print("Le but du jeu est de terrasser chaque vague d'ennemis aléatoire à chaque partie.")
    print("À chaque vague, vous devez vaincre les ennemis pour passer à la vague suivante.")
    print("Le jeu se termine si tous vos héros sont morts ou si vous arrivez à vaincre le dragon.")
    print("Vous pouvez utiliser différents types de héros pour combattre les ennemis :")
    print("   - Le Guerrier inflige de gros dégâts mais a peu de points de vie.")
    print("   - Le Mage peut lancer des sorts pour faire des dégats de zone.")
    print("   - Le Guerisseur peut soigner vos héros blessés.")
    print("   - Le Chasseur tire des flèches sur les ennemis mais en a un nombre limité.")
    print("Chaque héros à un nombre de potion selon la difficulté permettant de soigner 3 PV")
    print("Mais attention, votre quête ne sera pas de tout repos, des événements aléatoire peuvent survenir aléatoirement à la fin de chaque vague")
    print("Bon jeu et bon courage !")
    print("========================================================================")

def attaque_dragon(vengeance): #l'attaque du dragon
    if vengeance==1: #l'heros l'a attaqué
        attaque = randint(0,6)
    else: #l'heros ne l'a pas attaqué
        attaque = randint(0,2)
    return attaque

def combat_boss(dragon_vie,liste_heros):

    vie_dragon = dragon_vie

    while liste_heros!={}:
        H.afficher_liste_heros(liste_heros) #montrer la liste des heros disponible
        heros_choisi = input("Choisi ton heros ") 
        while heros_choisi not in liste_heros:
            heros_choisi = input("Ce hero n'existe pas, choisi ton heros ") 

        #Tour des heros ------------
        if heros_choisi == 'Guerisseur' : 
            action = input('Que voulez vous faire ? Attaquer (A), Potions (P) ou Soigner (S) ') #Si le joueur à mal écrit son action
            while action != 'A' and action != 'S' and action!= 'P' :  
                print("Veuillez réécrire votre action")
                action = input('Que voulez vous faire ? Attaquer (A), Potions (P) ou Soigner (S) ') #Si le joueur à mal écrit son action
        
            if action == 'A' : 
                vie_dragon -= attaque_heros(liste_heros,heros_choisi)
                print("Il reste",vie_dragon,"point de vie au dragon.","\n")
            elif action == 'S':
                choix = input("Qui voulez vous soigner? Guerrier, Chasseur, Guerisseur ou Mage? ") #Choix de qui soigner
                soigner(liste_heros,choix)
            elif action == 'p' :
                potions(liste_heros, heros_choisi)

        else : #Si le héros n'est pas le Guerisseur 
            choix = input("Que voulez vous faire? Attaquer (A) ou Potions (P) ")
            while choix!= 'A' and choix!= 'P' :
                print("Veuillez réécrire votre action")
                choix = input('Que voulez vous faire ? Attaquer (A) ou Potions (P) ') #Si le joueur à mal écrit son action
            if choix == 'A' : 
                vie_dragon -= attaque_heros(liste_heros,heros_choisi)
                print("Il reste",vie_dragon,"point de vie au dragon.","\n") 
            elif choix == 'P' :
                potions(liste_heros, heros_choisi)
        
        if vie_dragon <= 0:
            print("Le dragon est mort! Victoire!")
            break

        #Tour du dragon ------------------
        for i in liste_heros:
            if i==heros_choisi:
                vie_inflige = attaque_dragon(1) #le dragon se venge (1)
                liste_heros[heros_choisi][0] -= vie_inflige 
                print("Le dragon s'est vengé et a infligé",vie_inflige,"de dégats à",heros_choisi)
            else:
                vie_inflige = attaque_dragon(0) #le dragon ne se venge pas et fait un AOE (0)
                liste_heros[i][0] -= vie_inflige
                print("Le dragon a infligé",vie_inflige,"de dégats à",i)

        #pour eviter un changement de dictionnaire pendant l'iteration, on fait une liste temporaire 'temp' 
        temp=[]
        for j in liste_heros:
            if liste_heros[j][0]<=0:
                temp.append(j)

        for k in tuple(temp):
            print(k,"est mort")
            liste_heros.pop(k)

        if liste_heros == {}:
            print("Tous les héros sont morts!. Défaite!")
            break

        print(" -------------------------------------------------","\n","-------------------------------------------------")

def combat(current_hero,numero_mechant,mechant_Vague,liste_heros):
           
    if current_hero == "Mage": #Shu-han
        for i in range (len(mechant_Vague)):
            if i == numero_mechant: #si c'est le mechant choisi
                vie_inflige = randint(0,liste_heros['Mage'][1]) 
                mechant_Vague[i][2] -= vie_inflige
                print("Le mage a infligé",vie_inflige,"point de dégats au méchant",i)
            else:
                vie_inflige = randint(0,2)
                mechant_Vague[i][2] -= vie_inflige #cause 2 pts de degat max a tous les mechants
                print("Le mage a infligé",vie_inflige,"point de dégats au méchant",i)

    else:
        mechant_Vague[numero_mechant][2] -= attaque_heros(liste_heros,current_hero) #l'action de tous les autres heros a l'exception du mage

    #pour eviter un changement de dictionnaire pendant l'iteration due au mage, on fait une liste temporaire 'temp' 
    temp=[]
    for j in range(len(mechant_Vague)):
        if mechant_Vague[j][2]<=0: #si le mechant est mort
            temp.append(j)

    for k in reversed(tuple(temp)): #la boucle tourne a l'envers pour eviter de changer d'index lors de la supression des mechants
        print('Mechant',k,"est mort")
        mechant_Vague.pop(k)
    
    #méchant attaque
    if len(mechant_Vague) != 0:
        if current_hero=="Chasseur":
            atk = randint(0, mechant_Vague[numero_mechant][1]) - 2 #Le chasseur subit moins de dégats
        else:
            atk = randint(0, mechant_Vague[numero_mechant][1])
        liste_heros[current_hero][0] -= atk #méchant attaque
        print (mechant_Vague[numero_mechant][0]," a infligé ",atk," points de dégats à ",current_hero)

    if liste_heros[current_hero][0] <= 0: #si héros est mort
        del liste_heros[current_hero] # supprime héros
        print("Le héros est mort!")


#Gère l'attaque des héros
def attaque_heros(liste_heros,HeroChoisi):
    atk = 0
    if HeroChoisi=='Chasseur': #Jean
        if liste_heros['Chasseur'][3]>0:
            atk=randint(0,liste_heros[HeroChoisi][1])
            liste_heros['Chasseur'][3] -= 1
            print(HeroChoisi,"a infligé",atk,"points de dégats")
        else:
            atk=randint(0,1)
            print(HeroChoisi,"n'a plus de fleche, il a infligé",atk,"points de dégats")
    
    elif HeroChoisi == "Guerisseur":
        choix = input('Qui voulez vous soigner ? Guerrier, Chasseur, Guerisseur ou Mage? ')
        soigner(liste_heros,choix)
        atk = randint(0,1)
        print(HeroChoisi,"a infligé",atk,"points de dégats")
      
    else:
        atk=randint(0,liste_heros[HeroChoisi][1])
        print(HeroChoisi,"a infligé",atk,"points de dégats")    
    return (atk)

#Fonction pour que le guerisseur soigne un héros
def soigner(liste_heros, choix): 
    if 'Guerisseur' not in liste_heros: #Si le guerisseur est mort
        print("Le guerisseur est mort, vous ne pouvez pas soigner.")
    else:
        if choix not in liste_heros:
            print("Le héros n'existe pas.")
        else:
            liste_heros[choix][0] += 2 #Ajoute 2 PV 
            print("Le", choix, "a maintenant", liste_heros[choix][0], "points de vie.")

#Fonction pour soigner un héros avec des potions
def potions(liste_heros, choix):
    if choix == 'Chasseur': 
        if liste_heros['Chasseur'][4] > 0:
            liste_heros['Chasseur'][4] -= 1 #Supprime 1 potion
            liste_heros['Chasseur'][0] += 2 #Ajoute 2 PV
            print(choix, "a utilisé une potion et a récupéré 2 PV.")
        else:
            print(choix, "n'a plus de potions.")
    else :
        if liste_heros[choix][3] > 0:
            liste_heros[choix][0] += 3 #Ajoute 3 PV
            liste_heros[choix][3] -= 1 #Supprime 1 potion
            print(choix, "a utilisé une potion et a récupéré 3 PV.")
        else:
            print(choix, "n'a plus de potions.")


#Fonction pour générer ou non des pièges à la fin de la vague (1 chance sur 2)
def generer_piege():
    piege_present = random.choice([True, False])
    return piege_present

# fonction pour affecter aléatoirement des dégâts à chaque héros
def degats_piege(liste_heros):
    for heros in liste_heros.values(): #Pour chaque héros, inflige entre 0 et 2 points de dégats aléatoirement
        degats = random.randint(0, 2)
        heros[0] -= degats
        if heros[0] <= 0: #Si le héros n'a plus de vie
            print(f"{heros[0]} est mort à cause du piège !")
            del liste_heros[heros[0]]

#Fonction pour générer ou non une fontaine à la fin de la vague (1 chance sur 3)
def generer_fontaine():
    fontaine_present = random.choice([True, False,False])
    return fontaine_present

#genere la fontaine qui soigne 3 PV à chaque héros
def fontaine(liste_heros):
    for heros in liste_heros.values():
        soin = 3
        heros[0] += soin
    
def boutique(liste_heros):
    while True:
        print("Bienvenue dans la boutique ! Voici les produits en vente :\n")
        print("Produit           | Prix")
        print("------------------|-----")
        print("Potion de santé   | 4   ")
        print("Potion de force   | 6   ")
        acheter = input("Voulez-vous faire des achats ? (O ou N)").upper()
        if acheter == "O":
            for heros in liste_heros:
                if liste_heros[heros][4] >= 4:
                    choix = input(f"{heros}, voulez-vous acheter une potion de santé ? (O ou N)").upper() 
                    if choix == "O":
                        liste_heros[heros][4] -= 4
                        liste_heros[heros][3] += 1
            ok = input("Voulez-vous faire d'autres achats ? (O ou N)").upper()
            if ok == "N":
                break
        elif acheter == "N":
            break

            

