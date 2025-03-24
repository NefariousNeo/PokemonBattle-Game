"""
Names: Daniel Bingham, Nikita Gurin
Date: March 20, 2025,
Description: a fire Pokémon that has two special moves: ember and fire blast.
"""
from pokemon import Pokemon
import random


class Fire(Pokemon):
    def __init__(self, name = None):
        """
        Constructor for Fire Pokémon objects.
        :param name: the name of the fire Pokémon.
        """
        super().__init__(name, 0)
        if name is None:
            self._name = random.choice(["Pontya", "Growlithe", "Vulpix"])

    def get_special_menu(self) -> str:
        """
        Gets the special menu for fire Pokémon.
        :return: str
        """
        return ("\nChoose a move:\n"
                "1. Ember\n"
                "2. Fire Blast")

    def _special_move(self, opponent, move):
        """
        Call special move, ember or fire blast,
        depending on move parameter on the opponent.
        :param opponent: the target Pokémon
        :param move: int representing the move
        :return:
        """
        if move == 1:
            return self._ember(opponent)
        else:
            return self._fire_blast(opponent)

    def _ember(self, opponent):
        """
        Does a random amount of damage from 2-6.
        Multiplies damage by mult which is calculated
        from the _battle_table and Pokémon types.
        :param opponent: the enemy Pokémon
        :return: str
        """
        dmg = random.randint(2, 6)
        mult = self._battle_table[self._poke_type][opponent._poke_type]
        effective = ""
        if mult == 2:
            effective = "It was SUPER EFFECTIVE!"
        elif mult == .5:
            effective = "It was not very effective."
        opponent._take_damage(int(dmg * mult))
        return (f"{self._name} burns {opponent._name} with EMBER for "
                f"{int(dmg * mult)} damage. {effective}")

    def _fire_blast(self, opponent):
        """
        Does a random amount of damage from 1-7.
        Multiplies damage by mult which is calculated
        from the _battle_table and Pokémon types.
        :param opponent: the enemy Pokémon
        :return: str
        """
        dmg = random.randint(1, 7)
        mult = self._battle_table[self._poke_type][opponent._poke_type]
        effective = ""
        if mult == 2:
            effective = "It was SUPER EFFECTIVE!"
        elif mult == .5:
            effective = "It was not very effective."
        opponent._take_damage(int(dmg * mult))
        return (f"{self._name} blasts {opponent._name} with a "
                f"FIRE BLAST for {int(dmg * mult)} damage. {effective}")
