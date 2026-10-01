 # Relatorio de Controle de Qualidade (QA) — SHORT-090
 Data da inspecao: 2026-09-30
 Arquivo analisado: videos/SHORT-090/export/SHORT-090_master.mp4
 Hash SHA256: ff7c72f2adaf0ba43ba6a767e43b34e5edf9cbe8bd02c3256f1079f4d410e599
 Status de QA: **APROVADO**
 
 ---
 
 ## 1. Verificacao Tecnica Objetiva
 
 | Criterio | Meta | Medido no Arquivo | Veredito |
 |---|---|---|---|
 | **Resolucao de Video** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
 | **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
 | **Codec de Video** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
 | **Duracao Total** | Entre 20s e 35s | 24.60 segundos | APROVADO |
 | **Audio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.3 LUFS** | APROVADO |
 | **Audio - True Peak** | <= 0.0 dBFS | **-1.5 dBFS** | APROVADO |
 | **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-090_legendas_pt-BR.srt | APROVADO |
 
 ---
 
 ## 2. Verificacao Editorial e de Conteudo
 
 1. **Cumprimento da promessa**: Analisa o paradoxo dos 11,4 milhoes de domicilios particulares vagos no Brasil (quase o dobro do deficit habitacional de 5,9 milhoes), a concentracao no Sudeste/capitais e a retencao imobiliaria com dados do Censo 2022 (IBGE) e Fundacao Joao Pinheiro.
 2. **Checagem de Fatos**:
    - 11,4 milhoes de domicilios vagos recenseados pelo IBGE (+ 6,7 mi de uso ocasional).
    - Deficit habitacional estimado em ~5,9 milhoes de moradias.
    - Mais de 580 mil imoveis vagos na capital paulista e ~350 mil no Rio de Janeiro.
 3. **Propriedade e Direitos**:
    - Graficos gerados em codigo autoral limpo (Matplotlib).
    - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
 4. **Declaracoes**:
    - Nao direcionado especificamente a criancas.
    - Conteudo alterado/sintetico: Sim (audio gerado por voz sintetizada com IA).
