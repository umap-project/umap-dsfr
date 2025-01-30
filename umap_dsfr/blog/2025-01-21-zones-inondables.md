---
title: Carte des Zones inondables & Bassin versant de la Neste
date: 2025-01-21
description: Le Pôle d’Equilibre Territorial et Rural (PETR) du Pays des Nestes a créé sur uMap une carte des zones inondables et une autre qui présente le bassin versant de la Neste.
image: /static/umap/img/blog/zones-inondables-neste.png
image_alt: Capture d’écran du site de la Neste
tags:
    - Témoignage
---

*Le Pôle d’Equilibre Territorial et Rural (PETR) du [Pays des Nestes](https://www.paysdesnestes.fr/) a créé sur uMap une carte des zones inondables et une autre qui présente le bassin versant de la Neste. Antoine Chabas, animateur du Programme d’Actions de Prévention des Inondations(PAPI) Neste, détaille les projets.*

J’avais participé à un Webinaire sur uMap en juillet, ce qui m’avait permis de découvrir cet outil bien plus simple dans la prise en main que QGIS, surtout pour **l’hébergement de la carte afin de la faire afficher sur un site internet**.

### La carte des zones inondables
La carte des zones inondables a été créée dans le cadre de [l’axe 5 du PAPI](https://www.observatoire-neste.fr/article/diagnostics-de-vulnerabilite) Neste 2 que le PETR du Pays des Nestes porte. L’axe 5 concerne la **réduction de la vulnérabilité des bâtis face aux inondations**.

<iframe width="100%" height="400px" frameborder="0" allowfullscreen allow="geolocation" src="//umap.incubateur.anct.gouv.fr/fr/map/cartographie-des-zones-inondables-du-bassin-versan_1384?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true"></iframe>

<p><a href="//umap.incubateur.anct.gouv.fr/fr/map/cartographie-des-zones-inondables-du-bassin-versan_1384?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true">Voir en plein écran</a></p>

Nous allons proposer aux propriétaires et gestionnaires de bâtiments situés en zone inondables la réalisation de diagnostics gratuits de vulnérabilité de leur bâti, afin qu’ils puissent réaliser à termes des travaux, subventionnés en partie par le Fonds Barnier, de réduction de la vulnérabilité du bien et des personnes occupant les locaux. **Cette carte va permettre aux futurs bénéficiaires du service, de voir si leurs habitations ou bâtis se situent en zone inondable**, ce qui représente la première étape de la démarche.

J’ai ainsi pu intégrer relativement facilement les couches de zones inondables des plans de prévention des risques naturels (PPRN) approuvés ou en cours d’approbation sur le territoire ainsi que la Cartographie Informative des Zones Inondables (CIZI) tout en affichant les bâtis situés dans ces zones.

Ce sont uniquement des données locales qui ont été utilisées donc il va falloir faire attention à mettre à jour au besoin les différentes couches utilisées.

Par l’intermédiaire de uMap, j’ai pu facilement intégrer la carte dans notre site de l’[Observatoire de la Neste](https://www.observatoire-neste.fr/article/cartographie-des-zones-inondables), ce qui nous permettra de transférer facilement l’information lors du déploiement du dispositif de réduction de vulnérabilité dans les prochains mois.

Les cartes interactives sont de bons outils visuels pour la communication et la sensibilisation.

### Carte interactive du bassin versant de la Neste

A la suite de cette première carte, j’ai utilisé à nouveau uMap pour réaliser une carte interactive pour la présentation du bassin versant de la Neste de manière générale. Ce sont à nouveau des couches locales qui ont été importées sur le site uMap.


<iframe width="100%" height="400px" frameborder="0" allowfullscreen allow="geolocation" src="//umap.incubateur.anct.gouv.fr/fr/map/bassin-versant-de-la-neste_1394?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true"></iframe>

<p><a href="//umap.incubateur.anct.gouv.fr/fr/map/bassin-versant-de-la-neste_1394?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true">Voir en plein écran</a></p>

Une fois que l’on a une première carte pour un territoire donné, **je trouve cela simple de pouvoir en créer de nouvelle sur les mêmes bases** et ainsi garder une certaine d’homogénéité d’affichage. J’ai copié la première carte, comme cela, j’avais déjà le format de base et similaire à la première. Cela permet d’avoir aussi une homogénéité dans le rendu, ce que je trouve important en termes de communication et sensibilisation. Sur la carte du bassin versant de la Neste, j’ai ajouté des données ponctuelles directement par l’intermédiaire de uMap comme pour les deux stations de Vigicrues sur Arreau ou encore la localisation des bureaux du Pôle Eau du PETR en charge de la compétence GEMAPI.

En juin, j’avais créé une première carte interactive à partir de QGIS, mais **j’avais rencontré des difficultés pour trouver un hébergeur me permettant de faire afficher cette carte sur l’Observatoire de la Neste**. Cette carte concerne les [repères de crues](https://www.observatoire-neste.fr/article/74-reperes-de-crues-poses-en-2022). Je pense qu’à terme, je la ferai également à partir de uMap, comme ont pu le faire nos voisins du syndicat mixte du [Pays de Lourdes et des Vallées des Gaves](https://umap.incubateur.anct.gouv.fr/blog/partager-linformation-mieux-prevenir-le-risque-inondation-avec-umap/).

Dans le cadre du PAPI Neste 2, nous allons également travailler avec les élus et la Préfecture sur les plans communaux de sauvegarde (PCS) et il est vrai que **uMap pourra être un outil pertinent concernant cette thématique.**

**Sur la partie gestion des milieux aquatiques et la prévention des inondations (GEMAPI), je pense que l’outil pourra être également utilisé** sur les travaux en cours ou réalisés sur le/les cours d’eau au vu de la simplicité de mise à jour ou d’ajout de données ponctuelles ou surfaciques.

<div class="fr-alert fr-alert--info">

Échange par email avec Antoine Chabas, le 21 janvier 2025

</div>
