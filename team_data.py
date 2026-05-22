"""
Compatibility aliases for the default prediction stage.

The project now keeps event/team/model data in tournament_data.py. This module
preserves the original imports used by the Stage 2 predictor scripts.
"""

from tournament_data import (
    DEFAULT_STAGE,
    EVENT,
    PREDICTION_WEIGHTS,
    get_stage,
    get_stage_matchups,
    get_stage_seeding,
    get_stage_teams,
)

STAGE_ID = DEFAULT_STAGE
STAGE = get_stage(STAGE_ID)
TEAMS_DATA = get_stage_teams(STAGE_ID)
ALL_TEAMS = list(TEAMS_DATA.keys())
INITIAL_SEEDING = get_stage_seeding(STAGE_ID)
ROUND_1_MATCHUPS = get_stage_matchups(STAGE_ID)
WEIGHTS = PREDICTION_WEIGHTS[STAGE_ID]
