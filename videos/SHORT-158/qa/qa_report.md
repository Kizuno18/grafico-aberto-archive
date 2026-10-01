# Relatorio de Controle de Qualidade (QA) — SHORT-158
Data da inspecao: 2026-10-01
Arquivo analisado: videos/SHORT-158/export/SHORT-158_master.mp4
Hash SHA256: 10137e4577e6026ea267782f5fdb222e6243530857d032e7acdd3460441cec69
Status de QA: **APROVADO**

---

## 1. Verificacao Tecnica Objetiva

| Criterio | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolucao de Video** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Video** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duracao Total** | Entre 18s e 35s | 18.70 segundos | APROVADO |
| **Audio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.7 LUFS** | APROVADO |
| **Audio - True Peak** | <= 0.0 dBFS | **-1.4 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-158_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificacao Editorial e de Conteudo

1. **Cumprimento da promessa**: Analisa o contingente de jovens de 15 a 29 anos que não estudam nem estão ocupados no mercado de trabalho (geração nem-nem) no Brasil.
2. **Checagem de Fatos**:
   - Dados apurados na PNAD Contínua (módulo Educação e Mercado de Trabalho) do IBGE e Ipea.
   - População de cerca de 10,9 milhões de jovens nessa condição (~20% da faixa etária).
   - Recorte de gênero crucial: cerca de 66% dos jovens nem-nem são mulheres, majoritariamente dedicadas a afazeres domésticos e cuidados não remunerados de dependentes.
3. **Propriedade e Direitos**:
   - Graficos autorais gerados via Matplotlib.
   - Voz neural local Piper TTS (pt_BR-faber-medium).
4. **Declaracoes**:
   - Nao direcionado a criancas.
   - Conteudo sintetico: Sim (voz sintetizada por IA).
