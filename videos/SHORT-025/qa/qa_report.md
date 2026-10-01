# Relatório de Controle de Qualidade (QA) — SHORT-025
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-025/export/SHORT-025_master.mp4
Hash SHA256: eb7db249b255b8509ce11eb4e775f8390a8643b8fbd1e7010fea74f57f1c9394
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 25.20 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.9 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-025_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a evolução do desemprego no Brasil de 2014 a 2024 usando dados oficiais da PNAD Contínua (IBGE).
2. **Checagem de Fatos**:
   - Mínima anterior em 2014: ~6,8%.
   - Pico da pandemia em 2020: 14,9% (mais de 14,5 milhões de pessoas desocupadas).
   - Queda recente em 2024: 6,8% (menor patamar em 10 anos).
   - População ocupada recorde: mais de 102 milhões de pessoas.
   - Desafio persistente: informalidade em torno de 38-39%.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
