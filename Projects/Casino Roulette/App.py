import random

# Définition des couleurs pour chaque numéro
def get_color(number):
    if number == 0:
        return "Vert"
    elif number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        return "Rouge"
    else:
        return "Noir"

def get_colonne(number):
    if number == 0:
        return None
    elif number % 3 == 1:
        return 1
    elif number % 3 == 2:
        return 2
    else:
        return 3

# Fonction pour faire tourner la roulette
def tourner_roulette(pari_type, mise, capital, details):
    numero = random.randint(0, 36)
    couleur = get_color(numero)
    print(f"\n🎯 La bille est tombée sur : {numero} ({couleur})")

    gain = 0

    if pari_type == "plein":
        if numero == details[0]:
            gain = mise * 35

    elif pari_type == "cheval":
        if numero in details:
            gain = mise * 17

    elif pari_type == "carré":
        if numero in details:
            gain = mise * 8

    elif pari_type == "sixain":
        if numero in details:
            gain = mise * 5

    elif pari_type == "colonne":
        if get_colonne(numero) == details[0]:
            gain = mise * 2

    elif pari_type == "douzaine":
        if numero in range(details[0], details[0] + 12):
            gain = mise * 2

    elif pari_type == "couleur":
        if couleur.lower() == details[0]:
            gain = mise * 2

    elif pari_type == "pair_impair":
        if numero != 0 and numero % 2 == details[0]:
            gain = mise * 2

    capital += gain - mise
    if gain > 0:
        print(f"💰 Bravo ! Vous avez gagné {gain}€ !")
    else:
        print(f"❌ Désolé, vous avez perdu {mise}€.")

    print(f"💼 Capital restant : {capital}€\n")
    return capital

def demander_pari():
    print("\nTypes de mise disponibles :")
    print("1 - Plein (un seul numéro)")
    print("2 - Cheval (2 numéros côte à côte)")
    print("3 - Carré (4 numéros en carré)")
    print("4 - Sixain (6 numéros en deux lignes)")
    print("5 - Colonne (1ère, 2ème ou 3ème)")
    print("6 - Douzaine (1-12, 13-24, 25-36)")
    print("7 - Couleur (rouge ou noir)")
    print("8 - Pair / Impair")

    choix = input("Entrez le numéro correspondant au type de mise : ")

    if choix == "1":
        num = int(input("Numéro entre 0 et 36 : "))
        return "plein", [num]
    
    elif choix == "2":
        a = int(input("Premier numéro (entre 1 et 35, pas 0 ou multiples de 3 sauf 33) : "))
        if a == 0 or a == 36 or a % 3 == 0:
            print("Mise cheval invalide.")
            return None, None
        return "cheval", [a, a + 1]
    
    elif choix == "3":
        a = int(input("Numéro en haut à gauche du carré (ex: 1 donne carré [1,2,4,5]) : "))
        if a % 3 == 0 or a > 32:
            print("Carré impossible à cette position.")
            return None, None
        return "carré", [a, a + 1, a + 3, a + 4]
    
    elif choix == "4":
        a = int(input("Premier numéro du sixain (ex: 1 -> [1,2,3,4,5,6]) : "))
        if a < 1 or a > 31 or a % 3 != 1:
            print("Sixain invalide.")
            return None, None
        return "sixain", list(range(a, a + 6))

    elif choix == "5":
        col = int(input("Colonne (1, 2 ou 3) : "))
        if col not in [1, 2, 3]:
            return None, None
        return "colonne", [col]

    elif choix == "6":
        debut = int(input("Entrez 1 pour 1-12, 13 pour 13-24, 25 pour 25-36 : "))
        if debut not in [1, 13, 25]:
            return None, None
        return "douzaine", [debut]

    elif choix == "7":
        couleur = input("Rouge ou Noir ? ").lower()
        if couleur not in ["rouge", "noir"]:
            return None, None
        return "couleur", [couleur]

    elif choix == "8":
        paire = input("Pair ou Impair ? ").lower()
        if paire == "pair":
            return "pair_impair", [0]
        elif paire == "impair":
            return "pair_impair", [1]
        else:
            return None, None

    else:
        print("Choix invalide.")
        return None, None

# Programme principal
if __name__ == "__main__":
    capital = 100
    print("🎰 Bienvenue à la roulette ! Vous commencez avec 100€.")

    while capital > 0:
        pari_type, details = demander_pari()
        if pari_type is None:
            continue

        try:
            mise = int(input(f"Combien voulez-vous miser ? (Capital : {capital}€) : "))
            if mise <= 0 or mise > capital:
                print("Mise invalide.")
                continue
        except ValueError:
            print("Veuillez entrer une somme valide.")
            continue

        input("Appuyez sur Entrée pour lancer la roulette...")
        capital = tourner_roulette(pari_type, mise, capital, details)

        if capital <= 0:
            print("💸 Vous avez perdu tout votre argent. Fin de la partie.")
            break

        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != 'o':
            print(f"🏁 Fin de la partie. Capital final : {capital}€")
            break
