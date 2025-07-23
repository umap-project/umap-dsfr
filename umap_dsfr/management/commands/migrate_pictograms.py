import json
import unicodedata
from pathlib import Path

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from umap.models import DataLayer, Map, Pictogram

FALLBACK_MAPPING = {
    "/uploads/pictogram/archaeological-site-24.png": "/static/umap/icons/osmic/Loisirs - Culture/site-archeologique.svg",
    "/uploads/pictogram/bicycle-24.png": "/home/ybon/Code/py/umap-dsfr/umap_dsfr/static/umap/icons/osmic/Mobilité - Transports/velo.svg",
    "/uploads/pictogram/books-24.png": "/static/umap/icons/osmic/Commerces - Services/librairie.svg",
    "/uploads/pictogram/c%C5%93ur.svg": "/static/umap/icons/osmic/Forme/coeur.svg",
    "/uploads/pictogram/car-24.png": "/static/umap/icons/osmic/Mobilité - Transports/voiture.svg",
    "/uploads/pictogram/castle-defensive-24.png": "/static/umap/icons/osmic/Loisirs - Culture/chateau-fort.svg",
    "/uploads/pictogram/castle-palace-24_pISgQ69.png": "/static/umap/icons/osmic/Loisirs - Culture/site-archeologique.svg",
    "/uploads/pictogram/charging-station-24.png": "/static/umap/icons/osmic/Commerces - Services/borne-recharge.svg",
    "/uploads/pictogram/clock-24.png": "/static/umap/icons/osmic/Divers/horloge.svg",
    "/uploads/pictogram/commercial-24_1.png": "/static/umap/icons/osmic/Bâtiment/immeuble.svg",
    "/uploads/pictogram/dentist-24.png": "/static/umap/icons/osmic/Santé/dentiste.svg",
    "/uploads/pictogram/doctor-24.png": "/static/umap/icons/osmic/Santé/docteur.svg",
    "/uploads/pictogram/doityourself-24.png": "/static/umap/icons/osmic/Commerces - Services/bricolage.svg",
    "/uploads/pictogram/drinking-water-24.png": "/static/umap/icons/osmic/Santé/eau_potable.svg",
    "/uploads/pictogram/elevator-24.png": "/static/umap/icons/osmic/Mobilité - Transports/bouton-ascenseur.svg",
    "/uploads/pictogram/elevator-24_YF20MP0.png": "/static/umap/icons/osmic/Mobilité - Transports/bouton-ascenseur.svg",
    "/uploads/pictogram/embassy-24_QLdIrbF.png": "/static/umap/icons/osmic/Etablissement public/ambassade.svg",
    "/uploads/pictogram/fire-station-24.png": "/static/umap/icons/osmic/Energie/gaz-feu.svg",
    "/uploads/pictogram/florist-24.png": "/static/umap/icons/osmic/Commerces - Services/fleuriste-fleurs.svg",
    "/uploads/pictogram/fort-24.png": "/static/umap/icons/osmic/Loisirs - Culture/chateau-fort.svg",
    "/uploads/pictogram/fountain.svg": "/static/umap/icons/osmic/Plein air et environnement/fontaine.svg",
    "/uploads/pictogram/furniture-24.png": "/static/umap/icons/osmic/Commerces - Services/meuble.svg",
    "/uploads/pictogram/hospital-24_QuccucK.png": "/static/umap/icons/osmic/Etablissement public/hopital.svg",
    "/uploads/pictogram/kiosk-24.png": "/static/umap/icons/osmic/Commerces - Services/kiosque.svg",
    "/uploads/pictogram/kiosk-24_G9G3RYg.png": "/static/umap/icons/osmic/Commerces - Services/kiosque.svg",
    "/uploads/pictogram/laundry-24.png": "/static/umap/icons/osmic/Commerces - Services/laverie.svg",
    "/uploads/pictogram/library-24.png": "/static/umap/icons/osmic/Commerces - Services/librairie.svg",
    "/uploads/pictogram/library-24_GqjNuCi.png": "/static/umap/icons/osmic/Commerces - Services/librairie.svg",
    "/uploads/pictogram/luggage-24.png": "/static/umap/icons/osmic/Commerces - Services/librairie.svg",
    "/uploads/pictogram/metro-24_mTWRUmS.png": "/static/umap/icons/osmic/Mobilité - Transports/rail-metro.svg",
    "/uploads/pictogram/museum-24_g5oBF0Z.png": "/static/umap/icons/osmic/Loisirs - Culture/musee.svg",
    "/uploads/pictogram/nightclub-24.png": "/static/umap/icons/osmic/Loisirs - Culture/musique.svg",
    "/uploads/pictogram/park2-24_1.png": "/static/umap/icons/osmic/Plein air et environnement/parc.svg",
    "/uploads/pictogram/pharmacy-24.png": "/static/umap/icons/osmic/Commerces - Services/pharmacie.svg",
    "/uploads/pictogram/power-wind-24.png": "/static/umap/icons/osmic/Energie/eolienne.svg",
    "/uploads/pictogram/recycling-24.png": "/static/umap/icons/osmic/Plein air et environnement/recyclage.svg",
    "/uploads/pictogram/rental-car-24.png": "/static/umap/icons/osmic/Commerces - Services/location_de_voitures.svg",
    "/uploads/pictogram/shoes-24.png": "/static/umap/icons/osmic/Divers/chaussure.svg",
    "/uploads/pictogram/stationery-24.png": "/static/umap/icons/osmic/Commerces - Services/papeterie.svg",
    "/uploads/pictogram/supermarket-24.png": "/static/umap/icons/osmic/Commerces - Services/supermarche.svg",
    "/uploads/pictogram/swimming-24.png": "/static/umap/icons/osmic/Sport/natation.svg",
    "/uploads/pictogram/toilets-24.png": "/static/umap/icons/osmic/Commerces - Services/toilettes.svg",
    "/uploads/pictogram/town-hall-24.png": "/static/umap/icons/osmic/Etablissement public/mairie.svg",
    "/uploads/pictogram/town-hall-24_2Ayx5vr.png": "/static/umap/icons/osmic/Etablissement public/mairie.svg",
    "/uploads/pictogram/toys-24.png": "/static/umap/icons/osmic/Education/jouets.svg",
    "/uploads/pictogram/tram-stop-24.png": "/static/umap/icons/osmic/Mobilité - Transports/rail-tram.svg",
    "/uploads/pictogram/tree-deciduous-24_lbqtWo6.png": "/static/umap/icons/osmic/Plein air et environnement/parc.svg",
    "/uploads/pictogram/veterinary-24.png": "/static/umap/icons/osmic/Commerces - Services/veterinaire.svg",
    "/uploads/pictogram/viewpoint-24.png": "/static/umap/icons/osmic/Loisirs - Culture/point_de_vue.svg",
    "/uploads/pictogram/water-tower-24.png": "/static/umap/icons/osmic/Bâtiment/chateau-eau.svg",
    "/uploads/pictogram/windmill-24.png": "/static/umap/icons/osmic/Loisirs - Culture/moulin_a_vent.svg",
    "/uploads/pictogram/embassy-24_1.png": "/static/umap/icons/osmic/Etablissement public/ambassade.svg",
    "/uploads/pictogram/industrial-24_1.png": "/static/umap/icons/osmic/Bâtiment/industrie.svg",
    "/uploads/pictogram/star-24-white.png": "/static/umap/icons/osmic/Forme/etoile_pleine.svg",
    "/uploads/pictogram/tree-deciduous.svg": "/static/umap/icons/osmic/Plein air et environnement/parc.svg",
    "/uploads/pictogram/castle-defensive.svg": "/static/umap/icons/osmic/Loisirs - Culture/chateau-fort.svg",
    "/uploads/pictogram/commercial-24.png": "/static/umap/icons/osmic/Bâtiment/immeuble.svg",
    "/uploads/pictogram/government.svg": "/static/umap/icons/osmic/Bâtiment/batiment-officiel.svg",
    "/uploads/pictogram/harbor.svg": "/static/umap/icons/osmic/Mobilité - Transports/port.svg",
    "/uploads/pictogram/railway-halt.svg": "/static/umap/icons/osmic/Mobilité - Transports/rail.svg",
    "/uploads/pictogram/star-24.png": "/static/umap/icons/osmic/Forme/etoile_pleine.svg",
    "/uploads/pictogram/town-hall.svg": "/static/umap/icons/osmic/Etablissement public/mairie.svg",
    "/uploads/pictogram/waste-basket.svg": "/static/umap/icons/osmic/Divers/poubelle.svg",
    "/uploads/pictogram/watchtower.svg": "/static/umap/icons/osmic/Bâtiment/tour.svg",
}


def normalize(s):
    stem = unicodedata.normalize(
        "NFKD", s.replace(" ", "_").replace("'", "").replace("œ", "%C5%93")
    )
    return "".join(c for c in stem if unicodedata.category(c) != "Mn")


def replace_options(options, mapping):
    replaced = False
    if "iconUrl" in options:
        old = options["iconUrl"]
        if old.startswith("/static/"):
            # already done
            return replaced
        if old.startswith("/"):
            key = options["iconUrl"]
            keys = [key]
            alt_key = key.replace("-24", "").replace(".png", ".svg")
            keys.append(alt_key)
            if "_" in alt_key:
                alt_key = alt_key.split("_")[0] + ".svg"
                keys.append(alt_key)
            for key in keys:
                new = mapping.get(key)
                if new:
                    break
            else:
                if not (new := FALLBACK_MAPPING.get(keys[0])):
                    print("!! Missing mapping for", old, keys, options)
                    return replaced
            if not finders.find(new.removeprefix("/static/")):
                print(f"new file does not exist (old: {old}, new: {new})")
            else:
                replaced = True
                options["iconUrl"] = new
    return replaced


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            help="Pretend to delete but just report",
            action="store_true",
        )

    def handle(self, *args, **options):
        pictograms = Pictogram.objects.all()
        mapping = {}
        media_root = Path(settings.MEDIA_ROOT).resolve()
        for picto in pictograms:
            key = picto.pictogram.path.replace(str(media_root), "/uploads")
            mapping[key] = (
                f"/static/umap/icons/osmic/{picto.category}/{Path(picto.pictogram.path).name}"
            )
        for mm in Map.objects.all():
            map_updated = replace_options(mm.settings["properties"], mapping)
            for rule in mm.settings["properties"].get("rules", []):
                map_updated = map_updated or replace_options(rule, mapping)
            if map_updated:
                print("Saved map", mm.pk)
                mm.save()
        geojson_saved = 0
        for dl in DataLayer.objects.all():
            dl_updated = replace_options(dl.settings, mapping)
            for rule in dl.settings.get("rules", []):
                dl_updated = replace_options(rule, mapping)
            if dl_updated:
                dl.save()
            with dl.geojson.open() as f:
                data = json.loads(f.read())
                data_updated = False
                for feature in data["features"]:
                    data_updated = data_updated or replace_options(
                        feature["properties"].get("_umap_options", {}), mapping
                    )
                if data_updated:
                    dl.geojson.save(dl.geojson.name, ContentFile(json.dumps(data)))
                    geojson_saved += 1
                    print("Saved datalayer", dl.pk)
        print("Geojson saved", geojson_saved)
