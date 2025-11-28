#!/usr/bin/env python3
"""
Test R2 matchups assuming best seeds won R1
"""

from prediction_algorithm import MajorPredictor
from team_data import ROUND_1_MATCHUPS, INITIAL_SEEDING


def main():
    predictor = MajorPredictor()

    print("=" * 100)
    print("ROUND 2 MATCHUPS - Assuming best seeds won Round 1".center(100))
    print("=" * 100)
    print()

    print("INITIAL SEEDING:")
    print("-" * 100)
    for i, team in enumerate(INITIAL_SEEDING, 1):
        print(f"#{i:>2}: {team}")
    print()

    # Determine R1 winners (best seed wins)
    print("=" * 100)
    print("ROUND 1 RESULTS (Best seeds win):")
    print("-" * 100)

    winners_1_0 = []
    losers_0_1 = []

    for team1, team2 in ROUND_1_MATCHUPS:
        seed1 = INITIAL_SEEDING.index(team1) + 1
        seed2 = INITIAL_SEEDING.index(team2) + 1

        # Better seed (lower number) wins
        if seed1 < seed2:
            winner = team1
            loser = team2
            winner_seed = seed1
            loser_seed = seed2
        else:
            winner = team2
            loser = team1
            winner_seed = seed2
            loser_seed = seed1

        winners_1_0.append(winner)
        losers_0_1.append(loser)

        print(f"#{seed1:>2} {team1:<15} vs #{seed2:>2} {team2:<15} → Winner: #{winner_seed} {winner}")

    print()

    # Create records dict
    records = {}
    for team in winners_1_0:
        records[team] = {'wins': 1, 'losses': 0}
    for team in losers_0_1:
        records[team] = {'wins': 0, 'losses': 1}

    active_teams = set(winners_1_0 + losers_0_1)

    # Use Swiss pairing algorithm
    matchups_r2 = predictor._create_swiss_pairings(records, active_teams)

    print("=" * 100)
    print("ROUND 2 MATCHUPS (Using Swiss Pairing with Seeding)".center(100))
    print("=" * 100)
    print()

    # Separate by bracket
    matchups_1_0 = []
    matchups_0_1 = []

    for team1, team2 in matchups_r2:
        if team1 in winners_1_0:
            matchups_1_0.append((team1, team2))
        else:
            matchups_0_1.append((team1, team2))

    print("🏆 1-0 BRACKET (Winner goes 2-0, Loser goes 1-1):")
    print("-" * 100)
    for team1, team2 in matchups_1_0:
        seed1 = INITIAL_SEEDING.index(team1) + 1
        seed2 = INITIAL_SEEDING.index(team2) + 1
        str1 = predictor.calculate_team_strength(team1)
        str2 = predictor.calculate_team_strength(team2)
        print(f"#{seed1:>2} {team1:<15} (Str: {str1:5.2f}) vs #{seed2:>2} {team2:<15} (Str: {str2:5.2f})")
    print()

    print("💀 0-1 BRACKET (Winner goes 1-1, Loser goes 0-2):")
    print("-" * 100)
    for team1, team2 in matchups_0_1:
        seed1 = INITIAL_SEEDING.index(team1) + 1
        seed2 = INITIAL_SEEDING.index(team2) + 1
        str1 = predictor.calculate_team_strength(team1)
        str2 = predictor.calculate_team_strength(team2)
        print(f"#{seed1:>2} {team1:<15} (Str: {str1:5.2f}) vs #{seed2:>2} {team2:<15} (Str: {str2:5.2f})")
    print()

    print("=" * 100)


if __name__ == "__main__":
    main()
