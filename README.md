# Laredoute Scraper

Ce projet est un outil de web scraping conçu pour extraire des informations sur les fournisseurs du site e-commerce La Redoute. Il utilise **Botasaurus**, un puissant framework de scraping, ainsi que **Pixi** pour la gestion des dépendances, afin d'automatiser la navigation sur le site, la gestion des pop-ups et le scraping de données spécifiques sur les fournisseurs.

## Fonctionnalités

* **Extraction des liens de catégories** : Récupère les liens des catégories de produits à partir d'un sitemap.
* **Extraction des informations des fournisseurs** : Navigue vers les pages de produits, identifie le fournisseur et extrait ses informations détaillées.
* **Sauvegarde en CSV** : Les liens de catégories et les données des fournisseurs sont sauvegardés dans des fichiers CSV pour une utilisation ultérieure.
* **Configuration automatisée** : Un `Makefile` est inclus pour simplifier l'installation et garantir que toutes les dépendances sont installées correctement.

---

## Prérequis

Voici les outils et logiciels nécessaires pour faire fonctionner le projet :

* **`make`** : L'outil de construction `make` est indispensable pour exécuter les commandes d'installation et de lancement définies dans le `Makefile`.
* **Python 3.x** : Le projet est développé en Python. Assurez-vous d'avoir une version 3.x (par exemple, 3.9 ou plus récente) installée sur votre système.
* **`curl` et `apt`** : Le script d'installation est conçu pour les systèmes d'exploitation basés sur Debian/Ubuntu. Assurez-vous que les commandes `curl` et `apt` sont disponibles.

---

## Installation et configuration

Le projet utilise `pixi` pour gérer les dépendances. Le `Makefile` fourni automatise l'ensemble du processus de configuration.

1.  **Ouvrez votre terminal** et naviguez jusqu'au répertoire racine du projet.
2.  **Exécutez la commande `setup`** : Cette commande installera `curl` (si ce n'est pas déjà présent), `pixi`, et toutes les dépendances du projet.

    ```bash
    make setup
    ```

> **Note :** Si vous rencontrez une erreur "dpkg was interrupted" pendant l'installation, le `Makefile` tentera automatiquement de la corriger et de poursuivre l'installation.

---

## Utilisation

Une fois la configuration terminée, vous pouvez lancer le script de scraping en utilisant le `Makefile`.

1.  **Lancez le scraper** : Cette commande exécutera le script Python principal qui gère la logique de scraping.

    ```bash
    make run
    ```

Le script affichera la progression dans la console au fur et à mesure du scraping. Les résultats seront sauvegardés dans des fichiers CSV dans le répertoire de votre projet.

---

## Pour les utilisateurs de Windows

Le `Makefile` est optimisé pour les systèmes basés sur Linux et macOS. Les utilisateurs de **Windows** doivent d'abord installer `make` via un environnement comme **Git Bash** ou **WSL (Windows Subsystem for Linux)**.

Une fois `pixi` installé, vous pouvez également lancer les commandes directement depuis votre terminal, sans utiliser `make`. Cela est particulièrement utile si vous rencontrez des problèmes avec `make` sur Windows.

* **Pour installer les dépendances** :
    ```bash
    pixi install
    ```
* **Pour lancer le scraper** :
    ```bash
    pixi run python src/main.py
    ```

Ces commandes vous permettent de contourner le `Makefile` et d'interagir directement avec **Pixi** pour gérer le projet.