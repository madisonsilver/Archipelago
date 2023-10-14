from typing import Dict

from Options import Choice, Toggle, Range, DeathLink, StartInventoryPool, AssembleOptions


class Difficulty(Choice):
    """How difficult the game's logic is.  Tricky includes non-obvious skips and glitches.
    Unreasonable includes inconsistent or very difficult skips."""
    display_name = "Logic Difficulty"
    option_standard = 0
    option_tricky = 1
    option_unreasonable = 2
    default = 0


class BossLocations(Toggle):
    """If enabled, adds an extra location and Seal for each boss."""
    display_name = "Boss Locations"
    default = False


class Ending(Choice):
    """The ending required for you to complete your run in Archipelago."""
    display_name = "Ending"
    option_bloody = 0
    option_bloodless = 1
    default = 0


class DeathLinkAmnesty(Range):
    """Amount of Deaths to take before sending a DeathLink signal, for balancing difficulty."""
    display_name = "Death Link Amnesty"
    range_start = 0
    range_end = 30
    default = 15


seedling_options: Dict[str, AssembleOptions] = {
    "start_inventory_from_pool": StartInventoryPool,
    "difficulty": Difficulty, "boss_locations": BossLocations, "ending": Ending, "deathlink": DeathLink,
    "deathlink_amnesty": DeathLinkAmnesty
}
