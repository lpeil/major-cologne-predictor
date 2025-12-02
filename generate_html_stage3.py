#!/usr/bin/env python3
"""
Generate HTML page for Stage 3 predictions
"""

from prediction_algorithm_stage3 import Stage3Predictor
from team_data_stage3 import TEAMS_DATA_STAGE3, ROUND_1_MATCHUPS_STAGE3

def generate_html():
    # Run predictions
    predictor = Stage3Predictor()
    results = predictor.simulate_swiss_stage(simulations=10000, first_round_matchups=ROUND_1_MATCHUPS_STAGE3)
    predictions = predictor.get_top_predictions(results)
    rankings = predictor.get_strength_rankings()

    # Calculate advancement probabilities
    advancement_probs = []
    for team in results:
        total_advance = results[team]['3-0'] + results[team]['3-1'] + results[team]['3-2']
        advancement_probs.append((team, total_advance, results[team]))
    advancement_probs.sort(key=lambda x: x[1], reverse=True)

    html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Budapest Major 2025 - Stage 3 Predictor</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            padding: 20px;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }

        h1 {
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .subtitle {
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 30px;
            color: #ddd;
        }

        .date-badge {
            text-align: center;
            display: inline-block;
            background: rgba(255, 255, 255, 0.1);
            padding: 8px 20px;
            border-radius: 20px;
            margin: 0 auto 30px;
            display: block;
            width: fit-content;
        }

        .section {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .section h2 {
            font-size: 1.8em;
            margin-bottom: 20px;
            border-bottom: 2px solid rgba(255, 255, 255, 0.2);
            padding-bottom: 10px;
        }

        .picks-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .pick-card {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
            border-radius: 12px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .pick-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .pick-card h3 {
            font-size: 1.4em;
            margin-bottom: 15px;
            color: #f093fb;
        }

        .team-item {
            background: rgba(0, 0, 0, 0.3);
            padding: 12px;
            margin: 8px 0;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-left: 4px solid #f5576c;
        }

        .team-name {
            font-weight: bold;
            font-size: 1.1em;
        }

        .team-prob {
            background: rgba(245, 87, 108, 0.3);
            padding: 4px 12px;
            border-radius: 15px;
            font-weight: bold;
        }

        .matchup-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .matchup {
            background: rgba(0, 0, 0, 0.3);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .matchup-title {
            color: #f093fb;
            font-weight: bold;
            margin-bottom: 8px;
        }

        .vs {
            text-align: center;
            color: #f5576c;
            font-weight: bold;
            margin: 5px 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        th {
            background: rgba(255, 255, 255, 0.05);
            font-weight: bold;
            color: #f093fb;
        }

        tr:hover {
            background: rgba(255, 255, 255, 0.05);
        }

        .rank-badge {
            background: rgba(245, 87, 108, 0.3);
            padding: 4px 8px;
            border-radius: 5px;
            font-size: 0.9em;
        }

        .confidence-high {
            color: #4ade80;
        }

        .confidence-medium {
            color: #fbbf24;
        }

        .confidence-low {
            color: #f87171;
        }

        .footer {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            color: #aaa;
            font-size: 0.9em;
        }

        .warning-box {
            background: rgba(251, 191, 36, 0.1);
            border-left: 4px solid #fbbf24;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 1.8em;
            }

            .picks-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎮 Budapest Major 2025</h1>
        <div class="subtitle">Stage 3 (Legends Stage) - Predictor</div>
        <div class="date-badge">📅 December 4-7, 2025 | 16 Teams Swiss System</div>

        <!-- Round 1 Matchups -->
        <div class="section">
            <h2>⚔️ Round 1 Matchups</h2>
            <div class="matchup-grid">
"""

    for i, (team1, team2) in enumerate(ROUND_1_MATCHUPS_STAGE3, 1):
        data1 = TEAMS_DATA_STAGE3[team1]
        data2 = TEAMS_DATA_STAGE3[team2]
        html += f"""
                <div class="matchup">
                    <div class="matchup-title">Match {i}</div>
                    <div>{team1} <span class="rank-badge">#{data1['hltv_rank']}</span></div>
                    <div class="vs">VS</div>
                    <div>{team2} <span class="rank-badge">#{data2['hltv_rank']}</span></div>
                </div>
"""

    html += """
            </div>
        </div>

        <!-- Pick'em Recommendations -->
        <div class="section">
            <h2>🎯 Pick'em Recommendations</h2>
            <div class="picks-grid">
                <div class="pick-card">
                    <h3>🏆 3-0 Picks (Choose 2)</h3>
"""

    for i in range(2):
        team, prob = predictions['3-0'][i]
        html += f"""
                    <div class="team-item">
                        <span class="team-name">{i+1}. {team}</span>
                        <span class="team-prob">{prob:.1f}%</span>
                    </div>
"""

    html += """
                </div>

                <div class="pick-card">
                    <h3>💀 0-3 Picks (Choose 2)</h3>
"""

    for i in range(2):
        team, prob = predictions['0-3'][i]
        html += f"""
                    <div class="team-item">
                        <span class="team-name">{i+1}. {team}</span>
                        <span class="team-prob">{prob:.1f}%</span>
                    </div>
"""

    html += """
                </div>

                <div class="pick-card" style="grid-column: 1 / -1;">
                    <h3>✅ Advancing Teams (Choose 6)</h3>
"""

    top_3_0_teams = {predictions['3-0'][0][0], predictions['3-0'][1][0]}
    advancement_filtered = [(t, p, r) for t, p, r in advancement_probs if t not in top_3_0_teams]

    for i, (team, prob, _) in enumerate(advancement_filtered[:6], 1):
        html += f"""
                    <div class="team-item">
                        <span class="team-name">{i}. {team}</span>
                        <span class="team-prob">{prob:.1f}%</span>
                    </div>
"""

    html += """
                </div>
            </div>
        </div>

        <!-- Simulation Results -->
        <div class="section">
            <h2>📊 Simulation Results (10,000 iterations)</h2>
            <table>
                <thead>
                    <tr>
                        <th>Team</th>
                        <th>3-0</th>
                        <th>3-1</th>
                        <th>3-2</th>
                        <th>Advance %</th>
                    </tr>
                </thead>
                <tbody>
"""

    for team, advance_prob, probs in advancement_probs:
        html += f"""
                    <tr>
                        <td><strong>{team}</strong> <span class="rank-badge">#{TEAMS_DATA_STAGE3[team]['hltv_rank']}</span></td>
                        <td>{probs['3-0']:.1f}%</td>
                        <td>{probs['3-1']:.1f}%</td>
                        <td>{probs['3-2']:.1f}%</td>
                        <td><strong>{advance_prob:.1f}%</strong></td>
                    </tr>
"""

    html += """
                </tbody>
            </table>
        </div>

        <!-- Team Strength Rankings -->
        <div class="section">
            <h2>💪 Team Strength Analysis</h2>
            <table>
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Team</th>
                        <th>Strength</th>
                        <th>HLTV</th>
                        <th>Source</th>
                    </tr>
                </thead>
                <tbody>
"""

    for i, (team, strength) in enumerate(rankings, 1):
        data = TEAMS_DATA_STAGE3[team]
        html += f"""
                    <tr>
                        <td>{i}</td>
                        <td><strong>{team}</strong></td>
                        <td>{strength:.2f}</td>
                        <td><span class="rank-badge">#{data['hltv_rank']}</span></td>
                        <td>{data['source']}</td>
                    </tr>
"""

    html += """
                </tbody>
            </table>
        </div>

        <div class="warning-box">
            <strong>⚠️ Important Notes:</strong>
            <ul style="margin-left: 20px; margin-top: 10px;">
                <li>Predictions based on statistical analysis and 10,000 Monte Carlo simulations</li>
                <li>CS2 has high variance - upsets are common in Swiss format</li>
                <li>3-0 and 0-3 picks are high-risk, high-reward choices</li>
                <li>Consider recent team news and your own research</li>
                <li>Top 8 teams advance to Champions Stage (Playoffs)</li>
            </ul>
        </div>

        <div class="footer">
            <p>Generated on December 3, 2025</p>
            <p>Data sources: HLTV.org, Liquipedia</p>
            <p>Good luck with your Pick'ems! 🎮</p>
        </div>
    </div>
</body>
</html>
"""

    return html

if __name__ == "__main__":
    print("Generating HTML for Stage 3...")
    html_content = generate_html()

    with open("stage3.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ HTML generated successfully: stage3.html")
