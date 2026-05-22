"""
Compatibility aliases for Cologne 2026 Stage 3 invite data.

Stage 3 is not simulation-ready until the eight Stage 2 qualifiers are known.
All mutable event/team/model data lives in tournament_data.py.
"""

from tournament_data import (
    EVENT,
    PREDICTION_WEIGHTS,
    get_stage,
    get_stage_matchups,
    get_stage_seeding,
    get_stage_teams,
)

STAGE_ID_STAGE3 = "stage3"
STAGE3 = get_stage(STAGE_ID_STAGE3)
TEAMS_DATA_STAGE3 = get_stage_teams(STAGE_ID_STAGE3)
ALL_TEAMS_STAGE3 = list(TEAMS_DATA_STAGE3.keys())
INITIAL_SEEDING_STAGE3 = get_stage_seeding(STAGE_ID_STAGE3)
ROUND_1_MATCHUPS_STAGE3 = get_stage_matchups(STAGE_ID_STAGE3)
WEIGHTS_STAGE3 = PREDICTION_WEIGHTS[STAGE_ID_STAGE3]
