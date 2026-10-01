# Relatório de Controle de Qualidade (QA) — PILOTO-001
Data da inspeção: 2026-09-18
Arquivo analisado: `videos/PILOTO-001/export/PILOTO-001_video_master.mp4`
Hash SHA256: `A607B0583E8E16DEEA82EB31BE6C6839BC8B633E43BAC33D76439430E0F54E93`
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1920x1080 (16:9) | 1920x1080 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 1m15s e 3m00s | 1 minuto e 33 segundos (93.02s) | APROVADO |
| **Áudio - Integrated Loudness** | -16.0 LUFS (± 1 LUFS) | **-15.9 LUFS** | APROVADO |
| **Áudio - True Peak** | <= -0.1 dBFS | **-0.1 dBFS** | APROVADO |
| **Áudio - Loudness Range** | <= 10 LU | 3.0 LU (dinâmica consistente) | APROVADO |
| **Áudio - Sample Rate** | 48.000 Hz / AAC | 48.000 Hz / AAC Estéreo | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | `PILOTO-001_legendas_pt-BR.srt` | APROVADO |
| **Miniatura (Thumbnail)** | 1280x720 PNG legível | `thumbnail.png` gerado | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: O vídeo responde diretamente à pergunta do título e da miniatura ("A Pirâmide Etária do Brasil Encolheu"). Não há clickbait falso nem desvios do assunto.
2. **Checagem de Fatos e Evidências**:
   - Todas as porcentagens e números citados (38,2% em 1980 -> 19,8% em 2022; taxa de fecundidade < 1,6; idade mediana de 29 para 35 anos) estão rigorosamente ancorados nos dados oficiais do IBGE Censo 2022 (Resultados do Universo) e no dossiê de fontes primárias.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código local via Matplotlib/Pillow (código 100% autoral).
   - Narração gerada via Piper TTS (voz Faber medium, treinada sobre dataset CC0 da NabuCasa, código aberto sob licença MIT, permitida para uso comercial).
   - Sem uso de bancos de imagem de terceiros, sem marcas registradas externas e sem exposição de dados pessoais ou privados.
4. **Declarações de Plataforma**:
   - Classificação de Público: **Não é conteúdo voltado para crianças** (audiência geral/adulta).
   - Conteúdo Alterado/Sintético: **Sim** (Áudio gerado por voz sintetizada com inteligência artificial, cumprindo expressamente a política de transparência 14328491 do YouTube).
   - Inserções pagas/patrocínio: **Não contém** (vídeo puramente editorial e educativo).
