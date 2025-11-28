"""
Team data for StarLadder Budapest Major 2025 - Stage 2
Data includes: HLTV rankings, Stage 1 results, recent form, expert analysis
Last updated: November 28, 2025
"""

TEAMS_DATA = {
    # Teams from Stage 1 (8 teams)
    "M80": {
        "source": "Stage 1 (3-0)",
        "hltv_rank": 24,
        "stage1_record": "3-0",
        "momentum": "excellent",  # 3-0 run, playing at new level
        "form_score": 9.5,  # Excellent form
        "upset_potential": "medium",
        "consistency": 8.5,
        "notes": "North American squad at new level, beat B8, PARIVISION, NRG"
    },
    "FlyQuest": {
        "source": "Stage 1 (3-0)",
        "hltv_rank": 32,
        "stage1_record": "3-0",
        "momentum": "excellent",  # 3-0 run but got tough draw
        "form_score": 9.0,
        "upset_potential": "high",  # Low confidence from public
        "consistency": 7.0,
        "notes": "Australian team, 3-0 run (beat Legacy, Imperial, Fluxo), faces NAVI first"
    },
    "NiP": {
        "source": "Stage 1 (3-1)",
        "hltv_rank": 30,
        "stage1_record": "3-1",
        "momentum": "good",
        "form_score": 7.5,
        "upset_potential": "medium",
        "consistency": 7.0,
        "notes": "Ninjas in Pyjamas, solid Stage 1 performance"
    },
    "B8": {
        "source": "Stage 1 (3-1)",
        "hltv_rank": 19,
        "stage1_record": "3-1",
        "momentum": "good",
        "form_score": 8.0,
        "upset_potential": "medium",
        "consistency": 7.5,
        "notes": "Best ranked team from Stage 1 qualifiers"
    },
    "fnatic": {
        "source": "Stage 1 (3-1)",
        "hltv_rank": 25,
        "stage1_record": "3-1",
        "momentum": "good",
        "form_score": 7.5,
        "upset_potential": "medium",
        "consistency": 7.5,
        "notes": "Legendary org, solid Stage 1 showing"
    },
    "FaZe": {
        "source": "Stage 1 (3-2)",
        "hltv_rank": 13,
        "stage1_record": "3-2",
        "momentum": "shaky",  # Looked "broken" but still favorites
        "form_score": 7.0,
        "upset_potential": "low",  # Despite struggles, still high potential
        "consistency": 6.0,
        "notes": "Struggled in Stage 1, looked disjointed but made it through"
    },
    "Imperial": {
        "source": "Stage 1 (3-2)",
        "hltv_rank": 28,  # Estimate
        "stage1_record": "3-2",
        "momentum": "moderate",
        "form_score": 6.5,
        "upset_potential": "high",
        "consistency": 6.0,
        "notes": "Brazilian team, barely made it through Stage 1, faces MIBR"
    },
    "PARIVISION": {
        "source": "Stage 1 (3-2)",
        "hltv_rank": 27,  # Estimate
        "stage1_record": "3-2",
        "momentum": "moderate",
        "form_score": 6.5,
        "upset_potential": "high",
        "consistency": 6.0,
        "notes": "Made it through at final hurdle, faces TYLOO"
    },

    # Direct invites (8 teams)
    "Aurora": {
        "source": "Direct invite",
        "hltv_rank": 8,  # Strong team, recent tournament winner
        "stage1_record": "N/A",
        "momentum": "excellent",  # Won PGL Masters Bucharest
        "form_score": 9.5,
        "upset_potential": "low",
        "consistency": 9.0,
        "notes": "Won PGL Masters Bucharest Nov 1, fresh from bootcamp, outrageous firepower (XANTARES, woxic)"
    },
    "NAVI": {
        "source": "Direct invite",
        "hltv_rank": 9,
        "stage1_record": "N/A",
        "momentum": "very good",
        "form_score": 9.0,
        "upset_potential": "low",
        "consistency": 9.0,
        "notes": "Natus Vincere, legendary Ukrainian org, faces FlyQuest first"
    },
    "3DMAX": {
        "source": "Direct invite",
        "hltv_rank": 12,
        "stage1_record": "N/A",
        "momentum": "good",
        "form_score": 8.0,
        "upset_potential": "medium",
        "consistency": 7.5,
        "notes": "French lineup, solid mid-tier team"
    },
    "Astralis": {
        "source": "Direct invite",
        "hltv_rank": 11,
        "stage1_record": "N/A",
        "momentum": "good",
        "form_score": 8.0,
        "upset_potential": "medium",
        "consistency": 8.0,
        "notes": "Legendary Danish org with dev1ce, experienced roster"
    },
    "Liquid": {
        "source": "Direct invite",
        "hltv_rank": 15,
        "stage1_record": "N/A",
        "momentum": "moderate",
        "form_score": 7.0,
        "upset_potential": "medium",
        "consistency": 7.0,
        "notes": "Team Liquid with NAF, EliGE - experienced but inconsistent"
    },
    "Passion UA": {
        "source": "Direct invite",
        "hltv_rank": 20,  # Estimate
        "stage1_record": "N/A",
        "momentum": "moderate",
        "form_score": 6.5,
        "upset_potential": "high",
        "consistency": 6.0,
        "notes": "International roster, less data available"
    },
    "TYLOO": {
        "source": "Direct invite",
        "hltv_rank": 35,  # Estimate, weak performance
        "stage1_record": "N/A",
        "momentum": "poor",  # 6 straight Bo3 losses
        "form_score": 4.0,
        "upset_potential": "very high",
        "consistency": 4.0,
        "notes": "Chinese team, 6 straight Bo3 losses, only 3 map wins, predicted to struggle"
    },
    "MIBR": {
        "source": "Direct invite",
        "hltv_rank": 40,  # Estimate, predicted as lowest rated
        "stage1_record": "N/A",
        "momentum": "poor",
        "form_score": 4.5,
        "upset_potential": "very high",
        "consistency": 4.5,
        "notes": "Predicted as lowest-rated team, insani and kl1m explosive duo, faces Imperial"
    }
}

# All 16 teams
ALL_TEAMS = list(TEAMS_DATA.keys())

# INITIAL SEEDING (used for Swiss system pairings)
# Based on combination of Valve Regional Standings and Stage 1 results
INITIAL_SEEDING = [
    "Aurora",       # 1
    "NAVI",         # 2
    "Liquid",       # 3
    "3DMAX",        # 4
    "Astralis",     # 5
    "TYLOO",        # 6
    "MIBR",         # 7
    "Passion UA",   # 8
    "M80",          # 9
    "FlyQuest",     # 10
    "B8",           # 11
    "fnatic",       # 12
    "NiP",          # 13
    "PARIVISION",   # 14
    "Imperial",     # 15
    "FaZe"          # 16
]

# OFFICIAL First Round Matchups (confirmed from HLTV - November 29, 2025)
# These are based on Stage 1 seeding and Valve Regional Standings
ROUND_1_MATCHUPS = [
    ("Astralis", "NiP"),           # 09:00 BO1
    ("3DMAX", "fnatic"),            # 09:00 BO1
    ("Passion UA", "FaZe"),         # 10:00 BO1
    ("PARIVISION", "TYLOO"),        # 10:00 BO1
    ("NAVI", "FlyQuest"),           # 11:00 BO1
    ("Aurora", "M80"),              # 11:00 BO1
    ("MIBR", "Imperial"),           # 12:00 BO1
    ("Liquid", "B8")                # 12:00 BO1
]
