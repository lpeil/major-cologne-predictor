#!/usr/bin/env python3
"""
Validate the configured Cologne 2026 Stage 1 data shape.
"""

from official_data import STAGE1_OFFICIAL_RANKS, STAGE1_OFFICIAL_ROUND_1_MATCHUPS
from team_data import INITIAL_SEEDING, ROUND_1_MATCHUPS, TEAMS_DATA


REQUIRED_FIELDS = {
    "source",
    "event_seed",
    "hltv_rank",
    "valve_rank",
    "stage_entry_record",
    "momentum",
    "form_score",
    "upset_potential",
    "consistency",
    "players",
    "notes",
}


def main():
    teams = set(TEAMS_DATA)
    assert len(teams) == 16
    assert set(INITIAL_SEEDING) == teams
    assert set(STAGE1_OFFICIAL_RANKS) == teams

    assert ROUND_1_MATCHUPS == STAGE1_OFFICIAL_ROUND_1_MATCHUPS
    assert len(ROUND_1_MATCHUPS) == 8

    matchup_teams = [team for matchup in ROUND_1_MATCHUPS for team in matchup]
    assert len(matchup_teams) == 16
    assert len(set(matchup_teams)) == 16
    assert set(matchup_teams) == teams

    for team, data in TEAMS_DATA.items():
        missing = REQUIRED_FIELDS - set(data)
        assert not missing, f"{team} missing fields: {sorted(missing)}"
        assert isinstance(data["hltv_rank"], int)
        assert isinstance(data["valve_rank"], int)
        assert data["hltv_rank"] == STAGE1_OFFICIAL_RANKS[team]["hltv_rank"]
        assert data["valve_rank"] == STAGE1_OFFICIAL_RANKS[team]["valve_rank"]
        assert len(data["players"]) == 5
        assert 0 <= data["form_score"] <= 10
        assert 0 <= data["consistency"] <= 10

    assert TEAMS_DATA["Liquid"]["hltv_rank"] == 26
    assert TEAMS_DATA["Liquid"]["valve_rank"] == 45
    assert TEAMS_DATA["BetBoom"]["players"] == ["Boombl4", "zorte", "d1Ledez", "Magnojez", "FL4MUS"]

    print("Stage 1 data validation passed.")


if __name__ == "__main__":
    main()
