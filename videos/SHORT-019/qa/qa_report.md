# Relatório de Controle de Qualidade (QA) — SHORT-019
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-019/export/SHORT-019_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 24.74 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-14.9 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.1 dBFS | **0.1 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-019_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Apresenta a menor cidade do Brasil e o ranking dos menores municípios com dados oficiais do Censo 2022 do IBGE.
2. **Checagem de Fatos**:
   - Menor município: Serra da Saudade (MG) com 833 habitantes.
   - Municípios com menos de 1.000 habitantes: 3 no total (Serra da Saudade, Borá e Anhanguera).
   - Contraste: São Paulo capital com 11.451.245 habitantes (Censo 2022).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
