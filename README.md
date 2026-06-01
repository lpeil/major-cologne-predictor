# IEM Cologne Major 2026 Predictor

Sistema de predição para Pick'ems do CS2 Major Cologne 2026 usando dados centralizados e simulações Monte Carlo do formato Swiss.

## Dados

Todas as informações que variam entre torneios, stages, rankings, lineups e ajustes do modelo ficam em:

- `official_data.py`: fontes, rankings oficiais e confrontos oficiais anunciados.
- `model_config.py`: hipóteses subjetivas do modelo, pesos, seed e número padrão de simulações.
- `tournament_data.py`: composição final dos stages, lineups, notas e compatibilidade com os aliases antigos.

Os dados oficiais e os parâmetros do modelo ficam separados para deixar claro o que veio de fonte externa e o que é ajuste interno de previsão.

Os arquivos `team_data.py` e `team_data_stage3.py` foram mantidos como aliases de compatibilidade.

## Uso

```bash
python3 predict_stage.py --simulations 1000 --seed 42
python3 generate_html.py --simulations 1000 --seed 42
```

Por padrão, o predictor roda o `stage1`, porque é o único stage do Cologne 2026 com os 16 times completos no snapshot atual. Stage 2 e Stage 3 já têm os convidados diretos no arquivo central, mas ainda dependem dos classificados dos stages anteriores.

`predict_stage2.py` continua existindo como wrapper de compatibilidade, mas o script principal agora é `predict_stage.py`.

## Validação

```bash
python3 test_data_validation.py
python3 test_swiss_pairing.py
python3 test_r2_best_seeds.py
```

Antes de atualizar previsões, edite os dados oficiais em `official_data.py`, ajuste hipóteses em `model_config.py` quando necessário, rode os testes acima e regenere o `index.html` com `generate_html.py`.

## Fonte

- HLTV IEM Cologne Major 2026 event hub: https://www.hltv.org/major/cologne
- HLTV Stage 1: https://www.hltv.org/events/9028/iem-cologne-major-2026-stage-1
- HLTV Stage 1 preview: https://www.hltv.org/news/44735/iem-cologne-major-stage-1-teams-format-schedule-talent-fantasy
- HLTV Round 1 matchups: https://www.hltv.org/news/44679/iem-cologne-major-stage-1-opening-matchups-announced
- Valve Regional Standings Major cutoff: https://www.hltv.org/valve-ranking/teams/major
- Valve Global Ranking atual: https://www.hltv.org/valve-ranking/teams/2026/june/1

Snapshot consultado em 2026-06-01.
