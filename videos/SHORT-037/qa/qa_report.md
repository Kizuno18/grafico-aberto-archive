# Relatório de Controle de Qualidade (QA) — SHORT-037
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-037/export/SHORT-037_master.mp4
Hash SHA256: 22bbe2735b0fe97768645d51f03e957d8ab9103290e431bfb68b0fbb572164ff
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 23.40 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.5 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.4 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-037_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a vitória histórica da saúde pública brasileira com a queda de mais de 85% na mortalidade infantil com base em estatísticas do Ministério da Saúde e IBGE.
2. **Checagem de Fatos**:
   - Taxa caiu de 82,8 óbitos por mil nascidos vivos em 1980 para menos de 12 por mil atualmente.
   - Redução acumulada superior a 85% em quatro décadas.
   - Fatores decisivos: vacinação pelo PNI, criação e expansão do SUS, ampliação da água tratada e cobertura de pré-natal/partos hospitalares (>98%).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
