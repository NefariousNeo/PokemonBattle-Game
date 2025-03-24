"""
Names: Daniel Bingham, Nikita Gurin
Date: March 20, 2025,
Description: a Poke abstract base class
"""

import random
import abc


class Pokemon(abc.ABC):
    def __init__(self, name , p_type):
        """
        The constructor for Pokemón objects.
        :param name: the name of the Pokemón
        :param p_type: the type of Pokemón
        """
        self._name = name
        self._poke_type = p_type
        self._battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]]
        self._hp = 25

    @property
    def hp(self):
        """
        Returns the current HP of the Pokemón.
        :return: self._hp
        """
        return self._hp

    def get_normal_menu(self):
        """
        Returns the normal move menu of the Pokemón.
        :return: a string of the normal move menu
        """
        return ("\nChoose a move:\n"
                "1. Slam\n"
                "2. Tackle")

    def _normal_move(self, opponent, move):
        """
        Calls self._slam or self._tackle
        depending on move parameter on the opponent.
        :param opponent: the enemy Pokemón
        :param move: an int representing the move
        :return: a call to self._slam or self._tackle
        """
        if move == 1:
            return self._slam(opponent)
        else:
            return self._tackle(opponent)

    def _slam(self, opponent):
        """
        Deals a random amount of damage (2-6)
        to the opponent.
        :param opponent: the enemy Pokemón
        :return: a string displaying who slams who and the damage dealt.
        """
        dmg = random.randint(2, 6)
        opponent._take_damage(dmg)
        return f"{self._name} SLAMS {opponent._name} for {dmg} damage"

    def _tackle(self, opponent):
        """
        Deals a random amount of damage (3-5)
        :param opponent: the enemy Pokemón
        :return: a string displaying who tackles who and the damage dealt.
        """
        dmg = random.randint(3, 5)
        opponent._take_damage(dmg)
        return f"{self._name} TACKLES {opponent._name} for {dmg} damage."

    @abc.abstractmethod
    def get_special_menu(self) -> str:
        """
        Returns the special menu of the Pokemón.
        Not implemented yet.
        :return: str
        """
        pass

    @abc.abstractmethod
    def _special_move(self, opponent, move) -> str:
        """
        Calls special move depending on the move parameter on the opponent.
        :param opponent: the enemy Pokemón
        :param move: int representing the move
        :return: str
        """
        pass

    def attack(self, opponent, type, move):
        """
        Calls self._normal_move or self._special_move depending
        on the move parameter on the opponent.
        :param opponent: the enemy Pokemón
        :param type: the type of move (normal/special) as int 1-2
        :param move: the int representing the move
        :return: a call to self._normal_move or self._special_move
        """
        if type == 1:
            return self._normal_move(opponent, move)
        else:
            return self._special_move(opponent, move)

    def __str__(self):
        """
        Prints the Pokemón's status as a string.
        :return: str (Pokemón's status)
        """
        return f"{self._name} HP: {self._hp}/25"

    def _take_damage(self, dmg):
        """
        Allows the Pokemón to take damage and makes sure
        self._hp does not go below 0 and if so reset to 0.
        :param dmg: the amount of damage dealt
        :return: None
        """
        self._hp -= dmg
        if self._hp <= 0:
            self._hp = 0



