#!/usr/bin/env python3
"""
Main prediction script for IEM Cologne Major 2026 Stage 3 invite data
Generates Pick'em recommendations based on simulations and analysis
Based on 16-team Swiss system format
"""

import sys
from model_config import DEFAULT_RANDOM_SEED, DEFAULT_SIMULATIONS
from prediction_algorithm_stage3 import Stage3Predictor
from team_data_stage3 import EVENT, STAGE3, TEAMS_DATA_STAGE3, ROUND_1_MATCHUPS_STAGE3


def print_header(text: str):
    """Print a formatted header"""
    print("\n" + "=" * 80)
    print(text.center(80))
    print("=" * 80 + "\n")


def print_team_strengths(predictor: Stage3Predictor):
    """Display team strength rankings"""
    print_header("TEAM STRENGTH ANALYSIS")

    rankings = predictor.get_strength_rankings()

    print(f"{'Rank':<6} {'Team':<20} {'Strength':<12} {'HLTV':<8} {'Source':<25} {'Momentum':<15}")
    print("-" * 95)

    for i, (team, strength) in enumerate(rankings, 1):
        data = TEAMS_DATA_STAGE3[team]
        source = data['source']
        print(f"{i:<6} {team:<20} {strength:<12.2f} "
              f"#{data['hltv_rank']:<7} {source:<25} {data['momentum']:<15}")


def print_simulation_results(results: dict, simulations: int, top_n: int = 8):
    """Display simulation probability results"""
    print_header(f"SIMULATION RESULTS ({simulations:,} iterations)")

    print(f"{'Team':<20} {'3-0':<10} {'3-1':<10} {'3-2':<10} {'2-3':<10} {'1-3':<10} {'0-3':<10}")
    print("-" * 90)

    # Sort by advancement probability (3-0 + 3-1 + 3-2)
    sorted_teams = sorted(results.items(),
                         key=lambda x: x[1]['3-0'] + x[1]['3-1'] + x[1]['3-2'],
                         reverse=True)

    for team, probs in sorted_teams:
        print(f"{team:<20} "
              f"{probs['3-0']:>6.2f}%   "
              f"{probs['3-1']:>6.2f}%   "
              f"{probs['3-2']:>6.2f}%   "
              f"{probs['2-3']:>6.2f}%   "
              f"{probs['1-3']:>6.2f}%   "
              f"{probs['0-3']:>6.2f}%")


def print_pickem_recommendations(predictor: Stage3Predictor, results: dict):
    """Display Pick'em recommendations with reasoning"""
    print_header("PICK'EM RECOMMENDATIONS")

    predictions = predictor.get_top_predictions(results)

    # 3-0 Predictions
    print("3-0 CANDIDATES (Choose 1)")
    print("-" * 80)
    for i, (team, prob) in enumerate(predictions['3-0'][:5], 1):
        data = TEAMS_DATA_STAGE3[team]
        confidence = "HIGH" if prob > 15 else "MEDIUM" if prob > 10 else "LOW"
        print(f"\n{i}. {team} - {prob:.2f}% probability [{confidence} CONFIDENCE]")
        print(f"   Rank: #{data['hltv_rank']} | Source: {data['source']} | Momentum: {data['momentum']}")
        print(f"   Rationale: {data['notes']}")

    # 0-3 Predictions
    print("\n\n0-3 CANDIDATES (Choose 1)")
    print("-" * 80)
    for i, (team, prob) in enumerate(predictions['0-3'][:5], 1):
        data = TEAMS_DATA_STAGE3[team]
        confidence = "HIGH" if prob > 15 else "MEDIUM" if prob > 10 else "LOW"
        print(f"\n{i}. {team} - {prob:.2f}% probability [{confidence} CONFIDENCE]")
        print(f"   Rank: #{data['hltv_rank']} | Source: {data['source']} | Momentum: {data['momentum']}")
        print(f"   Rationale: {data['notes']}")

    # 3-1 and 3-2 (Advancing teams)
    print("\n\nADVANCEMENT CANDIDATES (3-1 or 3-2)")
    print("-" * 80)
    print("Choose 5 teams most likely to advance to Playoffs:")
    print()

    # Combine 3-0, 3-1, 3-2 probabilities for total advancement chance
    advancement_probs = []
    for team in results:
        total_advance = results[team]['3-0'] + results[team]['3-1'] + results[team]['3-2']
        advancement_probs.append((team, total_advance, results[team]))

    advancement_probs.sort(key=lambda x: x[1], reverse=True)

    for i, (team, advance_prob, probs) in enumerate(advancement_probs[:12], 1):
        data = TEAMS_DATA_STAGE3[team]
        print(f"{i:>2}. {team:<18} - {advance_prob:>6.2f}% to advance "
              f"(3-0: {probs['3-0']:>5.2f}% | 3-1: {probs['3-1']:>5.2f}% | 3-2: {probs['3-2']:>5.2f}%)")


def print_recommended_picks(predictor: Stage3Predictor, results: dict):
    """Display final recommended Pick'em selections"""
    print_header("FINAL PICK'EM RECOMMENDATIONS")

    predictions = predictor.get_top_predictions(results)

    print("\nYOUR PICK'EM SLATE:\n")

    # 3-0 picks (2 teams)
    print("3-0 Picks (Choose 2):")
    for i in range(2):
        team, prob = predictions['3-0'][i]
        print(f"  {i+1}. {team:<18} ({prob:.2f}% probability)")

    # 0-3 picks (2 teams)
    print("\n0-3 Picks (Choose 2):")
    for i in range(2):
        team, prob = predictions['0-3'][i]
        print(f"  {i+1}. {team:<18} ({prob:.2f}% probability)")

    # Advancing teams (exclude top 2 3-0 picks, include top 6)
    print("\nAdvancing Teams (Choose 6):")

    top_3_0_teams = {predictions['3-0'][0][0], predictions['3-0'][1][0]}

    advancement_probs = []
    for team in results:
        if team not in top_3_0_teams:  # Skip the 3-0 picks
            total_advance = results[team]['3-0'] + results[team]['3-1'] + results[team]['3-2']
            advancement_probs.append((team, total_advance))

    advancement_probs.sort(key=lambda x: x[1], reverse=True)

    for i, (team, prob) in enumerate(advancement_probs[:6], 1):
        print(f"  {i}. {team:<18} ({prob:.2f}% to advance)")

    print("\n" + "-" * 80)
    print("\nIMPORTANT NOTES:")
    print("   * These predictions are based on statistical analysis and simulations")
    print("   * CS2 has high variance - upsets are common in Swiss format")
    print("   * Consider your own research and recent team news")
    print("   * The 3-0 and 0-3 picks are high-risk, high-reward choices")
    print(f"   * {STAGE3['name']} runs {STAGE3['date_range']}")
    print("   * Top 8 teams advance to Playoffs (Champions Stage)")
    print("\nTOTAL PICKS: 2x (3-0) + 2x (0-3) + 6x (Advance) = 10 teams")


def print_round1_matchups():
    """Display Round 1 matchups"""
    print_header(f"ROUND 1 MATCHUPS ({STAGE3['date_range']})")

    print("All matches are Best-of-1 (BO1)\n")

    for i, (team1, team2) in enumerate(ROUND_1_MATCHUPS_STAGE3, 1):
        data1 = TEAMS_DATA_STAGE3[team1]
        data2 = TEAMS_DATA_STAGE3[team2]
        print(f"Match {i}: {team1:<15} (#{data1['hltv_rank']:<2}) vs {team2:<15} (#{data2['hltv_rank']:<2})")

    print("\nOnly direct Stage 3 invites are currently present in the data file.")


def main():
    """Main execution function"""
    print_header(f"{EVENT['name'].upper()} - {STAGE3['name'].upper()} PREDICTOR")
    print("Data-driven Pick'em analysis using VRS seed proxy, form, and simulations")
    print("Stage 3 is not complete until eight Stage 2 qualifiers are known.")
    print("Current data contains only the eight direct Stage 3 invites.\n")

    # Initialize predictor
    print("Initializing predictor...")
    predictor = Stage3Predictor()

    # Show Round 1 matchups
    print_round1_matchups()

    # Show team strengths
    print_team_strengths(predictor)

    # Run simulations
    print(f"\nRunning {DEFAULT_SIMULATIONS:,} Monte Carlo simulations of Swiss bracket...")
    print("Using seeded Round 1 matchups for currently known Stage 3 invites")
    print(f"Using seed {DEFAULT_RANDOM_SEED}")
    print("(This may take a moment...)\n")

    results = predictor.simulate_swiss_stage(
        simulations=DEFAULT_SIMULATIONS,
        first_round_matchups=ROUND_1_MATCHUPS_STAGE3,
        seed=DEFAULT_RANDOM_SEED,
    )

    # Display results
    print_simulation_results(results, DEFAULT_SIMULATIONS)

    # Show detailed recommendations
    print_pickem_recommendations(predictor, results)

    # Show final picks
    print_recommended_picks(predictor, results)

    print("\n" + "=" * 80)
    print("Good luck with your Pick'ems!")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrediction interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nErro: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
