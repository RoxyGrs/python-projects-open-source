import tkinter as tk
from tkinter import messagebox, font
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
        if numero in details:
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
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f4f8")

        self.capital = 100

        self.custom_font = font.Font(family="Helvetica", size=12)
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")

        self.label_title = tk.Label(root, text="🎰 Roulette Casino 🎰", font=self.title_font, bg="#f0f4f8", fg="#2c3e50")
        self.label_title.pack(pady=15)

        self.label_capital = tk.Label(root, text=f"Capital : {self.capital}€", font=self.custom_font, bg="#f0f4f8", fg="#34495e")
        self.label_capital.pack(pady=5)

        self.pari_type_var = tk.StringVar(value="plein")

        # Frame pour le choix des options
        frame_options = tk.Frame(root, bg="#f0f4f8")
        frame_options.pack(pady=10, fill="x", padx=30)

        tk.Label(frame_options, text="Type de mise :", font=self.custom_font, bg="#f0f4f8", fg="#34495e").grid(row=0, column=0, sticky="w")
        options = ["plein", "couleur", "pair", "impair"]
        self.option_menu = tk.OptionMenu(frame_options, self.pari_type_var, *options, command=self.on_pari_change)
        self.option_menu.config(font=self.custom_font, bg="white")
        self.option_menu.grid(row=0, column=1, sticky="ew", padx=10)

        tk.Label(frame_options, text="Détails du pari :", font=self.custom_font, bg="#f0f4f8", fg="#34495e").grid(row=1, column=0, sticky="w", pady=8)
        self.entry_details = tk.Entry(frame_options, font=self.custom_font)
        self.entry_details.grid(row=1, column=1, sticky="ew", padx=10)
        frame_options.columnconfigure(1, weight=1)

        tk.Label(root, text="Mise en € :", font=self.custom_font, bg="#f0f4f8", fg="#34495e").pack(anchor="w", padx=30, pady=(15, 5))
        self.entry_mise = tk.Entry(root, font=self.custom_font)
        self.entry_mise.pack(fill="x", padx=30)

        self.btn_jouer = tk.Button(root, text="Jouer", font=self.custom_font, bg="#27ae60", fg="white", activebackground="#2ecc71", command=self.jouer)
        self.btn_jouer.pack(pady=20, ipadx=10, ipady=5)

        self.result_label = tk.Label(root, text="", font=self.custom_font, bg="#f0f4f8", fg="#2c3e50", wraplength=350, justify="left")
        self.result_label.pack(padx=30, pady=10)

        self.on_pari_change(self.pari_type_var.get())  # Pour gérer la désactivation de details au démarrage

    def on_pari_change(self, value):
        if value in ["pair", "impair"]:
            self.entry_details.delete(0, tk.END)
            self.entry_details.config(state="disabled")
        else:
            self.entry_details.config(state="normal")

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
                details = []
            else:
                raise ValueError()
        except Exception as e:
            messagebox.showerror("Erreur", f"Détails du pari invalides.\n{e}")
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
