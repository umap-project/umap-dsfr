---
title: Interopérabilité Qgis - uMap
date: 2025-03-28
description: La Carte des écoles de l’Aude utilise deux outils, Qgis et uMap pour profiter des atouts de chacun. Thierry Munoz, Enseignant Référent aux Usages du Numérique (ERUN) de la Circonscription Lézignan-Corbières et Minervois détaille sa méthode.
image: /static/umap/img/blog/interoperabilite-qgis.png
image_alt: Carte uMap des écoles de l’Aude 2024.
tags:
    - Témoignage
---

*[La Carte des écoles de l’Aude](https://umap.incubateur.anct.gouv.fr/fr/map/ecoles-de-laude-2024_269#10/43.0719/2.5461) utilise deux outils, Qgis et uMap pour profiter des atouts de chacun. Thierry Munoz, Enseignant Référent aux Usages du Numérique (ERUN) de la Circonscription Lézignan-Corbières et Minervois détaille sa méthode :*


Je travaille avec [QGIS](https://docs.qgis.org/3.40/fr/docs/user_manual/index.html), car je peux lier des données json (limites des communes, du département, localisation des écoles) à un tableur avec comme clé commune le n°INSEE et/ou l’UAI (Unité Administrative Immatriculée). L’interface demande moins de clics qu’un travail direct dans uMap qui nécessite de naviguer dans les différents menus. Pour une quantité de données faibles, il est envisageable de réaliser la carte directement dans uMap, ce n’est pas le car lorsque les données sont nombreuses : QGIS est alors plus ergonomique. La courbe d’apprentissage de Qgis est élevée, mais elle vaut le détour.

J’ai utilisé cette méthode bien avant la mise en place de l’instance uMap pour les agents publics afin de dépasser les limites d’uMap avec une solution plus puissante. Ce serait peut-être moins nécessaire aujourd’hui, avec les progrès de uMap.
**J’ai choisi QGIS, car c’est un logiciel libre, ce qui le rend donc plus pérenne et accessible au plus grand nombre** : tant qu’à se former, mieux vaut investir dans du durable plutôt qu’être à la merci des éditeurs propriétaires ou des passations de marché qui peuvent imposer un changement d’outil « du jour au lendemain ».

Je possède donc un modèle de base dans QGIS sur lequel je m’appuie à chaque fois pour créer de nouvelles cartes. Ainsi, je me contente de changer la table de données liées pour avoir de nouvelles informations et réaliser les filtres que je souhaite.
L’intérêt de QGIS réside également dans le fait de pouvoir travailler hors-ligne et de ne publier dans uMap que le travail final. Qgis permet aussi d’imprimer au format pdf, selon différents styles à l’aide de modèles pré-établis (page A4, A3, filtrages spécifiques…) et de gagner du temps une fois créés ces modèles ré-utilisables.

Par contre **uMap permet justement une publication en ligne impossible avec QGIS** (à moins d’installer un serveur et une machinerie lourde) avec la limitation en termes d’accès sécurisé. Le fait de ne pas pouvoir limiter l’accès des cartes uMap aux seuls services ou personnes autorisés, réduit l’intérêt professionnel pour un usage en interne de uMap avec des données « sensibles ».

> On pourrait envisager par exemple une carte permettant de gérer dynamiquement les moyens de remplacements du premier degré sur le département au jour le jour au niveau de la DSDEN (Direction des services départementaux de l’Éducation nationale) et faire en sorte que les circonscriptions disposent et complètent la carte au moment. La carte reste à construire complètement, mais voici un usage qui me semblerait intéressant et qui n’est pas possible actuellement.

**Grâce à l’interopérabilité permise avec des formats de fichiers ouverts, je peux échanger des données entre ces deux outils que sont QGIS et uMap**, ce qui à mon sens les rend très complémentaires.

<div class="fr-alert fr-alert--info">

Grand merci à Thierry Munoz pour le partage d’expérience, le 28 mars 2025.

</div>
