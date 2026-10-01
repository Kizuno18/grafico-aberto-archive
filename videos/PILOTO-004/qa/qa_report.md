# Relatório de Controle de Qualidade (QA) — PILOTO-004
Data da inspeção: 2026-09-20
Arquivo analisado: ideos/PILOTO-004/export/PILOTO-004_video_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1920x1080 (16:9) | 1920x1080 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 1m15s e 2m30s | 1 minuto e 36 segundos (96.34s) | APROVADO |
| **Áudio - Integrated Loudness** | -16.0 LUFS (± 1 LUFS) | **-16.5 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.0 dBFS** | APROVADO |
| **Áudio - Loudness Range** | <= 10 LU | 3.7 LU (dinâmica consistente) | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | PILOTO-004_legendas_pt-BR.srt | APROVADO |
| **Miniatura (Thumbnail)** | 1280x720 PNG legível | 	humbnail.png gerado | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Explica a estrutura da carga tributária brasileira com dados da Receita Federal e do IPEA.
2. **Checagem de Fatos**:
   - Carga tributária bruta: ~33,1% do PIB (Receita Federal / Fazenda).
   - Tributos sobre consumo (bens e serviços): 44,2% da arrecadação.
   - Folha salarial / previdência: 26,1%.
   - Renda, lucros e capital: 23,4%.
   - Propriedade: 4,8%.
   - Impacto na baixa renda (POF IBGE / IPEA): famílias até 2 SM pagam 26,5% da renda em tributos indiretos vs 10,1% nos 10% mais ricos.
   - Comparativo OCDE: OCDE tributa mais renda (34%) do que consumo (32%).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
