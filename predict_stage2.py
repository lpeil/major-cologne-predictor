#!/usr/bin/env python3
"""
Main prediction script for Budapest Major 2025 Stage 2
Generates Pick'em recommendations based on simulations and analysis
"""

import sys
from prediction_algorithm import MajorPredictor
from team_data import TEAMS_DATA, ROUND_1_MATCHUPS


def print_header(text: str):
    """Print a formatted header"""
    print("\n" + "=" * 80)
    print(text.center(80))
    print("=" * 80 + "\n")


def print_team_strengths(predictor: MajorPredictor):
    """Display team strength rankings"""
    print_header("TEAM STRENGTH ANALYSIS")

    rankings = predictor.get_strength_rankings()

    print(f"{'Rank':<6} {'Team':<20} {'Strength':<12} {'HLTV':<8} {'Stage 1':<12} {'Momentum':<15}")
    print("-" * 80)

    for i, (team, strength) in enumerate(rankings, 1):
        data = TEAMS_DATA[team]
        print(f"{i:<6} {team:<20} {strength:<12.2f} "
              f"#{data['hltv_rank']:<7} {data['stage1_record']:<12} {data['momentum']:<15}")


def print_simulation_results(results: dict, top_n: int = 8):
    """Display simulation probability results"""
    print_header("SIMULATION RESULTS (10,000 iterations)")

    print(f"{'Team':<20} {'3-0':<10} {'3-1':<10} {'3-2':<10} {'2-3':<10} {'1-3':<10} {'0-3':<10}")
    print("-" * 90)

    # Sort by 3-0 probability
    sorted_teams = sorted(results.items(), key=lambda x: x[1]['3-0'], reverse=True)

    for team, probs in sorted_teams[:top_n]:
        print(f"{team:<20} "
              f"{probs['3-0']:>6.2f}%   "
              f"{probs['3-1']:>6.2f}%   "
              f"{probs['3-2']:>6.2f}%   "
              f"{probs['2-3']:>6.2f}%   "
              f"{probs['1-3']:>6.2f}%   "
              f"{probs['0-3']:>6.2f}%")

    print("\n... (showing top 8 by 3-0 probability)")


def print_pickem_recommendations(predictor: MajorPredictor, results: dict):
    """Display Pick'em recommendations with reasoning"""
    print_header("PICK'EM RECOMMENDATIONS")

    predictions = predictor.get_top_predictions(results)

    # 3-0 Predictions
    print("🏆 3-0 CANDIDATES (Choose 1)")
    print("-" * 80)
    for i, (team, prob) in enumerate(predictions['3-0'][:5], 1):
        data = TEAMS_DATA[team]
        confidence = "HIGH" if prob > 15 else "MEDIUM" if prob > 10 else "LOW"
        print(f"\n{i}. {team} - {prob:.2f}% probability [{confidence} CONFIDENCE]")
        print(f"   Rank: #{data['hltv_rank']} | Stage 1: {data['stage1_record']} | Momentum: {data['momentum']}")
        print(f"   Rationale: {data['notes']}")

    # 0-3 Predictions
    print("\n\n💀 0-3 CANDIDATES (Choose 1)")
    print("-" * 80)
    for i, (team, prob) in enumerate(predictions['0-3'][:5], 1):
        data = TEAMS_DATA[team]
        confidence = "HIGH" if prob > 15 else "MEDIUM" if prob > 10 else "LOW"
        print(f"\n{i}. {team} - {prob:.2f}% probability [{confidence} CONFIDENCE]")
        print(f"   Rank: #{data['hltv_rank']} | Stage 1: {data['stage1_record']} | Momentum: {data['momentum']}")
        print(f"   Rationale: {data['notes']}")

    # 3-1 and 3-2 (Advancing teams)
    print("\n\n✅ ADVANCEMENT CANDIDATES (3-1 or 3-2)")
    print("-" * 80)
    print("Choose 5 teams most likely to advance to Stage 3:")
    print()

    # Combine 3-0, 3-1, 3-2 probabilities for total advancement chance
    advancement_probs = []
    for team in results:
        total_advance = results[team]['3-0'] + results[team]['3-1'] + results[team]['3-2']
        advancement_probs.append((team, total_advance, results[team]))

    advancement_probs.sort(key=lambda x: x[1], reverse=True)

    for i, (team, advance_prob, probs) in enumerate(advancement_probs[:10], 1):
        data = TEAMS_DATA[team]
        print(f"{i:>2}. {team:<18} - {advance_prob:>6.2f}% to advance "
              f"(3-0: {probs['3-0']:>5.2f}% | 3-1: {probs['3-1']:>5.2f}% | 3-2: {probs['3-2']:>5.2f}%)")


def print_recommended_picks(predictor: MajorPredictor, results: dict):
    """Display final recommended Pick'em selections"""
    print_header("🎯 FINAL PICK'EM RECOMMENDATIONS")

    predictions = predictor.get_top_predictions(results)

    print("\n📋 YOUR PICK'EM SLATE:\n")

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
    print("\n⚠️  IMPORTANT NOTES:")
    print("   • These predictions are based on statistical analysis and simulations")
    print("   • CS2 has high variance - upsets are common in Swiss format")
    print("   • Consider your own research and recent team news")
    print("   • The 3-0 and 0-3 picks are high-risk, high-reward choices")
    print("   • Stage 2 runs November 29 - December 2, 2025")
    print("\n📊 TOTAL PICKS: 2x (3-0) + 2x (0-3) + 6x (Advance) = 10 teams")


def main():
    """Main execution function"""
    print_header("BUDAPEST MAJOR 2025 - STAGE 2 PREDICTOR")
    print("Data-driven Pick'em analysis using HLTV rankings, form, and simulations")
    print("Based on 16-team Swiss system format\n")

    # Initialize predictor
    print("Initializing predictor...")
    predictor = MajorPredictor()

    # Show team strengths
    print_team_strengths(predictor)

    # Run simulations
    print("\nRunning 10,000 Monte Carlo simulations of Swiss bracket...")
    print("Using REAL Round 1 matchups from HLTV (November 29, 2025)")
    print("(This may take a moment...)\n")

    results = predictor.simulate_swiss_stage(simulations=10000, first_round_matchups=ROUND_1_MATCHUPS)

    # Display results
    print_simulation_results(results)

    # Show detailed recommendations
    print_pickem_recommendations(predictor, results)

    # Show final picks
    print_recommended_picks(predictor, results)

    print("\n" + "=" * 80)
    print("Good luck with your Pick'ems! 🎮")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrediction interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
