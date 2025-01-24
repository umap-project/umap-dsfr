---
title: uMap, au cœur de la formation et de la recherche
date: 2025-01-22
description: Ce témoignage présente deux usages d’uMap, l’un pour la formation des étudiants géographes et l’autre pour l’affichage des données de la recherche.
image: /static/umap/img/blog/umap-formation-recherche.png
image_alt: Carte du SIG de l’OSM Pyrénées
tags:
    - Témoignage
---

*Émilie Lerigoleur, ingénieure d’études CNRS à l’[UMR GEODE](https://geode.univ-tlse2.fr/) (Géographie de l’Environnement) - [université de Toulouse II](https://www.univ-tlse2.fr/) - explique son utilisation d’uMap et les apports de l’outil qu’elle associe à d’autres (#interopérabilité). Ce témoignage présente deux usages d’uMap, l’un pour la formation des étudiants géographes et l’autre pour l’affichage des données de la recherche de plusieurs laboratoires sur un même fond de carte (#websig).*

### Vous utilisez uMap dans le cadre de la formation des géographes – dont certains travailleront plus tard en collectivités

Émilie Lerigoleur : J’ai la chance d’intervenir en master pour accompagner les **étudiants sur les techniques géomatiques et l’utilisation des données**. Mon public se compose de **géographes qui réalisent de nombreux diagnostics territoriaux, sans être forcément experts des outils informatiques. Je recherche donc des outils faciles à prendre en main.**

Pour l’enseignement en webmapping, j’utilisais généralement Qgis pour créer des cartes, c’est l’outil de base du Sig. Une fois la carte réalisée, nous la transférions sur des solutions web. Qgis permet également de verser des cartes sur le serveur Qgis cloud. Pour simplifier, j’essayais de trouver **des solutions de carte en ligne, qui évitent d’avoir à gérer l’hébergement**. J’ai découvert uMap il y a trois ou quatre ans et un collègue m’a parlé de l’[instance pour les agents publics](https://umap.incubateur.anct.gouv.fr/fr/).

Même si les cartes concernent des recherches publiques et n’embarquent pas de données à caractère personnel, je suis rassurée par cet environnement en .gouv.fr. Je trouve uMap bien conçu, pratique et ludique. Les cours se déroulent en deux séances pour un total de huit heures – dont sept de pratique. **Je constate que les séances portent leurs fruits, car les étudiants essaient de réutiliser uMap au cours de leurs stages et prennent l’outil en main.**

<div class="fr-alert fr-alert--info">
<h4 class="fr-alert__title">❓ Webmapping (ou cartographie en ligne)</h4>

Processus qui permet l’utilisation et l’analyse de cartes sur Internet.

</div>

### La carte des risques en Ariège est une base de cours qui présente plusieurs fonctionnalités d’uMap

Émilie Lerigoleur : J’ai mis cette carte au point pour faire cours à des masters 1 dans l’optique d’utiliser les données de la plateforme [Géorisques](https://www.georisques.gouv.fr/) car **j’encourage l’utilisation des données ouvertes**. J’apprends aux étudiants à **aller chercher des données, les mettre en forme, créer des popups**. J’essaie d’explorer toutes les fonctionnalités possibles, dont l’affichage en clusters de points et en [carte de chaleur](https://umap.incubateur.anct.gouv.fr/fr/map/tuto-carte-de-chaleur-avec-les-arbres-urbains-a-me_1250#14/49.1003/6.2184).


**La carte des risques en Ariège**

<iframe width="100%" height="400px" frameborder="0" allowfullscreen allow="geolocation" src="//umap.incubateur.anct.gouv.fr/fr/map/carte-des-risques-environnementaux-en-ariege_553?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=datafilters&captionBar=false&captionMenus=true"></iframe>

<p><a href="//umap.incubateur.anct.gouv.fr/fr/map/carte-des-risques-environnementaux-en-ariege_553?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=datafilters&captionBar=false&captionMenus=true">Voir en plein écran</a></p>

L’idée est de leur apprendre à générer ce type de cartes et bien maîtriser tous les menus, les réglages des différentes couches, les couleurs. **Nous passons un peu de temps sur les options d’interactions et la manipulation des gabarits.** J’ai d’ailleurs préparé un support qui explique étape par étape comment générer un gabarit de popup « sur mesure ». Les étudiants apprennent au préalable les bases du code html, un peu de CSS pour la mise en forme et un peu de javascript. Ainsi, ils créent un mini-site web où ils apprennent à intégrer leur carte uMap dans une balise.

**Les étudiants seront sans doute amenés à travailler avec des informaticiens** et c’est souvent là que le bât blesse : « se comprendre entre géographes et informaticiens ». Fournir aussi aux géographes un peu de **vocabulaire et de compréhension va faciliter les échanges**.

Étant habituée à la pratique via des logiciels SIG, j’ai expérimenté une limite sur cette carte sur le choix des couleurs, car les palettes sont un peu contraignantes. Elles ne permettent pas d’en créer une avec un code. Pour autant, cette carte répond parfaitement aux besoins de l’enseignement, elle reste lisible. **Je souhaite valoriser un maximum cette solution auprès des étudiants, c’est un bon compromis simple à prendre en main et qui offre de nombreuses fonctionnalités**.


### La carte du websig de l’[Observatoire Hommes Milieux des Pyrénées](https://ohm-pyrenees.in2p3.fr/) présente une base des données de la recherche

Émilie Lerigoleur : Notre unité de recherches pilote des recherches sur la vallée pyrénéenne du Haut Vicdessos depuis 2010, puis de la haute vallée des Gaves dès 2015. **Les données d’observations recueillies sont abondantes. Plusieurs laboratoires travaillent sur un même espace, sans avoir forcément connaissance du travail de chacun.** Chaque année, les chercheurs des différents laboratoires procèdent à des recensements d’informations, inventaires de biodiversité, carottages, sondages dans des lacs ou tourbières… Cette carte intègre de très nombreux points et j’utilise les clusters pour les photos afin de les proposer seulement en zoomant.

**Web SIG de l’OPHM Pyrénées**

<iframe width="100%" height="400px" frameborder="0" allowfullscreen allow="geolocation" src="//umap.incubateur.anct.gouv.fr/fr/map/web-sig-de-lohm-pyrenees_564?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true"></iframe>

<p><a href="//umap.incubateur.anct.gouv.fr/fr/map/web-sig-de-lohm-pyrenees_564?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true">Voir en plein écran</a></p>

Cette carte est co-construite, avec l’objectif de présenter « qui a fait quoi, quand et comment ». Elle affiche quelques données de relevés de végétation, mais les autres pictogrammes renvoient à ce que l’on appelle « la métadonnée ».

<div class="fr-alert fr-alert--info">
<h4 class="fr-alert__title">❓ Métadonnée</h4>

C’est l’ensemble structuré de données qui servent à définir ou à décrire une ressource.

</div>


**Zoom sur la [tourbière de Bernadouze](https://umap.incubateur.anct.gouv.fr/fr/map/web-sig-de-lohm-pyrenees_564#16/42.80278/1.42425), cartographie de végétation et sondages**


<figure>
<img src="/static/umap/img/blog/umap-formation-recherche-tourbiere.png" alt="Capture d’un écran uMap avec une popup ouverte.">
<figcaption>

Ici la fenêtre popup indique la méthode et l’instrument utilisés, la période, le contact pour en savoir plus.

</figcaption>
</figure>


### Ce projet réunit vraiment tous les choix vertueux, le partage, les communs, la valorisation des métadonnées.

Émilie Lerigoleur : C’est mon métier, ce que je porte depuis des années. Ces ambitions ne sont pas toujours évidentes à mettre en pratique car les chercheurs sont parfois assez paternalistes avec leurs données. Je propose des modèles sur tableur pour récupérer les informations que je mets en forme. Voilà pourquoi la carte présente de très nombreux points et reste très touffue.

La principale difficulté rencontrée a concerné l’affichage des photographies. Des collègues photographient les paysages depuis des années et nous disposons d’une photothèque assez conséquente. Mais c’est autre outil qui ne s’interopère pas. J’ai trouvé une solution pour créer cette interopérabilité : sur la carte, les gros pavés blancs renvoient aux ressources placées sur la photothèque. J’ai réussi à y récupérer le lien vers chaque image et à les faire s’afficher, en paramétrant le calque en mode « cluster ». **Je tenais vraiment à mettre en pratique cette idée d’interopérabilité.**

Si je dois apporter une touche de critique : la carte est trop chargée. Je me rassure en pensant que le scientifique qui travaille sur un secteur peut zoomer et interagir directement avec toutes les données qui le concernent. **La carte fonctionne donc comme un point d’entrée.** Le choix des icônes constitue également un point noir lorsque les couches de données sont nombreuses, et c’est le cas de cette carte. Il faudrait pouvoir grouper des couches, comme dans un SIG. J’aime bien les visuels petits et je ne peux pas régler la taille de la goutte par exemple, ni l’ordre de superposition des pictogrammes. Cela explique que la carte présente à la fois de tout petits points et de gros pictogrammes quand on l’ouvre. C’est un peu dommage.

**Voilà pour les critiques, mais je suis très contente de l’utilisation de cet outil et l’ai présenté aux collègues scientifiques à un séminaire en fin d’année, tous les participants ont été d’accord sur cet usage**. J’ai envie de continuer à promouvoir uMap, je le trouve vraiment aisé. J’ai en tête de nombreux petits projets de création de cartes interactives via uMap dans différents projets de recherche, et pourquoi pas organiser des formations en interne à mon laboratoire pour leur apprendre à l’utiliser, etc.

<div class="fr-alert fr-alert--info">
<h4 class="fr-alert__title">❓ Truc et astuces</h4>

Pour zoomer sur la tourbière, il faut renseigner ses coordonnées géographiques dans l’outil de recherches uMap en haut à gauche : <code>42.80278,1.42425</code>. Et pour connaître les coordonnées géographiques d’un secteur, il faut centrer la carte sur la zone et recopier les coordonnées dans l’URL de la carte, par exemple ici : [<code>https://umap.incubateur.anct.gouv.fr/fr/map/web-sig-de-lohm-pyrenees_564#16/42.80278/1.42425</code>](https://umap.incubateur.anct.gouv.fr/fr/map/web-sig-de-lohm-pyrenees_564#16/42.80278/1.42425)

</div>

<br>

#### Pour aller plus loin :

CV d’Emilie Lerigoleur : [https://cv.hal.science/emilie-lerigoleur](https://cv.hal.science/emilie-lerigoleur)

<div class="fr-alert fr-alert--info">

Entretien avec Sophie Clairet, géographe, Chargée de déploiement, le 7 janvier 2025.

</div>

