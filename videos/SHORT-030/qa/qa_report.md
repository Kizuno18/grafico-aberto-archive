# Relatório de Controle de Qualidade (QA) — SHORT-030
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-030/export/SHORT-030_master.mp4
Hash SHA256: 7431c282538350eb4585d6b25ba7a3a1603cf7cd57f49f051898b12db529b849
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 22.96 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.1 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.4 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-030_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa o investimento educacional por aluno no Brasil em comparação com a média da OCDE e países desenvolvidos com dados oficiais do Education at a Glance e INEP.
2. **Checagem de Fatos**:
   - Investimento por aluno na educação básica no Brasil: cerca de US$ 3.500/ano (PPA).
   - Média da OCDE: aproximadamente US$ 11.500/ano (mais de 3 vezes o valor brasileiro).
   - Investimento em proporção do PIB: Brasil gasta em torno de 6% do PIB, semelhante ou superior à média dos países ricos (~5%).
   - Explicação do paradoxo: o PIB per capita é menor e a proporção de jovens em idade escolar é maior, reduzindo o valor por estudante.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
