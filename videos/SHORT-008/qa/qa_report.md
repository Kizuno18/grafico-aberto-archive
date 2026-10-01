# Relatório de Controle de Qualidade (QA) — SHORT-008
Data da inspeção: 2026-09-20
Arquivo analisado: ideos/SHORT-008/export/SHORT-008_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 26.85 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -16.0 LUFS | **-15.4 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-008_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Revela dados oficiais do Censo 2022 sobre habitação, comparando casas e apartamentos.
2. **Checagem de Fatos**:
   - Moradores em casas: 84,8% (171,3 milhões de pessoas, Censo 2022).
   - Moradores em apartamentos: 12,5% (25,2 milhões de pessoas, Censo 2022).
   - Evolução: 7,6% (2000) -> 8,5% (2010) -> 12,5% (2022) — crescimento de 47%.
   - Santos (SP): 63,4% em apartamentos (líder isolada nacional).
   - Balneário Camboriú (57,2%) e Vitória (45,4%) no topo da verticalização.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
