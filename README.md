# Pokémon Battle Game

Welcome to the Pokémon Battle game! In this game, you will face off against three randomly selected Pokémon in a 1 vs. 3 battle. Choose your Pokémon wisely and use your attacks strategically to defeat your opponents.

## How to Play

1. **Start the Game**: Run the `main()` function to begin the game.
2. **Opponent Selection**: Three opponent Pokémon will be randomly selected from Fire, Water, and Grass types.
3. **Choose Your Pokémon**: Select your Pokémon from the following options:
   - Charmander (Fire type)
   - Squirtle (Water type)
   - Bulbasaur (Grass type)
4. **Battle**: Engage in a battle with each opponent Pokémon. Choose your attack type (Normal or Special) and select your move.
5. **Victory Conditions**: Defeat all three opponent Pokémon to win the game. If your Pokémon's HP reaches zero, you lose the game. Note that it is currently almost impossible to beat this game by defeating all 3 Pokémon.

## Game Logic

The game logic is implemented in the `main()` function. Here is a brief overview of the key components:

- **Opponent Pokémon Selection**: Three opponent Pokémon are randomly selected using `random.randint(1, 3)`.
- **User Pokémon Selection**: The user selects their Pokémon from the available options.
- **Battle Mechanics**: The user and opponent take turns attacking each other. The user chooses the attack type and move, while the opponent's attacks are randomly selected.
- **Victory Conditions**: The game ends when either all opponent Pokémon are defeated or the user's Pokémon's HP reaches zero.

## Installation
Use your terminal.

First, clone this repository:
```bash
git clone https://github.com/NefariousNeo/PokemonBattle-Game
```
Next, navigate to the project directory:
```bash
cd PokemonBattle-Game
```

Ensure you have Python installed!
If not, download it here: https://www.python.org/downloads/

Run the game:
```bash
python main.py
```

Enjoy!

