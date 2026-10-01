# Relatório de Controle de Qualidade (QA) — SHORT-043
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-043/export/SHORT-043_master.mp4
Hash SHA256: f81a13363c1f483b9a0f3dbdd156f4e098b7811eeac0996f526b81e2ffa0e470
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 22.00 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.0 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.2 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-043_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a evolução do tráfego aéreo de passageiros no Brasil desde 2000 e os aeroportos mais movimentados com dados oficiais da ANAC.
2. **Checagem de Fatos**:
   - Volume anual de passageiros no país ultrapassa 112 milhões (tráfego quase quadruplicou em relação aos anos 2000, quando registrava ~30 milhões).
   - Guarulhos (GRU) é o maior aeroporto com mais de 40 milhões de passageiros/ano, seguido por Congonhas com ~22 milhões e Brasília com ~15 milhões.
   - A rota aérea Congonhas-Santos Dumont (Ponte Aérea) figura entre as 5 rotas domésticas mais densas do mundo.
   - Mais de 90 milhões de passageiros voam em rotas estritamente domésticas no Brasil.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
