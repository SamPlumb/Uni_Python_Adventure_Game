"""
KeyError: The Keeper of the Golden Key

This file contains the core logic functions for the KeyError game.

The use of comments and docstrings throughout the codebase enhances readability and maintainability,
allowing other developers (or the future self) to understand the purpose and functionality of each
part of the codebase. This is especially important in a game development context, where multiple
functions may interact in complex ways, and clear documentation can clarify these interactions
and the game logic.

The use of type hints throughout the code provides additional clarity on the expected data types
for function parameters and return values, which can help to prevent bugs and improve
code readability.

Each function includes a description of its purpose, the parameters it accepts, and the results
it produces, providing a clear understanding of its functionality. This approach
makes testing and debugging easier. The documentation section discusses the method used to
create the function, why the approach was chosen, and any relevant information about the
function's role in the game.
"""

import json
import random
from datetime import timedelta
from shutil import get_terminal_size
from sys import exit as sys_exit
from textwrap import wrap
# Imports -
from time import sleep, time

# Local imports -
import menus


def d_box(text: list[str], align: int):
    '''
    ### Dynamic Box Function
    This function creates a dynamically sized box around a list of strings. 
    Text wrapping is used to ensure that long strings fit within the box and terminal window.
    The box is centred in the terminal, and the text can be aligned left, right, or center based 
    on the align parameter.

    #### Parameters:
    - text (list[str]): A list of strings to be displayed within the box.
    - align (int): Alignment of the text within the box. 0 = left, 1 = right, 2 = center.

    #### Exceptions:
    - ValueError: If the align parameter is not 0, 1, or 2
    - ValueError: If the text parameter is not a list of strings.

    #### Results:
    - The list of strings displayed within a dynamic box with specified alignment.

    #### Documentation:
    Good menu design is fundamental to creating an engaging user experience in text-based games. 
    Players should be able to easily understand and navigate the menus, which is achieved through 
    clear labelling, consistent layout, and intuitive design to avoid confusion and enhance 
    immersion (Krishnamohan Yagneswaran, 2024).

    This function aims to improve readability and user comfort by creating a consistent box design
    for all menus, enhancing the visual appeal of the game interface. The box is centred to keep
    the player's focus on the content, and text wrapping ensures that all information is visible
    without overwhelming the player with long lines of text that may extend beyond the terminal 
    width.
    '''

    # Parameter validation and set alignment string
    alignment: str = "^"

    if align == 0:
        alignment: str = "<"

    elif align == 1:
        alignment: str = ">"

    elif align == 2:
        alignment: str = "^"

    elif align not in [0, 1, 2]:
        raise ValueError(
            "Alignment must be 0 (left), 1 (right), or 2 (center).")

    # Text validation and box width calculations
    if isinstance(text, list) and all(isinstance(item, str) for item in text):

        longest_item = max(text, key=len)
        max_width = min(len(longest_item) + 4,
                        get_terminal_size().columns - 6,
                        150)

    else:
        raise ValueError("Text must be a list of strings.")

    # Text wrapping and box width calculation
    wrapped_lines = []

    for item in text:

        if len(item) > max_width - 4:
            wrapped_lines.extend(wrap(item, width=max_width - 4))

        else:
            wrapped_lines.append(item)

    box_width = max(len(line) for line in wrapped_lines) + 4
    terminal_width = get_terminal_size().columns
    padding = max(0, (terminal_width - box_width - 2) // 2)

    # Build and print the text box
    print(" " * padding + f"╔{'═' * box_width}╗")

    for item in wrapped_lines:

        if "\033[1m" in item and "\033[0m" in item:
            print(" " * padding + f"║ {item:{alignment}{box_width + 6}} ║")

        else:
            print(" " * padding + f"║ {item:{alignment}{box_width - 2}} ║")

    print(" " * padding + f"╚{'═' * box_width}╝")


def exit_game(delay: int = 3):
    '''
    ### Exit Game Function
    This function prints an exit message, waits for a specified delay in seconds,
    and then exits the game.

    #### Parameters:
    - delay (int): The number of seconds to wait before exiting the game. (Default: 3)

    #### Results:
    - Prints an exit message, waits for the specified delay, and then exits the game.

    #### Documentation:
    sys.exit() over other exit methods is considered the practice to exit a Python 
    program as it raises the SystemExit exception without relying on the site module, 
    allowing for a clean exit and proper cleanup of resources (McKee, 2024). 
    exit() and quit() are not recommended for production code as they are intended
    for use within the Python interpreter and may not work as expected in all environments.

    A delay before sys.exit() is called is included purely to allow the player to read 
    the exit message before the game closes, enhancing the user experience so the player 
    does not miss the message. 
    '''

    sleep_delay = delay

    d_box(["Thank you for playing!",
           "Exiting Game..."], align=2)

    sleep(sleep_delay)
    sys_exit()


def start_timer():
    '''
    ### Start Game Timer Function
    This function starts the game timer by recording the current time in seconds 
    when the game begins.

    #### Results:
    - The current time in seconds as an integer when the function is called.

    #### Documentation:
    The time() function from the time module returns the current time in seconds, 
    providing a simple and effective way to track the player's time to complete the 
    game as a scoring mechanism.
    '''

    return int(time())


def end_timer(start_time: int):
    '''
    ### End Game Timer Function
    This function calculates the time difference between the start time and the current time,
    in seconds, to determine total time taken to complete the game.

    #### Parameters:
    - start_time (int): The start time in seconds when the game timer was initiated.

    #### Results:
    - The time difference between the start time and the current time in seconds as an integer.

    #### Documentation:
    By calculating the time difference between the start and end times, we can determine the total
    time taken by the player to complete the game, which is used as a scoring mechanism.
    '''

    return int(time() - start_time)


def calculate_score(p_time: int):
    '''
    ### Calculate and format player score function
    This function takes the player's game time in seconds and converts it into a more
    readable format using hours, minutes, and seconds.

    #### Parameters:
    - p_time (int): The player's game time in seconds.

    #### Results:
    - str: A formatted string representing the player's time in hours, minutes, and seconds.

    #### Documentation:
    Time-based scoring enables a techniques called speedrunning, where players aim to 
    complete the game in the shortest time possible, adding replayability and competition 
    through the leaderboard (Lafond, 2018).
    '''

    p_time_str = str(timedelta(seconds=int(p_time))).split(":")

    if int(p_time_str[0]) == 0:  # If hours is 0

        p_time_str.pop(0)

        if int(p_time_str[0]) == 0:  # If minutes is 0

            p_time_str.pop(0)

            # If player time only includes seconds
            return f"{int(p_time_str[0])} Seconds"

        # If player time includes minutes print minutes and seconds
        return f"{int(p_time_str[0])} Minutes, {int(p_time_str[1])} Seconds"

    # If player time includes hours print full time
    return f"{int(p_time_str[0])} Hours, {int(p_time_str[1])} Minutes, {int(p_time_str[2])} Seconds"


def menu_delay(delay=0.5):
    '''
    ### Menu Delay Function
    This function introduces a delay between menu displays to enhance the user 
    experience by preventing menus from appearing too quickly.

    #### Parameters:
    - delay (float): The number of seconds to wait before displaying the next menu. (Default: 0.5)

    #### Results:
    - The game will pause for the specified time before proceeding to the next menu or action.

    #### Documentation:
    Introducing a delay between menus can improve the user experience by allowing players 
    to read and process the information on the screen before the next menu appears, 
    preventing confusion and menus from appearing too quickly. This is especially important 
    in text-based games where players rely on reading the text to understand the game 
    state and make decisions. 
    '''

    return sleep(delay)


def get_usable_items(plr_inv_dict: dict, usable_items: list) -> list:
    '''
    ### Get Usable Items Function
    This function checks the player's inventory against a list of usable game
    items to determine which items can be used.

    #### Parameters:
    - plr_inv_dict (dict): The player's inventory dictionary.
    - usable_items (list): A list of items usable in the game.

    #### Results:
    - list: A list of item names that the player can currently use based on their inventory.

    #### Documentation:
    The function filters the list of usable items to include only items in the player's 
    inventory with a quantity greater than 0, ensuring that players can only attempt 
    to use items they actually have. It is essential to perform these validation 
    steps for the game logic to function correctly, preventing errors, for instance, 
    when trying to use non-existent items. The result of this function is a list of 
    usable items that is used in menus or other game scripts.
    '''

    usable_items = [
        item for item in usable_items if plr_inv_dict.get(item, 0) > 0]

    return usable_items


def get_craftable_items(plr_inv_dict: dict, crafting_recipes: dict) -> list:
    '''
    ### Craftable Items Function
    This function checks the player's inventory against the crafting recipes
    to determine which items can be crafted.

    #### Parameters:
    - plr_inv_dict (dict): The player's inventory dictionary.
    - crafting_recipes (dict): A dictionary containing the crafting recipes.

    #### Results:
    - list: A list of item names that the player can currently craft based on their inventory.

    #### Documentation:
    The function filters crafting recipes to include only those for which the player has 
    the required materials in their inventory, ensuring players can only attempt to 
    craft items they have the resources for, preventing errors or false positives that 
    could enable crafting something that shouldn't be craftable. The result of this 
    function is a list of craftable items that is used in menus or other game scripts.
    '''

    # Filter the crafting recipes to include only those that can currently be crafted
    craftables = [
        item for item, requirements in crafting_recipes.items()
        if all(plr_inv_dict.get(req, 0) >= qty for req, qty in requirements.items())
    ]

    return craftables


def distribute_r_objects(r_object_dict: dict, rooms_dict: dict) -> dict:
    '''
    ### Distribute Room Objects to All Rooms Function
    This function distributes room objects randomly across all rooms, 
    each room receives 2 random objects from the room_items dictionary.

    #### Parameters:
    - r_object_dict (dict): Dictionary of room objects.
    - rooms_dict (dict): Dictionary of rooms to distribute objects across.

    #### Results:
    - rooms_dict (dict): Updated rooms dictionary with room objects distributed.

    #### Documentation:
    This function ensures that each room has a unique set of objects, 
    enhancing the game's unpredictability and replayability. 
    By randomly distributing objects, players will have different 
    experiences each time they play, encouraging exploration and discovery 
    as they cannot rely on memorising object locations.
    '''

    # List of all room objects names
    base_items = [item for item in r_object_dict.keys()]

    # Build a pool large enough for all rooms
    required_items = len(rooms_dict) * 2
    item_pool = []

    while len(item_pool) < required_items:
        item_pool.extend(random.sample(base_items, len(base_items)))

    # Distribute 2 objects to each room
    for room_id in rooms_dict.keys():
        rooms_dict[room_id]["objects"] = [item_pool.pop() for _ in range(2)]

    return rooms_dict


def distribute_plr_items(p_items_dict: dict, rooms_dict: dict) -> dict:
    '''
    ### Distribute Player Items To All Rooms Function
    This function randomly distributes 2 items per room in the hospital, 
    with 3 Golden Key Pieces and 1 Surgical Glue, which are required to win the game.

    #### Parameters:
    - p_items_dict (dict): Dictionary of player items.
    - rooms_dict (dict): Dictionary of rooms to distribute items across.

    #### Results:
    - rooms_dict (dict): Updated rooms dictionary with player items distributed.

    #### Documentation:
    This function ensures that essential items required to win the game are 
    included in the distribution, while also providing a variety of other 
    items to enhance gameplay. The random distribution of items adds an element 
    of unpredictability, encouraging players to explore and interact with different 
    rooms to find the necessary items to progress and ultimately win the game.
    '''

    essential_items = ["Golden Key Piece",
                       "Golden Key Piece",
                       "Golden Key Piece",
                       "Surgical Glue"]

    # List of all player items with essential items included without duplicates
    base_items = [item for item in p_items_dict.keys()
                  if item not in essential_items]

    # Total items needed minus essential items
    required_items = len(rooms_dict) * 2 - len(essential_items)

    while len(base_items) < required_items:
        base_items.extend(random.sample(base_items, len(base_items)))

    all_items = base_items + essential_items

    random.shuffle(all_items)

    # Distribute 2 items to each room
    for room_id in rooms_dict.keys():
        rooms_dict[room_id]["player_items"] = [all_items.pop()
                                               for _ in range(2)]

    return rooms_dict


def plr_spawn(rooms_dict: dict) -> str:
    '''
    ### Player Spawn Function
    This function randomly selects a starting room for the player at the beginning of the game.

    #### Parameters:
    - rooms (dict): The dictionary containing all room information.

    #### Results:
    - str: The name of the randomly selected starting room for the player.

    #### Documentation:
    Selecting a random starting room introduces variability to the game, 
    offering a different experience each time it's played. This feature promotes 
    exploration and stops players from relying on memorising a fixed starting point, 
    boosting replayability and engagement.
    '''

    return random.choice([room_info["name"] for room_info in rooms_dict.values()])


def get_room_objects_and_items(current_room: str, rooms_dict: dict) -> tuple[list, list]:
    '''
    ### Current Room Investigate Function
    This function retrieves the objects and player items in the 
    current room for further investigation and determines what 
    the player can interact with there.

    #### Parameters:
    - current_room (str): The name of the current room.
    - rooms (dict): The dictionary containing all room information, 
    including objects and player items.

    #### Results:
    - tuple[list, list]: A tuple containing two lists:
    - The first list contains the objects available in the current room for investigation.
    - The second list contains the player items.

    #### Documentation:
    This is a reusable, modular function that gathers items for the current room to be 
    used with the main game loop, enabling the player to examine the current room and 
    see which objects and items are available for interaction. By retrieving this information, 
    the game can offer the player options to interact with the room's contents, 
    enhancing the gameplay experience and encouraging exploration.
    '''

    room_objects = []
    plr_items = []

    # Get current room data
    for _, room_info in rooms_dict.items():

        if room_info["name"] == current_room:
            room_objects = room_info["objects"]
            plr_items = room_info["player_items"]

    return room_objects, plr_items


def exits_current_room(current_room: str, rooms_dict: dict) -> list:
    '''
    ### Exits In Current Room Function
    This function retrieves the list of exits available in the current room.

    #### Parameters:
    - current_room (str): The name of the current room.
    - rooms (dict): The dictionary containing all room information.

    #### Results:
    - list: A list of exits available in the current room. Returns empty list if room not found.

    #### Documentation:
    This helper function enables the game to identify the available exits in 
    the current room, allowing the player to navigate through the hospital. 
    It achieves this by retrieving the current exits, offering movement 
    options to the player, which enhances the gameplay experience and promotes exploration.
    '''

    for _, room_info in rooms_dict.items():

        if room_info["name"] == current_room:
            return room_info["exits"]

    return []


def pick_up_plr_item(current_room: str, rooms_dict: dict,
                     item: str, plr_inv_dict: dict, item_index: int):
    '''
    ### Pick Up Player Item Function
    This function allows the player to pick up an item from the current room 
    and add it to their inventory. The item is transferred to the player's inventory 
    and removed from the room. This function activates when the player decides to 
    pick up an item while investigating a room.

    #### Parameters:
    - current_room (str): The name of the current room.
    - rooms (dict): The dictionary containing all room information.
    - item (str): The name of the item to be removed from the room.
    - plr_inv_dict (dict): The player's inventory dictionary.
    - item_index (int): The index of the item being investigated.

    #### Results:
    - The player item is added to the player's inventory and 
    removed from the room's player items list.
    - If the item has already been picked up, the function does nothing.

    #### Documentation:
    This function enables players to interact with the environment by picking up items, 
    which is a key element of adventure games. Transferring items from the room to the 
    player's inventory allows players to gather resources and advance through the game. 
    The function includes validation to ensure that the item is present in the room and 
    has not already been collected, preventing errors and providing a seamless gameplay experience.
    '''

    for _, room_info in rooms_dict.items():

        if room_info["name"] == current_room:

            # Check if item is in the room and not already picked up
            if item in room_info["player_items"] and item != "Empty":
                # Add item to player inventory
                plr_inv_dict[item] = plr_inv_dict.get(item, 0) + 1

                # Remove item from room
                room_info["player_items"][item_index] = "Empty"


def use_item(plr_inv_dict: dict, current_room: str, item: str) -> bool:
    '''
    ### Use Item Function
    This function handles the usage of items from the player's inventory.
    Validation confirms that the item exists, is usable, and performs the appropriate action.

    #### Parameters:
    - plr_inv_dict (dict): The player's inventory dictionary.
    - current_room (str): The name of the current room.
    - item (str): The name of the item to use.

    #### Result:
    - bool: True if the win condition is met, False otherwise.

    #### Documentation:
    This function allows players to use items from their inventory, which is essential 
    for interacting with the game world and progressing through the level. 
    By validating items and their effects, the function ensures that players can only 
    use items they have. Correct actions are taken based on the item used,
    thereby enabling a positive gameplay experience and helping them complete the game successfully.
    '''

    if plr_inv_dict.get(item, 0) <= 0:
        d_box(["You cannot use that item."], 2)
        return False

    # Define item effects
    item_effects = {
        "Map": lambda: (menus.open_map(), False)[1],
        "Golden Key": lambda: True if current_room == "Hospital Reception" else
        (d_box(["You try to use the Golden Key, but cannot find a suitable lock."], 2), False)[1]
    }

    if item in item_effects:
        return item_effects[item]()

    d_box(["You cannot use that item."], 2)
    return False


def craft_item(plr_inv_dict: dict, crafting_recipes: dict, item: str) -> bool:
    '''
    ### Crafting Function
    This functions handles the crafting of items, allowing the player to combine items into
    new items based on predefined crafting recipes.

    #### Parameters:
    - plr_inv_dict (dict): The player's inventory dictionary.
    - crafting_recipes (dict): A dictionary containing the crafting recipes.
    - item (str): The name of the item to craft.

    #### Result:
    - bool: True if the item was successfully crafted, False otherwise.

    #### Documentation:
    Crafting is a common mechanic in adventure games that allows players to combine items
    to create new ones, which adds depth to gameplay. This function verifies whether 
    the player has the necessary items in their inventory to craft the desired item 
    according to the crafting recipes. If the player meets the requirements, 
    the function updates the player's inventory by adding the crafted item and removing 
    the used materials. This introduces a level of complexity to the game, 
    requiring multiple items to escape the hospital and win the game.
    '''

    if item not in crafting_recipes:
        d_box(["You cannot craft that item."], 2)
        return False

    requirements = crafting_recipes[item]

    # Check if player has the required items in their inventory
    if all(plr_inv_dict.get(req, 0) >= qty for req, qty in requirements.items()):

        # Remove the crafting requirements from the player's inventory
        for req, qty in requirements.items():
            plr_inv_dict[req] -= qty

        # Add the crafted item to the player's inventory
        plr_inv_dict[item] = plr_inv_dict.get(item, 0) + 1
        return True

    # If the requirements are not met (should not be possible due to get_craftable_items validation)
    return False


# Leaderboard Functions -
def load_leaderboard(filename: str = "leaderboard.json") -> list[dict]:
    '''
    ### Load Leaderboard Function
    This function loads the leaderboard data from a specified JSON file
    (filename parameter). Potential errors are handled to prevent crashes,
    and the loaded data is returned as a list of dictionaries, sorted by 
    score in ascending order. 

    #### Parameters:
    - filename (str): The name of the JSON file to load the leaderboard data from.

    #### Exceptions:
    - FileNotFoundError: If the specified file does not exist.
    - Exception: To catch any other potential errors.

    #### Results:
    - leaderboard_data (list[dict]): A list of dictionaries containing the leaderboard data 
    with player names as keys and their times in seconds as values.
    - If the file is not found or an error occurs, the function returns an empty list.

    #### Documentation:
    This function allows players to load stored leaderboard data, to see their scores 
    and compare them with others, even after the game has been closed, promoting 
    replayability and competition. The function includes error handling to address 
    potential issues, ensuring the game can handle errors without crashing.
    '''

    try:
        with open(filename, "r", encoding="utf-8") as file:

            leaderboard_data = json.load(file)

            # Sort the leaderboard data by score in ascending order (lower times are better)
            leaderboard_data.sort(key=lambda x: x["score"])

            return leaderboard_data

    except FileNotFoundError:

        return []

    except Exception:

        return []


def save_leaderboard(leaderboard_data: list[dict], filename: str = "leaderboard.json"):
    '''
    ### Save Leaderboard Function
    This function takes a list of dictionaries containing player data saving
    it to a specified JSON file with proper formatting.

    #### Parameters:
    - leaderboard_data (list[dict]): A list of dictionaries containing the leaderboard data.
    - filename (str): The name of the JSON file to save the leaderboard data to.

    #### Exceptions:
    - IOError: If there is an error writing to the file.
    - Exception: To catch any other potential errors.

    #### Results:
    - If the file is saved successfully, the function returns None.
    - If an error occurs, the function displays an error message.

    #### Documentation:
    This function stores leaderboard data, allowing players to see their scores even 
    after the game has closed. The persistent style of recording player scores enables
    anyone who has the leaderboard save file to compete and try to beat each other's 
    scores, which increases the game's real-world applicability beyond a demo. 
    The saving function includes error handling to address potential issues, 
    ensuring the game can handle errors without crashing and losing any unsaved data.
    '''

    # Sort the leaderboard data by score in ascending order (lower times are better)
    leaderboard_data.sort(key=lambda x: x["score"])

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(leaderboard_data, file, indent=4)

    except IOError as error:
        d_box(["An error occurred while saving leaderboard: " + str(error)], 2)
    except Exception as error:
        d_box(["An unexpected error occurred: " + str(error)], 2)


def add_new_score(p_name: str, p_time: int, filename: str = "leaderboard.json"):
    '''
    ### Add New Score To Leaderboard Function
    This function loads existing leaderboard data from the JSON file specified 
    by the filename parameter, formats the game data for JSON storage, and 
    overwrites the file with the updated leaderboard. If no existing leaderboard 
    data is found, it creates a new leaderboard with the provided player's name and time.
    
    #### Parameters:
    - p_name (str): The name of the player to add to the leaderboard.
    - p_time (int): The time taken by the player to complete the game.
    - filename (str): The name of the JSON file to load and save the leaderboard data.

    #### Exceptions:
    - ValueError: If the player name is invalid (not a string or empty).
    - ValueError: If the player time is invalid (not an integer or negative).

    #### Results:
    - If the score is successfully added, the function saves the updated leaderboard and
    returns None.
    - If the player name or time is invalid, the function displays an appropriate error message
    and does not add the score to the leaderboard.

    #### Documentation:
    This logic function adds collected data to the leaderboard, allowing players to view 
    the new score, promoting replayability and competition. The function calls other 
    functions to perform more modular tasks, such as loading and saving elements.
    '''

    # Data Validation
    if not p_name or not isinstance(p_name, str):
        d_box(["Invalid player name. Score not added to leaderboard."], 2)
        return

    if not isinstance(p_time, (int, float)):
        d_box(["Invalid player time. Score not added to leaderboard."], 2)
        return

    if p_time < 0:
        d_box([f"You must have super powers to have a score of {p_time}."
               "Score not added to leaderboard."], 2)
        return

    leaderboard_data = load_leaderboard(filename) or []

    new_score = {"player_name": p_name.capitalize(),
                 "score": p_time}

    leaderboard_data.append(new_score)

    save_leaderboard(leaderboard_data, filename)


def remove_score_from_leaderboard(leaderboard_entry: dict, filename: str = "leaderboard.json"):
    '''
    ### Remove Player Score From Leaderboard Function
    This function loads the existing leaderboard data from a JSON file, removes the 
    selected player's data from the leaderboard if it exists, and then overwrites the JSON file. 

    #### Parameters:
    - leaderboard_entry (dict): The leaderboard entry to remove.
    - filename (str): The name of the JSON file to load and save the leaderboard data.

    #### Results:
    - If the entry is successfully removed, the function saves the updated leaderboard and
    displays a confirmation message. 
    - If the entry is not found or if there is an error, the function 
    displays an appropriate error message.

    #### Documentation:
    This function enables players to remove their scores, allowing them 
    to manage leaderboard entries and correct mistakes or remove 
    unwanted scores. The function includes error handling to account 
    for cases where the entry does not exist or where loading the leaderboard 
    data fails, preventing crashes and providing feedback to the user.
    '''

    leaderboard_data = load_leaderboard(filename) or []

    # Can only be called when there are leaderboard entries, but this is here as a safeguard.
    if not leaderboard_data:
        d_box(["An error has occurred, No leaderboard data available."], 2)
        return

    updated_leaderboard = [
        entry for entry in leaderboard_data if entry != leaderboard_entry]

    # Safeguard as this function is only called when the entry exists.
    if len(updated_leaderboard) == len(leaderboard_data):
        d_box(["An error has occurred, Player not found in leaderboard."], 2)
        return

    # If the entry was removed successfully, save the updated leaderboard
    save_leaderboard(updated_leaderboard, filename)
    d_box(["The leaderboard entry has been removed from leaderboard."], 2)
    return

# END OF FILE #
