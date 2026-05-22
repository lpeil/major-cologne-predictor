"""
Prediction algorithm for the default Major Swiss stage.
Uses weighted factors configured in tournament_data.py.
"""

import random
from typing import Dict, List, Tuple
from team_data import TEAMS_DATA, ALL_TEAMS, INITIAL_SEEDING, STAGE, WEIGHTS
from tournament_data import MOMENTUM_STAGE_SCORE, RECORD_SCORE, UPSET_MULTIPLIERS


class MajorPredictor:
    """
    Predicts outcomes for the configured Major stage using weighted factors:
    - VRS/ranking proxy
    - Recent form/momentum
    - Stage entry performance/status
    - Consistency score
    """

    def __init__(self):
        self.teams = TEAMS_DATA
        self.stage = STAGE
        self.record_key = STAGE["record_key"]
        self.weights = WEIGHTS

    def calculate_team_strength(self, team: str) -> float:
        """
        Calculate overall team strength score (0-100)
        Higher score = stronger team
        """
        data = self.teams[team]

        # Ranking score (inverted - lower rank number is better). When both
        # HLTV and Valve ranks are present, blend current form and invite rank.
        hltv_score = max(10, 100 - (data['hltv_rank'] * 1.15))
        valve_score = max(10, 100 - (data.get('valve_rank', data['hltv_rank']) * 1.15))
        rank_score = (hltv_score * 0.60) + (valve_score * 0.40)

        # Form score (already 0-10, scale to 0-100)
        form_score = data['form_score'] * 10

        # Stage entry performance/status score
        record = data[self.record_key]
        stage_entry_score = RECORD_SCORE.get(record)
        if stage_entry_score is None:
            stage_entry_score = MOMENTUM_STAGE_SCORE[data['momentum']]

        # Consistency score (0-10, scale to 0-100)
        consistency_score = data['consistency'] * 10

        # Weighted sum
        total_score = (
            rank_score * self.weights['rank'] +
            form_score * self.weights['form'] +
            stage_entry_score * self.weights['stage_entry'] +
            consistency_score * self.weights['consistency']
        )

        return round(total_score, 2)

    def get_strength_rankings(self) -> List[Tuple[str, float]]:
        """
        Get all teams ranked by calculated strength
        Returns list of (team_name, strength_score) tuples
        """
        rankings = []
        for team in ALL_TEAMS:
            strength = self.calculate_team_strength(team)
            rankings.append((team, strength))

        # Sort by strength (highest first)
        rankings.sort(key=lambda x: x[1], reverse=True)
        return rankings

    def predict_matchup(self, team1: str, team2: str) -> Tuple[str, float]:
        """
        Predict winner of a single matchup
        Returns (winner, win_probability)
        """
        strength1 = self.calculate_team_strength(team1)
        strength2 = self.calculate_team_strength(team2)

        # Calculate win probability using logistic function
        # Difference of 10 points ≈ 60% win rate
        # Difference of 20 points ≈ 73% win rate
        diff = strength1 - strength2
        prob1 = 1 / (1 + 10 ** (-diff / 25))

        # Add small randomness for upset potential
        upset_factor = self.teams[team2]['upset_potential']
        prob1 *= UPSET_MULTIPLIERS[upset_factor]

        if prob1 > 0.5:
            return (team1, prob1)
        else:
            return (team2, 1 - prob1)

    def simulate_swiss_stage(self, simulations: int = 10000, first_round_matchups=None) -> Dict[str, Dict[str, float]]:
        """
        Simulate the Swiss system bracket multiple times
        Returns probability distribution for each team's final record

        Args:
            simulations: Number of Monte Carlo simulations to run
            first_round_matchups: Optional list of (team1, team2) tuples for fixed round 1 matchups
        """
        results = {team: {'3-0': 0, '3-1': 0, '3-2': 0, '2-3': 0, '1-3': 0, '0-3': 0}
                   for team in ALL_TEAMS}

        for _ in range(simulations):
            # Track each team's W-L record
            records = {team: {'wins': 0, 'losses': 0} for team in ALL_TEAMS}
            active_teams = set(ALL_TEAMS)

            # Simulate rounds until all teams have 3 wins or 3 losses
            round_num = 1
            while active_teams:
                # Use fixed matchups for round 1 if provided, otherwise use Swiss pairing
                if round_num == 1 and first_round_matchups is not None:
                    matchups = first_round_matchups
                else:
                    # Pair teams with similar records (Swiss system)
                    matchups = self._create_swiss_pairings(records, active_teams)

                if not matchups:
                    raise RuntimeError("Swiss pairing produced no matchups for active teams")

                # Simulate each matchup
                for team1, team2 in matchups:
                    winner, prob = self.predict_matchup(team1, team2)

                    # Probabilistic outcome
                    if random.random() < prob:
                        records[winner]['wins'] += 1
                        loser = team2 if winner == team1 else team1
                        records[loser]['losses'] += 1
                    else:
                        # Upset!
                        loser = winner
                        winner = team2 if winner == team1 else team1
                        records[winner]['wins'] += 1
                        records[loser]['losses'] += 1

                    # Remove teams that are done (3W or 3L)
                    if records[winner]['wins'] == 3:
                        active_teams.discard(winner)
                    if records[loser]['losses'] == 3:
                        active_teams.discard(loser)

                round_num += 1

            # Record final results
            for team in ALL_TEAMS:
                wins = records[team]['wins']
                losses = records[team]['losses']
                record = f"{wins}-{losses}"
                results[team][record] += 1

        # Convert counts to probabilities
        for team in ALL_TEAMS:
            for record in results[team]:
                results[team][record] = round((results[team][record] / simulations) * 100, 2)

        return results

    def _create_swiss_pairings(self, records: Dict, active_teams: set) -> List[Tuple[str, str]]:
        """
        Create pairings for Swiss system using initial seeding
        Teams with same record are paired: best seed vs worst seed within the group
        - 1st seed plays last seed
        - 2nd seed plays 2nd-to-last seed
        - etc.
        This prevents strong teams from eliminating each other too early.
        """
        # Group teams by their record
        by_record = {}
        for team in active_teams:
            record = (records[team]['wins'], records[team]['losses'])
            if record not in by_record:
                by_record[record] = []
            by_record[record].append(team)

        matchups = []
        leftovers = []
        for record_group in by_record.values():
            # Sort teams by initial seeding (maintain seeding order)
            record_group.sort(key=lambda team: INITIAL_SEEDING.index(team))

            # Pair teams: best vs worst, 2nd best vs 2nd worst, etc.
            n = len(record_group)
            for i in range(n // 2):
                matchups.append((record_group[i], record_group[n - 1 - i]))

            if len(record_group) % 2 == 1:
                leftovers.append(record_group[n // 2])

        leftovers.sort(key=lambda team: (
            records[team]['wins'] - records[team]['losses'],
            -INITIAL_SEEDING.index(team),
        ), reverse=True)
        for i in range(0, len(leftovers) - 1, 2):
            matchups.append((leftovers[i], leftovers[i + 1]))

        return matchups

    def get_top_predictions(self, results: Dict) -> Dict[str, List[Tuple[str, float]]]:
        """
        Get top candidates for each outcome category
        Returns dict with keys: '3-0', '3-1', '3-2', '0-3'
        """
        predictions = {
            '3-0': [],
            '3-1': [],
            '3-2': [],
            '0-3': []
        }

        for team in ALL_TEAMS:
            for outcome in ['3-0', '3-1', '3-2', '0-3']:
                prob = results[team][outcome]
                predictions[outcome].append((team, prob))

        # Sort each category by probability
        for outcome in predictions:
            predictions[outcome].sort(key=lambda x: x[1], reverse=True)

        return predictions
