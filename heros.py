#heros

def difficulte():
    print("Tout d'abord choisissez votre niveau de difficulté : facile (1), difficile (2) ou élevé (3)")
    difficulte = input("Entrez votre niveau de difficulté : ")
    while difficulte!= '1' and difficulte!= '2' and difficulte!= '3' and difficulte!= '4':
        difficulte = input("Entrez votre niveau de difficulté : ")

    #[vie, attaque, soin, potions] pour le chasseur il a des fleches
    if difficulte == '1' : #Facile
            liste_heros={
                'Guerrier':[16,10,0,3],
                'Chasseur':[20,6,0,10,3],
                'Guerisseur':[20,2,4,3],
                'Mage':[20,8,0,3]
            }
    elif difficulte == '2' : #normal
        liste_heros={
            'Guerrier':[13,7,0,2],
            'Chasseur':[15,5,0,7,2],
            'Guerisseur':[15,1,3,2],
            'Mage':[15,6,0,2]
        }
    elif difficulte == '3' : #difficile
        liste_heros={
            'Guerrier':[8,5,0,1],
            'Chasseur':[10,3,0,5,1],
            'Guerisseur':[10,0,2,1,],
            'Mage':[10,4,0,1]
        }
    return liste_heros

#Afficher la liste des héros en vie
def afficher_liste_heros(liste_heros):
    print("Liste des héros en vie:")
    print("+---+-------------+-------+---------+---------+")
    print("| # |     Nom     |  PV   | Flèches | Potions |")
    print("+---+-------------+-------+---------+---------+")
    for i, (hero_name, hero_stats) in enumerate(liste_heros.items()):  
        if hero_name == "Chasseur": 
            print(f"| {i+1} | {hero_name:^10} | {hero_stats[0]:^5} | {hero_stats[3]:^7} | {hero_stats[4]:^7} |")
        else:
            print(f"| {i+1} | {hero_name:^10} | {hero_stats[0]:^5} |         | {hero_stats[3]:^7} |")
    print("+---+-------------+-------+---------+---------+")

