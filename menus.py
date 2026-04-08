"""
KeyError: The Keeper of the Golden Key

Each menu function includes a description of the menu's purpose, the parameters it accepts,
and the output it produces. The menus are designed to appear in a dynamic box (d_box) to maintain
a consistent user interface throughout the game. Separating the menu functions into a
distinct module enhances organisation and ease of maintenance, making it simpler to
update or modify the menus without impacting the core game logic.
"""

# Imports -
import random

import scripts


def invalid_choice_menu(user_choice: str, num_choices: int):
    '''
    ### Invalid Choice Menu Function
    This function displays the invalid choice menu with a message indicating 
    that the user's input is not a valid option and prompts them to enter a valid choice.

    #### Parameters:
    - user_choice (str): The invalid choice input by the user
    - num_choices (int): The number of valid choices available

    #### Results:
    - The invalid choice menu displayed within a dynamic box with centered text

    #### Documentation:
    Providing feedback on invalid choices is crucial in text-based adventure games to guide 
    players towards making valid inputs and prevent frustration.
    '''

    invalid_menu = [
        f"'{user_choice}' is an invalid choice.",
        "-------------------------------",
        f"Please enter the number of your selection (1 - {num_choices}):"
    ]

    scripts.menu_delay()
    scripts.d_box(invalid_menu, align=2)


def main_menu():
    '''
    ### Main Menu Function
    This function displays the main menu with game title, description with instructions, 
    and options for the player to start the game, view the leaderboard,
    remove an existing leaderboard entry, or exit the game.

    #### Results:
    - The main menu displayed within a dynamic box with centered text

    #### Documentation:
    The main menu acts as the player's first point of contact with the game, 
    offering vital information about the game's premise and guiding them on their next steps. 
    It sets the mood for the adventure and provides clear options for navigating the game, 
    improving the overall user experience.
    '''

    menu = [
        "\033[1mKeyError: The Keeper of the Golden Key\033[0m",
        "-------------------------------",
        "In this adventure, your goal is to escape the abandoned hospital.",
        "Explore rooms, and collect items to assemble the key and escape!",
        "-------------------------------",
        f"{'1. Start Game':28}",
        f"{'2. View Leaderboard':28}",
        f"{'3. Remove Leaderboard Entry':28}",
        f"{'4. Exit':28}",
        "-------------------------------",
        "Enter Your Choice (1-4): "
    ]

    scripts.menu_delay()
    return scripts.d_box(menu, align=2)


def game_intro_menu():
    '''
    ### Game Intro Menu
    This function displays the game introduction menu, featuring a randomly 
    selected narrative describing the player's situation and surroundings in the hospital.

    #### Results:
    - The game start menu displayed within a dynamic box with centered text

    #### Documentation:
    The game's introduction menu immerses the player in its world and creates 
    a sense of urgency to escape the hospital by any means necessary. 
    Offering a randomly selected narrative adds variety to each new game, 
    enabling a different story if replayed. 
    '''

    f_intro_text_1 = [
        "You find yourself waking up in a strange place, not knowing how you got here. "
        "Disoriented and frightened, a sense of urgency fills your mind. "
        "As you look around, you realise that you are trapped "
        "in an abandoned hospital with no way out."
    ]

    f_intro_text_2 = [
        "Looking around, you realise that you are in never ending abandoned hospital. "
        "It seems like you have been here for a while, "
        "but you have no memory of how you got here or why."
    ]

    f_intro_text_3 = [
        "Confused about how you arrived here and with no memory of your past, "
        "you feel a growing sense of curiosity and unease. "
        "It appears to be a hospital, only recognisable by its clinical wallpaper, "
        "but it seems abandoned, old and decrepit, with peeling paint and broken windows. "
    ]

    f_intro_text_4 = [
        "You wake up in a dimly lit room, your head throbbing with pain and confusion. "
        "As you look around, you see that you are in an abandoned hospital room "
        "with doorways leading to different parts of the hospital."
    ]

    # Randomly select an introduction text to display and build the introduction menu
    intro_menu = random.choice(
        [f_intro_text_1, f_intro_text_2, f_intro_text_3, f_intro_text_4])

    intro_menu.extend([
        "-------------------------------",
        "You need to find a way out of this place, but you have no idea where to start."
    ])

    scripts.menu_delay()
    scripts.d_box(intro_menu, align=2)


def display_leaderboard(filename: str = "leaderboard.json"):
    '''
    ### Display Leaderboard Function
    This function loads the leaderboard data from a JSON file and formats it for display.
    It converts the player's time from seconds to a more readable format (hours, minutes, seconds)
    and displays the leaderboard in a dynamic box.

    #### Parameters:
    - filename (str): The name of the JSON file to load the leaderboard data from.
    (Default: "leaderboard.json")

    #### Results:
    - The leaderboard data displayed within a dynamic box.
    - If no leaderboard data is available, returns a message indicating so.

    #### Documentation:
    Showing the leaderboard enables players to compare their performance with others, 
    cultivating a competitive spirit and a sense of achievement. This also motivates 
    them to replay the game to improve their scores and advance in rankings (Lafond, 2018).
    '''

    leaderboard_data = scripts.load_leaderboard(filename)

    if not leaderboard_data:
        scripts.menu_delay()
        return scripts.d_box(["No leaderboard data available."], 2)

    # Format each leaderboard entry with a number
    leaderboard_entries = [
        f"{i + 1}. {entry['player_name']}: {scripts.calculate_score(entry['score'])}"
        for i, entry in enumerate(leaderboard_data)]

    # Calculate the max character length for consistent padding
    max_entry_length = max(len(entry) for entry in leaderboard_entries)

    # Build the leaderboard menu with the title and formatted entries
    leaderboard_menu = [
        "\033[1mLeaderboard\033[0m",
        "-------------------------------",
        *[f"{entry:{max_entry_length}}" for entry in leaderboard_entries]
    ]

    scripts.menu_delay()
    return scripts.d_box(leaderboard_menu, 2)


def remove_leaderboard_entry(filename: str = "leaderboard.json"):
    '''
    ### Remove Leaderboard Entry Function
    This function loads the leaderboard data from a JSON file and displays it formatted,
    allowing the player to select an entry to remove from the leaderboard.

    #### Parameters:
    - filename (str): The name of the JSON file to load the leaderboard data from.
    (Default: "leaderboard.json")

    #### Results:
    - The leaderboard data list for further processing (removing the selected entry).
    - Empty list if no leaderboard data is available.

    #### Documentation:
    Allowing players to remove leaderboard entries can help delete outdated or irrelevant scores.
    This also gives players control over their data and can enhance 
    their overall experience with the game.
    '''

    leaderboard_data = scripts.load_leaderboard(filename)

    if not leaderboard_data:
        scripts.menu_delay()
        scripts.d_box(["No leaderboard data available."], 2)
        return []

    # Build formatted leaderboard entries
    leaderboard_entries = [
        f"{i + 1}. {entry['player_name']}: {scripts.calculate_score(entry['score'])}"
        for i, entry in enumerate(leaderboard_data)
    ]

    # Calculate max length for consistent formatting and add return to previous menu option
    num_entries = len(leaderboard_data) + 1

    # Add return to previous menu option
    return_option = [f"{num_entries}. Return to Previous Menu"]

    # Calculate the maximum character length of the leaderboard entries
    max_entry_length = max(
        len(entry) for entry in leaderboard_entries + return_option)

    remove_menu = [
        "\033[1mRemove Leaderboard Entry\033[0m",
        "-------------------------------",
        *[f"{entry:{max_entry_length}}" for entry in leaderboard_entries],
        f"{return_option[0]:{max_entry_length}}",
        "-------------------------------",
        f"Enter Your Choice (1 - {num_entries}):"
    ]

    scripts.menu_delay()
    scripts.d_box(remove_menu, 2)

    return leaderboard_data


def you_win_menu(win_time: int):
    '''
    ### You Win Menu
    This function displays the win menu with a congratulatory message 
    and time taken to complete the game.

    #### Parameters:
    - win_time (int): The player's time in seconds taken to complete the game

    #### Results:
    - The You Win menu displayed within a dynamic box

    #### Documentation:
    This menu function is called when the player wins the game. 
    The win menu serves as a rewarding conclusion to the player's escape from the hospital, 
    providing a sense of accomplishment and closure. The inclusion of the time taken
    to complete the game adds a competitive element, encouraging players to replay
    and improve their performance.
    '''

    win_menu = [
        "The golden key fits the lock on the hospital reception door, "
        "it opens and you step through...",
        "The door slams shut behind you, "
        "and you find yourself outside the hospital in the bright sunlight.",
        "You have escaped the hospital and ready to start a new life, "
        "free from the horrors of the hospital.",
        "--------------------------------",
        "Congratulations, you have won the game!",
        f"Your time was {scripts.calculate_score(win_time)}.",
        "--------------------------------",
        "Please enter your name to record your score on the leaderboard: "
    ]

    scripts.menu_delay()
    scripts.d_box(win_menu, align=2)


def user_options_menu(use_item: bool, craft_item: bool):
    '''
    ### User Options Menu
    This function shows the user options menu with choices for the player to select. 
    The options displayed in the menu are generated dynamically based on the player's 
    inventory and possible actions.

    #### Parameters:
    - use_item (bool): If the player has usable items in their inventory
    - craft_item (bool): If the player has craftable items in their inventory

    #### Results:
    - The user options menu displayed within a dynamic box,
    with options based on the player's inventory and available actions.

    #### Documentation:
    The user options menu is the main menu when the game is active, 
    offering players a clear set of actions they can take based on their current situation. 
    Generating options dynamically according to the player's inventory and potential 
    actions creates a more immersive and personalised gaming experience. 
    This also reduces confusion by excluding actions that cannot be performed. 
    '''

    options = ["Move Room", "Explore Room", "View Pockets", "Exit Game"]

    # Add addition option if the player has items to use or craftable items
    if use_item:
        options.insert(len(options) - 1, "Use Item")

    if craft_item:
        options.insert(len(options) - 1, "Craft Item")

    # Calculate options length
    options_len = len(options)

    options_menu = [
        "\033[1mWhat would you like to do?\033[0m",
        "-------------------------------",
        *[f"{i + 1}. {option:14}" for i, option in enumerate(options)],
        "-------------------------------",
        f"Enter Your Choice (1-{options_len}):"
    ]

    scripts.menu_delay()
    scripts.d_box(options_menu, align=2)


def move_room_menu(current_room: str, rooms_dict: dict) -> list:
    '''
    ### Move Room Menu
    This function provides the player with a move menu with the available exits, 
    allowing them to navigate the hospital. 

    #### Parameters:
    - current_room (str): The name of the current room the player is in
    - rooms_dict (dict): A dictionary containing all rooms and their exits

    #### Results:
    - The move room menu displayed within a dynamic box with centered text
    - Returns a list of the available exits from the current room

    #### Documentation:
    The move room menu is a crucial component of the game, enabling players to 
    explore the hospital and progress through the story. 
    '''

    current_exits = scripts.exits_current_room(current_room, rooms_dict)

    # Narrative text for moving to another room
    narrative_option_1 = [
        "You look around the room, searching for any possible exits. "
        "After a moment of searching, you find the following exits:"
    ]

    narrative_option_2 = [
        "You take a moment to gather your thoughts and plan your next move. "
        "You see the following exits from the current room:"
    ]

    narrative_option_3 = [
        "You take a deep breath and decide to move to another room. "
        "You see the following exits from the current room:"
    ]

    exits_max_len = max(len(exits) for exits in current_exits)

    # Build the narrative menu with a randomly selected narrative option and the available exits
    narrative_menu = random.choice(
        [narrative_option_1, narrative_option_2, narrative_option_3])

    narrative_menu.extend([
        "-------------------------------",
        *[f"{exits[:3]} {exits[4:]:{exits_max_len}}" for exits in current_exits],
        "-------------------------------",
    ])

    menu_choices = current_exits + ["Stay in Current Room"]
    max_exit_len = max(len(exits) for exits in menu_choices)

    # Build move menu with the available exits and an option to stay in the current room
    move_menu = [
        f"You are currently in the {current_room}.",
        "-------------------------------",
        "Where would you like to go?",
        *[f"{i + 1}. {exits[4:]:{max_exit_len}}"
          for i, exits in enumerate(current_exits)],
        f"{len(menu_choices)}. {"Stay in current room":{max_exit_len}}",
        "-------------------------------",
        f"Enter Your Choice (1-{len(menu_choices)}):"
    ]

    scripts.menu_delay()
    scripts.d_box(narrative_menu, align=2)

    scripts.menu_delay()
    scripts.d_box(move_menu, align=2)

    return current_exits


def explore_room_menu(current_room: str, current_exits: list, room_objects: list):
    '''
    ### Explore Room menu
    This function presents the explore room menu, 
    showing a description of the current room, its available exits, and objects within. 

    #### Parameters:
    - current_room (str): The name of the current room the player is exploring
    - current_exits (list): A list of exits available in the current room
    - room_objects (list): A list of objects available in the current room

    #### Results:
    - The explore room menu displayed within a dynamic box with centered text

    #### Documentation:
    To enhance immersion, the room description is randomly chosen from a set
    of prewritten descriptions. When the player is in a particular room,
    a unique description for that room is displayed. The menu offers the player 
    the option to investigate one of the objects or return to the previous menu.
    '''

    # Format current room, exits, and objects for display
    current_room = current_room.lower()
    current_exits = [exits.lower() for exits in current_exits]
    f_room_objects = [obj.lower() for obj in room_objects]

    f_text_1 = [
        "The air is thick with dust, and the faint sound of dripping water echoes in the distance. "
        "Within a small puddle, you notice a sign that fell off the wall that reads "
        f"You are currently in the {current_room} and there are exits to the "
        f"{', '.join([exits[4:] for exits in current_exits])}. "
        f"Next to the puddle there is a {f_room_objects[0]}. "
        f"A broken {f_room_objects[1]} is next to the door to the {current_exits[0][4:]}."
    ]

    f_text_2 = [
        "The room is overgrown with vines and the walls are covered in peeling paint. "
        "On one side of the room, there is a sign; "
        "it is barely legible due to cracks on its surface. "
        f"You make out that you are currently in a {current_room}. "
        f"Exits {', '.join([exits[4:] for exits in current_exits])}. "
        f"Among the debris, you notice a {f_room_objects[0]} and a {f_room_objects[1]}."
    ]

    f_text_3 = [
        "The room is dimly lit, the walls are covered in faded wallpaper, "
        "and the floor is littered with debris. "
        f"You find yourself in a {current_room}, "
        f"with exits to the {', '.join([exits[4:] for exits in current_exits])}. "
        f"On the floor, you notice a {f_room_objects[0]} and a {f_room_objects[1]}."
    ]

    # Randomly select a narrative description for the room
    room_details = random.choice([f_text_1, f_text_2, f_text_3])

    # If the player is in a specific room, display a unique description for that room
    if current_room.lower() == "storage room":

        room_details = [
            "The tiny storage room is pitch black with the only light "
            "coming from its two doorways, "
            "one leading to an operating theater and the other to the patient ward. "
            f"Trying to find your way around the room you stumble into a {f_room_objects[0]} "
            f"and next to the exit there is a {f_room_objects[1]}."
        ]

    elif current_room.lower() == "hospital reception":

        room_details = [
            "As your eyes adjust from the bright light shining through the massive windows, "
            "you notice two big welcome desks with barrier ropes strung across the floor. "
            "You think that you must be at the hospital reception "
            "and immediately try to find a way out, "
            "but you can only find a door with a massive almost mythical padlock... "
            "It seems like there are only two exits, "
            "to what seems like a waiting room and a cafeteria to the right."
        ]

    # Build the explore room menu with the room details and options
    room_objects_char_len = max(len(obj) for obj in room_objects)

    room_details.extend([
        "-------------------------------",
        "Would you like to investigate one of these objects further?",
        "-------------------------------",
        f"1. {room_objects[0]:<{room_objects_char_len}}",
        f"2. {room_objects[1]:<{room_objects_char_len}}",
        f"3. {"Back":<{room_objects_char_len}}",
        "-------------------------------",
        "Enter Your Choice (1-3):"
    ])

    scripts.menu_delay()
    scripts.d_box(room_details, align=2)


def investigate_object_menu(room_object: str, plr_item: str):
    '''
    ### Investigate Object Menu
    This function displays the investigate object menu with a description 
    of the object being examined. It provides feedback on whether the 
    player has already examined the object or if they have discovered a new 
    item to add to their inventory.

    #### Parameters:
    - room_object (str): The object in the room
    - plr_item (str): The item found within the object

    #### Results:
    - Text displayed when picking up an item or indicating the object is empty

    #### Documentation:
    The investigate object menu is a key component of the game, enabling 
    players to interact with their surroundings and find new items. It offers feedback 
    on the player's actions, boosting immersion and guiding them through the game.
    '''

    is_empty = plr_item == "Empty"

    # Format the object being investigated for display
    room_object = room_object.lower()
    plr_item = plr_item.lower()

    # If the object is empty
    if is_empty:
        investigate_menu = [
            f"You approach the {room_object}, but find nothing of interest inside.",
            "-------------------------------",
            "It seems you have already investigated this object and taken its contents."
        ]

    # If the object contains an item
    else:
        investigate_menu = [
            f"You approach the {room_object}, its surface covered in grime. "
            f"As you examine the {room_object} more closely, "
            f"you find a {plr_item} hidden within it.",
            "-------------------------------",
            "You carefully pick up the item and add it to your inventory."
        ]

    scripts.menu_delay()
    scripts.d_box(investigate_menu, align=2)


def view_inventory(plr_inv_dict: dict):
    '''
    ### View Inventory Menu
    This function displays the player's inventory in a formatted menu. 
    It filters out any items with a quantity of 0 and formats the remaining 
    items and their quantities for display. If the player's inventory is empty, 
    a message appears indicating their pockets are empty.

    #### Parameters:
    - plr_inv_dict (dict): A dictionary of the player's inventory items and their quantities.

    #### Results:
    - The inventory menu displayed within a dynamic box with centered text, 
    showing the player's current inventory items and their quantities.

    #### Documentation:
    This menu function enables the player to view their current inventory, 
    helping them keep track of the items they have collected throughout the game. 
    '''

    # Filter items with quantity > 0
    plr_items = {item: qty
                 for item, qty in plr_inv_dict.items()
                 if qty > 0}

    if not plr_items:
        inventory_menu = ["Your Pockets are empty."]

    else:
        max_item_length = max(len(item) for item in plr_items.keys())

        # Build the inventory menu with the player's items and their quantities
        inventory_menu = [
            "\033[1mYour Pockets:\033[0m",
            "-------------------------------",
            *[f"{item:{max_item_length}} : {qty}" for item,
            qty in plr_items.items()],
            "-------------------------------"
        ]

    scripts.menu_delay()
    scripts.d_box(inventory_menu, align=2)


def crafting_menu(craftable_items: list):
    '''
    ### Crafting Menu
    This function displays the crafting menu, listing items the player can craft from 
    their inventory using the game's crafting recipes. If the player cannot craft any items, 
    a message is displayed indicating so.

    #### Parameters:
    - plr_inv_dict (dict): A dictionary of the player's inventory items.
    - craftable_items (list): A list of items that the player can craft.

    #### Results:
    - The crafting menu is displayed based on what items can be crafted.
    - If the player cannot craft anything, a message is displayed indicating so.

    #### Documentation:
    Crafting is a common mechanic in adventure games that allows players to combine items. 
    This game requires crafting the win-condition item, the golden key, which enhances the gameplay. 
    The crafting menu checks whether the player has the necessary items in their inventory to 
    craft the desired item based on the crafting recipes. If the player meets the requirements, 
    the function updates the player's inventory by adding the crafted item and removing 
    the used materials. This adds a layer of complexity to the game, 
    requiring multiple items to escape the hospital and win.
    '''

    if craftable_items:

        len_craftables: int = len(craftable_items)

        crafting_text = [
            "\033[1mCrafting Menu\033[0m",
            "-------------------------------"
        ]

        for i, item in enumerate(craftable_items, start=1):
            crafting_text.append(f"{i}. {item}")

        crafting_text.extend([
            f"{len_craftables + 1}. Return to Previous Menu",
            "-------------------------------",
            f"Enter Your Choice (1-{len_craftables + 1}):"
        ])

    else:

        crafting_text = [
            "You cannot craft anything at the moment."
        ]

    scripts.menu_delay()
    scripts.d_box(crafting_text, align=2)


def use_item_menu(usable_items: list):
    '''
    ### Use Item Menu
    This function displays the use item menu with options for the player
    to use items from their inventory.

    #### Parameters:
    - usable_items (list): A list of the usable items in the player's inventory.

    #### Results:
    - The use item menu is displayed based on what items can be used.
    - if the player cannot use any items, a message is displayed indicating so.

    #### Documentation:
    Using items enables further functionality for collectable items within the game, 
    adding game elements like a Map to help navigate the hospital. 
    Items without uses can be a part of the game as clutter and 'red herrings', 
    but the inclusion of items with a purpose makes the world feel more alive. 
    This menu checks the player's inventory for usable items and displays them as options.
    '''

    if usable_items:

        len_usable: int = len(usable_items)

        use_item_text = [
            "\033[1mUse Item Menu\033[0m",
            "-------------------------------"
        ]

        for i, item in enumerate(usable_items, start=1):
            use_item_text.append(f"{i}. {item}")

        use_item_text.extend([
            f"{len_usable + 1}. Return to Previous Menu",
            "-------------------------------",
            f"Enter Your Choice (1-{len_usable + 1}):"
        ])

    else:
        use_item_text = [
            "You have no usable items in your inventory at the moment."
        ]

    scripts.menu_delay()
    scripts.d_box(use_item_text, align=2)


# Submenu for using an item -
def open_map():
    '''
    ### Open Map Function
    This function displays the map of the hospital in a ASSCI art style. 
    The map shows the layout of the hospital and the 
    different rooms and exits available to the player.

    #### Results:
    - The map displayed within a dynamic box with centered text.

    #### Documentation:
    The map is a helpful item in the game, 
    offering players a visual overview of the hospital's layout. 
    This assists players in navigating the hospital more efficiently and planning their movements, 
    increasing their chances of a better score by escaping more quickly.
    '''
    map_layout = [
        "              ┌─────────⚿ ────────┐ ",
        "              │                   │ ",
        "              │  Hotel Reception  │ ",
        "              │   ▲           ▲   │ ",
        "┌─────────────┴── │ ┬──────── │ ──┴┐",
        "│                 ▼ │         ▼    │",
        "│  Waiting Room     │   Cafeteria  │",
        "│                 ◄───►            │",
        "│        ▲          ├──────────────┘",
        "└─┬───── │ ─────────┴──────────────┐",
        "  │      ▼                         │",
        "  │                Patient Ward    │",
        "  │              ▲             ▲   │",
        "┌─┴───────────── │ ────┬────── │ ─┬┘",
        "│                ▼     │       ▼  │ ",
        "│  Operating Theater   │   Storage│ ",
        "│                    ◄───► Room   │ ",
        "│                      ├──────────┘ ",
        "└──────────────────────┘            "
    ]

    scripts.menu_delay()
    scripts.d_box(map_layout, align=2)

# END OF FILE #
