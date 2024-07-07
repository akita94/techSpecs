# TechSpecs Tracker

TechSpecs Tracker est une application GUI Python qui affiche des informations détaillées sur le système sur lequel elle s'exécute. L'application utilise Tkinter pour l'interface utilisateur et des modules tels que platform et psutil pour récupérer et afficher les informations système.

## Fonctionnalités

- Affiche des informations sur le système d'exploitation (nom, version, architecture).
- Affiche des détails sur le processeur (modèle, fréquence, nombre de cœurs).
- Affiche des informations sur la RAM (totale, disponible).
- Affiche des détails sur le disque dur (espace total, espace utilisé, espace libre, pourcentage d'utilisation).
- Affiche des informations sur l'alimentation (simulée).
- Affiche des détails sur le refroidissement du CPU (simulé).
- Affiche des détails sur la carte mère (uniquement sous Windows, en utilisant WMIC).
- Affiche des détails sur la carte graphique (uniquement sous Windows, en utilisant WMIC).
- Affiche des détails sur le système d'exploitation (nom de build, mises à jour installées).

## Prérequis

- Python 3.x installé sur votre système.
- Les modules suivants doivent être installés :
  - `psutil`
  - `tkinter` (généralement inclus avec Python)

## Installation et Utilisation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/yourusername/TechSpecs-Tracker.git
   cd TechSpecs-Tracker
