---
title: uMap au cœur de la communication des Chambres d’agriculture
date: 2024-07-10
description: Voici le témoignage de Frédéric Guimier, Consultant Communication et projets numériques au sein de la Chambre d’agriculture Pays de la Loire.
image: /static/umap/img/blog/umap-chambre-agriculture.png
image_alt: Une carte incrustée sur le site de Chambre d’agriculture Pays de la Loire.
tags:
    - Témoignage
---


*Dégoogliser les sites Internet, respecter le RGPD, simplifier et fluidifier l’affichage d’informations en carte pour les agriculteurs et le grand public, accélérer la mise à jour des fonds de cartes… voici autant de raisons pour généraliser uMap sur les sites des Chambres d’agriculture et former les agents à son utilisation. Voici le témoignage de Frédéric Guimier, Consultant Communication et projets numériques au sein de la [Chambre d’agriculture Pays de la Loire](https://pays-de-la-loire.chambres-agriculture.fr/).*

## Vous avez présenté votre expérience lors de [State of the Map 2023](https://peertube.openstreetmap.fr/w/iLpz3PziyVbt86wQsAdFVB?start=2s). Elle est vraiment éclairante pour de nombreux agents et services publics.

Frédéric Guimier : Nous avons choisi d’utiliser uMap notamment pour des **raisons de RGPD et d’affichage mobile plus abouti que la concurrence**, et pour sa **simplicité d’utilisation par les services communication**. Le bon affichage sur mobile d’uMap a été un facteur clé de décision, car nos sites Internet sont de plus en plus consultés sur mobile (de 35 à 60 % de navigation sur mobile, suivant le site consulté).
Au quotidien, au sein d’une équipe nationale métier qui accompagne l’ensemble des équipes Communication des Chambres d’agriculture, **je coordonne la gestion des sites Internet des Chambres d’agriculture et des outils qui gravitent autour**, dont uMap. Concrètement, j’assure l’interface entre nos services informatiques, notre prestataire de tierce maintenance applicative (marché public actuellement attribué à la [société Ewill](https://www.agence-ewill.com/) d’Amiens), et les utilisateurs répartis sur tout le territoire national (dont l’outremer). **Former et accompagner les utilisateurs, c’est le nerf de la guerre de la réussite des projets.**

## Et quelle est votre utilisation de uMap ?

Frédéric Guimier : Les services Communication ont besoin de pouvoir communiquer certaines informations sur des cartes, plus claires qu’un long texte. **uMap est donc d’abord un support de communication comme un autre (vidéo, photo, graphique, …)**. Il permet de **publier rapidement des cartes en lien avec l’actualité.** Ou de produire rapidement une carte pour un événement, à propos d’une crise.
L’utilisation d’uMap au détriment de Google Maps, s’est faite d’abord pour obtenir un **meilleur rendu des cartes sur smartphone**. Puis, dans le cadre d’une **politique globale de strict respect du RGPD**, nous supprimons totalement le recours à  Google Maps, comme nous l’avons fait avec Google Analytics remplacé par [Matomo](https://fr.matomo.org/) (ex-Piwix). Sur le site de la Chambre d’agriculture des Pays de la Loire, récemment modernisé, **aucun cookie intrusif n’est utilisé !**
La nouvelle version d’uMap apporte des améliorations intéressantes (centrage automatique sur les données, appel direct de [Framacalc](https://framacalc.org/abc/fr/) sans passer par un import du csv notamment.

<div class="fr-alert fr-alert--info">
<h3 class="fr-alert__title">❓ Framacalc & GRIST, les tableurs associés à uMap</h3>

uMap permet d’afficher les données de tableaux. Framacalc est proposé par [Framasoft](https://framasoft.org/fr/), association d’éducation populaire, qui héberge Framacarte, instance de uMap ouverte à tous les utilisateurs. [GRIST](https://donnees.incubateur.anct.gouv.fr/toolbox/grist) fait partie de la suite numérique de la DINUM et s’adresse aux agents publics. Voir le [film de démonstration](https://tube.numerique.gouv.fr/w/kya6m1aFtgDcy2LMkgUBya) et le [lien vers GRIST](https://grist.incubateur.net/).

</div>

Cependant, **uMap est un outil de communication, pas un SIG**. Nos géomaticiens travaillent sur des commandes très techniques, à forte valeur ajoutée, qui sortent du champ de la communication. **Pour autant, nos cartes ne sont pas vides, et peuvent être assez riches en contenus**, pour peu que ceux-ci soient très spécialisés sur un élément précis et fluctuant, comme c’est le cas du **[site Val’fumier](https://valorisation-fumier-ifce.chambres-agriculture.fr/)**.

<iframe width="100%" height="400px" frameborder="0" allowfullscreen allow="geolocation" src="//umap.openstreetmap.fr/fr/map/valfumier_757298?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true"></iframe><p><a href="//umap.openstreetmap.fr/fr/map/valfumier_757298?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true">Carte de l’offre de fumier consultable sur le site Val’fumier (voir en plein écran)</a></p>

Le site Val’fumier, présenté à State of The Map en 2023 fournit un bon exemple. **Les données sont gérées directement par le service communication au format .csv** (en flux prochainement).
Avec Val’fumier, nous avons commencé par une **opération régionale, elle est nationale aujourd’hui** :
Toutes les régions placent des données en ligne, soit une vingtaine de personnes issues de chambres d’agriculture et IFCE (Institut Français du Cheval et de l’Équitation). Chaque région travaille son fichier. csv, dont les données sont alimentées via un formulaire de contribution disponible sur le site Internet Val’fumier. La carte est mise à jour de manière autonome par les agents. **Plus de 20 personnes en collaboration, totalement en autonomie (après une courte initiation à uMap)**. Et le résultat répond au besoin actuel, à **coût très économique**.

*Formulaire d’offre de fumier qui nourrit la carte précédente :*

<figure>
<img src="/static/umap/img/blog/valfumier-formulaire.gif" class="fr-responsive-img" alt="GIF animé pour accéder au formulaire du site Val’fumier.">
<figcaption>

Capture d’écran du site Val’fumier, 9 juillet 2024.

</figcaption>
</figure>



Nous allons moderniser le site Val’fumier durant l’été 2024, et **tirer parti des récentes évolutions uMap** pour améliorer tant le rendu pour les internautes, que simplifier la mise à jour des informations à afficher, pour les collègues qui mettent à jour la carte.
Jusqu’à présent, un court module uMap était inclus dans la formation initiale de nos webmasters. Dès le second trimestre 2025, nous allons proposer aux équipes communication une formation dédiée à uMap, par l’intermédiaire de notre centre de formation intégré ([RESOLIA](https://resolia.chambres-agriculture.fr/)). La [société Cartocité](https://cartocite.fr/) sera sollicitée pour animer cette formation.  J’interviendrai pour **faire le lien entre uMap, OSM et notre système web** basé sur le CMS Typo3 et bien recadrer les limites de **cet outil de communication**, qui ne doit pas se substituer à notre SIG.

## Et quels sont vos souhaits pour la suite ?

Frédéric Guimier : Nous devons travailler sur les **zones de frontière entre deux régions** par exemple, en particulier lorsque les données sont nombreuses. Dans ce cas là, il peut être intéressant de quitter uMap pour une base de données géographiques, quitte à rediriger un flux vers uMap pour l’affichage sur une petite carte.
Je vais continuer à faire de la cartographie et à me mobiliser pour **bouger les lignes afin que les services communications aient accès aux données géographiques** via des API et que l’on puisse **travailler main dans la main avec nos géomaticiens**.
Ce qui est pratique avec uMap : je me rends compte qu’un « objet » est mal positionné sur le fond de carte ? Je peux le modifier dans OpenStreetMap. Et la modification est immédiate grâce à la **réactivité des serveurs OSM.**

*La fonctionnalité qui permet d’éditer OSM et de mettre à jour le fond de carte :*

<figure>
<img src="/static/umap/img/blog/osm-edition-fond-carte.gif" class="fr-responsive-img" alt="GIF animé pour passer de la carte uMap à l’édition dans OpenStreetMap.">
<figcaption>

Capture d’écran du 9 juillet 2024

</figcaption>
</figure>



## Effectivement, c’est très pratique de pouvoir contribuer au fond OpenStreetMap !

Frédéric Guimier : Et **les « métiers » également y contribuent** ! De l’avis d’[entreprises comme Michelin](https://peertube.openstreetmap.fr/w/4VUXE5v4YKwNvt8gz9Pe1c), les routes sont bien mieux renseignées sur les fonds OSM que par le prestataire qu’ils payaient à l’époque. Si elles sont moins précises dans une zone industrielle, Michelin intervient avec ses techniciens et la communauté OSM sur le terrain si bien que les cartes sont très vite à jour.
Notre approche est de privilégier **les méthodes agiles**, développer ce dont on a besoin. N’importe qui peut faire de la cartographie avec StreetComplete. C’est ludique. **Ce qui coûte cher dans la donnée, c’est sa collecte et sa mise à jour** : est-ce que le magasin est toujours ouvert ? Si des milliers de personnes participent à la vérification et à la mise à jour, la collecte est communautaire et gratuite et sera toujours plus actualisée que les autres solutions. Et les fonds de carte OSM apportent une **continuité géographique aux frontières puisqu’OSM est un projet mondial**.

<div class="fr-alert fr-alert--info">
<h3 class="fr-alert__title">🔆 <a href="https://streetcomplete.app/">StreetComplete</a> : pour compléter les fonds OpenStreetMap en s’amusant</h3>

Cette application permet de contribuer à la base OpenStreetMap sous forme de « quêtes » en répondant à un système de questions simples.

</div>

En dehors de mon travail, **j’ai créé un groupe local OSM à Angers**. Nous nous réunissons chaque mois et essayons d’élargir le public de « mappeurs » OSM. Notre (encore petite) communauté locale de « mappers » participe régulièrement, avec **des séances de « cartoparties » pour vérifier et mettre à jour le fond de carte OSM**. L’Association OpenStreetMap France peut prêter des outils pour contribuer à Panoramax - aux groupes locaux constitués seulement car le matériel coûte cher. Les photos sont versées sur Panoramax.

<div class="fr-alert fr-alert--info">
<h3 class="fr-alert__title">🔆 <a href="https://panoramax.fr/#focus=pic&map=20/48.8458639/2.4248417&pic=7bde6d85-a442-4f1b-bd87-86197157b8f0&speed=250&xyz=266.00/0.00/55">Panoramax</a> : photo-cartographiez vos territoires</h3>

Panoramax permet la mise en commun et l’exploitation de photos de terrain. Et il est tout à fait possible d’appeler ces photos dans uMap !

</div>

<div class="fr-alert fr-alert--info">

Entretien réalisé le 10 juin 2024 avec Sophie Clairet, géographe, chargée de déploiement sur uMap pour les agents publics.

* Pour toute question, problème : umap@anct.beta.gouv.fr
* L’instance uMap pour les agents publics : [https://umap.incubateur.anct.gouv.fr/fr/](https://umap.incubateur.anct.gouv.fr/fr/)
* Les webinaires : [page d’inscription](https://grist.incubateur.anct.gouv.fr/o/anct/forms/uaGwXjRXcWmiZCRmU72vjv/94)

</div>
