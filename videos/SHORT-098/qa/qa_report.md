 # Relatorio de Controle de Qualidade (QA) — SHORT-098
 Data da inspecao: 2026-09-30
 Arquivo analisado: videos/SHORT-098/export/SHORT-098_master.mp4
 Hash SHA256: 49a179c4ed55c97b31b67973213de42c88d9b11f89e4a85e6963c7bf254d123c
 Status de QA: **APROVADO**
 
 ---
 
 ## 1. Verificacao Tecnica Objetiva
 
 | Criterio | Meta | Medido no Arquivo | Veredito |
 |---|---|---|---|
 | **Resolucao de Video** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
 | **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
 | **Codec de Video** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
 | **Duracao Total** | Entre 20s e 35s | 22.48 segundos | APROVADO |
 | **Audio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.8 LUFS** | APROVADO |
 | **Audio - True Peak** | <= 0.0 dBFS | **-1.5 dBFS** | APROVADO |
 | **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-098_legendas_pt-BR.srt | APROVADO |
 
 ---
 
 ## 2. Verificacao Editorial e de Conteudo
 
 1. **Cumprimento da promessa**: Analisa a diferenca demografica no Brasil (6 milhoes de mulheres a mais), a razao de sexo nas capitais (Recife e Salvador com ~85 homens/100 mulheres) e os fatores de longevidade e mortalidade masculina com dados do Censo 2022 (IBGE).
 2. **Checagem de Fatos**:
    - Populacao feminina de 104,5 mi vs masculina de 98,5 mi (diferenca de 6,0 milhoes).
    - Recife (84,9) e Salvador (85,2) sao as capitais com menor proporcao de homens por 100 mulheres.
    - Expectativa de vida feminina cerca de 7 anos superior a masculina.
 3. **Propriedade e Direitos**:
    - Graficos gerados em codigo autoral limpo (Matplotlib).
    - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
 4. **Declaracoes**:
    - Nao direcionado especificamente a criancas.
    - Conteudo alterado/sintetico: Sim (audio gerado por voz sintetizada com IA).
