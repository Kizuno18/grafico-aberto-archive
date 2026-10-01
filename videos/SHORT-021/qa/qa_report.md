# Relatório de Controle de Qualidade (QA) — SHORT-021
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-021/export/SHORT-021_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 24.34 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.5 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-021_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Apresenta e contextualiza a evolução da idade média ao casar e da taxa de divórcios no Brasil com base nas Estatísticas do Registro Civil do IBGE.
2. **Checagem de Fatos**:
   - Idade média ao casar: subiu de 23/26 anos (1990) para 31 anos (mulheres) e 33,5 anos (homens) em 2022.
   - Duração média do casamento até o divórcio: caiu de 17,5 anos (2000) para 13,8 anos (2022).
   - Relação casamentos/divórcios: aproximadamente 1 divórcio para cada 2,3 casamentos civis.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
