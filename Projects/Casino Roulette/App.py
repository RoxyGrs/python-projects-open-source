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
def tourner_roulette(pari, mise, capital):
    numero = random.randint(0, 36)
    couleur = get_color(numero)
    print(f"\n La bille est tombée sur : {numero} ({couleur})")

    if numero == pari:
        gain = mise * 35
        capital += gain
        print(f" Bravo ! Vous avez gagné {gain}€ !")
    else:
        capital -= mise
        print(f" Désolé, vous avez perdu {mise}€.")

    print(f" Capital restant : {capital}€\n")
    return capital

# Lancer le programme
if __name__ == "__main__":
    capital = 100

    print(" Bienvenue à la roulette ! Vous commencez avec 100€.\n")

    while capital > 0:
        try:
            pari = int(input("Choisissez un chiffre entre 0 et 36 : "))
            if pari < 0 or pari > 36:
                print("Veuillez entrer un chiffre valide entre 0 et 36.")
                continue
        except ValueError:
            print("Entrée invalide. Veuillez entrer un chiffre.")
            continue

        try:
            mise = int(input(f"Combien voulez-vous miser ? (Capital : {capital}€) : "))
            if mise <= 0 or mise > capital:
                print("Mise invalide. Elle doit être supérieure à 0 et inférieure ou égale à votre capital.")
                continue
        except ValueError:
            print("Entrée invalide. Veuillez entrer une somme d'argent.")
            continue

        input("Appuyez sur Entrée pour faire tourner la roulette...")
        capital = tourner_roulette(pari, mise, capital)

        if capital <= 0:
            print(" Vous avez perdu tout votre argent. Fin de la partie.")
            break

        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != 'o':
            print(f" Fin de la partie. Capital final : {capital}€")
            break
