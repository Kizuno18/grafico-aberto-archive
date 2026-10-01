# Relatório de Controle de Qualidade (QA) — SHORT-050
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-050/export/SHORT-050_master.mp4
Hash SHA256: b4373dba9c9e41c295d324720c8c202a5ba29fa17455e9a116e3973ff7ad84fa
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 25.56 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.6 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.4 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-050_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a revolução das motocicletas no Brasil e a transformação da mobilidade com dados oficiais da Senatran e do IBGE.
2. **Checagem de Fatos**:
   - Frota de motocicletas saltou de 4,0 milhões (2000) para mais de 33,5 milhões (2024), crescendo mais de 8 vezes.
   - Na região Nordeste, as motos representam cerca de 50% de toda a frota automotiva registrada.
   - Em centenas de cidades do interior, a proporção chega a 2 a 3 motos para cada automóvel de passeio.
   - Impacto econômico: inclusão produtiva e transporte de baixo custo, contrastando com o desafio das internações no SUS por acidentes.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
