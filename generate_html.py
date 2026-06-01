#!/usr/bin/env python3
"""
Generate index.html for the configured Stage 1 predictions.
"""

import argparse
from html import escape

from model_config import DEFAULT_RANDOM_SEED, DEFAULT_SIMULATIONS
from prediction_algorithm import MajorPredictor
from team_data import EVENT, STAGE, TEAMS_DATA, ROUND_1_MATCHUPS


def pct(value):
    return f"{value:.2f}%"


def format_simulations(value):
    return f"{value:,}".replace(",", ".")


def build_rows(results, predictor):
    strengths = dict(predictor.get_strength_rankings())
    rows = []
    for team, probs in results.items():
        advance = probs["3-0"] + probs["3-1"] + probs["3-2"]
        rows.append((team, advance, strengths[team], probs, TEAMS_DATA[team]))
    rows.sort(key=lambda row: row[1], reverse=True)
    return rows


def render_pick(team, value, css_class, meta=None):
    meta_html = f'<div class="meta">{escape(meta)}</div>' if meta else ""
    meta_line = f"\n                            {meta_html}" if meta_html else ""
    return f"""
                    <div class="pick">
                        <div>
                            <div class="team">{escape(team)}</div>{meta_line}
                        </div>
                        <div class="percent {css_class}">{pct(value)}</div>
                    </div>"""


def render_matchups():
    items = []
    for index, (team1, team2) in enumerate(ROUND_1_MATCHUPS, 1):
        items.append(
            f'<div class="match"><small>Match {index}</small><strong>{escape(team1)}</strong>'
            f'<div class="vs">vs</div><strong>{escape(team2)}</strong></div>'
        )
    return "\n".join(items)


def render_table(rows):
    table_rows = []
    for team, advance, strength, probs, data in rows:
        red_class = " red" if probs["0-3"] >= 13 else ""
        table_rows.append(
            f"""                        <tr><td><strong>{escape(team)}</strong></td><td class="num">{data['hltv_rank']}</td><td class="num">{data.get('valve_rank', data['hltv_rank'])}</td><td class="num">{strength:.2f}</td><td class="num">{pct(probs['3-0'])}</td><td class="num">{pct(probs['3-1'])}</td><td class="num">{pct(probs['3-2'])}</td><td class="num green">{pct(advance)}</td><td class="num{red_class}">{pct(probs['0-3'])}</td><td class="players">{escape(', '.join(data['players']))}</td></tr>"""
        )
    return "\n".join(table_rows)


def generate_html(simulations=DEFAULT_SIMULATIONS, seed=DEFAULT_RANDOM_SEED):
    predictor = MajorPredictor()
    results = predictor.simulate_swiss_stage(
        simulations=simulations,
        first_round_matchups=ROUND_1_MATCHUPS,
        seed=seed,
    )
    rows = build_rows(results, predictor)
    predictions = predictor.get_top_predictions(results)

    top_3_0 = predictions["3-0"][:2]
    top_0_3 = predictions["0-3"][:2]
    top_3_0_teams = {team for team, _ in top_3_0}
    advancement_picks = [(team, advance) for team, advance, *_ in rows if team not in top_3_0_teams][:6]

    sims_label = format_simulations(simulations)
    first_3_0 = "\n".join(
        render_pick(
            team,
            prob,
            "green",
            f"HLTV #{TEAMS_DATA[team]['hltv_rank']} · VRS #{TEAMS_DATA[team].get('valve_rank', TEAMS_DATA[team]['hltv_rank'])} · Strength {dict(predictor.get_strength_rankings())[team]:.2f}",
        )
        for team, prob in top_3_0
    )
    first_0_3 = "\n".join(
        render_pick(
            team,
            prob,
            "red",
            f"HLTV #{TEAMS_DATA[team]['hltv_rank']} · VRS #{TEAMS_DATA[team].get('valve_rank', TEAMS_DATA[team]['hltv_rank'])} · Strength {dict(predictor.get_strength_rankings())[team]:.2f}",
        )
        for team, prob in top_0_3
    )
    advance_html = "\n".join(render_pick(team, value, "blue") for team, value in advancement_picks)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(EVENT['name'])} - {escape(STAGE['name'])} Predictions</title>
    <meta name="description" content="Predicoes para o {escape(STAGE['name'])} do {escape(EVENT['name'])} com {sims_label} simulacoes Monte Carlo do formato Swiss.">
    <style>
        :root {{
            --bg: #0d1117;
            --panel: #151b23;
            --panel-soft: #1d2632;
            --line: #303947;
            --text: #ecf2f8;
            --muted: #9ba8b7;
            --blue: #58a6ff;
            --green: #4ade80;
            --red: #fb7185;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0;
            background: var(--bg);
            color: var(--text);
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            line-height: 1.5;
        }}
        .topbar {{
            border-bottom: 1px solid var(--line);
            background: rgba(13, 17, 23, 0.94);
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        .nav {{
            max-width: 1180px;
            margin: 0 auto;
            padding: 14px 20px;
            display: flex;
            justify-content: space-between;
            gap: 16px;
            align-items: center;
        }}
        .brand {{ font-weight: 800; letter-spacing: 0; }}
        .nav span:last-child {{ color: var(--muted); font-size: 14px; }}
        main {{ max-width: 1180px; margin: 0 auto; padding: 36px 20px 56px; }}
        .hero {{
            display: grid;
            grid-template-columns: minmax(0, 1.3fr) minmax(280px, 0.7fr);
            gap: 28px;
            align-items: end;
            padding-bottom: 28px;
            border-bottom: 1px solid var(--line);
        }}
        h1 {{ margin: 0 0 14px; font-size: clamp(34px, 6vw, 68px); line-height: 0.95; letter-spacing: 0; }}
        .lead {{ color: var(--muted); max-width: 720px; font-size: 18px; margin: 0; }}
        .summary {{
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 18px;
            display: grid;
            gap: 12px;
        }}
        .summary-row {{
            display: flex;
            justify-content: space-between;
            gap: 14px;
            border-bottom: 1px solid var(--line);
            padding-bottom: 10px;
        }}
        .summary-row:last-child {{ border-bottom: 0; padding-bottom: 0; }}
        .summary-row span, .meta, .note, footer {{ color: var(--muted); }}
        section {{ margin-top: 34px; }}
        h2 {{ margin: 0 0 16px; font-size: 24px; letter-spacing: 0; }}
        .grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }}
        .card {{
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 18px;
            min-width: 0;
        }}
        .card h3 {{
            margin: 0 0 14px;
            font-size: 16px;
            color: var(--muted);
            font-weight: 700;
            letter-spacing: 0;
            text-transform: uppercase;
        }}
        .pick {{
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 12px;
            align-items: baseline;
            padding: 11px 0;
            border-top: 1px solid var(--line);
        }}
        .pick:first-of-type {{ border-top: 0; padding-top: 0; }}
        .team {{ font-weight: 800; overflow-wrap: anywhere; }}
        .meta {{ font-size: 13px; }}
        .percent, .num {{ font-variant-numeric: tabular-nums; }}
        .percent {{ font-weight: 800; }}
        .green {{ color: var(--green); }}
        .red {{ color: var(--red); }}
        .blue {{ color: var(--blue); }}
        .matchups {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }}
        .match {{
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 14px;
        }}
        .match small {{ color: var(--muted); display: block; margin-bottom: 8px; }}
        .vs {{ color: var(--muted); font-size: 12px; margin: 6px 0; }}
        .table-wrap {{
            overflow-x: auto;
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--panel);
        }}
        table {{ width: 100%; border-collapse: collapse; min-width: 980px; }}
        th, td {{ padding: 12px 14px; text-align: left; border-bottom: 1px solid var(--line); vertical-align: top; }}
        th {{
            color: var(--muted);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0;
            background: var(--panel-soft);
        }}
        td {{ font-size: 14px; }}
        tr:last-child td {{ border-bottom: 0; }}
        .num {{ text-align: right; white-space: nowrap; }}
        .players {{ color: var(--muted); max-width: 280px; }}
        .note {{ font-size: 14px; margin-top: 12px; }}
        footer {{ border-top: 1px solid var(--line); margin-top: 40px; padding-top: 20px; font-size: 14px; }}
        @media (max-width: 900px) {{ .hero, .grid {{ grid-template-columns: 1fr; }} .matchups {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} }}
        @media (max-width: 560px) {{ main {{ padding: 26px 14px 44px; }} .nav {{ align-items: flex-start; flex-direction: column; }} .matchups {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <div class="topbar">
        <div class="nav">
            <span class="brand">{escape(EVENT['name'])} Predictor</span>
            <span>{escape(STAGE['name'])} · {sims_label} simulações Monte Carlo · seed {seed}</span>
        </div>
    </div>
    <main>
        <section class="hero">
            <div>
                <h1>Cologne 2026 Stage 1 Predictions</h1>
                <p class="lead">Predições atualizadas para o primeiro Swiss stage usando a base centralizada de times, rankings HLTV, VRS, lineups, forma, consistência e potencial de upset.</p>
            </div>
            <div class="summary">
                <div class="summary-row"><span>Evento</span><strong>{escape(EVENT['name'])}</strong></div>
                <div class="summary-row"><span>Stage</span><strong>{escape(STAGE['name'])} · 2 a 5 de junho</strong></div>
                <div class="summary-row"><span>Formato</span><strong>16 times Swiss</strong></div>
                <div class="summary-row"><span>Snapshot</span><strong>1 de junho de 2026</strong></div>
            </div>
        </section>
        <section>
            <h2>Picks Recomendados</h2>
            <div class="grid">
                <article class="card"><h3>3-0 Picks</h3>{first_3_0}
                </article>
                <article class="card"><h3>0-3 Picks</h3>{first_0_3}
                </article>
                <article class="card"><h3>Avançar</h3>{advance_html}
                </article>
            </div>
            <p class="note">A lista de avanço exclui os dois picks escolhidos para 3-0, seguindo o padrão atual do script.</p>
        </section>
        <section>
            <h2>Round 1 Oficial</h2>
            <div class="matchups">{render_matchups()}</div>
        </section>
        <section>
            <h2>Tabela Completa</h2>
            <div class="table-wrap">
                <table>
                    <thead>
                        <tr>
                            <th>Time</th><th class="num">HLTV</th><th class="num">VRS</th><th class="num">Strength</th>
                            <th class="num">3-0</th><th class="num">3-1</th><th class="num">3-2</th>
                            <th class="num">Avança</th><th class="num">0-3</th><th>Lineup</th>
                        </tr>
                    </thead>
                    <tbody>
{render_table(rows)}
                    </tbody>
                </table>
            </div>
            <p class="note">As porcentagens podem variar quando o número de simulações ou a seed mudam.</p>
        </section>
        <footer>
            Dados oficiais em official_data.py, parâmetros subjetivos em model_config.py e composição em tournament_data.py. Resultados gerados localmente com {sims_label} simulações.
        </footer>
    </main>
</body>
</html>
"""


def parse_args():
    parser = argparse.ArgumentParser(description="Generate the static prediction HTML page.")
    parser.add_argument("--simulations", type=int, default=DEFAULT_SIMULATIONS)
    parser.add_argument("--seed", type=int, default=DEFAULT_RANDOM_SEED)
    parser.add_argument("--output", default="index.html")
    return parser.parse_args()


def main():
    args = parse_args()
    html = generate_html(simulations=args.simulations, seed=args.seed)
    with open(args.output, "w", encoding="utf-8") as output:
        output.write(html)
    print(f"Generated {args.output} with {args.simulations:,} simulations and seed {args.seed}.")


if __name__ == "__main__":
    main()
