# rsw-simulation

Projet de simulation d'écran de blocage Windows écrit en Python.

## Description

Ce dépôt contient un script Python simple (`rsw.py`) imitant une attaque de type ransomware. Le script bloque certaines interactions clavier et propos une saisie de code pour «déverrouiller» l'écran.

> Ce projet est uniquement destiné à des fins pédagogiques et de démonstration. Il ne doit pas être utilisé pour nuire ou pour déployer des logiciels malveillants.

## Fonctionnalités

- Affiche une fenêtre plein écran sans bordure
- Bloque des raccourcis clavier courants tels que `Alt+F4`, `Escape`, `Ctrl+Q`, `Alt+Tab`, et d'autres
- Propose un champ de saisie pour un code d'accès
- Affiche un message de déblocage en cas de code correct
- Conserve un message d'avertissement et une fausse adresse de paiement

## Prérequis

- Python 3.x
- `tkinter` installé
- Ce script utilise des appels Windows via `ctypes`, il est donc prévu pour une exécution sous Windows.

## Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/jeanchristophe-Git/rsw-simulation.git
   cd rsw-simulation
   ```

2. Vérifier que Python 3 et `tkinter` sont disponibles :

   ```bash
   python --version
   python -c "import tkinter"
   ```

## Exécution

Lancer le script :

```bash
python rsw.py
```

### Code d'accès de démonstration

- `DEMO2026`

## Comportement

- Si le bon code est saisi, un message de succès apparaît et la fenêtre se ferme après 3 secondes.
- Si le code est incorrect, le champ est réinitialisé et un message d'erreur s'affiche.
- La fenêtre tente de bloquer les actions de l'utilisateur pour simuler une situation de verrouillage.

## Limitations

- Le blocage de touches via `ctypes.windll.user32.BlockInput(True)` est très agressif et peut rendre le système difficile à contrôler.
- Ce script n'est pas un ransomware réel et ne chiffre aucune donnée.
- Il sert uniquement à montrer une interface d'alerte et un mécanisme basique de blocage local.

## Avertissement

N'utilisez ce code que sur des machines de test et dans un cadre autorisé. Ne l'exécutez pas sur un système de production ou sur des ordinateurs qui ne vous appartiennent pas.

## Licence

Ce dépôt est libre d'utilisation à des fins éducatives. Toute utilisation malveillante est strictement déconseillée.