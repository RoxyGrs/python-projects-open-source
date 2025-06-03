import random

def get_color(number):
    if number == 0:
        return "Vert"
    elif number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        return "Rouge"
    else:
        return "Noir"

def tourner_roulette():
    numero = random.randint(0, 36)
    couleur = get_color(numero)
    print(f"\ La bille est tombée sur : {numero} ({couleur})")
    return numero

def calcul_gain(type_pari, mise, numeros_pari, numero_gagnant):
    if numero_gagnant in numeros_pari:
        if type_pari == "plein":
            return mise * 35
        elif type_pari == "cheval":
            return mise * 17
        elif type_pari == "carre":
            return mise * 8
        elif type_pari == "sixain":
            return mise * 5
        elif type_pari in ["double_colonne", "double_douzaine"]:
            return mise * 2
    return -mise

def saisir_numeros(type_pari):
    try:
        if type_pari == "plein":
            n = int(input("Entrez un numéro entre 0 et 36 : "))
            return [n] if 0 <= n <= 36 else []
        elif type_pari == "cheval":
            nums = list(map(int, input("Entrez 2 numéros séparés par un espace : ").split()))
            return nums if len(nums) == 2 else []
        elif type_pari == "carre":
            nums = list(map(int, input("Entrez 4 numéros séparés par un espace : ").split()))
            return nums if len(nums) == 4 else []
        elif type_pari == "sixain":
            nums = list(map(int, input("Entrez 6 numéros séparés par un espace : ").split()))
            return nums if len(nums) == 6 else []
        elif type_pari == "double_colonne":
            choix = input("Choisissez : '1-12 et 13-24' ou '13-24 et 25-36' : ")
            if choix == "1-12 et 13-24":
                return list(range(1, 25))
            elif choix == "13-24 et 25-36":
                return list(range(13, 37))
        elif type_pari == "double_douzaine":
            choix = input("Choisissez : '1-18 et 19-36' : ")
            if choix == "1-18 et 19-36":
                return list(range(1, 37))
    except:
        pass
    return []

# Lancer le programme
if __name__ == "__main__":
    capital = 100
    print(" Bienvenue à la roulette ! Vous commencez avec 100€.\n")

    types_paris = ["plein", "cheval", "carre", "sixain", "double_colonne", "double_douzaine"]

    while capital > 0:
        print(" Types de paris disponibles :", ", ".join(types_paris))
        type_pari = input("Choisissez un type de pari : ").lower()

        if type_pari not in types_paris:
            print(" Type de pari invalide.\n")
            continue

        numeros_pari = saisir_numeros(type_pari)
        if not numeros_pari:
            print(" Nombres invalides pour ce type de pari.\n")
            continue

        try:
            mise = int(input(f"Combien voulez-vous miser ? (Capital : {capital}€) : "))
            if mise <= 0 or mise > capital:
                print(" Mise invalide.\n")
                continue
        except ValueError:
            print(" Entrée invalide pour la mise.\n")
            continue

        input(" Appuyez sur Entrée pour faire tourner la roulette...")
        numero_gagnant = tourner_roulette()
        gain = calcul_gain(type_pari, mise, numeros_pari, numero_gagnant)
        capital += gain

        if gain > 0:
            print(f" Bravo ! Vous avez gagné {gain}€ !")
        else:
            print(f" Vous avez perdu {mise}€.")

        print(f" Capital restant : {capital}€\n")

        if capital <= 0:
            print(" Vous avez perdu tout votre argent. Fin de la partie.")
            break

        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != 'o':
            print(f" Fin de la partie. Capital final : {capital}€")
            break
