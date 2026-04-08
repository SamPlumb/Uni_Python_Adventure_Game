'''
KeyError: The Keeper of the Golden Key

- This file contains unit tests for the scripts.py file.
'''

import time

import game_data as data
import menus
import scripts


def test_timer(time_simulated: int = 1):
    '''
    Test the timer functions to ensure it works correctly.

    Tests:
    - start_timer should return a value, and it should be a number of type int or float
    - end_timer should return a positive number (int or float)
    - end_timer should return the correct elapsed time based on the simulated time
    '''

    try:
        # Test start_timer function
        print("Testing timer functions")

        start_time = scripts.start_timer()

        # Validate return value
        assert start_time is not None, \
            "start_timer should return a value"

        # Validate return type
        assert isinstance(start_time, (int, float)), \
            f"start_timer should return a number, got {type(start_time)}"

        # Testing end_timer function (requires simulating time passing)

        # Simulate time passing
        print(f"Simulating {time_simulated} second(s) passing...")
        time.sleep(time_simulated)

        # Call end_timer function
        total_time = scripts.end_timer(start_time)

        # Validate return type
        assert isinstance(total_time, (int, float)), \
            f"Time should be a number, got {type(total_time)}"

        # Validate elapsed time is positive
        assert total_time > 0, \
            f"Time should be positive, got {total_time} second/s"

        # Validate elapsed time is correctly calculated
        assert total_time == time_simulated, \
            f"Time should be {time_simulated} second/s, got {total_time} second/s"

        # If all assertions pass, print success message
        print(f"✓ Timer test passed. Elapsed time: {total_time} second/s")

    # Catch assertion errors and print failure message
    except AssertionError as e:
        print(f"✗ Timer test failed: {e}")

    except Exception as e:
        print(f"✗ Timer test error: {e}")


def test_calculate_score(test_time: int = 120):
    '''
    Test the calculate score function to ensure it calculates the score correctly.

    Tests:
    - calculate_score should return a string value representing the score
    - If the time is under 60 seconds, the score should be "Seconds" Only
    - If the time is over 60 seconds but under 3600 seconds (1 hour), 
    the score should be "Minutes and Seconds"
    - If the time is over 3600 seconds (1 hour), the score should be "Hours, Minutes and Seconds"
    '''

    try:
        # Test calculate_score function
        score = scripts.calculate_score(test_time)

        # Validate return type
        assert isinstance(
            score, str), f"Score should be a string, got {type(score)}"

        # If the time is under 60 seconds, the score should be "Seconds" Only
        if test_time < 60:

            assert score == f"{test_time} Seconds", \
                f"Score should be '{test_time} Seconds', got '{score}'"

        # If the time is over 60 seconds but under 3600 seconds (1 hour),
        # the score should be "Minutes and Seconds"
        elif 60 < test_time < 3600:

            minutes = test_time // 60
            seconds = test_time % 60

            expected_score = f"{minutes} Minutes, {seconds} Seconds"

            assert score == expected_score, \
                f"Score should be '{expected_score}', got '{score}'"

        # If the time is over 3600 seconds (1 hour),
        # the score should be "Hours, Minutes and Seconds"
        else:

            hours = test_time // 3600
            minutes = (test_time % 3600) // 60
            seconds = test_time % 60

            expected_score = f"{hours} Hours, {minutes} Minutes, {seconds} Seconds"

            assert score == expected_score, \
                f"Score should be '{expected_score}', got '{score}'"

        # If all assertions pass, print success message
        print(f"✓ Calculate score test passed. Score: {score}")

    # Catch assertion errors and print failure message
    except AssertionError as e:
        print(f"✗ Calculate score test failed: {e}")

    except Exception as e:
        print(f"✗ Calculate score test error: {e}")


def test_item_distribution(r_objects: dict, p_items: dict, rooms_dict: dict):
    '''
    Test the item distribution function to ensure it distributes items correctly.

    Tests:
    - distribute_r_objects should distribute 2 objects to each room in rooms_dict
    - distribute_plr_items should distribute 2 player items to each room in rooms_dict
    and that 3 golden key pieces and at least 1 surgical glue should be in the hospital
    '''

    # Test room objects distribution
    try:
        scripts.distribute_r_objects(r_objects, rooms_dict)

        # see if 2 objects are in each room
        assert all(len(rooms_dict[room]['objects']) == 2 for room in rooms_dict), \
            "Not all rooms have 2 objects distributed correctly."

        print("✓ Object distribution test passed. All rooms have 2 objects distributed correctly.")

    except AssertionError as e:
        print(f"✗ Object distribution test failed: {e}")

    except Exception as e:
        print(f"✗ Object distribution test error: {e}")

    # Test player items distribution
    try:
        scripts.distribute_plr_items(p_items, rooms_dict)

        # See if 2 items are in each room
        assert all(len(rooms_dict[room]['player_items']) == 2 for room in rooms_dict), \
            "Not all rooms have 2 player items distributed correctly."

        print("✓ Item distribution test passed. 2 player items in each room.")

        # Check if 3 golden key pieces are distributed in the rooms
        golden_key_pieces_count = sum(
            rooms_dict[room]['player_items'].count('Golden Key Piece') for room in rooms_dict)

        assert golden_key_pieces_count == 3, \
            f"Expected 3 Golden Key Pieces to be distributed, but found {golden_key_pieces_count}."

        print("✓ Golden Key Piece distribution test passed. 3 Golden Key Pieces in rooms.")

        # Check if a Surgical Glue is distributed in the rooms
        surgical_glue_count = sum(
            rooms_dict[room]['player_items'].count('Surgical Glue') for room in rooms_dict)

        assert surgical_glue_count >= 1, \
            f"Expected at least 1 Surgical Glue to be distributed, but found {surgical_glue_count}."

        print(
            "✓ Surgical Glue distribution test passed. At least 1 Surgical Glue in rooms.")

    except AssertionError as e:
        print(f"✗ Item distribution test failed: {e}")

    except Exception as e:
        print(f"✗ Item distribution test error: {e}")


def test_plr_spawn(rooms_dict: dict):
    '''
    Test the player spawn function to ensure it works correctly.

    Tests:
    - plr_spawn should return a valid room name from rooms_dict where the player is spawned
    '''

    try:
        plr_location = scripts.plr_spawn(rooms_dict)

        # Validate that the player location is a valid room in the rooms_dict
        assert plr_location in [room["name"] for room in rooms_dict.values()], \
            f"Player location '{plr_location}' is not a valid room in the rooms_dict."

        print("✓ Player spawn test passed. Player spawned in a valid room.")

    except Exception as e:
        print(f"✗ Player spawn test error: {e}")


def test_use_item(plr_inv_dict: dict, current_room: str):
    '''
    Test the use item function to ensure it works correctly.

    Tests:
    - use_item should return a boolean value indicating if the win condition is met
    - Using the Map should not set the win condition to True
    - Using the Golden Key in the Hospital Reception should set the win condition to True
    - Using the Golden Key outside the Hospital Reception should not set the win condition to True
    '''

    # Add all useable items to player inventory for testing
    for item in data.useable_items:
        plr_inv_dict[item] = 1

    # Test useable items
    try:
        # Test using each useable item in the Hospital Reception
        for item in data.useable_items:
            win_condition = scripts.use_item(plr_inv_dict, current_room, item)

            # Check that the win condition is a boolean value
            assert isinstance(win_condition, bool), \
                f"Win condition should be a boolean, got {type(win_condition)}"

            print(
                f"✓ Using {item} test passed. Win condition is a boolean value.")

            # The Map opens the map menu and returns False, we can check the function returns False
            if item == "Map":
                assert win_condition is False, \
                    "Using Map should not set the win condition to True"

                print(
                    "✓ Using Map test passed. Map does not set win condition to True.")

            # Check that using the Golden Key in the Hospital Reception sets win condition to True
            if item == "Golden Key" and current_room == "Hospital Reception":
                assert win_condition is True, (
                    "Using Golden Key in the Hospital Reception "
                    "should set the win condition to True"
                )

                print(
                    "✓ Using Golden Key in the Hospital Reception "
                    "test passed. Win condition set to True."
                )

            if item == "Golden Key" and current_room != "Hospital Reception":
                assert win_condition is False, (
                    "Using the Golden Key outside the Hospital Reception "
                    "should not set the win condition to True"
                )

                print(
                    "✓ Using the Golden Key outside the Hospital Reception "
                    "test passed. Win condition not set to True."
                )

    except AssertionError as e:
        print(f"✗ Use item test failed: {e}")

    except Exception as e:
        print(f"✗ Use item test error: {e}")

    print("✓ Use item test passed. All items used successfully.")

    # Reset player inventory after testing
    for item in plr_inv_dict:
        plr_inv_dict[item] = 0


def test_crafting(plr_inv_dict: dict, crafting_recipes: dict):
    '''
    Test the crafting function to ensure it crafts items correctly.

    Tests:
    - craft_item should return a boolean value indicating if the crafting was successful
    - Crafting each craftable item with the required materials should return True
    - Crafting an item without the required materials should return False
    '''

    # Add materials for crafting all craftable items to player inventory for testing
    for item, materials in crafting_recipes.items():
        for material in materials:
            plr_inv_dict[material] = materials[material]

    # Test crafting each craftable item
    try:
        for item in crafting_recipes:
            success = scripts.craft_item(plr_inv_dict, crafting_recipes, item)

            # Check that the crafting result is a boolean value
            assert isinstance(success, bool), \
                f"Crafting result should be a boolean, got {type(success)}"

            print(
                f"✓ Crafting Boolean {item} test passed. Crafting result is a boolean value.")

            # Check that crafting was successful
            assert success is True, \
                f"Crafting {item} should be successful with the provided materials."

            print(f"✓ Crafting {item} test passed. Item crafted successfully.")

    except AssertionError as e:
        print(f"✗ Crafting test failed: {e}")

    except Exception as e:
        print(f"✗ Crafting test error: {e}")

    # Reset player inventory after testing
    for item in plr_inv_dict:
        plr_inv_dict[item] = 0


def test_leaderboard_functions():
    '''
    Test the leaderboard functions to ensure they work correctly.

    Tests:
    - load_leaderboard should return a list of scores from the test leaderboard file
    - save_leaderboard should save the leaderboard data to the test leaderboard file
    - add_new_score should add a new score to the test leaderboard file
    - remove_score_from_leaderboard should remove a score from the test leaderboard file
    '''

    # Test data for leaderboard and add new score functions
    test_leaderboard = [
        {"player_name": "Alice", "score": 30},
        {"player_name": "Bob", "score": 250},
        {"player_name": "Charlie", "score": 4000}
    ]

    print("Test leaderboard data:", test_leaderboard)

    # Test loading and saving leaderboard functions
    try:
        scripts.save_leaderboard(test_leaderboard, "test_leaderboard.json")

        test_leaderboard_data = scripts.load_leaderboard(
            "test_leaderboard.json")

        # Validate that the loaded leaderboard matches the saved leaderboard
        assert test_leaderboard_data == test_leaderboard, \
            "Loaded leaderboard does not match the saved leaderboard."

        print(
            "✓ Leaderboard load/save test passed. Leaderboard saved and loaded correctly.")

        # Test displaying leaderboard function
        print("\n Testing display_leaderboard function with test leaderboard data:")

        menus.display_leaderboard("test_leaderboard.json")

    except AssertionError as e:
        print(f"✗ Leaderboard load/save test failed: {e}")

    except Exception as e:
        print(f"✗ Leaderboard load/save test error: {e}")

    # Test adding new score function
    test_new_score = {
        "player_name": "Test player",
        "score": 350
    }

    # Add new score to the leaderboard
    try:
        scripts.add_new_score(
            test_new_score["player_name"], test_new_score["score"], "test_leaderboard.json")

        # Load the updated leaderboard to check if the new score was added
        updated_leaderboard_data = scripts.load_leaderboard(
            "test_leaderboard.json")

        # Validate that the new score was added to the leaderboard
        assert any(score["player_name"] == test_new_score["player_name"]
                   and score["score"] == test_new_score["score"]
                   for score in updated_leaderboard_data) is True, \
            "New score was not added to the leaderboard."

        print("✓ Add new score test passed. New score added successfully.")

        # To test if new score was added successfully, we can display the updated leaderboard
        print("\n Leaderboard data after adding new score:")
        menus.display_leaderboard("test_leaderboard.json")

    except AssertionError as e:
        print(f"✗ Add new score test failed: {e}")

    except Exception as e:
        print(f"✗ Add new score test error: {e}")

    # Remove test player score after testing
    try:
        scripts.remove_score_from_leaderboard(
            test_new_score, "test_leaderboard.json")

        # Load the updated leaderboard to check if the test player score was removed
        updated_leaderboard_data = scripts.load_leaderboard(
            "test_leaderboard.json")

        # Validate that the test player score was removed from the leaderboard
        assert any(score["player_name"] == test_new_score["player_name"]
                   and score["score"] == test_new_score["score"]
                   for score in updated_leaderboard_data) is False, \
            "Test player score was not removed from the leaderboard."

        print("✓ Remove score test passed. Test player score removed successfully.")

        # To test if the score was removed successfully, we can display the final leaderboard
        print("\n Leaderboard data after removing test player score:")
        menus.display_leaderboard("test_leaderboard.json")

    except AssertionError as e:
        print(f"✗ Remove score test failed: {e}")

    except Exception as e:
        print(f"✗ Remove score test error: {e}")


def test_exit_game():
    '''
    Test the exit_game function to ensure it exits the game properly.
    '''

    # Test exit_game function
    try:

        scripts.exit_game()

    except SystemExit:
        print("exit_game function works correctly.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    # Test timer with a simulated time (parameter can be adjusted to test different time values)
    test_timer(3)

    # Test calculate score with different time values to cover all cases
    test_calculate_score(45)
    test_calculate_score(200)
    test_calculate_score(4000)

    # Test item distribution with the game data dictionaries
    test_item_distribution(data.room_objects, data.plr_items, data.hosp_rooms)

    # Test player spawn with the hospital rooms dictionary
    test_plr_spawn(data.hosp_rooms)

    # Test use item with the player inventory and a room (can be adjusted to test different rooms)
    test_use_item(data.plr_inventory, "Hospital Reception")

    # Test crafting with the player inventory and crafting recipes
    test_crafting(data.plr_inventory, data.crafting_recipes)

    # Test leaderboard functions (loading, saving, displaying, adding new scores)
    test_leaderboard_functions()

    # Test Exit Game function
    # Note: This will exit the script when called, so it should be the last test run
    test_exit_game()

    # END OF FILE #
