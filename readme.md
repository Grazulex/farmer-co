# Projet Farmer Co

Ce projet utilise Python 3. Voici les étapes pour créer un environnement virtuel et installer les dépendances à partir d'un fichier `requirements.txt`.

## Prérequis

- Python 3.x doit être installé sur votre machine.
- `pip` doit être installé et accessible depuis la ligne de commande.

## Étapes

### 1. Créer un environnement virtuel

Pour créer un environnement virtuel, utilisez la commande suivante :

```bash
python3 -m venv env
```

### 2. Activer l'environnement virtuel

- Sur Windows :

```bash
.\env\Scripts\activate
```

- Sur macOS et Linux :

```bash
source env/bin/activate
```

### 3. Installer les dépendances

Une fois l'environnement virtuel activé, installez les dépendances à partir du fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

### 4. Désactiver l'environnement virtuel

Pour désactiver l'environnement virtuel, utilisez la commande suivante :

```bash
deactivate
```

## Remarques

- Assurez-vous de toujours activer l'environnement virtuel avant de travailler sur le projet.
- Si vous ajoutez de nouvelles dépendances, n'oubliez pas de mettre à jour le fichier `requirements.txt` avec la commande :

```bash
pip freeze > requirements.txt
```
