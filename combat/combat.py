import math


class combat:
    def __init__(self, player, enemy, special_attack):
        self.player = player
        self.specials = special_attack
        self.enemy = enemy
        defense = False

    def attack(self):
        self.enemy.health -= self.player.damage + self.player.weapon.damage - self.enemy.armor.value
        if (defense == True):
            self.player.armor.value /= 2
            defense = False

        print(f"{self.player.name} attaque {self.enemy.name} et lui inflige {self.player.damage} points de dégats")
        print(f"{self.enemy.name} a {self.enemy.health} points de vie")

    def special_attack(self):
        if (self.player.mp < self.specials.mp_cost):
            print("Vous n'avez pas assez de mana")
            return
        else:
            self.enemy.health -= self.specials.damage - self.enemy.armor.value
            self.player.mp -= self.specials.mp_cost

        if (defense == True):
            self.player.armor.value /= 2
            defense = False

        print(f"{self.player.name} attaque {self.enemy.name} et lui inflige {self.player.special_damage} points de dégats")
        print(f"{self.enemy.name} a {self.enemy.health} points de vie")

    def defend(self):
        if (defense == True):
            self.player.armor.value /= 2
            defense = False
        self.player.armor.value *= 2
        defense = True
        print(f"{self.player.name} se défend")

    def heal(self):
        if self.player.potion == 0:
            print("Vous n'avez pas de potion")
            return
        else:
            self.player.health += 10
            self.player.potion -= 1
        print(f"{self.player.name} se soigne de {self.player.heal} points de vie")
        print(f"{self.player.name} a {self.player.health} points de vie")

    def run(self):
        if math.random() < 0.4:
            print("Vous prenez la fuite")
            if defense == True:
                self.player.armor.value /= 2
                defense = False
            exit()
        else:
            print("Vous ne parvenez pas à fuir")
            return
