 # Relatorio de Controle de Qualidade (QA) — SHORT-060
 Data da inspecao: 2026-09-26
 Arquivo analisado: videos/SHORT-060/export/SHORT-060_master.mp4
 Hash SHA256: 92248e7457ed400099f11a442ef632bc10c627b3b1bdd771178fa80f99377d84
 Status de QA: **APROVADO**
 
 ---
 
 ## 1. Verificacao Tecnica Objetiva
 
 | Criterio | Meta | Medido no Arquivo | Veredito |
 |---|---|---|---|
 | **Resolucao de Video** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
 | **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
 | **Codec de Video** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
 | **Duracao Total** | Entre 20s e 35s | 23.61 segundos | APROVADO |
 | **Audio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.3 LUFS** | APROVADO |
 | **Audio - True Peak** | <= 0.0 dBFS | **-1.5 dBFS** | APROVADO |
 | **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-060_legendas_pt-BR.srt | APROVADO |
 
 ---
 
 ## 2. Verificacao Editorial e de Conteudo
 
 1. **Cumprimento da promessa**: Analisa os 51 milhoes de beneficiarios de planos de saude no Brasil (25% da populacao), a disparidade regional e a dependencia do mercado formal com dados da ANS e IBGE.
 2. **Checagem de Fatos**:
    - 25% da populacao tem convenio medico privado; 75% dependem exclusivamente do SUS.
    - Disparidade regional: Sudeste (36%, SP 40%) vs Norte (11%) e Nordeste (14%).
    - 82% dos planos sao coletivos/empresariais, atrelados a carteira assinada.
 3. **Propriedade e Direitos**:
    - Graficos gerados em codigo autoral limpo (Matplotlib).
    - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
 4. **Declaracoes**:
    - Nao direcionado especificamente a criancas.
    - Conteudo alterado/sintetico: Sim (audio gerado por voz sintetizada com IA).
