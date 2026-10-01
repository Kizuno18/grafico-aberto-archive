# Relatório de Controle de Qualidade (QA) — SHORT-017
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-017/export/SHORT-017_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 26.87 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.3 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.1 dBFS | **0.1 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-017_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Esclarece com rigor técnico a diferença entre o PIB agropecuário estrito (IBGE) e o PIB do Agronegócio da cadeia estendida (CEPEA/USP).
2. **Checagem de Fatos**:
   - Agropecuária primária (IBGE Contas Nacionais): ~7% do PIB.
   - Cadeia completa do Agronegócio (CEPEA/USP e CNA): ~24% a 27% do PIB (incluindo insumos, agroindústria e agrosserviços).
   - Exportações: Agronegócio responde por aproximadamente 49% a 50% das exportações totais brasileiras (MDIC Comex Stat).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
