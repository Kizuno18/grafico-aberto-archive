# Relatório de Controle de Qualidade (QA) — SHORT-026
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-026/export/SHORT-026_master.mp4
Hash SHA256: e86f57964121f045d856db8571b3f2c8a2e207ab1125abd5294fa77ac9504334
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 21.48 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.6 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-026_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a virada demográfica nos municípios brasileiros onde já existem mais idosos do que crianças, com base no Censo 2022 do IBGE.
2. **Checagem de Fatos**:
   - Mais de 1.300 cidades têm índice de envelhecimento maior que 100.
   - Índice nacional subiu de 30,7 (2010) para 55,2 (2022).
   - Coqueiro Baixo (RS) é a campeã nacional com 290 idosos por 100 crianças.
   - Porto Alegre (92,0) e Rio de Janeiro (89,0) são as capitais mais envelhecidas.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
