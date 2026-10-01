# Relatório de Controle de Qualidade (QA) — SHORT-035
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-035/export/SHORT-035_master.mp4
Hash SHA256: 0d808e26ec60f40a992573f9e19c298901f1fbd6d6aff329ffd0a0d6afbf8ee4
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 26.04 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.7 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-035_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a trajetória dos homicídios no Brasil desde o pico histórico de 2017 até a queda recente, com base nos dados oficiais do IPEA e FBSP (Atlas da Violência).
2. **Checagem de Fatos**:
   - Em 2017, o país registrou 65.602 homicídios (taxa de 31,6 por 100 mil habitantes).
   - Recuo acumulado de mais de 30% a 35%, estabilizando na faixa de 21 por 100 mil habitantes (menor número em mais de uma década).
   - Contrastes regionais severos: São Paulo registra taxa abaixo de 7 por 100 mil, enquanto estados do Norte e Nordeste registram taxas acima de 35 por 100 mil.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
