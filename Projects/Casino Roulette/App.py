import random

# Définition des couleurs pour chaque numéro
def get_color(number):
    if number == 0:
        return "Vert"
    elif number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        return "Rouge"
    else:
        return "Noir"

# Fonction pour faire tourner la roulette
def tourner_roulette():
    numero = random.randint(0, 36)
    couleur = get_color(numero)
    print(f"La bille est tombée sur : {numero} ({couleur})")

# Lancer le programme
if __name__ == "__main__":
    while True:
        input("Appuie sur Entrée pour faire tourner la roulette...")
        tourner_roulette()
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != 'o':
            print("Merci d'avoir joué !")
            break

