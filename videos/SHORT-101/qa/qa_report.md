 # Relatorio de Controle de Qualidade (QA) — SHORT-101
 Data da inspecao: 2026-09-30
 Arquivo analisado: videos/SHORT-101/export/SHORT-101_master.mp4
 Hash SHA256: 56e1c5f107f7f039b444fdf89e86462150e4d62176aeabf8735d04d19bab0b4e
 Status de QA: **APROVADO**
 
 ---
 
 ## 1. Verificacao Tecnica Objetiva
 
 | Criterio | Meta | Medido no Arquivo | Veredito |
 |---|---|---|---|
 | **Resolucao de Video** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
 | **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
 | **Codec de Video** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
 | **Duracao Total** | Entre 20s e 35s | 24.04 segundos | APROVADO |
 | **Audio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.4 LUFS** | APROVADO |
 | **Audio - True Peak** | <= 0.0 dBFS | **-1.5 dBFS** | APROVADO |
 | **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-101_legendas_pt-BR.srt | APROVADO |
 
 ---
 
 ## 2. Verificacao Editorial e de Conteudo
 
 1. **Cumprimento da promessa**: Analisa o papel vital das aposentadorias do INSS na sustentacao de lares brasileiros (1 em cada 5 lares com idoso dependem exclusivamente dessa renda), o fato de o INSS superar o FPM em 70% das cidades e a reducao da extrema pobreza com dados do IBGE, Ipea e MPS.
 2. **Checagem de Fatos**:
    - Mais de 35% dos domicilios no Brasil tem pelo menos um idoso com beneficio previdenciario.
    - Em 70% dos municipios, o valor pago aos aposentados pelo INSS e maior que o FPM da prefeitura.
    - Sem a previdencia, a pobreza na terceira idade saltaria de 2% para mais de 50%.
 3. **Propriedade e Direitos**:
    - Graficos gerados em codigo autoral limpo (Matplotlib).
    - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
 4. **Declaracoes**:
    - Nao direcionado especificamente a criancas.
    - Conteudo alterado/sintetico: Sim (audio gerado por voz sintetizada com IA).
