# Relatório de Controle de Qualidade (QA) — SHORT-032
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-032/export/SHORT-032_master.mp4
Hash SHA256: a3d2b3707c1e5bdda5ee049d0c477800e05aee7b01f707c896c8bdecf648451e
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 24.68 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.6 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.4 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-032_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a desigualdade geográfica na distribuição de médicos no Brasil com base nas estatísticas oficiais do CFM e no estudo Demografia Médica da USP.
2. **Checagem de Fatos**:
   - Total de médicos no Brasil ultrapassa 570 mil profissionais ativos.
   - Densidade nas capitais: média de 6,2 médicos por mil habitantes (em capitais como Vitória chega a 14/mil).
   - Densidade no interior: média de apenas 1,6 médico por mil habitantes.
   - Concentração regional: Sudeste concentra mais de 53% de todos os médicos do país.
   - Mais de 2.500 municípios têm menos de 1 médico por mil habitantes.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
