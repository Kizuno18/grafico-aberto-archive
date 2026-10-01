# Relatório de Controle de Qualidade (QA) — SHORT-007
Data da inspeção: 2026-09-20
Arquivo analisado: ideos/SHORT-007/export/SHORT-007_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 31.16 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -16.0 LUFS | **-15.5 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-007_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Revela com dados oficiais do Banco Central o ganho real acumulado do salário mínimo acima da inflação.
2. **Checagem de Fatos**:
   - Salário em julho/1994: R$ 64,79 (BACEN SGS Série 1619).
   - Inflação acumulada IPCA (1994-2026): fator de 8,90x (BACEN SGS Série 433).
   - Salário corrigido só pela inflação: R$ 576,89.
   - Salário oficial atual: R$ 1.621,00.
   - Ganho real líquido: +181,0% (poder de compra multiplicado por 2,8x).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
