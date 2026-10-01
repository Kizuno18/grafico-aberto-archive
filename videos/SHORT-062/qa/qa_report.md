 # Relatorio de Controle de Qualidade (QA) — SHORT-062
 Data da inspecao: 2026-09-26
 Arquivo analisado: videos/SHORT-062/export/SHORT-062_master.mp4
 Hash SHA256: 0432ace220a30d5f5977f3cc1d05aa53d483ba2a62675d31e6fee1daff968f88
 Status de QA: **APROVADO**
 
 ---
 
 ## 1. Verificacao Tecnica Objetiva
 
 | Criterio | Meta | Medido no Arquivo | Veredito |
 |---|---|---|---|
 | **Resolucao de Video** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
 | **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
 | **Codec de Video** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
 | **Duracao Total** | Entre 20s e 35s | 20.66 segundos | APROVADO |
 | **Audio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.5 LUFS** | APROVADO |
 | **Audio - True Peak** | <= 0.0 dBFS | **-1.5 dBFS** | APROVADO |
 | **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-062_legendas_pt-BR.srt | APROVADO |
 
 ---
 
 ## 2. Verificacao Editorial e de Conteudo
 
 1. **Cumprimento da promessa**: Analisa a transicao etaria da maternidade no Brasil (maes 30+ saltando para 35% e queda da gravidez na juventude para 12%) com dados do Sinasc/DataSUS e IBGE.
 2. **Checagem de Fatos**:
    - Maes com menos de 20 anos cairam de 23,5% (2000) para 12,4% (2024).
    - Maes com 30 anos ou mais subiram de 21,8% para 35,1% dos partos.
    - Taxa de fecundidade alcancou 1,57 filho por mulher.
 3. **Propriedade e Direitos**:
    - Graficos gerados em codigo autoral limpo (Matplotlib).
    - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
 4. **Declaracoes**:
    - Nao direcionado especificamente a criancas.
    - Conteudo alterado/sintetico: Sim (audio gerado por voz sintetizada com IA).
