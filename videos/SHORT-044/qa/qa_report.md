# Relatório de Controle de Qualidade (QA) — SHORT-044
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-044/export/SHORT-044_master.mp4
Hash SHA256: 92a20a855f7895df2f10bbc41bde4e88586174a104aa628c362f8b9733d30e1a
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 24.68 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.7 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-044_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a jornada histórica da alfabetização no Brasil de 1940 a 2022 com base nas séries dos Censos Demográficos do IBGE.
2. **Checagem de Fatos**:
   - Em 1940, mais de 56% da população com 15 anos ou mais era analfabeta.
   - No Censo 2022, a taxa recuou para 7,0%, com 93,0% da população alfabetizada.
   - Entre jovens de 15 a 19 anos, a taxa de alfabetização supera 99%.
   - Desafio remanescente: analfabetismo residual concentrado em idosos (>16%) e no Nordeste (~14,2%).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
