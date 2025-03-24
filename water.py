"""
Names: Daniel Bingham, Nikita Gurin
Date: March 20, 2025,
Description: a water Pokémon that has two special moves: water gun and bubble beam.
"""
from pokemon import Pokemon
import random


class Water(Pokemon):
    def __init__(self, name = None):
        """
        Constructor for Water Pokémon objects.
        Inherits from Pokémon class.
        :param name: the name of the water Pokémon.
        """
        super().__init__(name, 1)
        if name is None:
            self._name = random.choice(["Staryu", "Magikarp", "Horsea"])

    def get_special_menu(self) -> str:
        """
        Gets the special menu for water Pokémon.
        :return: str
        """
        return ("\nChoose a move:\n"
                "1. Water Gun\n"
                "2. Bubble Beam")

    def _special_move(self, opponent, move):
        """
        Call special move, water gun or bubble beam,
        depending on move parameter on the opponent.
        :param opponent: the target Pokémon
        :param move: int representing the move
        :return: call to _water_gun or _bubble_beam
        """
        if move == 1:
            return self._water_gun(opponent)
        else:
            return self._bubble_beam(opponent)

    def _water_gun(self, opponent):
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
                f"WATER GUN for {int(dmg * mult)}. {effective}")

    def _bubble_beam(self, opponent):
        """
        Does a random amount of damage from 3-5.
        Multiplies damage by mult which is calculated
        from the _battle_table and Pokémon types.
        :param opponent: the enemy Pokémon
        :return: str
        """
        dmg = random.randint(3, 5)
        mult = self._battle_table[self._poke_type][opponent._poke_type]
        effective = ""
        if mult == 2:
            effective = "It was SUPER EFFECTIVE!"
        elif mult == .5:
            effective = "It was not very effective."
        opponent._take_damage(int(dmg * mult))
        return (f"{self._name} blasts {opponent._name} with a "
                f"BUBBLE BEAM for {int(dmg * mult)}. {effective}")
