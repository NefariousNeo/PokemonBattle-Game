"""
Names: Daniel Bingham, Nikita Gurin
Date: March 20, 2025,
Description: a grass Pokémon that has two special moves: razor leaf and solar beam.
"""
from pokemon import Pokemon
import random


class Grass(Pokemon):
    def __init__(self, name = None):
        """
        Constructor for Grass Pokémon objects.
        Inherits from Pokémon class.
        :param name: the name of the grass Pokémon.
        """
        super().__init__(name, 2)
        if name is None:
            self._name = random.choice(["Oddish", "Bellsprout", "Exeggcute"])

    def get_special_menu(self) -> str:
        """
        Gets the special menu for grass Pokémon.
        :return: str
        """
        return ("\nChoose a move:\n"
                "1. Razor Leaf\n"
                "2. Solar Beam")

    def _special_move(self, opponent, move):
        """
        Call special move, razor leaf or solar beam,
        depending on move parameter on the opponent.
        :param opponent: the target Pokémon
        :param move: int representing the move
        :return: call to razor_leaf or solar_beam
        """
        if move == 1:
            return self._razor_leaf(opponent)
        else:
            return self._solar_beam(opponent)

    def _razor_leaf(self, opponent):
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
        return (f"{self._name} slices {opponent._name} with RAZOR "
                f"sharp LEAVES for {int(dmg * mult)} damage. {effective}")

    def _solar_beam(self, opponent):
        """
        Does a random amount of damage from 3-5.
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
        return (f"{self._name} blasts {opponent._name} with a "
                f"SOLAR BEAM for {int(dmg * mult)} damage. {effective}")
