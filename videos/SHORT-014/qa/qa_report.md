# Relatório de Controle de Qualidade (QA) — SHORT-014
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-014/export/SHORT-014_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 25.78 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.4 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.2 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-014_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a evolução da expectativa de vida de 1940 a 2024 com dados da Tábua de Mortalidade do IBGE.
2. **Checagem de Fatos**:
   - Expectativa de vida em 1940: 45,5 anos (IBGE).
   - Expectativa de vida em 1980: 62,5 anos.
   - Expectativa atual: 76,4 anos (IBGE).
   - Ganho acumulado: +30,9 anos de vida (+68%).
   - Fatores principais: vacinação, saneamento básico e redução drástica da mortalidade infantil.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
