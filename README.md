<button onclick="copyToClipboard(`# TechSpecs Tracker

TechSpecs Tracker est une application Python GUI qui affiche les informations détaillées du système sur lequel elle est exécutée. L'application utilise Tkinter pour l'interface utilisateur et des modules comme platform et psutil pour récupérer et afficher les informations système.

`)">Copier le titre</button>

<button onclick="copyToClipboard(`## Fonctionnalités

Affiche les informations sur le système d'exploitation (nom, version, architecture).
Affiche les détails du processeur (modèle, fréquence, nombre de cœurs).
Affiche les informations sur la mémoire vive (RAM).
Affiche les détails du disque dur (espace total, utilisé, libre, pourcentage d'utilisation).
Affiche les informations sur l'alimentation (PSU) (simulées).
Affiche les détails du refroidissement du processeur (simulés).
Affiche les détails de la carte mère (sur Windows uniquement, utilisant WMIC).
Affiche les détails de la carte graphique (sur Windows uniquement, utilisant WMIC).
Affiche les détails du système d'exploitation (nom de build, mises à jour installées).
`)">Copier les fonctionnalités</button>

<button onclick="copyToClipboard(`## Prérequis

Python 3.x installé sur votre système.
Les modules suivants doivent être installés :
`psutil`
`tkinter` (normalement inclus avec Python)
`)">Copier les prérequis</button>

<button onclick="copyToClipboard(`## Installation et Utilisation

Cloner le dépôt :
```bash
git clone https://github.com/votre-utilisateur/TechSpecs-Tracker.git
cd TechSpecs-Tracker
```

Installer les dépendances :
Assurez-vous que les modules requis sont installés :
```bash
pip install psutil
```

Lancer l'application :
```bash
python TechSpecs.py
```

Utilisation :
Une fois l'application lancée, elle affichera les détails du système dans une interface utilisateur conviviale.

`)">Copier l'installation et l'utilisation</button>

<button onclick="copyToClipboard(`## Auteur

Ajoutez vos informations d'auteur ici.

`)">Copier l'auteur</button>

<button onclick="copyToClipboard(`## Licence

Ce projet est sous licence MIT.

`)">Copier la licence</button>

<script>
function copyToClipboard(text) {
  const el = document.createElement('textarea');
  el.value = text;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
  alert('Copié !');
}
</script>
