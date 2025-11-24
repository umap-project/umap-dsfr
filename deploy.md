# How to deploy on lasuite servers

1. Lancer uMap localement avec l'extension DSFR
1. Corriger si besoin et faire une nouvelle version de umap-dsfr avec un tag de la forme YYYY.MM.DD
    https://github.com/umap-project/umap-dsfr

1. Changer la version de umap et le cas échéant umap-dsfr dans umap-dsfr-moncomptepro (dans le Dockerfile)

    https://gitlab.com/incubateur-territoires/startups/donnees-et-territoires/umap-dsfr-moncomptepro/

1. Commiter et taguer avec la date courante (YYYY.MM.DD) et git push, attendre le temps qu'une nouvelle image soit créée, à suivre sur cette page:

    https://gitlab.com/incubateur-territoires/startups/donnees-et-territoires/umap-dsfr-moncomptepro/-/jobs?kind=BUILD

1. Sur lasuite-deploiement, modifier la version de umap (à la fois pour staging et prod si l'intention est de mettre en prod ensuite), en mettant le tag de umap-dsfr-moncomptepro, sur la branche **umap-staging** (ou sinon il faudra changer
la valeur de TARGET REVISION dans argocd preprod, dans l'onglet DETAILS), dans le fichier suivant:

    manifests/umap/helmfile.yaml

1. Aller sur ArgoCD de preprod:

    https://argocd-preprod.beta.numerique.gouv.fr/applications/argocd/umap-staging

1. Cliquer sur "Sync" et "Synchronize", puis attendre que tous les cœurs soient verts

1. Tester en preprod https://umap-new.dev.incubateur.anct.gouv.fr/

1. Si tout est bon, merger la brancher umap-staging sur main

1. Aller sur ArgoCD de prod:

    https://argocd.beta.numerique.gouv.fr/applications/argocd/umap

1. Sync again, and BOOM, tester en prod :)
