---
title: "Mission d’appui sécurité civile à Mayotte : uMap au cœur de l’action"
date: 2025-04-17
description: Nicolas Godelu, géomaticien du Service Départemental d’Incendie et de Secours de l’Isère (SDIS38), présente comment uMap a été utilisé à Mayotte pour le suivi des missions au lendemain du passage du cyclone Chido le 14 décembre 2024.
image: /static/umap/img/blog/mission-mayotte.png
image_alt: Photographie du centre opérationnel de commandement.
tags:
    - Témoignage
---

*En cas de catastrophe, des pompiers issus de diverses unités sont déployés en Mission d’Appui de la Sécurité Civile (MASC). Ils se relaient sur plusieurs semaines avant de se désengager et de passer la main aux autorités locales. Ce schéma n’admet aucune hésitation, tout est urgent, y compris la réalisation de cartes qui permettent le suivi des actions. Nicolas Godelu, géomaticien du Service Départemental d’Incendie et de Secours de l’Isère ([SDIS38](https://www.sdis38.fr/)), présente comment uMap a été utilisé à Mayotte pour le suivi des missions au lendemain du passage du cyclone Chido le 14 décembre 2024.*

## La MASC : des équipes engagées pour des missions très diverses !

Nicolas Godelu : Les premiers contingents qui arrivent fin décembre ont surtout géré le déblaiement des bâtiments. Le 18 janvier, le Commandant Christophe Peyre du SDIS38 est engagé sur la partie commandement. Il m’appelle **dès le 22 janvier et nous mettons en place la carte uMap dès ce jour-là**.

<figure>
<img src="/static/umap/img/blog/mission-mayotte-frise.png" class="fr-responsive-img" alt="Frise chronologique des évènements.">
<figcaption>

Source : Nicolas Godelu, présentation au [GéoSDIS 2025](https://www.sdis34.fr/geosdis2025-dans-lherault/).

</figcaption>
</figure>

Les actions des équipes sur le terrain sont très variées : déblaiement, bâchage, nettoyage des établissements scolaires, mise en place d’un hôpital de campagne, nettoyage des ravines, actions de vaccination, réception du fret aérien, maritime… La gestion de la logistique constitue une composante importante.
Pour coordonner le tout, il faut **recréer un centre opérationnel de commandement**. Il intègre des pompiers issus de SDIS différents et établit les priorités, par exemple la réouverture des écoles dès fin janvier 2025, puis les décline en différentes missions.

## La mise en place de l’outil cartographique

Nicolas Godelu : Lorsque le Cdt Peyre arrive le 20 janvier, les équipes utilisent plusieurs cartes générées sur Google My Maps. Et deux problèmes se posaient aux utilisateurs : elles étaient **limitées à un certain nombre de calques** sans que l’outil permette de les débloquer ; et surtout, il n’était **pas centralisé** puisque plusieurs cartes étaient maintenues en parallèle. **Difficile dans ces conditions au Cdt Peyre de disposer d’une vision unique et harmonisée des opérations !**
C’est la raison pour laquelle il m’a très vite appelé pour me demander si je disposais d’un outil qui puisse répondre aux besoins.

<div class="fr-alert fr-alert--info">
<h3 class="fr-alert__title">❓ Besoins identifiés</h3>

- un outil pour cartographier les différentes missions et assurer un suivi, un historique
- qui soit accessible en ligne et sur PC (l’usage mobile était très limité à Mayotte)
- avec une gestion souple des droits

</div>

J’ai regardé rapidement ce qui existait. Les équipes m’ont envoyé les données intégrées dans Google My Maps et je leur ai proposé deux exemples réalisés sur uMap et MaCarte de l’IGN. **Le choix s’est porté sur uMap**, déjà utilisé auparavant au SDIS de Haute-Garonne par le Cdt Peyre. J’ai finalisé l’intégration de leurs données via l’import-export. Nous avons fait un point rapide quelques jours plus tard avec le Lieutenant Ramuntxo Recarte du SDIS des Landes, qui aura la charge de la gestion de la carte : il était à l’aise avec l’outil. Je n’ai pas eu grand-chose à expliquer, **ils ont trouvé rapidement les fonctionnalités qu’ils souhaitaient**.

## Le bilan du suivi des missions sur uMap
Nicolas Godelu : **Globalement l’outil a été bien utilisé, bien intégré avec un bilan de 179 missions** entre le 20 janvier et le 4 février. Les équipes avaient besoin de détailler les missions dans les popups :


<figure>
<img src="/static/umap/img/blog/mission-mayotte-carte.png" class="fr-responsive-img" alt="Capture d’écran d’une carte uMap de Mayotte.">
<figcaption>

Source : Carte réalisée sur uMap dans le cadre de la MASC à Mayotte, Nicolas Godelu, présentation au [GéoSDIS 2025](https://www.sdis34.fr/geosdis2025-dans-lherault/).

</figcaption>
</figure>


Une **fonctionnalité très intéressante** : pouvoir **changer un objet d’une couche (calque) à l’autre**, de « en cours » à « terminé » puisque nos calques concernaient le suivi des missions. Et **dans une même couche, il est possible de créer des objets ponctuels, linéaires et surfaciques**. Pour des utilisateurs non-géomaticiens, c’est un degré d’abstraction très intéressant. Au fil des missions, les utilisateurs ont changé les secteurs, qui n’était pas initialement dessiné ainsi.

## La carte a servi quotidiennement à la remontée d’information à l’échelon national

Nicolas Godelu : Cette carte a été présentée au niveau du CORSEC (Centre Opérationnel de Réponse de la Sécurité Civile). **Ces exports de cartes uMap ont donc été utilisés à un niveau stratégique de la sécurité civile**. Il est assez gratifiant de voir le travail utilisé, et par autant d’utilisateurs le long de **toute la chaîne d’intervention et de décision**.

## Quel est le bilan de cette utilisation d’uMap ?

Nicolas Godelu : parmi les points positifs, nous retenons une **grande autonomie des utilisateurs**. Cela vient du fait que **l’outil est plutôt bien conçu**. Il ne permet certes pas de pousser très loin la personnalisation, mais il offre une base accessible à tous.
Au début, les équipes ont nourri quelques inquiétudes à utiliser l’[instance OpenStreetMap](https://umap.openstreetmap.fr/fr/), même si l’écosystème OSM ne leur était pas inconnu, rapidement dissipées. Je n’avais pas à ce moment-là la connaissance de l’instance [destinée aux agents publics](https://umap.incubateur.anct.gouv.fr/fr/). uMap est **un outil simple à prendre en main sans création de compte** – pour la version OpenStreetMap. Dans ce type d’utilisation, il n’est en revanche pas possible de restreindre les droits à une personne qui dispose du lien d’édition.

## La création d’un compte permet d’affiner la gestion des droits et de gérer des cartes en équipe.
Nicolas Godelu : Justement, la création de comptes réfrénait les équipes. J’ai vu que sur l’instance pour les agents publics, il suffit de disposer d’un compte sur ProConnect pour se créer un accès. **Nous avons probablement la solution à notre problème** : une connexion à ProConnect et une carte sur l’instance uMap pour les agents publics afin de gérer les droits plus finement.

## Une fois connecté avec ProConnect, vous pouvez créer une équipe
Nicolas Godelu : Il faut avoir en tête que les équipes sont très diverses, composées de plusieurs SDIS, qui se succèdent dans le temps. Elles ont l’habitude de créer des comptes à la volée, pour les missions, de manière que les cartes ne soient pas rattachées à un SDIS en particulier. Peut-être que **si chacun a son compte ProConnect, on peut facilement donner les droits à un nouveau qui arrive** dans une équipe qui porte le nom de la mission – et non d’un SDIS.

## Et quelles sont les difficultés rencontrées ?

Nicolas Godelu : Outre la gestion des droits à affiner, la principale difficulté concerne l’export en .csv des données. En effet, les équipes ont utilisé des **caractères spéciaux dans les popups qui ont posé un problème**. J’ai communiqué le problème à Yohan Boniface*, car il était un peu difficile de réparer ces exports. Les équipes avaient besoin d’exporter la donnée dans un tableur, pas forcément d’en importer. Yohan m’a parlé de GRIST, dont l’utilisation permet plutôt d’afficher des données dans uMap, mais cela ne correspond pas exactement à ce que les équipes ont besoin de réaliser.
De plus, nous avons **besoin de visualiser plus finement les reliefs** dans le cadre du suivi du nettoyage des ravines. Nous avons utilisé Google Earth afin de profiter d’une vue 3D. J’ai également transmis ce besoin à Yohan. L’IGN propose un [site sur Mayotte](https://mayotte.ign.fr/), on peut naviguer sur les différentes photographies aériennes, on aurait pu utiliser ces fonds.
Parmi les autres sujets identifiés, nous avons **besoin de fonds de plans personnalisés**.


<div class="fr-alert fr-alert--info">

Nota : il est possible d’utiliser un autre fond que ceux proposés dans uMap, à partir du moment où il est tuilé. Pour ce faire, cliquer sur les paramètres de la carte en barre de droite et ajouter le lien vers le fond de carte. Pour tuiler un fond de carte, [Mapwarper](https://www.mapwarper.net/) est un outil relativement facile (en anglais).

</div>

L’**usage mobile** de la carte uMap fut très limité à Mayotte (du fait du déploiement tardif de cette carte) mais pourrait être intéressant ailleurs, tout comme l’**usage déconnecté**. Des possibilités techniques existent : une fois le réseau rétabli, les informations sont synchronisées.

## Quelles sont vos priorités dans la perspective, hélas, d’une nouvelle catastrophe ?

Nicolas Godelu : La sécurité civile a besoin d’un outil de cartographie utilisé par des équipes très diverses (plusieurs SDIS), présentes sur le terrain sur une courte durée. Il doit donc **garantir rapidité et simplicité pour des utilisateurs non formés**.
De plus, il ne doit **pas être rattaché à un SDIS en particulier** afin de permettre un transfert rapide du suivi aux autorités locales après le désengagement.
Un groupe de travail des géomaticiens existe (GéoSDIS) mais nous sommes généralement sollicités dans l’urgence, une carte doit être réalisée en quelques heures, il est alors trop tard pour communiquer entre nous et mettre en commun nos outils/données/méthodes. Une solution serait d’**utiliser une équipe Tchap pour gagner en réactivité**.

Enfin, **l’outil uMap pourrait être utilisé par des SDIS pour leurs besoins internes** lorsque qu’ils ne disposent pas d’outils adaptés (réseau de mesures, …).

<figure>
<img src="/static/umap/img/blog/mission-mayotte-nicolas-godelu.jpeg" class="fr-responsive-img" alt="Photo de Nicolas Godelu au micro lors du GéoSDIS 2025.">
<figcaption>

Source : Nicolas Godelu partage cette expérience avec l’ensemble des géomaticiens des SDIS lors du  [GéoSDIS 2025](https://www.sdis34.fr/geosdis2025-dans-lherault/).

</figcaption>
</figure>

<div class="fr-alert fr-alert--info">

Nota : avec la fonctionnalité « temps réel », plusieurs équipes qui interviennent peuvent modifier la carte en même temps.

</div>

Il serait intéressant de **se doter d’un « kit » initialisé par un géomaticien, avec la gestion des droits clé en main, en lien avec Grist, Docs... tous les outils de [la suite numérique de l’État](https://lasuite.numerique.gouv.fr/). Il nous faudrait également un espace de stockage (drive).**
Un moteur de recherche qui permette de naviguer dans les différents fonds de plan disponibles serait un plus, car ils sont nombreux et variés, entre les fonds OSM, IGN, photo aérienne IGN…

*Yohan Boniface est créateur et développeur de uMap depuis son origine en 2013. L'outil étant totalement libre et ouvert, vous pouvez rejoindre la communauté des contributeurs.*

<div class="fr-alert fr-alert--info">

Propos recueillis par Sophie Clairet le 17 avril 2025.

</div>

