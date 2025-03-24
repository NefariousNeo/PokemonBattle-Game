"""
Names: Daniel Bingham, Nikita Gurin
Date: March 20, 2025,
Description: the main function where this Pokémon Battle game is run.
"""
import fire
import grass
import water
import random


def main():
    """
    Main function where the game logic is implemented.
    :return: None
    """
    opp_pokemons = []
    for _ in range(3):
        opp_type = random.randint(1, 3)
        if opp_type == 1:
            opp_pokemons.append(fire.Fire())
        elif opp_type == 2:
            opp_pokemons.append(water.Water())
        else:
            opp_pokemons.append(grass.Grass())
    print("PROF OAK: Hello Trainer! Today you're off to\nfight your first "
          "1 vs. 3 Pokémon battle!")
    opp_counter = 1
    for p in opp_pokemons:
        print(f"{opp_counter}. {p}")
        opp_counter += 1
    print("Select the Pokémon that you will battle with.")
    print("1. I choose you, Charmander.\n"
          "2. Squirtle! GO!\n"
          "3. We can do it together, Bulbasaur!")

    your_pokemon = None
    while True:  # validate user input
        try:
            choice = int(input("Choose a Pokemon: "))
            if choice not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Only enter a number (1-3)")
        else:
            if choice == 1:
                your_pokemon = fire.Fire("Charmander")
            elif choice == 2:
                your_pokemon = water.Water("Squirtle")
            elif choice == 3:
                your_pokemon = grass.Grass("Bulbasaur")
            break
        
    print("\n -- TRAINER BATTLE -- ")
    
    while opp_pokemons and your_pokemon is not None:
        print("TRAINER: I choose you:")
        print(f"{opp_pokemons[0]}\n")

        print(your_pokemon)
        while True:  # validate user input
            try:
                attack_type = int(input("Choose an Attack Type:\n"
                                        "1. Normal\n"
                                        "2. Special\n"
                                        "Enter attack type: "))
                if attack_type not in [1, 2]:
                    raise ValueError
            except ValueError:
                print("Only enter a number (1-2)")
            else:
                if attack_type == 1:
                    print(your_pokemon.get_normal_menu())
                if attack_type == 2:
                    print(your_pokemon.get_special_menu())
                while True:  # while loop to validate user input for move
                    try:
                        move = int(input("Enter move: "))
                        if move not in [1, 2]:
                            raise ValueError
                    except ValueError:
                        print("Only enter a number (1-2)")
                    else:
                        break
                break
            
        print(f"\n{your_pokemon.attack(opp_pokemons[0], attack_type, move)}")
        
        if opp_pokemons[0].hp == 0:
            opp_pokemons.pop(0)
            print("TRAINER: NOOOOO! You defeated my pokemon!\n")
            continue

        if opp_pokemons[0].hp > 0:
            print(f"{opp_pokemons[0].attack(your_pokemon, random.randint(1,2), random.randint(1, 2))}\n")

        if your_pokemon.hp == 0:
            print("TRAINER: HA! I defeated you, come back when you get a better Pokemon...")
            break  # end the game if the user's Pokémon's hp is 0

    if not opp_pokemons:  # if the user defeats all 3 Pokémon
        print("\nCongratulations! You won somehow!")


if __name__ == "__main__":
    main()
