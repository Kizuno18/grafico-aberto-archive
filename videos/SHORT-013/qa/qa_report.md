# Relatório de Controle de Qualidade (QA) — SHORT-013
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-013/export/SHORT-013_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 21.41 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.5 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-013_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a explosão de domicílios unipessoais no Brasil com base no Censo 2022.
2. **Checagem de Fatos**:
   - Domicílios unipessoais: 18,9% dos lares (13,7 milhões de domicílios, Censo 2022).
   - Em 2010: 12,2% (7 milhões).
   - Média de moradores por domicílio: 2,79 pessoas (pela primeira vez abaixo de 3).
   - Em 1960: média era de 5,3 moradores por casa.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
