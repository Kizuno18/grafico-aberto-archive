# Relatório de Controle de Qualidade (QA) — SHORT-011
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-011/export/SHORT-011_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 25.53 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.4 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.1 dBFS | **0.1 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-011_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a montanha-russa da taxa Selic com dados históricos oficiais do Banco Central.
2. **Checagem de Fatos**:
   - Selic máxima: 45,0% a.a. em março de 1999 (Copom / BACEN SGS 432).
   - Selic mínima: 2,0% a.a. em agosto de 2020 (Copom / BACEN SGS 432).
   - Juro real estrutural no Brasil: 6% a 7% a.a. acima da inflação.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
