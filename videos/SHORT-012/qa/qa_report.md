# Relatório de Controle de Qualidade (QA) — SHORT-012
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-012/export/SHORT-012_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 26.91 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.3 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.4 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-012_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a evolução do Índice de Gini de 1995 a 2024 com dados oficiais do IBGE e do IPEA.
2. **Checagem de Fatos**:
   - Gini em 1995: 0,600 (PNAD / IPEA).
   - Gini em 2014: 0,515 (mínima histórica).
   - Gini atual (2024): ~0,518 (PNAD Contínua IBGE).
   - Queda relativa: ~13,7% (aproximadamente 14%).
   - Posição global: Brasil segue no top 15 de maior desigualdade do mundo (PNUD / Banco Mundial).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
