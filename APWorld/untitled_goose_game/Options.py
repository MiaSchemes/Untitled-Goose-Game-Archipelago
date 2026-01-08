from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions


class StartingArea(Choice):
    """Which area the player starts with access to. 
    Without this, you'd be stuck at the hub with nothing to do!
    Model Village is not an option since it's the finale area."""
    display_name = "Starting Area"
    option_garden = 0
    option_high_street = 1
    option_back_gardens = 2
    option_pub = 3
    option_random = 4
    default = 4  # Random by default


class IncludeExtraGoals(Toggle):
    """Include post-game extra challenge goals as locations."""
    display_name = "Include Extra Goals"
    default = False


class IncludeSpeedrunGoals(Toggle):
    """Include speedrun challenge goals (complete areas before noon)."""
    display_name = "Include Speedrun Goals"
    default = False


class IncludeItemPickups(Toggle):
    """Include first-time item pickups as locations (100+ additional checks)."""
    display_name = "Include Item Pickups"
    default = True


class IncludeDragItems(Toggle):
    """Include first-time drag item locations (50+ additional checks for heavy/draggable items)."""
    display_name = "Include Drag Items"
    default = True


class IncludeInteractions(Toggle):
    """Include interaction locations (ringing bells, spinning windmills, breaking boards, etc.)."""
    display_name = "Include Interactions"
    default = True


class IncludeNPCSouls(Toggle):
    """When enabled, NPCs won't appear until you receive their soul item.
    This adds NPC souls to the item pool and gates NPC-related goals behind them."""
    display_name = "Include NPC Souls"
    default = True


class IncludePropSouls(Toggle):
    """When enabled, items can't be picked up or dragged until you receive their soul.
    This adds prop souls to the item pool and gates item interactions behind them."""
    display_name = "Include Prop Souls"
    default = True


class FillerWeightMegaHonk(Range):
    """Weight for Mega Honk in filler pool. Set to 0 to disable."""
    display_name = "Filler Weight: Mega Honk"
    range_start = 0
    range_end = 100
    default = 10


class FillerWeightSpeedyFeet(Range):
    """Weight for Speedy Feet in filler pool. Set to 0 to disable."""
    display_name = "Filler Weight: Speedy Feet"
    range_start = 0
    range_end = 100
    default = 10


class FillerWeightSilentSteps(Range):
    """Weight for Silent Steps in filler pool. Set to 0 to disable."""
    display_name = "Filler Weight: Silent Steps"
    range_start = 0
    range_end = 100
    default = 5


class FillerWeightGooseDay(Range):
    """Weight for A Goose Day (stored buff) in filler pool. Set to 0 to disable."""
    display_name = "Filler Weight: A Goose Day"
    range_start = 0
    range_end = 100
    default = 10


class TrapWeightTiredGoose(Range):
    """Weight for Tired Goose trap. Set to 0 to disable this trap."""
    display_name = "Trap Weight: Tired Goose"
    range_start = 0
    range_end = 100
    default = 5


class TrapWeightConfusedFeet(Range):
    """Weight for Confused Feet trap. Set to 0 to disable this trap."""
    display_name = "Trap Weight: Confused Feet"
    range_start = 0
    range_end = 100
    default = 5


class TrapWeightButterbeak(Range):
    """Weight for Butterbeak trap. Set to 0 to disable this trap."""
    display_name = "Trap Weight: Butterbeak"
    range_start = 0
    range_end = 100
    default = 5


class TrapWeightSuspiciousGoose(Range):
    """Weight for Suspicious Goose trap. Set to 0 to disable this trap."""
    display_name = "Trap Weight: Suspicious Goose"
    range_start = 0
    range_end = 100
    default = 5


class Goal(Choice):
    """What is required to complete the game."""
    display_name = "Goal"
    option_steal_bell = 0
    option_all_main_goals = 1
    option_all_goals = 2
    default = 0


class DeathLink(Toggle):
    """When you get caught/shooed, everyone dies. When someone else dies, you get teleported to the hub."""
    display_name = "Death Link"
    default = False


@dataclass
class GooseGameOptions(PerGameCommonOptions):
    starting_area: StartingArea
    include_extra_goals: IncludeExtraGoals
    include_speedrun_goals: IncludeSpeedrunGoals
    include_item_pickups: IncludeItemPickups
    include_drag_items: IncludeDragItems
    include_interactions: IncludeInteractions
    include_npc_souls: IncludeNPCSouls
    include_prop_souls: IncludePropSouls
    filler_weight_mega_honk: FillerWeightMegaHonk
    filler_weight_speedy_feet: FillerWeightSpeedyFeet
    filler_weight_silent_steps: FillerWeightSilentSteps
    filler_weight_goose_day: FillerWeightGooseDay
    trap_weight_tired_goose: TrapWeightTiredGoose
    trap_weight_confused_feet: TrapWeightConfusedFeet
    trap_weight_butterbeak: TrapWeightButterbeak
    trap_weight_suspicious_goose: TrapWeightSuspiciousGoose
    goal: Goal
    death_link: DeathLink