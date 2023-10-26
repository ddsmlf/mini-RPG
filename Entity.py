import json

class Entity:
    def __init__(self, nom, classe, pv_max, pv, mp_max, mp, force, armure, arme, liste_pouvoirs, defense, emplacement):
        self.nom = nom
        self.classe = classe
        self.pv_max = pv_max
        self.pv = pv
        self.mp_max = mp_max
        self.mp = mp
        self.force = force
        self.armure = armure
        self.arme = arme
        self.liste_pouvoirs = liste_pouvoirs
        self.defense = defense
        self.emplacement = emplacement

    def combat(self, action, cible, player, competence=None):
        pass
        # sauvegarde des attributs de l'entité dans un fichier json


    def sauvegarder(self):
        sauvegarde = {}
        sauvegarde[self.nom] = {
            "classe": self.classe,
            "pv_max": self.pv_max,
            "pv": self.pv,
            "mp_max": self.mp_max,
            "mp": self.mp,
            "force": self.force,
            "armure": self.armure,
            "arme": self.arme,
            "liste_pouvoirs": self.liste_pouvoirs,
            "defense": self.defense,
            "emplacement": self.emplacement
        }

        try:
            with open("save.json", "r") as fichier_sauvegarde:
                sauvegarde_precedente = json.load(fichier_sauvegarde)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            sauvegarde_precedente = {}

        sauvegarde_precedente.update(sauvegarde)

        with open("save.json", "w") as fichier_sauvegarde:
            json.dump(sauvegarde_precedente, fichier_sauvegarde, indent=4)

