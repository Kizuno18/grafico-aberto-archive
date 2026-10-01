# Relatório de Controle de Qualidade (QA) — SHORT-009
Data da inspeção: 2026-09-20
Arquivo analisado: ideos/SHORT-009/export/SHORT-009_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 24.87 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -16.0 LUFS | **-15.3 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-009_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Compara a produtividade por hora trabalhada no Brasil e no mundo, explicando as causas econômicas reais da diferença salarial.
2. **Checagem de Fatos**:
   - EUA: ~US$ 87 por hora trabalhada (The Conference Board Total Economy Database).
   - Coreia do Sul: ~US$ 49 / h.
   - Brasil: ~US$ 20 / h (The Conference Board / IPEA).
   - Em 1980, Brasil atingia ~40% da produtividade americana; hoje está em ~23%.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
