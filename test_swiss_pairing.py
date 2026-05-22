#!/usr/bin/env python3
"""
Validate Swiss pairings for the current configured Stage 1 dataset.
"""

from prediction_algorithm import MajorPredictor
from team_data import INITIAL_SEEDING, ROUND_1_MATCHUPS, TEAMS_DATA


def r1_best_seed_records():
    records = {}
    for team1, team2 in ROUND_1_MATCHUPS:
        seed1 = INITIAL_SEEDING.index(team1)
        seed2 = INITIAL_SEEDING.index(team2)
        winner, loser = (team1, team2) if seed1 < seed2 else (team2, team1)
        records[winner] = {"wins": 1, "losses": 0}
        records[loser] = {"wins": 0, "losses": 1}
    return records


def main():
    predictor = MajorPredictor()
    records = r1_best_seed_records()
    active_teams = set(TEAMS_DATA)

    assert set(INITIAL_SEEDING) == active_teams
    assert len(ROUND_1_MATCHUPS) == 8
    assert len(records) == 16

    matchups = predictor._create_swiss_pairings(records, active_teams)
    flattened = [team for matchup in matchups for team in matchup]

    assert len(matchups) == 8
    assert sorted(flattened) == sorted(active_teams)

    for team1, team2 in matchups:
        assert team1 != team2
        assert records[team1] == records[team2], (team1, records[team1], team2, records[team2])

    print("Swiss pairing algorithm validated for the current Stage 1 data.")
    for team1, team2 in matchups:
        record = f"{records[team1]['wins']}-{records[team1]['losses']}"
        print(f"{record}: {team1} vs {team2}")


if __name__ == "__main__":
    main()
