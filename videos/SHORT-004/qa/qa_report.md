# Relatório de Controle de Qualidade (QA) — SHORT-004
Data da inspeção: 2026-09-19
Arquivo analisado: ideos/SHORT-004/export/SHORT-004_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 23.68 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -16.0 LUFS | **-14.2 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.1 dBFS | **0.1 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-004_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: A promessa de explicar a queda da taxa de fecundidade é cumprida diretamente com números oficiais do IBGE.
2. **Checagem de Fatos**:
   - Taxa em 1960: 6,28 filhos por mulher (IBGE Censo 1960).
   - Taxa em 2022: 1,57 filho por mulher (IBGE Censo 2022 / Projeções 2024).
   - Variação relativa: Queda de 75% comprovada aritmeticamente.
   - Nível de reposição populacional: 2,1 filhos por mulher (ONU / IBGE).
   - Menor patamar de nascimentos em 40 anos (< 2,6 milhões no Registro Civil IBGE).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
