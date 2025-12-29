# ENSAE-Prog2A
# Projet Python pour la Data Science
    Groupe : Rou Senghak, Turri Barthélemy, Ban Bunrong

# Sujet : 
Dans quelle mesure la température quotidienne influence-t-elle la consommation d’électricité dans les régions françaises ?

# Motivations : 
La consommation d'électricité est un enjeu central des économies modernes, en cela qu'il reflète en partie l'activité des ménages, mais aussi celle de l'industrie et de l'économie en général. La consommation d'électricité est toutefois aussi liée à des enjeux de prévision énergétique et de stabilité du réseau. Dans un contexte de dérèglement climatique et d'une volatilité accrue du climat, comprendre les déterminants de la demande d'électricité est un enjeu de taille. 
Nous avons choisi, pour ce projet, de porter notre analyse sur la température et son lien avec la consommation d'électricité des ménages, car la température est un facteur clef de la consommation d'électricité quotidienne des citoyens, et car ses effets, souvent saisonniers, se manifestent de façon hétérogène à l'échelle du territoire.


# Modèles utilisés : 
Régression linéaire, Régression Ridge, Arbre de décision

# Données utilisées : 
Données de consommation d'électricité : https://www.rte-france.com/donnees-publications/eco2mix-donnees-temps-reel/telecharger-indicateurs

Données météorologiques extraites grâce à l'API NASA : https://www.rte-france.com/donnees-publications/eco2mix-donnees-temps-reel/telecharger-indicateurs


# Reproduction du projet : 
Les données brutes sont déjà inclues dans le dépôt, donc un clonage suffit, aucun téléchargement manuel n'est requis.

Pour cloner le projet : 
git clone https://github.com/ROUSenghak/Python_Project_2A.git

Pour se placer dans le dossier : 
cd Python_Project_2A

Pour installer les dépendances :
pip install -r requirements.txt

Ensuite, pour générer le jeu de données utilisé dans l'analyse, exécuter successivement les cellules du notebook 1_data_preparation.ipynb 

Pour reproduire l'analyse, exécuter ensuite successivement les cellules du notebook analysis_visualization.ipynb

