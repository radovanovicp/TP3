import random
import time

def jeu_combat():

    niveau_vie = 20
    des_joueur = random.randint(1,6)
    des_adversaire = random.randint(1,6)

    jeu = int(input("""
Que voulez-vous faire?:
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir une autre porte
3- Afficher les règles du jeu
4- Quitter la partie
                        """))
    if jeu == "3" :
        print("""
Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
 
La partie se termine lorsque les points de vie de l’usager tombent sous 0.
 
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
""")



    if jeu == "4":
        exit()

    if jeu == "1":
        print(f"Votre force est de {des_joueur}")
        time.sleep(0.5)
        print(f"Le force de votre adversaire est de {des_adversaire}")
        time.sleep(0.5)
        if des_joueur < des_adversaire:
            print("Vous avez perdu cette partie")
        if des_joueur > des_adversaire:
            print("Vous avez gagnez cette partie")

jeu_combat()