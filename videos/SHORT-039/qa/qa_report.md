# Relatório de Controle de Qualidade (QA) — SHORT-039
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-039/export/SHORT-039_master.mp4
Hash SHA256: 2fe93d4ae76d0dce38fc6dfdff2ca43bbb386781018c2c92d7cd388a3a02639b
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 22.80 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.5 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.3 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-039_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa o tempo diário despendido pela população urbana no transporte público e trânsito com dados oficiais do IPEA e ANTP (Simob).
2. **Checagem de Fatos**:
   - Em São Paulo e no Rio de Janeiro, o tempo médio diário de deslocamento casa-trabalho (ida e volta) aproxima-se de 2 horas (entre 95 e 105 minutos).
   - Aproximadamente 1 em cada 5 trabalhadores metropolitanos gasta mais de 2 horas por dia no trânsito.
   - O ônibus urbano continua sendo o pilar central, respondendo por mais de 85% de todas as viagens do transporte público coletivo nacional.
   - Prejuízo de congestionamentos estimado em mais de R$ 100 bilhões anuais em produtividade e combustível.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
