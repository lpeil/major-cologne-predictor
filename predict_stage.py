#!/usr/bin/env python3
"""
Main prediction script for the configured IEM Cologne Major 2026 stage.
"""

import argparse
import sys

from model_config import DEFAULT_RANDOM_SEED, DEFAULT_SIMULATIONS
from prediction_algorithm import MajorPredictor
from team_data import EVENT, STAGE, TEAMS_DATA, ROUND_1_MATCHUPS


def print_header(text: str):
    print("\n" + "=" * 80)
    print(text.center(80))
    print("=" * 80 + "\n")


def print_team_strengths(predictor: MajorPredictor):
    print_header("TEAM STRENGTH ANALYSIS")

    rankings = predictor.get_strength_rankings()
    record_key = STAGE["record_key"]
    record_label = STAGE["record_label"]
    print(f"{'Rank':<6} {'Team':<20} {'Strength':<12} {'HLTV':<8} {'VRS':<8} {record_label:<12} {'Momentum':<15}")
    print("-" * 80)

    for i, (team, strength) in enumerate(rankings, 1):
        data = TEAMS_DATA[team]
        print(f"{i:<6} {team:<20} {strength:<12.2f} "
              f"#{data['hltv_rank']:<7} #{data.get('valve_rank', data['hltv_rank']):<7} "
              f"{data[record_key]:<12} {data['momentum']:<15}")


def print_simulation_results(results: dict, simulations: int, top_n: int = 8):
    print_header(f"SIMULATION RESULTS ({simulations:,} iterations)")

    print(f"{'Team':<20} {'3-0':<10} {'3-1':<10} {'3-2':<10} {'2-3':<10} {'1-3':<10} {'0-3':<10}")
    print("-" * 90)

    sorted_teams = sorted(results.items(), key=lambda x: x[1]['3-0'], reverse=True)
    for team, probs in sorted_teams[:top_n]:
        print(f"{team:<20} "
              f"{probs['3-0']:>6.2f}%   "
              f"{probs['3-1']:>6.2f}%   "
              f"{probs['3-2']:>6.2f}%   "
              f"{probs['2-3']:>6.2f}%   "
              f"{probs['1-3']:>6.2f}%   "
              f"{probs['0-3']:>6.2f}%")

    print(f"\n... (showing top {top_n} by 3-0 probability)")


def print_pickem_recommendations(predictor: MajorPredictor, results: dict):
    print_header("PICK'EM RECOMMENDATIONS")
    predictions = predictor.get_top_predictions(results)

    print("3-0 CANDIDATES (Choose 1)")
    print("-" * 80)
    for i, (team, prob) in enumerate(predictions['3-0'][:5], 1):
        data = TEAMS_DATA[team]
        confidence = "HIGH" if prob > 15 else "MEDIUM" if prob > 10 else "LOW"
        print(f"\n{i}. {team} - {prob:.2f}% probability [{confidence} CONFIDENCE]")
        print(f"   HLTV: #{data['hltv_rank']} | VRS: #{data.get('valve_rank', data['hltv_rank'])} | "
              f"{STAGE['record_label']}: {data[STAGE['record_key']]} | Momentum: {data['momentum']}")
        print(f"   Players: {', '.join(data['players'])}")
        print(f"   Rationale: {data['notes']}")

    print("\n\n0-3 CANDIDATES (Choose 1)")
    print("-" * 80)
    for i, (team, prob) in enumerate(predictions['0-3'][:5], 1):
        data = TEAMS_DATA[team]
        confidence = "HIGH" if prob > 15 else "MEDIUM" if prob > 10 else "LOW"
        print(f"\n{i}. {team} - {prob:.2f}% probability [{confidence} CONFIDENCE]")
        print(f"   HLTV: #{data['hltv_rank']} | VRS: #{data.get('valve_rank', data['hltv_rank'])} | "
              f"{STAGE['record_label']}: {data[STAGE['record_key']]} | Momentum: {data['momentum']}")
        print(f"   Players: {', '.join(data['players'])}")
        print(f"   Rationale: {data['notes']}")

    print("\n\nADVANCEMENT CANDIDATES")
    print("-" * 80)
    advancement_probs = []
    for team in results:
        total_advance = results[team]['3-0'] + results[team]['3-1'] + results[team]['3-2']
        advancement_probs.append((team, total_advance, results[team]))
    advancement_probs.sort(key=lambda x: x[1], reverse=True)

    for i, (team, advance_prob, probs) in enumerate(advancement_probs[:10], 1):
        print(f"{i:>2}. {team:<18} - {advance_prob:>6.2f}% to advance "
              f"(3-0: {probs['3-0']:>5.2f}% | 3-1: {probs['3-1']:>5.2f}% | 3-2: {probs['3-2']:>5.2f}%)")


def print_recommended_picks(predictor: MajorPredictor, results: dict):
    print_header("FINAL PICK'EM RECOMMENDATIONS")
    predictions = predictor.get_top_predictions(results)

    print("\nYOUR PICK'EM SLATE:\n")
    print("3-0 Picks (Choose 2):")
    for i in range(2):
        team, prob = predictions['3-0'][i]
        print(f"  {i+1}. {team:<18} ({prob:.2f}% probability)")

    print("\n0-3 Picks (Choose 2):")
    for i in range(2):
        team, prob = predictions['0-3'][i]
        print(f"  {i+1}. {team:<18} ({prob:.2f}% probability)")

    print("\nAdvancing Teams (Choose 6):")
    top_3_0_teams = {predictions['3-0'][0][0], predictions['3-0'][1][0]}
    advancement_probs = []
    for team in results:
        if team not in top_3_0_teams:
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
    print(f"   * {STAGE['name']} runs {STAGE['date_range']}")


def parse_args():
    parser = argparse.ArgumentParser(description="Run Major Swiss stage predictions.")
    parser.add_argument("--simulations", type=int, default=DEFAULT_SIMULATIONS)
    parser.add_argument("--seed", type=int, default=DEFAULT_RANDOM_SEED)
    return parser.parse_args()


def main():
    args = parse_args()

    print_header(f"{EVENT['name'].upper()} - {STAGE['name'].upper()} PREDICTOR")
    print("Data-driven Pick'em analysis using HLTV rank, VRS rank, form, and simulations")
    print("Based on 16-team Swiss system format\n")

    predictor = MajorPredictor()
    print_team_strengths(predictor)

    print(f"\nRunning {args.simulations:,} Monte Carlo simulations of Swiss bracket...")
    print(f"Using Round 1 matchups from the current stage data and seed {args.seed}")
    print("(This may take a moment...)\n")
    results = predictor.simulate_swiss_stage(
        simulations=args.simulations,
        first_round_matchups=ROUND_1_MATCHUPS,
        seed=args.seed,
    )

    print_simulation_results(results, args.simulations)
    print_pickem_recommendations(predictor, results)
    print_recommended_picks(predictor, results)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrediction interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
