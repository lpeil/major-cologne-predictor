"""
Subjective model configuration for Major predictions.

Official event data should live in official_data.py. Values here are model
assumptions and can be tuned without changing the tournament snapshot.
"""

DEFAULT_SIMULATIONS = 1000
DEFAULT_RANDOM_SEED = 42

RANK_BLEND = {
    "hltv": 0.60,
    "valve": 0.40,
}

UPSET_MULTIPLIERS = {
    "very low": 1.00,
    "low": 1.00,
    "medium": 0.97,
    "high": 0.93,
    "very high": 0.90,
}

MOMENTUM_STAGE_SCORE = {
    "excellent": 95,
    "very good": 85,
    "good": 75,
    "moderate": 60,
    "shaky": 45,
    "poor": 30,
}

RECORD_SCORE = {
    "3-0": 100,
    "3-1": 80,
    "3-2": 60,
    "N/A": None,
}

PREDICTION_WEIGHTS = {
    "stage1": {
        "rank": 0.35,
        "form": 0.30,
        "stage_entry": 0.20,
        "consistency": 0.15,
    },
    "stage2": {
        "rank": 0.35,
        "form": 0.30,
        "stage_entry": 0.20,
        "consistency": 0.15,
    },
    "stage3": {
        "rank": 0.35,
        "form": 0.30,
        "stage_entry": 0.20,
        "consistency": 0.15,
    },
}
