#mechant

import random

#Créer des vagues de méchants aléatoirement
#[Nom, Attaque, vie]
def creation_vague_mechants(vague):
    types_mechants = ["troll", "orc", "gobelin", "squelette"]
    mechants_vague = []
    if vague < 4:
        for i in range(2 + vague):
            type_mechant = random.choice(types_mechants)
            if type_mechant == "troll":
                mechants_vague.append(["troll", 4, 5])
            elif type_mechant == "orc":
                mechants_vague.append(["orc", 5, 10])
            elif type_mechant == "gobelin":
                mechants_vague.append(["gobelin", 3, 7])
            elif type_mechant == "squelette":
                mechants_vague.append(["squelette", 12, 2])
    else:
        mechants_vague.append(["dragon", 6, 15])
    return mechants_vague


#Afficher la liste des méchants en vie
def afficher_liste_mechants(mechant_Vague):
    print("Liste des méchants en vie:")
    print("+---+------------+-------+")
    print("| # |    Nom     |  PV   |")
    print("+---+------------+-------+")
    for i, mech in enumerate(mechant_Vague): #Permet de retourner un tuple 
        print(f"| {i} | {mech[0]:^10} | {mech[2]:^5} |") #Retourne un tableau commençant par 0 avec le nom des méchants en vie et leur pv
    print("+---+------------+-------+")

