"""
Official or source-derived tournament data references.

This module is intentionally limited to data that comes from event pages,
rankings, rosters, or announced matchups. Subjective model assumptions live in
model_config.py.
"""

OFFICIAL_SOURCES = {
    "event_hub": "https://www.hltv.org/major/cologne",
    "stage1": "https://www.hltv.org/events/9028/iem-cologne-major-2026-stage-1",
    "stage1_opening_matchups": "https://www.hltv.org/news/44679/iem-cologne-major-stage-1-opening-matchups-announced",
    "valve_major_cutoff": "https://www.hltv.org/valve-ranking/teams/major",
}

STAGE1_OFFICIAL_RANKS = {
    "GamerLegion": {"hltv_rank": 11, "valve_rank": 12},
    "B8": {"hltv_rank": 16, "valve_rank": 16},
    "BetBoom": {"hltv_rank": 17, "valve_rank": 18},
    "MIBR": {"hltv_rank": 29, "valve_rank": 19},
    "HEROIC": {"hltv_rank": 23, "valve_rank": 23},
    "Lynn Vision": {"hltv_rank": 45, "valve_rank": 25},
    "BIG": {"hltv_rank": 32, "valve_rank": 26},
    "TYLOO": {"hltv_rank": 31, "valve_rank": 27},
    "SINNERS": {"hltv_rank": 27, "valve_rank": 28},
    "M80": {"hltv_rank": 24, "valve_rank": 29},
    "Liquid": {"hltv_rank": 25, "valve_rank": 36},
    "Sharks": {"hltv_rank": 51, "valve_rank": 38},
    "NRG": {"hltv_rank": 34, "valve_rank": 43},
    "Gaimin Gladiators": {"hltv_rank": 46, "valve_rank": 51},
    "THUNDER dOWNUNDER": {"hltv_rank": 80, "valve_rank": 56},
    "FlyQuest": {"hltv_rank": 58, "valve_rank": 74},
}

STAGE1_OFFICIAL_ROUND_1_MATCHUPS = [
    ("GamerLegion", "NRG"),
    ("B8", "TYLOO"),
    ("HEROIC", "Sharks"),
    ("BetBoom", "Gaimin Gladiators"),
    ("BIG", "Liquid"),
    ("M80", "Lynn Vision"),
    ("MIBR", "THUNDER dOWNUNDER"),
    ("SINNERS", "FlyQuest"),
]
