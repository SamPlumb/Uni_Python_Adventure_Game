"""
KeyError: The Keeper of the Golden Key

This is the main file for the KeyError game. It contains the main game loop,
manages the game states and performs input validation.

The main game loop is structured to continuously run until the player chooses to exit the game,
using while loops to manage different game states and user interactions.
Game variables are used to track the current state of the game, such as whether the main menu is active,
"""

import game_data as data
# Local Imports #
import menus
import scripts

# Game Variables #
game_main_menu: bool = True  # Whether the main menu is active
game_win: bool = False  # If the player has won the game
start_timer: int = 0  # Initialize game start timer

current_room: str = ""  # Current room name
current_exits: list = []  # Current room exits

# Main Game Loop #
while True:

    while game_main_menu:

        menus.main_menu()

        user_choice = input().strip()

        # Invalid Choice
        if user_choice not in ["1", "2", "3", "4"]:
            menus.invalid_choice_menu(user_choice, 4)

        # Start Game
        elif user_choice == "1":

            # Game Setup Logic #

            # Set player's starting room
            current_room: str = scripts.plr_spawn(data.hosp_rooms)

            # Distribute player items and room objects to all rooms by updating the rooms dictionary
            scripts.distribute_r_objects(data.room_objects, data.hosp_rooms)
            scripts.distribute_plr_items(data.plr_items, data.hosp_rooms)

            # Start game timer
            start_timer = scripts.start_timer()

            # Display game introduction menu
            menus.game_intro_menu()

            # Set False to enter main game loop
            game_main_menu: bool = False

            # End of Game Setup Logic #

        # View Leaderboard
        elif user_choice == "2":

            menus.display_leaderboard("leaderboard.json")

        # Remove A Score From Leaderboard
        elif user_choice == "3":

            plr_leaderboard = menus.remove_leaderboard_entry(
                "leaderboard.json")

            # Check to see if there are entries in the leaderboard to remove
            if not plr_leaderboard:

                pass

            else:

                # Calculate amount of leaderboard entries - +1 for return to main menu option
                leaderboard_len = len(plr_leaderboard) + 1

                # Input validation for remove leaderboard entry options
                while True:

                    user_choice = input().strip()

                    # Invalid Choice (not a digit or not in range of options)
                    if not user_choice.isdigit() or \
                            int(user_choice) not in range(1, leaderboard_len + 1):

                        menus.invalid_choice_menu(user_choice, leaderboard_len)

                    # Return to main menu
                    elif user_choice == str(leaderboard_len):

                        break

                    # Remove selected leaderboard entry
                    else:

                        leaderboard_entry_to_remove: dict = plr_leaderboard[
                            int(user_choice) - 1]

                        scripts.remove_score_from_leaderboard(leaderboard_entry_to_remove,
                                                              "leaderboard.json")

                        break

        # Exit Game
        elif user_choice == "4":

            scripts.exit_game()

    while game_win:

        # Calculate player's completion time
        plr_win_time: int = int(scripts.end_timer(start_timer))

        # Display win menu
        menus.you_win_menu(plr_win_time)

        # Get player name for leaderboard with input validation to ensure a valid name is entered
        while True:

            player_name = input().strip()

            if not player_name:

                scripts.d_box(
                    ["Player name cannot be empty. Please enter a valid name."], align=2)

            # Add score to leaderboard and return to main menu
            else:
                scripts.add_new_score(player_name, plr_win_time)

                game_main_menu: bool = True
                game_win: bool = False

                break

    # Game State #
    while not game_main_menu and not game_win:

        # Calculate total user options based on available actions
        choices: int = 4  # Move, Explore, Inventory, Exit

        use_item_option: bool = False
        craft_item_option: bool = False

        # Check if player can use items
        usable_items = scripts.get_usable_items(
            data.plr_inventory, data.usable_items)

        if usable_items:
            choices += 1
            use_item_option: bool = True

        # Check if player can craft any items
        craftable_items = scripts.get_craftable_items(
            data.plr_inventory, data.crafting_recipes)

        if craftable_items:
            choices += 1
            craft_item_option: bool = True

        menus.user_options_menu(use_item_option, craft_item_option)
        user_choice = input().strip()

        # Invalid Choice
        if not user_choice.isdigit() or int(user_choice) not in range(1, choices + 1):
            menus.invalid_choice_menu(user_choice, choices)

        # Exit Game (last option)
        elif user_choice == str(choices):
            scripts.exit_game()

        # Move Room (option 1)
        if user_choice == "1":

            # Get current room exits for display and additional logic
            current_exits: list = menus.move_room_menu(current_room,
                                                       data.hosp_rooms)

            # Total move options is based on number of exits from current room
            # +1 for return to user options menu
            options: int = len(current_exits) + 1

            while True:

                user_choice = input().strip()

                # Invalid Choice
                if not user_choice.isdigit() or int(user_choice) not in range(1, options + 1):

                    menus.invalid_choice_menu(user_choice, options)

                # Return to user options menu (last option)
                elif user_choice == str(options):

                    break

                # Move to selected room
                else:

                    old_room: str = current_room

                    current_room = current_exits[int(user_choice) - 1][4:]

                    scripts.d_box([
                        f"You have left the {old_room} and entered the {current_room}"], align=2)

                    break

        # Explore Room (option 2)
        elif user_choice == "2":

            # Get room objects and player items for current room for display and additional logic
            room_objects, room_plr_items = scripts.get_room_objects_and_items(current_room,
                                                                              data.hosp_rooms)

            current_exits = scripts.exits_current_room(current_room,
                                                       data.hosp_rooms)

            menus.explore_room_menu(current_room, current_exits, room_objects)

            while True:

                user_choice = input().strip()

                # Invalid Choice
                if not user_choice.isdigit() or user_choice not in ["1", "2", "3"]:

                    menus.invalid_choice_menu(user_choice, 3)

                # Return to user options menu
                elif user_choice == "3":

                    break

                # Investigate selected object
                else:

                    choice_index = int(user_choice) - 1

                    menus.investigate_object_menu(room_objects[choice_index],
                                                  room_plr_items[choice_index])

                    scripts.pick_up_plr_item(current_room,
                                             data.hosp_rooms,
                                             room_plr_items[choice_index],
                                             data.plr_inventory,
                                             choice_index)

                    break

        # View Inventory (option 3)
        elif user_choice == "3":

            menus.view_inventory(data.plr_inventory)

        # Use Item or Craft Item -
        elif use_item_option or craft_item_option:

            menu_option: str = ""

            # Determine which menu option was selected
            if use_item_option and craft_item_option:

                if user_choice == str(choices - 1):
                    menu_option: str = "craft"

                elif user_choice == str(choices - 2):
                    menu_option: str = "use"

            elif use_item_option:
                if user_choice == str(choices - 1):
                    menu_option: str = "use"

            elif craft_item_option:
                if user_choice == str(choices - 1):
                    menu_option: str = "craft"

            # Use Item
            if menu_option == "use":

                menus.use_item_menu(usable_items)
                max_opt: int = len(usable_items) + 1

                while True:
                    user_choice = input().strip()

                    # Invalid Choice
                    if not user_choice.isdigit() or int(user_choice) not in range(1, max_opt + 1):
                        menus.invalid_choice_menu(user_choice, max_opt)

                    # Return to main options menu
                    elif user_choice == str(max_opt):
                        break

                    # Use selected item
                    else:

                        win_condition: bool = scripts.use_item(data.plr_inventory,
                                                               current_room,
                                                               usable_items[int(user_choice) - 1])
                        if win_condition:
                            game_win: bool = True
                        break

            # Craft Item
            elif menu_option == "craft":

                menus.crafting_menu(craftable_items)
                max_opt: int = len(craftable_items) + 1

                while True:
                    user_choice = input().strip()

                    # Invalid Choice
                    if not user_choice.isdigit() or int(user_choice) not in range(1, max_opt + 1):
                        menus.invalid_choice_menu(user_choice, max_opt)

                    # Return to main options menu
                    elif user_choice == str(max_opt):
                        break

                    # Craft selected item
                    else:
                        success: bool = scripts.craft_item(data.plr_inventory,
                                                           data.crafting_recipes,
                                                           craftable_items[int(user_choice) - 1])

                        # Crafting result messages

                        # Crafting successful
                        if success:
                            scripts.d_box(
                                [f"You crafted a "
                                 f"{craftable_items[int(user_choice) - 1]}!"], 2)
                            break

                        # Crafting not successful

                        # Should not be possible due to validation in get_craftable_items,
                        # but included for edge case scenarios
                        scripts.d_box(
                            ["You do not have the required materials to craft a "
                             f"{craftable_items[int(user_choice) - 1]}."
                             "Keep exploring to find the necessary items!"], align=2)
                        break
# END OF FILE #
