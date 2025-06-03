import tkinter as tk
from tkinter import messagebox
import random

def get_color(number):
    if number == 0:
        return "Vert"
    elif number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        return "Rouge"
    else:
        return "Noir"

def tourner_roulette(pari_type, mise, capital, details):
    numero = random.randint(0, 36)
    couleur = get_color(numero)
    resultat = f"La bille est tombée sur : {numero} ({couleur})\n"

    gain = 0

    if pari_type == "plein":
        # details = liste de numéros joués
        if numero in details:
            # Chaque numéro misé paie 35 fois la mise / nombre de numéros joués
            # On peut faire la mise totale répartie ou la mise par numéro ?
            # Ici on considère la mise totale répartie uniformément
            gain = mise * 35 / len(details)

    elif pari_type == "couleur":
        if couleur.lower() == details[0]:
            gain = mise * 2

    elif pari_type == "pair":
        if numero != 0 and numero % 2 == 0:
            gain = mise * 2

    elif pari_type == "impair":
        if numero != 0 and numero % 2 == 1:
            gain = mise * 2

    capital += gain - mise

    if gain > 0:
        resultat += f"Bravo ! Vous avez gagné {gain:.2f}€ !\n"
    else:
        resultat += f"Désolé, vous avez perdu {mise}€.\n"

    resultat += f"Capital restant : {capital:.2f}€"
    return capital, resultat

class RouletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roulette Casino")
        self.capital = 100

        self.label_capital = tk.Label(root, text=f"Capital : {self.capital}€")
        self.label_capital.pack()

        self.pari_type_var = tk.StringVar(value="plein")
        self.entry_details = tk.Entry(root)
        self.entry_mise = tk.Entry(root)

        self.setup_interface()

    def setup_interface(self):
        tk.Label(self.root, text="Type de mise :").pack()
        options = ["plein", "couleur", "pair", "impair"]
        tk.OptionMenu(self.root, self.pari_type_var, *options).pack()

        tk.Label(self.root, text="Détails du pari :\n"
                                 "- Pour 'plein' : entrez un ou plusieurs numéros séparés par des virgules (ex: 7,13,25)\n"
                                 "- Pour 'couleur' : rouge ou noir\n"
                                 "- Pour 'pair' ou 'impair' : laissez vide").pack()
        self.entry_details.pack()

        tk.Label(self.root, text="Mise en € :").pack()
        self.entry_mise.pack()

        tk.Button(self.root, text="Jouer", command=self.jouer).pack(pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def jouer(self):
        try:
            mise = float(self.entry_mise.get())
            if mise <= 0 or mise > self.capital:
                raise ValueError("Mise invalide.")
        except ValueError:
            messagebox.showerror("Erreur", "Entrez une mise valide.")
            return

        pari_type = self.pari_type_var.get()
        raw_details = self.entry_details.get().strip().lower()

        try:
            if pari_type == "plein":
                if not raw_details:
                    raise ValueError("Entrez au moins un numéro.")
                details = [int(x) for x in raw_details.split(",")]
                for num in details:
                    if num < 0 or num > 36:
                        raise ValueError("Numéro de plein invalide.")
            elif pari_type == "couleur":
                if raw_details not in ["rouge", "noir"]:
                    raise ValueError("Couleur invalide.")
                details = [raw_details]
            elif pari_type in ["pair", "impair"]:
                # Pas besoin de détails
                details = []
            else:
                raise ValueError()
        except:
            messagebox.showerror("Erreur", "Détails du pari invalides.")
            return

        self.capital, resultat = tourner_roulette(pari_type, mise, self.capital, details)
        self.label_capital.config(text=f"Capital : {self.capital:.2f}€")
        self.result_label.config(text=resultat)

        if self.capital <= 0:
            messagebox.showinfo("Fin", "Vous avez perdu tout votre argent.")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RouletteApp(root)
    root.mainloop()
