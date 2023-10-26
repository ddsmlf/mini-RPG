import json

class Entity:
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        self.emplacement = (0,0)
        
        # Charge les caractéristiques à partir du fichier "stack.json"
        with open("stack.json", "r") as fichier_stack:
            data = json.load(fichier_stack)
            types_personnages = data.get("types_personnages")
            for type_personnage in types_personnages:
                if type_personnage["nom"] == self.classe:
                    self.pv_max = type_personnage["pv_max"]
                    self.mp_max = type_personnage["mp_max"]
                    self.force = type_personnage["force"]
                    self.liste_pouvoirs = type_personnage["liste_pouvoirs"]
                    self.defense = type_personnage["defense"]
        self.pv = self.pv_max
        self.mp = self.mp_max

    def combat(self, action, cible, player, competence=None):
        pass
        # Sauvegarde des attributs de l'entité dans un fichier JSON

    def deplacer(self, direction):
        pass

    def changer_tenue(self, tenue):
        pass

    def sauvegarder(self):
        sauvegarde = {}
        sauvegarde[self.nom] = {
            "classe": self.classe,
            "pv_max": self.pv_max,
            "pv": self.pv,
            "mp_max": self.mp_max,
            "mp": self.mp,
            "force": self.force,
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
