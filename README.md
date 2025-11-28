# Budapest Major 2025 - Stage 2 Predictor

Sistema de predição baseado em ciência de dados para os Pick'ems do CS2 Major Budapest 2025 - Stage 2.

## 🎯 Objetivo

Prever os resultados do Stage 2 (Swiss system) usando análise estatística e simulações Monte Carlo, ajudando você a preencher seus Pick'ems com base em dados reais ao invés de achismo.

## 📊 Metodologia

O algoritmo utiliza múltiplos fatores ponderados:

1. **HLTV Ranking (30%)** - Rankings oficiais dos times
2. **Forma Recente (30%)** - Performance recente e momentum
3. **Performance Stage 1 (25%)** - Resultados do primeiro stage
4. **Consistência (15%)** - Histórico de estabilidade

### Simulação Swiss System

- 10,000 simulações Monte Carlo do bracket Swiss
- Calcula probabilidades para cada resultado possível (3-0, 3-1, 3-2, 2-3, 1-3, 0-3)
- Considera upset potential e matchups

## 🏆 Recomendações Principais

### 3-0 Pick: **Aurora** (52.94% probabilidade)
- Campeões recentes (PGL Masters Bucharest)
- Roster com firepower absurda (XANTARES, woxic)
- Voltando de bootcamp focado

### 0-3 Pick: **MIBR** (61.47% probabilidade)
- Time com rating mais baixo
- Forma recente ruim
- Primeira rodada contra Imperial (outro time fraco)

### Times para Avançar (escolha 5):
1. **NAVI** (93.62% de avançar)
2. **M80** (89.26% de avançar)
3. **Astralis** (77.50% de avançar)
4. **3DMAX** (73.83% de avançar)
5. **B8** (69.58% de avançar)

## 📁 Arquivos do Projeto

- `team_data.py` - Dados dos 16 times (rankings, forma, Stage 1)
- `prediction_algorithm.py` - Algoritmo de predição e simulação
- `predict_stage2.py` - Script principal para gerar recomendações

## 🚀 Como Usar

```bash
python3 predict_stage2.py
```

## 📈 Interpretação dos Resultados

### Probabilidades
- **Alta confiança**: >15% de probabilidade
- **Média confiança**: 10-15%
- **Baixa confiança**: <10%

### Fatores de Upset
- Times com alto "upset potential" podem surpreender
- Swiss format tem alta variância
- Resultados individuais são difíceis de prever, mas tendências são mais confiáveis

## ⚠️ Disclaimer

- Baseado em dados até 28 de Novembro de 2025
- CS2 tem alta variância - upsets são comuns
- Use como guia, não como garantia
- Considere notícias recentes e mudanças de roster
- O Stage 2 acontece de 29 Nov - 2 Dez 2025

## 🔄 Atualizações Futuras

Para melhorar o algoritmo:
- [ ] Adicionar histórico head-to-head detalhado
- [ ] Incluir estatísticas de mapas
- [ ] Analisar matchups específicos da primeira rodada
- [ ] Adicionar fator de sorte no bracket
- [ ] Incorporar odds de casas de apostas

## 📚 Fontes de Dados

- HLTV.org (rankings e estatísticas)
- Liquipedia (resultados Stage 1)
- Análises de especialistas (Pley, Hotspawn)

---

**Good luck com seus Pick'ems! 🎮**
