# Dossiê de fontes — t_60b3fc7d (R1 fixes)

Extração direta das fontes primárias em 2026-08-15. QA: confira qualquer número aqui.

## 1. Qwen3.8-27B — model card oficial
Fonte: https://huggingface.co/Qwen/Qwen3.8-27B (README raw, `/raw/main/README.md`)

Tabelas do card têm colunas: **Qwen3.8-27B | Qwen3.6-27B | Qwen3.7-Plus | Muse Glimmer-30B | Opus4.6 Max**
(Nomes GPT-5.6 Sol, Opus 4.8, Opus 5 e Qwen3.8-Max NÃO aparecem em nenhuma coluna. Qwen3.8-Max só existe no título de uma citação bibliográfica.)

| Benchmark | Q3.8 | Q3.6 | Q3.7-Plus | Muse | Opus4.6 Max |
|---|---|---|---|---|---|
| Terminal-Bench 2.1 | 73,0 | 63,4 | 64,0 | 51,7 | 78,2 |
| SWE-bench Pro | 61,7 | 53,5 | 57,6 | 51,2 | 53,4 |
| NL2Repo-Bench | 42,3 | 36,2 | 41,1 | — | 47,6 |
| DeepSWE 1.1 | 42,2 | 13,3 | 14,2 | — | — |
| QwenSWEBench | 79,0 | 49,3 | 59,2 | — | 63,8 |
| CoWorkBench | 70,7 | 61,0 | 65,1 | — | 68,2 |
| JobBench | 33,4 | 21,8 | 27,6 | — | — |
| Agents' Last Exam Pass@1/Score | 20,4/42,9 | 10,6/27,3 | 13,2/33,6 | — | — |
| IFBench | 79,5 | 69,1 | 79,1 | 77,0 | 62,5 |
| GPQA Diamond | 89,2 | 87,8 | 90,3 | 83,5 | 91,3 |
| HLE | 30,8 | 24,0 | 34,7 | 22,0 | 40,0 |
| LiveCodeBench v6 | 90,3 | 83,9 | 89,6 | — | 88,8 |
| OSWorld-Verified | 84,3 | 63,9 | 73,3 | 65,9 | 72,7 |
| WebArena-Verified | 64,8 | 48,8 | 55,3 | — | — |
| AndroidWorld | 81,9 | 70,3 | 81,0 | — | 62,0 |
| RecreationBench | 47,1 | 29,8 | 30,2 | — | — |
| ClawEval-MM Pass@3 | 57,4 | 42,6 | 57,4 | — | 52,5 |
| SWE-MM | 38,6 | 25,7 | 30,0 | — | 27,1 |
| Vision2Web | 62,9 | 45,0 | 42,1 | — | — |
| MathVision | 90,0/94,6 (s/c CI) | 85,1 | 90,3 (s/ CI) | — | 65,5 (s/ CI) |
| BabyVision | 65,7/85,6 | 28,9 | 64,7/70,4 | — | 12,6 (s/ CI) |
| CharXiv (RQ) | 83,7/90,2 | 78,4 | 85,8/85,9 | 78,8 | 66,0 (s/ CI) |
| OmniDocBench 1.5 | 91,1 | 89,4 | 91,4 | 75,8 | 86,6 |
| RealWorldQA | 85,9 | 84,1 | 86,9 | — | 73,9 |
| ERQA | 65,5 | 62,5 | 69,8 | — | 40,8 |

Nota do card (SWE-bench Pro): "Except for Opus4.6 Max, which uses the officially reported score, all models are evaluated with the Claude Code harness at temp=1.0, top_p=0.95, 256K context."

## 2. Gemma 3 27B — Technical Report
Fonte: https://arxiv.org/abs/2503.19786 (HTML, arxiv.org/html/2503.19786)

**Table 6 (modelos IT, zero-shot)** — mapeamento por cell-ID `S4.T6.2.6.x`:
GPQA Diamond: .6=64,7 é **Gemini 2.0 Pro**; .15=**42,4 é Gemma 3 27B IT** (colunas: G1.5Flash 51,0 · G1.5Pro 59,1 · G2.0Flash 60,1 · G2.0Pro 64,7 · G2-27B 34,3 · G3-1B 19,2 · G3-4B 30,8 · G3-12B 40,9 · G3-27B 42,4)
- MMLU-Pro 67,5 · LiveCodeBench 29,7 · MATH 89,0 · GPQA Diamond 42,4 · MMMU (val) 64,9

**Table 18 (modelos IT)**: MMLU 76,9 · MBPP 74,4 · **HumanEval 87,8** · GSM8K 95,9 · IFEval 90,4 · BBH 87,6

**Pre-trained (Tables 9/10)**: GPQA 24,3 · MMLUpro 52,2 · MATH 50,0 · GSM8K 82,6 · MBPP 65,6 · HumanEval 51,8 (o "48,8" usado antes NÃO existe no TR; 48,8 é MMMU do 4B e sub-scores multilíngues)

O README HF de google/gemma-3-27b-it NÃO tem tabela de evals (repo com acesso restrito; números vivem no TR).

## 3. GPT-OSS-20B — model card
Fonte: https://arxiv.org/abs/2508.10925 Table 3 (gpt-oss-120b | gpt-oss-20b, low/medium/high)

gpt-oss-20b (low | medium | high):
- GPQA Diamond (no tools): 56,8 | **66,0** | 71,5
- GPQA Diamond (with tools): 58,0 | 67,1 | 74,2
- HLE (no tools): 4,2 | 7,0 | 10,9 — HLE (with tools): 6,3 | **8,8** | 17,3
- MMLU: 80,4 | 84,0 | 85,3
- SWE-bench Verified: 37,4 | **53,2** | 60,7
- AIME 2025 (no tools): 37,1 | 72,1 | 91,7
- MMMLU (multilíngue, average): 67,0 | 73,5 | 75,7 ← o "73,6" antigo era aproximado disto, NÃO MMLU-Pro
- **MMLU-Pro e IFEval NÃO constam em nenhuma fonte oficial** (README HF, GitHub, blog, arXiv) → removidos da página

## Decisões aplicadas em benchmarks.html
1. Coluna "Referência de fronteira" → "Referências do model card" com Qwen3.7-Plus/Muse/Opus4.6 Max (fonte única: card). Zero "—" na tabela principal.
2. Gemma 3 27B: números do modelo **instruct** (linkado na página), fonte arXiv 2503.19786 T6/T18. GPQA 42,4 como principal, base 24,3 citado como parêntese.
3. GPQA take-away: 89,2 − 42,4 = **46,8 pontos** (não 65); vs GPT-OSS: 89,2 − 66,0 = **23,2**.
4. GPT-OSS: GPQA 66,0 (medium, sem tools) · HLE 8,8 (com tools, medium) · MMLU 84,0 substitui o MMLU-Pro inexistente; IFEval 91,95 removido.
5. Typos: "grandeidade"→"grandeza"; "—benchmarks"→corrigido na reescrita.
