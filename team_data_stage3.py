"""
Team data for StarLadder Budapest Major 2025 - Stage 3 (Legends Stage)
Data includes: HLTV rankings, Stage 2 results, recent form
Last updated: December 3, 2025
Stage 3 Format: 16-team Swiss System (8 from Stage 2 + 8 Legends)
"""

TEAMS_DATA_STAGE3 = {
    # LEGENDS - Direct invites to Stage 3 (Top 8 seeds)
    "FURIA": {
        "source": "Legend (Direct invite)",
        "hltv_rank": 1,
        "stage2_record": "N/A",
        "momentum": "excellent",
        "form_score": 10.0,
        "upset_potential": "very low",
        "consistency": 9.5,
        "notes": "#1 HLTV team, dominant form, favorites to win the Major"
    },
    "Vitality": {
        "source": "Legend (Direct invite)",
        "hltv_rank": 2,
        "stage2_record": "N/A",
        "momentum": "excellent",
        "form_score": 9.8,
        "upset_potential": "very low",
        "consistency": 9.5,
        "notes": "#2 HLTV, reigning champions, elite firepower with ZywOo"
    },
    "Falcons": {
        "source": "Legend (Direct invite)",
        "hltv_rank": 3,
        "stage2_record": "N/A",
        "momentum": "excellent",
        "form_score": 9.5,
        "upset_potential": "low",
        "consistency": 9.0,
        "notes": "#3 HLTV, Saudi Arabian powerhouse, star-studded roster"
    },
    "MOUZ": {
        "source": "Legend (Direct invite)",
        "hltv_rank": 4,
        "stage2_record": "N/A",
        "momentum": "very good",
        "form_score": 9.0,
        "upset_potential": "low",
        "consistency": 8.5,
        "notes": "#4 HLTV, consistent top team, German organization"
    },
    "MongolZ": {
        "source": "Legend (Direct invite)",
        "hltv_rank": 5,
        "stage2_record": "N/A",
        "momentum": "very good",
        "form_score": 8.8,
        "upset_potential": "low",
        "consistency": 8.0,
        "notes": "#5 HLTV, rising Mongolian squad, exciting playstyle"
    },
    "Spirit": {
        "source": "Legend (Direct invite)",
        "hltv_rank": 6,
        "stage2_record": "N/A",
        "momentum": "very good",
        "form_score": 8.5,
        "upset_potential": "low",
        "consistency": 8.5,
        "notes": "#6 HLTV, Team Spirit, former Major winners, experienced"
    },
    "G2": {
        "source": "Legend (Direct invite)",
        "hltv_rank": 7,
        "stage2_record": "N/A",
        "momentum": "good",
        "form_score": 8.0,
        "upset_potential": "medium",
        "consistency": 7.5,
        "notes": "#7 HLTV, legendary org with NiKo, inconsistent but dangerous"
    },
    "paiN": {
        "source": "Legend (Direct invite)",
        "hltv_rank": 10,
        "stage2_record": "N/A",
        "momentum": "good",
        "form_score": 7.5,
        "upset_potential": "medium",
        "consistency": 7.0,
        "notes": "#10 HLTV, Brazilian squad, dark horse contender"
    },

    # FROM STAGE 2 - Qualified teams (Seeds 9-16)
    "NAVI": {
        "source": "Stage 2 (3-0)",
        "hltv_rank": 9,
        "stage2_record": "3-0",
        "momentum": "excellent",
        "form_score": 9.5,
        "upset_potential": "low",
        "consistency": 9.0,
        "notes": "Natus Vincere, perfect 3-0 in Stage 2, legendary Ukrainian org"
    },
    "FaZe": {
        "source": "Stage 2 (3-0)",
        "hltv_rank": 13,
        "stage2_record": "3-0",
        "momentum": "excellent",
        "form_score": 9.0,
        "upset_potential": "low",
        "consistency": 8.5,
        "notes": "FaZe Clan, perfect 3-0 in Stage 2, rebounded from shaky Stage 1"
    },
    "3DMAX": {
        "source": "Stage 2 (3-2)",
        "hltv_rank": 12,
        "stage2_record": "3-2",
        "momentum": "moderate",
        "form_score": 7.0,
        "upset_potential": "medium",
        "consistency": 7.5,
        "notes": "French lineup, barely made it through at 3-2"
    },
    "Liquid": {
        "source": "Stage 2 (3-2)",
        "hltv_rank": 15,
        "stage2_record": "3-2",
        "momentum": "moderate",
        "form_score": 7.0,
        "upset_potential": "medium",
        "consistency": 7.0,
        "notes": "Team Liquid, scraped through at 3-2, inconsistent"
    },
    "B8": {
        "source": "Stage 2 (3-1)",
        "hltv_rank": 19,
        "stage2_record": "3-1",
        "momentum": "good",
        "form_score": 8.0,
        "upset_potential": "medium",
        "consistency": 7.5,
        "notes": "Solid performances in both Stage 1 and Stage 2"
    },
    "Passion UA": {
        "source": "Stage 2 (3-2)",
        "hltv_rank": 20,
        "stage2_record": "3-2",
        "momentum": "moderate",
        "form_score": 6.5,
        "upset_potential": "high",
        "consistency": 6.0,
        "notes": "Barely made it through at 3-2, clear underdog"
    },
    "PARIVISION": {
        "source": "Stage 2 (3-1)",
        "hltv_rank": 27,
        "stage2_record": "3-1",
        "momentum": "good",
        "form_score": 7.5,
        "upset_potential": "high",
        "consistency": 6.5,
        "notes": "Solid 3-1 performance, showing resilience"
    },
    "Imperial": {
        "source": "Stage 2 (3-1)",
        "hltv_rank": 28,
        "stage2_record": "3-1",
        "momentum": "good",
        "form_score": 7.5,
        "upset_potential": "high",
        "consistency": 6.5,
        "notes": "Brazilian squad, clutched through both stages"
    }
}

# All 16 teams in Stage 3
ALL_TEAMS_STAGE3 = list(TEAMS_DATA_STAGE3.keys())

# INITIAL SEEDING for Stage 3
# Seeds 1-8: Legends (by Valve Global Standings)
# Seeds 9-16: Stage 2 qualifiers (by Swiss & Buchholz scores)
INITIAL_SEEDING_STAGE3 = [
    "FURIA",        # 1
    "Vitality",     # 2
    "Falcons",      # 3
    "MOUZ",         # 4
    "MongolZ",      # 5
    "Spirit",       # 6
    "G2",           # 7
    "paiN",         # 8
    "NAVI",         # 9 (3-0 from Stage 2)
    "FaZe",         # 10 (3-0 from Stage 2)
    "B8",           # 11 (3-1 from Stage 2)
    "3DMAX",        # 12 (3-2 from Stage 2)
    "PARIVISION",   # 13 (3-1 from Stage 2)
    "Imperial",     # 14 (3-1 from Stage 2)
    "Liquid",       # 15 (3-2 from Stage 2)
    "Passion UA"    # 16 (3-2 from Stage 2)
]

# OFFICIAL Round 1 matchups for Stage 3 (confirmed from Liquipedia - December 4, 2025)
# Based on Buchholz tiebreaker system
ROUND_1_MATCHUPS_STAGE3 = [
    ("FURIA", "NAVI"),            # Match 1
    ("Vitality", "FaZe"),         # Match 2
    ("Falcons", "B8"),            # Match 3
    ("MongolZ", "Imperial"),      # Match 4
    ("MOUZ", "PARIVISION"),       # Match 5
    ("Spirit", "Liquid"),         # Match 6
    ("G2", "Passion UA"),         # Match 7
    ("paiN", "3DMAX")             # Match 8
]
