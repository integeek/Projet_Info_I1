#Main

import config as C
import mechant as M
import heros as H


print("Bienvenue dans le jeu !")
print("Voici les règles du jeu :")
C.afficher_regles()
liste_heros = H.difficulte()

vague = 1
relancer = 1

relancer = True
while relancer == True :

    while vague <  4:
        print("La vague actuelle est la vague : ",vague) #affiche la vague actuelle
        mechant_Vague = M.creation_vague_mechants(vague)

        while len(liste_heros) > 0 and len(mechant_Vague) > 0: #continue tant qu'il reste des héros ou des mechants
            H.afficher_liste_heros(liste_heros)
            M.afficher_liste_mechants(mechant_Vague)

            choix_heros = input("Qui voulez vous choisir ? Guerrier, Chasseur, Guerisseur ou Mage? ") #Choix de qui utiliser
            while choix_heros not in liste_heros : 
                print("Veuillez réécrire votre personnage")
                choix_heros = input("Qui voulez vous choisir ? Guerrier, Chasseur, Guerisseur ou Mage ? ") #Si le joueur à mal écrit son personnage
                
            if choix_heros == 'Guerisseur' : 
                action = input('Que voulez vous faire ? Attaquer (A), Potions (P) ou Soigner (S) ') #Si le joueur à mal écrit son action
                while action != 'A' and action != 'S' and action!= 'P' :  
                    print("Veuillez réécrire votre action")
                    action = input('Que voulez vous faire ? Attaquer (A), Potions (P) ou Soigner (S) ') #Si le joueur à mal écrit son action
            
                if action == 'A' : 
                    choix_mechant = int(input('Qui voulez vous attaquer ? Entrez le numéro du mechant : '))
                    C.combat(choix_heros,choix_mechant,mechant_Vague,liste_heros)
                elif action == 'S':
                    choix = input("Qui voulez vous soigner? Guerrier, Chasseur, Guerisseur ou Mage? ") #Choix de qui soigner
                    C.soigner(liste_heros,choix)
                elif action == 'p' :
                    C.potions(liste_heros, choix_heros)

            else : #Si le héros n'est pas le Guerisseur 
                choix = input("Que voulez vous faire? Attaquer (A) ou Potions (P) ")
                while choix!= 'A' and choix!= 'P' :
                    print("Veuillez réécrire votre action")
                    choix = input('Que voulez vous faire ? Attaquer (A) ou Potions (P) ') #Si le joueur à mal écrit son action
                if choix == 'A' : 
                    choix_mechant = int(input('Qui voulez vous attaquer ? Entrez le numéro du mechant : '))
                    C.combat(choix_heros,choix_mechant,mechant_Vague,liste_heros)
                elif choix == 'P' :
                    C.potions(liste_heros, choix_heros)
        # gestion des pièges
        if C.generer_piege():
            print("Attention ! Un piège a été déclenché !")
            C.degats_piege(liste_heros)
        if C.generer_fontaine():
            print("Vous avez trouvé une fontaine ! Chaque héros regagne 3 PV")
            C.fontaine(liste_heros)
        vague +=1
        liste_heros['Chasseur'][3]=5 #réinitialiser les flèches du Chasseur
            
    if vague == 4: #Combat final par Shu-Han
        vague_actuel = M.creation_vague_mechants(vague) #[["dragon",6,15]]
        dragon_vie = vague_actuel[0][2]

        print("----------Combat final----------")
        C.combat_boss(dragon_vie,liste_heros)

    demande = str(input("Rejouer? Entrez oui ou non."))
    if demande == 'oui':
        relancer = True
        vague = 1
    else:
        relancer = False
