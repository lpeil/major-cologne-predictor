#!/usr/bin/env python3
"""
Validate Round 2 Swiss pairings when the better seed wins every Round 1 match.
"""

from prediction_algorithm import MajorPredictor
from team_data import INITIAL_SEEDING, ROUND_1_MATCHUPS


def better_seed_winners():
    winners = []
    losers = []
    for team1, team2 in ROUND_1_MATCHUPS:
        seed1 = INITIAL_SEEDING.index(team1)
        seed2 = INITIAL_SEEDING.index(team2)
        if seed1 < seed2:
            winners.append(team1)
            losers.append(team2)
        else:
            winners.append(team2)
            losers.append(team1)
    return winners, losers


def assert_valid_pairings(matchups, records, active_teams):
    flattened = [team for matchup in matchups for team in matchup]
    assert len(matchups) == len(active_teams) // 2
    assert sorted(flattened) == sorted(active_teams)

    for team1, team2 in matchups:
        assert team1 != team2
        assert records[team1] == records[team2], (team1, records[team1], team2, records[team2])


def main():
    predictor = MajorPredictor()
    winners, losers = better_seed_winners()
    records = {team: {"wins": 1, "losses": 0} for team in winners}
    records.update({team: {"wins": 0, "losses": 1} for team in losers})
    active_teams = set(winners + losers)

    matchups = predictor._create_swiss_pairings(records, active_teams)
    assert_valid_pairings(matchups, records, active_teams)

    one_zero = [matchup for matchup in matchups if records[matchup[0]]["wins"] == 1]
    zero_one = [matchup for matchup in matchups if records[matchup[0]]["losses"] == 1]
    assert len(one_zero) == 4
    assert len(zero_one) == 4

    print("Round 2 best-seed scenario validated.")
    for team1, team2 in matchups:
        record = f"{records[team1]['wins']}-{records[team1]['losses']}"
        print(f"{record}: {team1} vs {team2}")


if __name__ == "__main__":
    main()
