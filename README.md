# Diagramme de Sankey - Open Food Facts

## 1. Présentation du projet
Ce projet vise à visualiser le trajet que suivent les aliments depuis :
- **L’origine des ingrédients** : d'où proviennent les matières premières.
- **Les lieux de fabrication** : où ces matières premières sont transformées.
- **Les lieux de consommation** : où les produits finis sont vendus ou consommés.

L'objectif est de répondre à la question : **"D’où viennent nos aliments ?"** et de sensibiliser les utilisateurs à l'importance de consommer local.

---

## 2. Jeu de données
Les données proviennent de la plateforme **Open Food Facts** et ont été fournies au format TSV. Elles contiennent des informations détaillées telles que :  
- Les **codes-barres**, **noms des produits**, et **images**.  
- Les **quantités**, **marques**, et **catégories** des produits.  
- Les **lieux de fabrication**, **ingrédients**, **allergènes**, et **additifs**.

Ces données ont été soigneusement nettoyées et filtrées pour répondre aux exigences du projet.

---

## 3. Processus de traitement des données

### Sélection et nettoyage
- **Filtrage** : Les produits incomplets ou sans informations essentielles (origine, lieu de fabrication, pays de consommation) ont été exclus.  
- **Normalisation** : Les noms de pays, régions et catégories ont été unifiés pour éviter les doublons.  
- **Structuration** : Les relations entre les ingrédients, lieux de fabrication et produits finis ont été organisées sous forme de graphes.

### Transformation et tri
- Les données ont été regroupées par :
  - **Région** : Origines des ingrédients.  
  - **Sous-région** ou **pays** : Lieux de fabrication.  
  - **Catégories** : Types de produits finis (par exemple, boissons, snacks, etc.).  
- Les flux entre ces entités ont été comptabilisés pour générer des poids relatifs (épaisseur des flèches dans le diagramme).

---

## 4. Visualisation interactive
Nous avons choisi de représenter ces données sous forme de **diagramme de Sankey** pour illustrer les flux entre :
1. **Origines des ingrédients**  
2. **Lieux de fabrication**  
3. **Points de vente**  
4. **Catégories des produits**

### Caractéristiques principales :
- **Épaisseur des flèches** : Proportionnelle à la quantité de produits ou d’ingrédients échangés.
- **Couleurs dynamiques** : Les flux d’ingrédients et de produits finis sont représentés avec des palettes distinctes pour faciliter leur distinction.  
- **Zoom et dézoom** : L’utilisateur peut naviguer entre les niveaux globaux (continent, région) et locaux (pays spécifiques).  
- **Labels interactifs** : En survolant les flèches, des informations contextuelles apparaissent, telles que le type d’ingrédient ou de produit impliqué.  
- **Classification des pays** :  
  - **Producteurs** (quantité élevée d’ingrédients).  
  - **Transformateurs** (lieux majeurs de fabrication).  
  - **Consommateurs** (pays où les produits sont principalement vendus).

---

## 5. Fonctionnalités avancées
### Filtres personnalisés :
- Afficher **uniquement les flux d’ingrédients** ou **uniquement les flux de produits finis**.  
- Visualiser les flux d’un produit ou d’une catégorie spécifique (recherche intégrée).  

### Prévision :
À terme, nous envisageons d’ajouter :
- Une vue **carte géographique** en complément pour observer les flux sur un plan spatial.  
- Des analyses de dépendance entre régions et catégories spécifiques.  

---

## 6. Technologies utilisées
- **[D3.js](https://d3js.org)** : Génération et animation des diagrammes interactifs.  
- **JavaScript** : Manipulation des données et logique d'interaction.  
- **HTML/CSS** : Structure et stylisation de l'interface utilisateur.

---

## 8.License

 Ce projet est sous licence MIT. Vous êtes libre de le modifier et de le redistribuer dans le respect de cette licence.
 
## Auteur : Berger Ghislain

## Données : Open Food Facts 

## 7. Installation
1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/nom_utilisateur/sankey-openfoodfacts.git
   
2.Accédez au dossier du projet :
   cd sankey-openfoodfacts

3. Ouvrez le fichier opendata.html dans un navigateur ou servez-le via un serveur local :
   ```python -m http.server 8000

---


