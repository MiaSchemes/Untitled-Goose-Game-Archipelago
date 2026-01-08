from typing import TYPE_CHECKING
from BaseClasses import Region
from .Locations import (
    location_table, extra_locations, speedrun_locations, 
    completion_location, milestone_locations, item_pickup_locations, drag_item_locations,
    interaction_locations, unique_item_locations, sandcastle_peck_locations, GooseGameLocation
)

if TYPE_CHECKING:
    from . import GooseGameWorld


def create_regions(world: "GooseGameWorld") -> None:
    """Create all regions and their locations
    
    Region Structure (Hub-based):
    
        Menu
          |
         Hub (Well - Starting Area)
        / | \ \
    Garden High Back Pub
           Street Gardens  \
                            Model Village
    
    The Hub (well area) is the starting location.
    - Garden, High Street, Back Gardens, Pub: Each requires their own access item
    - Model Village: Requires BOTH Pub Access AND Model Village Access
    - Victory: Requires ALL 5 access items (must carry bell back through every area)
    """
    
    multiworld = world.multiworld
    player = world.player
    
    # Create regions
    menu = Region("Menu", player, multiworld)
    hub = Region("Hub", player, multiworld)  # Starting area at the well
    garden = Region("Garden", player, multiworld)
    high_street = Region("High Street", player, multiworld)
    back_gardens = Region("Back Gardens", player, multiworld)
    pub = Region("Pub", player, multiworld)
    model_village = Region("Model Village", player, multiworld)
    
    # Add regions to multiworld
    multiworld.regions += [menu, hub, garden, high_street, back_gardens, pub, model_village]
    
    # Create connections - HUB-BASED
    # Hub is the starting area, all other areas require access items
    menu.connect(hub)  # Hub is starting area - always accessible
    
    # All areas connect directly FROM the hub
    # Rules for these entrances are set in Rules.py
    hub.connect(garden, "To Garden")
    hub.connect(high_street, "To High Street")
    hub.connect(back_gardens, "To Back Gardens")
    hub.connect(pub, "To Pub")
    hub.connect(model_village, "To Model Village")
    
    # Helper to add location to correct region
    def add_location(loc_name: str, loc_id: int, region_name: str):
        region = multiworld.get_region(region_name, player)
        location = GooseGameLocation(player, loc_name, loc_id, region)
        region.locations.append(location)
    
    # Add main goal locations (always included)
    for loc_name, loc_data in location_table.items():
        add_location(loc_name, loc_data.id, loc_data.region)
    
    # Add extra goal locations if enabled
    if world.options.include_extra_goals:
        for loc_name, loc_data in extra_locations.items():
            add_location(loc_name, loc_data.id, loc_data.region)
        
        for loc_name, loc_data in completion_location.items():
            add_location(loc_name, loc_data.id, loc_data.region)
    
    # Add speedrun goal locations if enabled
    if world.options.include_speedrun_goals:
        for loc_name, loc_data in speedrun_locations.items():
            add_location(loc_name, loc_data.id, loc_data.region)
    
    # Add milestone locations based on goal option
    goal = world.options.goal.value
    if goal == 1:  # All Main Goals
        for loc_name, loc_data in milestone_locations.items():
            if loc_name == "All Main Task Lists Complete":
                add_location(loc_name, loc_data.id, loc_data.region)
    elif goal == 2:  # All Goals
        for loc_name, loc_data in milestone_locations.items():
            if loc_name == "All Tasks Complete":
                add_location(loc_name, loc_data.id, loc_data.region)
    
    # Add item pickup locations if enabled
    if world.options.include_item_pickups:
        for loc_name, loc_data in item_pickup_locations.items():
            add_location(loc_name, loc_data.id, loc_data.region)
        
        # Add unique tracked item locations (position-based carrots, etc.)
        for loc_name, loc_data in unique_item_locations.items():
            add_location(loc_name, loc_data.id, loc_data.region)
    
    # Add drag item locations if enabled (separate toggle from pickups)
    if world.options.include_drag_items:
        for loc_name, loc_data in drag_item_locations.items():
            add_location(loc_name, loc_data.id, loc_data.region)
    
    # Add interaction locations if enabled
    if world.options.include_interactions:
        for loc_name, loc_data in interaction_locations.items():
            add_location(loc_name, loc_data.id, loc_data.region)
    
    # Add sandcastle peck locations (always included - core gameplay)
    for loc_name, loc_data in sandcastle_peck_locations.items():
        add_location(loc_name, loc_data.id, loc_data.region)
    
    # Victory condition - depends on goal option
    # Goal 0: Steal Bell - just need the Golden Bell and all access items
    # Goal 1: All Main Goals - need all main task lists complete
    # Goal 2: All Goals - need all goals including extras and speedrun
    include_prop_souls = bool(world.options.include_prop_souls.value)
    goal = world.options.goal.value
    
    # Base items always needed
    base_items = [
        "Garden Access", "High Street Access", "Back Gardens Access", 
        "Pub Access", "Model Village Access"
    ]
    
    if include_prop_souls:
        base_items.extend(["Timber Handle Soul", "Golden Bell Soul"])
    
    if goal == 0:  # Steal Bell
        if include_prop_souls:
            multiworld.completion_condition[player] = lambda state, p=player: (
                state.has("Golden Bell", p) and
                state.has("Timber Handle Soul", p) and
                state.has("Golden Bell Soul", p) and
                state.has("Garden Access", p) and
                state.has("High Street Access", p) and
                state.has("Back Gardens Access", p) and
                state.has("Pub Access", p) and
                state.has("Model Village Access", p)
            )
        else:
            multiworld.completion_condition[player] = lambda state, p=player: (
                state.has("Golden Bell", p) and
                state.has("Garden Access", p) and
                state.has("High Street Access", p) and
                state.has("Back Gardens Access", p) and
                state.has("Pub Access", p) and
                state.has("Model Village Access", p)
            )
    elif goal == 1:  # All Main Goals
        if include_prop_souls:
            multiworld.completion_condition[player] = lambda state, p=player: (
                state.has("Golden Bell", p) and
                state.has("All Main Goals Complete", p) and
                state.has("Timber Handle Soul", p) and
                state.has("Golden Bell Soul", p) and
                state.has("Garden Access", p) and
                state.has("High Street Access", p) and
                state.has("Back Gardens Access", p) and
                state.has("Pub Access", p) and
                state.has("Model Village Access", p)
            )
        else:
            multiworld.completion_condition[player] = lambda state, p=player: (
                state.has("Golden Bell", p) and
                state.has("All Main Goals Complete", p) and
                state.has("Garden Access", p) and
                state.has("High Street Access", p) and
                state.has("Back Gardens Access", p) and
                state.has("Pub Access", p) and
                state.has("Model Village Access", p)
            )
    else:  # All Goals (goal == 2)
        if include_prop_souls:
            multiworld.completion_condition[player] = lambda state, p=player: (
                state.has("Golden Bell", p) and
                state.has("All Goals Complete", p) and
                state.has("Timber Handle Soul", p) and
                state.has("Golden Bell Soul", p) and
                state.has("Garden Access", p) and
                state.has("High Street Access", p) and
                state.has("Back Gardens Access", p) and
                state.has("Pub Access", p) and
                state.has("Model Village Access", p)
            )
        else:
            multiworld.completion_condition[player] = lambda state, p=player: (
                state.has("Golden Bell", p) and
                state.has("All Goals Complete", p) and
                state.has("Garden Access", p) and
                state.has("High Street Access", p) and
                state.has("Back Gardens Access", p) and
                state.has("Pub Access", p) and
                state.has("Model Village Access", p)
            )