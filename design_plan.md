# **KeyError: The Keeper of the Golden Key**

**Description:**

This file contains the initial design plan for the adventure game, serving as a blueprint for its development and
helping organise the code and functionality systematically. It details the game ideas, features to implement, and the
main game loop structure.

### TODO

- Change when the room is explored, add the objects to the options menu to investigate

### Idea Brainstorming

- Location
    - Hospital
    - School
    - Manor House (Cludeo like?)

- Theme
    - Old, Abandoned (Escape From Tarkov)
    - Post Apocalypse (Fallout)
    - Zombie theme (Last of Us)
    - Futuristic (Space Engineers)
    - Prison (Prison Architect, The Escapists)

- Scoring system
    - Time-based scoring system?
    - Achievements to get better scores?

- Persistent Storage
    - JSON file system to store game data
    - Store game scores?

- Collectable Items
    - Weapons, Tools, Materials, Useful misc tems

- Usable items
    - ASCCI Map, Golden Key

- Crafting System
    - Collect pieces of the key to craft the Golden Key to win the game

- Locked Doors / Puzzles to reach some rooms of the Hospital.
    - Escape through a locked door with the key

### Game Plan, Design, Structure

#### Game Design

- Location: Hospital
    - Goal: Escape the hospital
    - 6 Rooms with ability to add more easily (code flexibility to add further rooms)
    - Objects in each room that can be explored to find items
- Theme: Mysterious, Abandoned
- Item based progression
    - Collectable items enable game progression with usable items
    - Golden Key Pieces are crafted to escape the hospital
- Scoring System
    - Time based (incentivising replayability and speedrunning)
- Persistent Storage with JSON to store player scores

#### Files

- main: Main game file that contains the game loop and overall game logic.
- menus: Contains functions for displaying various game menus (main menu, inventory, etc.).
- scripts: Contains utility functions and other helper functions
- game_data: Contains game data such as rooms, descriptions, items, and other game-related information.
- tests: Contains unit tests for the game's functions to ensure they work as expected.
- README.md: A Markdown file that provides an overview of the game, instructions on how to play, and any other relevant
  information.

### Main Game Loop Structure

#### Main menu

- Display the main menu with options to start the game, view the leaderboard, remove a leaderboard entry, or exit.
- Get user input for menu choice and handle the corresponding action.

#### Game start

- Display the game start screen with an introduction to the game's story and setting.
- Initialise the player's starting room and inventory.

#### Game loop

- Actions
    - Explore, Inventory, Exit
- Explore
    - Move to another room, investigate objects, collect items
- Inventory
    - View the player's current inventory.
- Exit: Exit the game.
- Handle user input for actions and implement the corresponding game logic for each action.
- If the player collects all necessary items and escapes, display a win screen and update the leaderboard with the
  player's score.
