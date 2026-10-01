 # Relatorio de Controle de Qualidade (QA) — SHORT-080
 Data da inspecao: 2026-09-26
 Arquivo analisado: videos/SHORT-080/export/SHORT-080_master.mp4
 Hash SHA256: 59b826c0bfc50dab56a124136113c6c6016bb49a83a5ffeeffdc8f51203c879c
 Status de QA: **APROVADO**
 
 ---
 
 ## 1. Verificacao Tecnica Objetiva
 
 | Criterio | Meta | Medido no Arquivo | Veredito |
 |---|---|---|---|
 | **Resolucao de Video** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
 | **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
 | **Codec de Video** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
 | **Duracao Total** | Entre 20s e 35s | 22.52 segundos | APROVADO |
 | **Audio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.5 LUFS** | APROVADO |
 | **Audio - True Peak** | <= 0.0 dBFS | **-1.5 dBFS** | APROVADO |
 | **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-080_legendas_pt-BR.srt | APROVADO |
 
 ---
 
 ## 2. Verificacao Editorial e de Conteudo
 
 1. **Cumprimento da promessa**: Analisa o salto da populacao em situacao de rua no Brasil (mais que triplicou: de 90 mil para quase 300 mil), a concentracao no Sudeste (>50%) e o perfil sociodemografico com dados do IPEA e CadUnico/MDS.
 2. **Checagem de Fatos**:
    - Contingente estimado pelo IPEA saltou de ~92k (2012) para ~290k (2024).
    - Mais de 50% concentrados no Sudeste (Sao Paulo capital tem mais de 50 mil).
    - Perfil: 85% homens adultos e 70% pretos e pardos (perda de renda/desemprego como causas principais).
 3. **Propriedade e Direitos**:
    - Graficos gerados em codigo autoral limpo (Matplotlib).
    - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
 4. **Declaracoes**:
    - Nao direcionado especificamente a criancas.
    - Conteudo alterado/sintetico: Sim (audio gerado por voz sintetizada com IA).
