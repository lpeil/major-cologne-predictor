# IEM Cologne Major 2026 Predictor

Sistema de predição para Pick'ems do CS2 Major Cologne 2026 usando dados centralizados e simulações Monte Carlo do formato Swiss.

## Dados

Todas as informações que variam entre torneios, stages, rankings, lineups e ajustes do modelo ficam em:

- `tournament_data.py`

Esse arquivo contém:

- metadados do evento
- times por stage
- lineups extraídas da página do HLTV
- seeds/ranking proxy
- pesos do modelo
- pontuações por record/momentum
- multiplicadores de upset
- pareamentos iniciais gerados por seed quando não houver confrontos oficiais

Os arquivos `team_data.py` e `team_data_stage3.py` foram mantidos como aliases de compatibilidade.

## Uso

```bash
python3 predict_stage2.py
```

Por padrão, o predictor roda o `stage1`, porque é o único stage do Cologne 2026 com os 16 times completos no snapshot atual. Stage 2 e Stage 3 já têm os convidados diretos no arquivo central, mas ainda dependem dos classificados dos stages anteriores.

## Fonte

- HLTV IEM Cologne Major 2026 event hub: https://www.hltv.org/major/cologne

Snapshot consultado em 2026-05-22.
