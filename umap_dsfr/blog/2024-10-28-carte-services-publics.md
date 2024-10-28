---
title: Faites « La » carte des services publics à partager sur votre site
date: 2024-10-28
description: Partager une carte des services sur un site, c’est garantir la compréhension rapide pour tous les publics.
image: /static/umap/img/blog/carte-services-publics.png
image_alt: Capture d’écran de « La carte des services publics »
tags:
    - Témoignage
---

*Partager une carte des services sur un site, c’est garantir la compréhension rapide pour tous les publics. À la clé : une meilleure attractivité, un gain de temps pour tous, agents comme usagers. La plupart du temps, le site de votre collectivité ou de votre service embarque déjà toutes les informations sur plusieurs pages différentes. Ce billet “pas-à-pas” propose de réaliser une carte très simple, un peu sur le modèle du témoignage publié en septembre [« La » carte des services au public à avoir sur son site](https://umap.incubateur.anct.gouv.fr/blog/la-carte-des-services-au-public-a-avoir-sur-son-site/).*


### Pour commencer

* Ouvrir [le site uMap pour les agents publics](https://umap.incubateur.anct.gouv.fr/fr/) et se connecter à son compte
* Cliquer sur « Créer une carte » puis dans l’outil de recherche, indiquer le nom de la commune ou zoomer sur la carte.

Pour simplifier, nous choisissons une petite commune, Abriès-Ristolas dans les Hautes-Alpes.

Quels sont les services à présenter ? Cela dépend des situations, dans le cas présent, par exemple :

- La mairie et la mairie déléguée
- L’école
- La bibliothèque
- Les musées
- Le point d’information tourisme
- Les parkings
- Les campings municipaux, ainsi que le parking pour camping-cars
- Les points d’eau potable
- Les départs domaine skiable et enduro
- Les terrains de sport
- Les points d’apport volontaires
- Le défibrillateur.

> Astuce : Pour établir la liste, on peut s’aider du fond de carte. La plupart des objets présents sur ce fond pourront être importés en un clic. Il en manque ? uMap permet de les ajouter au fond de carte (lien vers le fond OSM). Cela s’appelle « contribuer ».

Le fond OpenStreetMap propose bien d’autres informations comme les sentiers de randonnée !

### Regrouper les informations par thématiques

Pour que la carte reste simple et lisible : regrouper les services par catégories. Chacune fera l’objet d’un calque associé à une couleur différente :

- La mairie et le contour de la commune
- L’école
- Les bibliothèques, les musées
- Les parkings et les points d’apport volontaire
- Tourisme et loisirs
- Urgence (il sera toujours possible d’ajouter autre chose que le défibrillateur)

### Créer un calque par thématique

Il est préférable de commencer par la création des calques pour gagner du temps ! On règle tout ce qui concerne le calque : couleur des objets, affichage ou non du nom au survol de la souris, des popups lorsqu’on clique.

> On peut toujours modifier à chaque étape et ajouter des calques.

Cliquer sur gérer les calques dans la barre de droite : <img src="/static/umap/img/blog/carte-services-publics-icone-calques.png" alt="Capture d’écran de l’icône pour gérer les calques.">

Créer un nouveau calque, lui donner un nom (ici « La commune et la mairie » et régler sa couleur et la forme des icônes dans les « Propriétés de la forme » et les options d’interaction, c’est-à-dire ce qui s’affiche :

<figure>
<img src="/static/umap/img/blog/carte-services-publics-options-interactions.png" alt="Capture d’écran des options d’interactions.">
<figcaption>

Capture d’écran des options d’interactions.

</figcaption>
</figure>

> Pour une carte qui intègre des illustrations, films, etc. le choix popup (grande) peut être plus approprié. Faites des tests, c’est le mieux.

Puis procéder de même avec les autres calques.

> Ne pas oublier d’enregistrer de temps en temps…

Voilà le résultat :

<figure>
<img src="/static/umap/img/blog/carte-services-publics-gerer-calques.png" alt="Capture d’écran du panneau de gestion des calques.">
<figcaption>

Capture d’écran du panneau de gestion des calques.

</figcaption>
</figure>

### Importer les données ou les ajouter une par une

Nous allons importer les données qui existent déjà en open data en utilisant l’assistant d’import.

Cliquer en barre de droite sur : <img src="/static/umap/img/blog/carte-services-publics-icone-import.png" alt="Capture d’écran de l’icone de gestion des imports.">

Puis :

<figure>
<img src="/static/umap/img/blog/carte-services-publics-assistants-import.png" alt="Capture d’écran des assistants d’import.">
<figcaption>

Capture d’écran des assistants d’import.

</figcaption>
</figure>

Pour importer le contour de la commune, cliquer sur « Communes de France », renseigner le nom de la commune et en bas de colonne choisir d’importer dans le calque dédié :

<figure>
<img src="/static/umap/img/blog/carte-services-publics-limites-communales.png" alt="Capture d’écran de sélection du calque.">
<figcaption>

Capture d’écran de sélection du calque.

</figcaption>
</figure>

Voilà le résultat :

<figure>
<img src="/static/umap/img/blog/carte-services-publics-contour-commune.png" class="fr-responsive-img" alt="Capture d’écran avec le contour de la commune.">
<figcaption>

Capture d’écran avec le contour de la commune.

</figcaption>
</figure>


Il est possible de supprimer la couleur de fond, ce que nous faisons en cliquant sur l’objet, le petit stylo et remplissage sur `off` dans les propriétés :

<figure>
<img src="/static/umap/img/blog/carte-services-publics-import-proprietes.png" alt="Capture d’écran du formulaire des propriétés de la forme">
<figcaption>

Capture d’écran du formulaire des propriétés de la forme.

</figcaption>
</figure>

Ajouter les mairies en positionnant le pointeur sur le fond de carte à l’endroit voulu : <img src="/static/umap/img/blog/carte-services-publics-icone-marqueur.png" alt="Capture d’écran de l’icône pour ajouter un marqueur.">

Puis compléter le panneau « Propriétés de l’élément » qui s’affiche à droite lors de l’ajout du pointeur :

<figure>
<img src="/static/umap/img/blog/carte-services-publics-mairie-nom-description.png" alt="Capture d’écran du nom et description pour la mairie">
<figcaption>

Capture d’écran du nom et description pour la mairie.

</figcaption>
</figure>

<figure>
<img src="/static/umap/img/blog/carte-services-publics-mairie-proprietes.png" alt="Capture d’écran du choix de propriétés pour la mairie">
<figcaption>

Capture d’écran du choix de propriétés pour la mairie.

</figcaption>
</figure>

<figure>
<img src="/static/umap/img/blog/carte-services-publics-mairie-picto.png" alt="Capture d’écran du choix de pictogramme pour la mairie">
<figcaption>

Capture d’écran du choix de pictogramme pour la mairie.

</figcaption>
</figure>

<figure>
<img src="/static/umap/img/blog/carte-services-publics-mairie-formulaire.png" class="fr-responsive-img" alt="Capture d’écran du formulaire d’édition pour la mairie">
<figcaption>

Capture d’écran du formulaire d’édition pour la mairie.

</figcaption>
</figure>

Préciser le nom et toutes les informations souhaitées dans **la description**.

**Cliquer sur le « ? » pour savoir comment associer une image, un lien, une vidéo.**

Horaires, contact, photo,… le nom du maire et du maire délégué par exemple, on obtient :


<figure>
<img src="/static/umap/img/blog/carte-services-publics-popup-mairie.png" alt="Capture d’écran de la popup pour la mairie">
<figcaption>

Capture d’écran de la popup pour la mairie avec des méta-données.

</figcaption>
</figure>

Ajouter les autres services depuis l’assistant d’import GeoDataMine, par exemple pour les bibliothèques, on clique sur la petite flèche d’import à droite : <img src="/static/umap/img/blog/carte-services-publics-icone-import.png" alt="Capture d’écran de l’icone de gestion des imports.">

Puis sur GeoDataMine :

<figure>
<img src="/static/umap/img/blog/carte-services-publics-bibliotheque-geodatamine.png" alt="Capture d’écran du formulaire permettant d’utiliser GeoDatamine.">
<figcaption>

Capture d’écran du formulaire permettant d’utiliser GeoDatamine.

</figcaption>
</figure>

Une fois le calque choisi, préciser les informations d’accès et pourquoi pas une photographie dans les « Propriétés de l’élément ». Pour afficher le panneau « Propriétés », cliquer sur le pointeur ou le forme concernée.

<figure>
<img src="/static/umap/img/blog/carte-services-publics-bibliotheque-photo.png" alt="Capture d’écran du formulaire permettant de définir une photographie.">
<figcaption>

Par exemple, une photographie de la bibliothèque sur le [site de la commune](https://www.abries-ristolas.fr/bibliotheque.html) peut être appelée dans uMap.

</figcaption>
</figure>


<figure>
<img src="/static/umap/img/blog/carte-services-publics-bibliotheque-picto.png" alt="Capture d’écran de la popup de bibliothèque avec un pictogramme de livre.">
<figcaption>

Il est possible d’ajouter un pictogramme de type « livre » afin de distinguer la bibliothèque des musées.

</figcaption>
</figure>


Continuer avec les différents services, en changeant de calque au fur et à mesure et en ajoutant les informations d’accès.

### Il manque une information sur le fond de carte OpenStreetMap ?

Certains *Points d’apport volontaires* sont manquants ?

On peut les ajouter au fond de carte OpenStreetMap en cliquant sur l’outil JOSM à gauche : <img src="/static/umap/img/blog/carte-services-publics-icone-josm.png" alt="Capture d’écran de l’icôné d’édition OSM.">

Une nouvelle page s’ouvre. Pour pouvoir modifier le fond OSM, il faut bien entendu s’enregistrer.

<figure>
<img src="/static/umap/img/blog/carte-services-publics-conteneurs-recyclage.png" alt="Capture d’écran avec une édition OSM">
<figcaption>

Ici nous en profitons pour ajouter des « Conteneur de recyclage ».

</figcaption>
</figure>

La mise à jour du fond de carte OpenStreetmap est immédiate, il faut quelques heures pour la propagation dans uMap. Nous allons donc ajouter les points manuellement sur la carte uMap afin qu’elle soit à jour immédiatement pour les besoins de ce billet.

<figure>
<img src="/static/umap/img/blog/carte-services-publics-point-manuel.png" alt="Capture d’écran avec un marqueur positionné.">
<figcaption>

Capture d’écran avec un marqueur positionné.

</figcaption>
</figure>

> Astuce : Pour bien repérer l’endroit dans uMap, il est conseillé d’utiliser la photo aérienne de l’IGN.

### Le résultat

<iframe width="100%" height="400px" frameborder="0" allowfullscreen allow="geolocation" src="//umap.incubateur.anct.gouv.fr/fr/map/la-carte-des-services-publics_894?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true"></iframe><p><a href="//umap.incubateur.anct.gouv.fr/fr/map/la-carte-des-services-publics_894?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=caption&captionBar=false&captionMenus=true">Voir en plein écran</a></p>

### Parmi les sources utilisées pour cette carte

- La [carte de territoire du Guillestrois Queyras](https://www.ccguillestroisqueyras.fr/la-com-com/le-territoire/carte-du-territoire/): pour vérification de certains points d’apport volontaire
- Reconnaissance de terrain
- Appel au Point d’information touristique pour le Parking Camping Cars mal situé sur la plupart des cartes.

### Pour toute question, problème

- Consultez [la documentation](https://discover.umap-project.org/fr/)
- Inscrivez vous à un [webinaire](https://umap.incubateur.anct.gouv.fr/fr/)
