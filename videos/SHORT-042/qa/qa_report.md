# Relatório de Controle de Qualidade (QA) — SHORT-042
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-042/export/SHORT-042_master.mp4
Hash SHA256: 428bc0ca494cf3f82f9bb2ceec6d940900916a68b6a4c274285f33f4668ae465
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 22.48 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-14.9 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.3 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-042_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a disparidade histórica entre a inflação dos alimentos (alimentação no domicílio) e o índice geral do IPCA com dados oficiais do IBGE.
2. **Checagem de Fatos**:
   - Entre 2010 e 2024, o IPCA Geral subiu cerca de 132%, enquanto a alimentação em casa acumulou alta de 188% (quase 60 pontos percentuais acima).
   - O peso do grupo alimentação consome em média 21% do orçamento familiar geral, mas ultrapassa 27% a 30% nas famílias de baixa renda medidas pelo INPC/POF.
   - Explicação estrutural: cotações em dólar das commodities agrícolas (soja, carne, milho, açúcar), eventos climáticos extremos e custos de frete rodoviário.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
