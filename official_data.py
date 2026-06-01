"""
Official or source-derived tournament data references.

This module is intentionally limited to data that comes from event pages,
rankings, rosters, or announced matchups. Subjective model assumptions live in
model_config.py.
"""

OFFICIAL_SOURCES = {
    "event_hub": "https://www.hltv.org/major/cologne",
    "stage1": "https://www.hltv.org/events/9028/iem-cologne-major-2026-stage-1",
    "stage1_preview": "https://www.hltv.org/news/44735/iem-cologne-major-stage-1-teams-format-schedule-talent-fantasy",
    "stage1_opening_matchups": "https://www.hltv.org/news/44679/iem-cologne-major-stage-1-opening-matchups-announced",
    "valve_major_cutoff": "https://www.hltv.org/valve-ranking/teams/major",
    "valve_current": "https://www.hltv.org/valve-ranking/teams/2026/june/1",
}

STAGE1_OFFICIAL_RANKS = {
    "GamerLegion": {"hltv_rank": 11, "valve_rank": 9},
    "B8": {"hltv_rank": 15, "valve_rank": 16},
    "BetBoom": {"hltv_rank": 17, "valve_rank": 17},
    "MIBR": {"hltv_rank": 20, "valve_rank": 20},
    "HEROIC": {"hltv_rank": 25, "valve_rank": 27},
    "Lynn Vision": {"hltv_rank": 31, "valve_rank": 24},
    "BIG": {"hltv_rank": 38, "valve_rank": 28},
    "TYLOO": {"hltv_rank": 29, "valve_rank": 32},
    "SINNERS": {"hltv_rank": 32, "valve_rank": 34},
    "M80": {"hltv_rank": 24, "valve_rank": 33},
    "Liquid": {"hltv_rank": 26, "valve_rank": 45},
    "Sharks": {"hltv_rank": 50, "valve_rank": 38},
    "NRG": {"hltv_rank": 33, "valve_rank": 53},
    "Gaimin Gladiators": {"hltv_rank": 60, "valve_rank": 55},
    "THUNDER dOWNUNDER": {"hltv_rank": 70, "valve_rank": 64},
    "FlyQuest": {"hltv_rank": 56, "valve_rank": 85},
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
