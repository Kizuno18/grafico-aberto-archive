# Relatório de Controle de Qualidade (QA) — SHORT-046
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-046/export/SHORT-046_master.mp4
Hash SHA256: 67cd6b49329d49a4afbb021f2631e0835d65f1fc9106ba4acf407838b8472200
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 23.76 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.2 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.1 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-046_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a partição e a concentração da renda no Brasil entre o topo e a base da pirâmide com microdados oficiais da PNAD Contínua do IBGE.
2. **Checagem de Fatos**:
   - Os 10% mais ricos concentram cerca de 41% a 42% de toda a massa de rendimentos nacional.
   - Os 50% com menores rendimentos (mais de 100 milhões de pessoas) dividem menos de 20% do total.
   - O rendimento médio per capita dos 50% da base situa-se em torno de R$ 600 por morador.
   - A razão entre o 1% do topo e a metade da base aproxima-se de 35 a 40 vezes.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
