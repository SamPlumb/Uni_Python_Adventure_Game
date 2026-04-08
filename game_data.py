"""
KeyError: The Keeper of the Golden Key

Game Data Module -
"""

# Hospital Rooms
hosp_rooms = {
    0: {"name": "Hospital Reception",
        "exits": ["← | Waiting Room", "→ | Cafeteria"],
        "objects": [],
        "player_items": []
        },

    1: {"name": "Waiting Room",
        "exits": ["↑ | Patient Ward", "← | Cafeteria", "↓ | Hospital Reception"],
        "objects": [],
        "player_items": []
        },

    2: {"name": "Storage Room",
        "exits": ["← | Operating Theater", "↓ | Patient Ward"],
        "objects": [],
        "player_items": []
        },

    3: {"name": "Operating Theater",
        "exits": ["↑ | Patient Ward", "→ | Storage Room"],
        "objects": [],
        "player_items": []
        },

    4: {"name": "Patient Ward",
        "exits": ["↑ | Operating Theater", "→ | Storage Room", "↓ | Waiting Room"],
        "objects": [],
        "player_items": []
        },

    5: {"name": "Cafeteria",
        "exits": ["↑ | Waiting Room", "→ | Hospital Reception"],
        "objects": [],
        "player_items": []
        }}

# Room Objects
room_objects = {"Filling Cabinet":
                    "description",

                "Medical Trolley":
                    "description",

                "Desk":
                    "description",

                "Locker":
                    "description",

                "Chair":
                    "description",

                "Vending Machine":
                    "description"
                }

# Player Objects
plr_items = {"Keycard":
                 "description",

             "Surgical Glue":
                 "description",

             "Fire Extinguisher":
                 "description",

             "Golden Key Piece":
                 "description",

             "Map":
                 "description",

             "Crowbar":
                 "description",

             "First Aid Kit":
                 "description",

             "Flashlight":
                 "description",

             "Scalpel":
                 "description",

             "Hammer":
                 "description"
             }

# Player starting inventory
plr_inventory = {"Keycard": 0,
                 "Surgical Glue": 0,
                 "Fire Extinguisher": 0,
                 "Golden Key Piece": 0,
                 "Map": 0,
                 "Crowbar": 0,
                 "First Aid Kit": 0,
                 "Flashlight": 0,
                 "Scalpel": 0,
                 "Hammer": 0,
                 "Golden Key": 0}

# Usable Items
usable_items = ["Map", "Golden Key"]

# Crafting Recipes
crafting_recipes = {"Golden Key": {"Golden Key Piece": 3, "Surgical Glue": 1}}
