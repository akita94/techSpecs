import platform
import psutil
import subprocess
import tkinter as tk
from tkinter import ttk

def get_system_info():
    system_info = {}

    # Informations sur le système d'exploitation
    system_info['Système'] = platform.system()
    system_info['Version'] = platform.release()
    system_info['Version détaillée'] = platform.version()

    # Informations sur le processeur
    system_info['Processeur'] = platform.processor()
    system_info['Architecture'] = platform.machine()
    freq = psutil.cpu_freq()
    system_info['Fréquence maximale'] = f"{freq.max / 1000:.2f} GHz"
    system_info['Fréquence actuelle'] = f"{freq.current / 1000:.2f} GHz"
    system_info['Cœurs physiques'] = psutil.cpu_count(logical=False)
    system_info['Cœurs logiques'] = psutil.cpu_count(logical=True)

    # Informations sur la mémoire vive (RAM)
    mem = psutil.virtual_memory()
    system_info['RAM totale'] = f"{mem.total / (1024 ** 3):.2f} GB"
    system_info['RAM disponible'] = f"{mem.available / (1024 ** 3):.2f} GB"

    # Informations sur le disque dur
    try:
        disk_info = psutil.disk_usage('/')
        system_info['Espace disque total'] = f"{disk_info.total / (1024 ** 3):.2f} GB"
        system_info['Espace disque utilisé'] = f"{disk_info.used / (1024 ** 3):.2f} GB"
        system_info['Espace disque libre'] = f"{disk_info.free / (1024 ** 3):.2f} GB"
        system_info['Utilisation du disque'] = f"{disk_info.percent}%"
    except:
        system_info['Espace disque total'] = "Non disponible"
        system_info['Espace disque utilisé'] = "Non disponible"
        system_info['Espace disque libre'] = "Non disponible"
        system_info['Utilisation du disque'] = "Non disponible"

    # Informations sur l'alimentation (PSU)
    system_info['Alimentation'] = "550W"

    # Informations sur le refroidissement du processeur
    system_info['Refroidissement CPU'] = "Air Cooler"

    # Informations sur la carte mère
    try:
        if platform.system() == "Windows":
            cmd = "wmic baseboard get product"
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            system_info['Carte mère'] = result.stdout.strip()
        else:
            system_info['Carte mère'] = "Non disponible sur ce système"
    except Exception as e:
        print(f"Erreur lors de la récupération de la carte mère : {e}")
        system_info['Carte mère'] = "Non disponible"

    # Informations sur la carte graphique (GPU)
    try:
        if platform.system() == "Windows":
            cmd = "wmic path win32_videocontroller get caption"
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            system_info['Carte graphique'] = result.stdout.strip()
        else:
            system_info['Carte graphique'] = "Non disponible sur ce système"
    except Exception as e:
        print(f"Erreur lors de la récupération de la carte graphique : {e}")
        system_info['Carte graphique'] = "Non disponible"

    # Informations sur le système d'exploitation
    system_info['Build du système'] = platform.platform()
    system_info['Mises à jour installées'] = "Non disponible"

    return system_info

def display_system_info():
    system_info = get_system_info()

    root = tk.Tk()
    root.title("Informations système")

    # Définition des couleurs personnalisées
    bg_color = "#1f1f23"  # Couleur de fond
    fg_color = "#ffffff"  # Couleur du texte
    detail_bg_color = "#2c2c32"  # Couleur de fond pour les détails
    bd_color = "#ffffff"  # Couleur de la bordure

    # Configuration de la fenêtre principale
    root.configure(bg=bg_color)

    # Frame pour le titre
    title_frame = ttk.Frame(root, padding="10", style="Title.TFrame")
    title_frame.pack(fill=tk.BOTH)

    description_label = ttk.Label(title_frame, text="Informations système", font=("Arial", 16, "bold"), style="Title.TLabel")
    description_label.pack()

    # Frame pour les détails
    detail_frame = ttk.Frame(root, padding="20", style="Details.TFrame", borderwidth=2, relief="solid")
    detail_frame.pack(fill=tk.BOTH, expand=True)

    # Définition du style pour les cadres et étiquettes
    ttk.Style().configure("Title.TFrame", background=bg_color)
    ttk.Style().configure("Title.TLabel", background=bg_color, foreground=fg_color, font=("Arial", 16, "bold"))
    ttk.Style().configure("Details.TFrame", background=detail_bg_color, bordercolor=bd_color)
    ttk.Style().configure("Details.TLabel", background=detail_bg_color, foreground=fg_color, font=("Arial", 12))

    row = 0
    for key, value in system_info.items():
        label_key = ttk.Label(detail_frame, text=key, font=("Arial", 12, "bold"))
        label_key.grid(row=row, column=0, sticky='w', padx=10, pady=5)

        label_value = ttk.Label(detail_frame, text=value, font=("Arial", 12))
        label_value.grid(row=row, column=1, sticky='w', padx=10, pady=5)

        row += 1

    root.mainloop()

if __name__ == "__main__":
    display_system_info()
