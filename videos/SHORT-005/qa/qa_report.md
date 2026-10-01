# Relatório de Controle de Qualidade (QA) — SHORT-005
Data da inspeção: 2026-09-19
Arquivo analisado: ideos/SHORT-005/export/SHORT-005_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 24.92 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -16.0 LUFS | **-15.9 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-005_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Apresenta e comprova com o Censo 2022 o esvaziamento das capitais históricas e o avanço do Centro-Oeste.
2. **Checagem de Fatos**:
   - Crescimento do Centro-Oeste: +1,23% ao ano (maior taxa entre regiões, IBGE Censo 2022).
   - Salvador: -9,6% (-258 mil pessoas).
   - Porto Alegre: -5,4% (-76 mil pessoas).
   - Rio de Janeiro: -1,7% (-109 mil pessoas).
   - Natal: -6,5% / Belém: -6,5%.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
