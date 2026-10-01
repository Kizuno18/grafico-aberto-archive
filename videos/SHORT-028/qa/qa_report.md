# Relatório de Controle de Qualidade (QA) — SHORT-028
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-028/export/SHORT-028_master.mp4
Hash SHA256: d0130b6bf16ede5919553afd45c11e6b06b4396f32de17db2057fdaf9928d301
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 24.36 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.0 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.2 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-028_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a transição religiosa no Brasil ao longo de 4 décadas com base nos dados oficiais dos Censos Demográficos do IBGE (1980 a 2022).
2. **Checagem de Fatos**:
   - Católicos passaram de 89,0% em 1980 para aproximadamente 52% atualmente.
   - Evangélicos quadruplicaram sua participação, indo de 6,6% para mais de 30%.
   - Pessoas sem religião declarada cresceram de 1,6% para cerca de 10%.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
