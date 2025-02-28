---
title: La carte interactive des subventions européennes
date: 2024-09-18
description: Communication, pilotage des budgets & aide à la décision.
image: /static/umap/img/blog/carte-subventions-europeennes.png
image_alt: Capture d’écran du site https://www.europelr.eu/cartes-interactives-des-financement
tags:
    - Témoignage
---


*La Maison de l’Europe de Montpellier propose une pleine page de cartes interactives des financements européens dans l’Hérault et l’Aveyron. Olivier Dedieu, son Directeur, détaille son objectif et le travail effectué sur les données. Ce témoignage d’un utilisateur qui n’est pas spécialiste de cartographie croise des besoins formulés en webinaire par des élus souhaitant visualiser sur leur territoire la répartition des dépenses, des subventions…*



## Les cartes interactives des financements européens

Ces cartes sont accessibles sur le site de la Maison de l'Europe de Montpellier, dans le menu [Financements européens](https://www.europelr.eu/cartes-interactives-des-financement) :

<figure>
<img src="/static/umap/img/blog/carte-subventions-europeennes.gif" class="fr-responsive-img" alt="Capture d’écran animée des cartes du site affichant les cartes, 19 septembre 2024.">
<figcaption>

Capture d’écran animée des cartes du site affichant les cartes, 19 septembre 2024.

</figcaption>
</figure>

Les cartes affichent des « clusters » afin de ne pas surcharger le résultat au départ. Au fur et à mesure du zoom, les détails se complètent car de nouveaux pointeurs apparaissent. Chaque calque accueille une thématique identifiée par une couleur. Il est possible de masquer un calque et d’utiliser la fonctionnalité de filtre de l’explorateur de données (en barre de gauche, les couches empilées).

Pour consulter les cartes sur uMap : [https://umap.openstreetmap.fr/fr/user/Maison%20de%20l'Europe%20de%20Montpellier/](https://umap.openstreetmap.fr/fr/user/Maison%20de%20l'Europe%20de%20Montpellier/)

## Pouvez-vous nous expliquer quel est l’objectif de ces cartes ?

Olivier Dedieu : La Maison de l’Europe est missionnée par la Commission européenne. Techniquement parlant, c’est une association, même si nos principaux financeurs sont publics, à commencer par la Commission européenne. Après avoir exercé comme agent public en collectivité et auprès des Services de l’État, j’ai rejoint la Maison de l’Europe en 2019. À mon arrivée peu avant les élections européennes, j’ai très vite été sollicité par **des habitants qui souhaitaient comprendre à quoi servait l’Union européenne et ce qu’elle finançait sur le territoire**. Or, je ne disposais pas d’outil, à part **des fichiers Excel qui restaient assez « difficiles à vendre »**.

Je me suis dit que le plus simple était sans doute de proposer des cartographies, même si je ne suis pas cartographe et que cette technicité m’échappe encore en grande partie. À l’époque, je savais que Google proposait une solution. La limite : c’était justement l’origine de l’outil. Un peu par hasard, j’ai découvert uMap.
Mon objectif est simple : nos concitoyens éprouvent des difficultés à appréhender l’Europe. **C’est tellement abstrait qu’il faut leur fournir « du concret » et c’est bien le rôle de ces cartes.** D’ailleurs, je me demande s’il est possible d’y placer des compteurs afin d’avoir une idée de leur diffusion. Et quelle est la logique de l’État, favoriser plutôt uMap que d’autres outils type Google ?

<div class="fr-alert fr-alert--info">
<h3 class="fr-alert__title">❓ Sur le programme uMap agents publics</h3>

Effectivement, l’objet du programme uMap est de fournir des outils aux agents publics qui soient hébergés en France, open source, sur lesquels nous ayons une certaine souveraineté, qui soient utilisables, intéressants et pas trop compliqués à manipuler non plus.

C’est dans ce contexte que nous avons décidé de participer au développement d’uMap. Cet outil opensource est né de la communauté OpenStreetMap voici plus de dix ans. Nous nous sommes rendu compte que de nombreuses collectivités, des enseignants… des agents publics dans des services très variés utilisaient l’outil dans le cadre professionnel et parfois aussi dans leur vie privée. Nous avons souhaité contribuer *a minima* à l’outil pour le faire évoluer dans le sens des besoins de ces agents et proposer également une instance dédiée. Cela permet de ne pas mélanger les cartes professionnelles et les cartes personnelles, de signer la carte avec le nom d’une collectivité plutôt qu’avec son nom personnel. Le but est aussi de proposer un outil de carto qui ne soit pas réservé à des géomaticiens.

</div>

## Et comment avez-vous réalisé vos cartes ?

Olivier Dedieu : Quand on n’est pas habitué à la cartographie, uMap ressemble « un peu à de l’hébreu ». **Je me suis formé via des tutoriels en ligne.** Et progressivement, je suis arrivé à réaliser les cartes telles que vous les voyez.

Je propose plusieurs types de cartes. Celles relatives à la Politique Agricole Commune (PAC) sont spécifiques, car je dispose de données de versements de subventions, mais pas de projets - sans information sur les projets financés donc. Par contre, pour tous les autres programmes, les informations sont plus complètes. **J’ai tenté de proposer des cartes digestes et visuelles.**

## La réalisation des cartes a pris beaucoup de temps ?

Olivier Dedieu : **La tâche la plus pénible à réaliser, ce n’est pas la cartographie** mais la récupération et le traitement des données avant de les importer dans uMap ! Certains programmes sont directement gérés par la Commission européenne ou ses agences, d’autres le sont par délégation par les autorités nationales - l’État ou des collectivités territoriales. Et le travail de mise en forme des données est plus ou moins bien réalisé. Par exemple, **les tableaux qui comportent des masques de cellules fusionnées posent de nombreux problèmes et les données sont parfois très difficilement mobilisables.**

**Deuxième limite, selon les dispositifs, je ne dispose pas des données à l’échelle adéquate.** Je m’occupe de deux départements en termes de communication, l’Hérault et l’Aveyron. J’ai donc besoin d’avoir une localisation des données a minima à leur échelle. Or les coordonnées sont la plupart du temps celles de la personne morale. Prenons le cas d’Horizon Europe, un gros programme de recherche dans l’Hérault. Je ne peux pas représenter les aides européennes régionales du CNRS car l’adresse administrative utilisée est celle du siège à Paris. Les gros opérateurs de recherche doivent donc m’expliquer ce qui relève des laboratoires implantés dans la région, sans quoi je ne peux pas géolocaliser une action régionale. Pour le moment, je n’ai pas encore effectué ce travail !
Un autre problème en recherche de données concerne le fond de relance européen. Après l’épisode de la gestion COVID, l’Union européenne a créé un fond de 150 milliards d’euros, lequel finance 40 % du Plan de relance français.

Voilà pourquoi le site présente des cartes dédiées, par exemple la carte du Plan de relance dans l’Aveyron :

<iframe width="100%" height="400px" frameborder="0" allowfullscreen allow="geolocation" src="//umap.openstreetmap.fr/en/map/le-plan-de-relance-europeen-dans-laveyron_953548?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true"></iframe><p><a href="//umap.openstreetmap.fr/en/map/le-plan-de-relance-europeen-dans-laveyron_953548?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true">See full screen</a></p>

Notre difficulté est de distinguer les financements français réalisés avec les fonds européens car nous ne disposons pas encore toutes les données. Par exemple sur la thématique des aides de l’État apprentissage et contrats de professionnalisation, recrutement de moins de 26 ans du plan de relance : **je n’arrive pas à obtenir les informations** des entreprises qui les ont recrutés. Je dispose d’un chiffre global pour le département, sans pouvoir le cartographier. **Il me suffirait du code postal des entreprises pour ventiler les données sur la carte**.

## Les données ne sont pas pensées pour être utilisées le long de toute la chaîne

Olivier Dedieu : Chacun réalise ses fichiers Excel dans son coin sans penser que d’autres pourraient en avoir besoin, notamment pour les utiliser sur une carte.

## En termes de traitement, comment est concoctée cette carte ?

Olivier Dedieu : **J’utilise la méthode la plus simple**. Je complète mon fichier Excel, j’intègre les adresses, villes et codes postaux et je convertis en .csv. Ensuite, j’utilise l’excellent site de l’État qui permet de faire du géocodage.
Une fois les données géocodées, j’ouvre uMap et importe les données. Il faut toujours vérifier le géocodage.

<div class="fr-alert fr-alert--info">
<h3 class="fr-alert__title">❓ Géocodage</h3>

Opération qui permet d’ajouter les coordonnées (latitude et longitude) à une adresse. Au besoin, [un petit tutoriel](https://uma-zammad.anct.cloud-ed.fr/help/fr-fr/6-tutoriels/8-ajouter-leur-geolocalisation-aux-adresses-geocodage) détaille comment faire.

</div>

## Aujourd’hui, pour actualiser vos cartes, vous effectuez la mise à jour de vos fichiers Excel, puis les réimportez ?

Olivier Dedieu : C’est cela, **j’ajoute des lignes sur le fichier Excel, puis il remplace le précédent.** Il existe sûrement des systèmes permettant d’automatiser, mais techniquement, je ne sais pas faire. Deuxième difficulté que j’ai remarquée, l’Union européenne a mis en place une présentation des projets qui renvoie à une page Internet. Lorsque l’adresse du site change, ce qui arrive parfois sans que nous soyons informés, le lien ne marche plus faute de redirection. Voilà peut-être la limite de mon modèle, il faudrait que je m’intéresse à ce sujet pour voir comment intégrer directement des liens corrigés si cela est possible.

## Avez vous des souhaits ?

Olivier Dedieu : J’aimerais disposer d’un bon vrai tutoriel. Et je ne comprends pas certains comportements de l’outil : pourquoi les lignes de mes fichiers n’apparaissent pas toujours dans le même ordre que le tableau initial ? On peut désormais ajouter une colonne (propriété) et j’aimerais bien pouvoir changer leur ordre. Pas grand-chose au final, et une fois passé le temps d’adaptation, uMap est vraiment un super outil.

<div class="fr-alert fr-alert--info">
<h3 class="fr-alert__title">Nota</h3>


Ces cartes sont réalisées sur l’instance uMap OpenStreetMap parce que la Maison de l’Europe de Montpellier est une association. Les personnes qui travaillent pour un service public sont invitées à créer une carte sur l’instance de uMap hébergée par l’ANCT : [https://umap.incubateur.anct.gouv.fr/fr/](https://umap.incubateur.anct.gouv.fr/fr/). Une documentation, l’inscription à des webinaires et à une infolettre sont accessibles depuis le site.

</div>

<div class="fr-alert fr-alert--info">

Propos recueillis par Sophie Clairet, géographe, Chargée de déploiement et Ariane Rose, Cheffe de projet - Incubateur des Territoires, le 25 juillet 2024.

</div>

