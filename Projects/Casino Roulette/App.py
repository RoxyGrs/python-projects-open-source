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
def tourner_roulette(pari):
    numero = random.randint(0, 36)
    couleur = get_color(numero)
    print(f"La bille est tombée sur : {numero} ({couleur})")
    if numero == pari:
        print("🎉 Félicitations ! Vous avez gagné !")
    else:
        print("😞 Perdu, réessayez !")

# Lancer le programme
if __name__ == "__main__":
    while True:
        try:
            pari = int(input("Choisissez un chiffre entre 0 et 36 : "))
            if pari < 0 or pari > 36:
                print("Veuillez entrer un chiffre valide entre 0 et 36.")
                continue
        except ValueError:
            print("Entrée invalide. Veuillez entrer un chiffre.")
            continue

        input("Appuie sur Entrée pour faire tourner la roulette...")
        tourner_roulette(pari)
        
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != 'o':
            print("Merci d'avoir joué !")
            break
