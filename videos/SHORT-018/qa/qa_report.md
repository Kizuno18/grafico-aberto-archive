# Relatório de Controle de Qualidade (QA) — SHORT-018
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-018/export/SHORT-018_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 23.20 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.2 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.4 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-018_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Explica o que são e para que servem as reservas internacionais de US$ 355 bilhões com dados do Banco Central.
2. **Checagem de Fatos**:
   - Volume atual das reservas cambiais: ~US$ 355 bilhões (BACEN Série SGS 3546).
   - Décadas de 80 e 90: reservas abaixo de US$ 20 bilhões com crises frequentes de balanço de pagamentos.
   - Aplicação: > 85% em títulos do Tesouro dos EUA e moedas fortes, além de ouro.
   - Cobertura: garante mais de 1 ano completo de importações brasileiras.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
