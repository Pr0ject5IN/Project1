import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial

port = "COM3"
baud = 9600
s = serial.Serial(port)
s.baudrate = baud

# Créer la fenêtre principale
root = tk.Tk()
root.title("MICRO:BIT")

# Définir la taille de la fenêtre
root.geometry("300x200")

# Variable pour suivre le bouton sélectionné
selected_button =0

# Liste des boutons
buttons = []

# Créer les boutons avec du texte
# Importation des bibliothèques nécessaires
import tkinter as tk
import serial

# Initialisation de l'interface graphique Tkinter
root = tk.Tk()
root.title("Interface de contrôle avec micro:bit")

# Initialisation des variables
buttons = []                                                                     # Liste pour stocker les boutons
selected_button = 0                                                              # Index du bouton  sélectionné

# Création de 20 boutons dynamiquement
for i in range(1, 21):
    button = tk.Button(root, text=f"Bouton {i}")                                 # Création d'un bouton
    button.pack(pady=5)                                                          # Ajout du bouton vertical
    buttons.append(button)                                                       # Ajout du bouton à la liste des boutons

# Fonction pour mettre à jour l'apparence des boutons en fonction de la sélection
def update_selection():
    for i, button in enumerate(buttons):                                         # Parcourir tous les boutons avec leur index
        if i == selected_button:                                                 # Si "i" correspond au bouton sélectionné
            button.config(bg="yellow")                                           # Mettre le bouton sélectionné en jaune
        else:
            button.config(bg="SystemButtonFace")                                 # Réinitialiser la couleur des boutons

# Fonction pour lire les données de la micro:bit
def read_microbit():
    global selected_button                                                       # Utiliser la variable globale pour suivre le bouton sélectionné
    if s.in_waiting > 0:                                                         # Vérifier si des données sont disponibles
        data = s.read()                                                          # Lire une donnée depuis la micro:bit
        try:
            data = data.decode('utf-8')                                          # Décoder les données en UTF-8
            if data == 'A':                                                      # Si gata est 'A'
                selected_button = (selected_button + 1) % len(buttons)           # Sélectionner le bouton suivant
            elif data == 'B':                                                    # Si data est 'B'
                selected_button = (selected_button - 1) % len(buttons)           # Sélectionner le bouton précédent
            elif data == 'logo':                                                 # Si data est 'logo'
                buttons[selected_button].config(bg="blue")                       # Changer la couleur du bouton sélectionné en bleu
                buttons[selected_button].event_generate("<Button-1>")            # Simuler un clic sur le bouton  (ca marche pas encore correctement)
            update_selection()                                                   # Mettre à jour les boutons
        except UnicodeDecodeError:
            pass                                                                 # Ignorer les données invalides
    root.after(100, read_microbit)                                               # toutes les 100ms

# Lancer la lecture des données de la micro:bit
root.after(100, read_microbit)

# Lancer la boucle principale de l'interface graphique Tkinter
root.mainloop()
