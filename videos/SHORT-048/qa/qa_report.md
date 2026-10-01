# Relatório de Controle de Qualidade (QA) — SHORT-048
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-048/export/SHORT-048_master.mp4
Hash SHA256: c757c2cbc9e1606b87b1b8eada70865273c3640e143d6cb35006ae2b83641dea
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 23.48 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.3 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-048_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a dinâmica populacional do Censo 2022 do IBGE, revelando que as cidades médias brasileiras (100 mil a 500 mil habitantes) crescem no dobro do ritmo das grandes metrópoles.
2. **Checagem de Fatos**:
   - Cidades médias cresceram a um ritmo médio de 1,3% ao ano entre 2010 e 2022.
   - Metrópoles acima de 1 milhão de habitantes cresceram em média apenas 0,3% a.a. (com capitais como Rio, Salvador e Porto Alegre registrando queda líquida de população).
   - Fatores de atração do interior: custo de moradia mais baixo, interiorização do agronegócio e logística, além de melhor qualidade de vida.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
