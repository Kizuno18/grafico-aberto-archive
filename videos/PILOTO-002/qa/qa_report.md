# Relatório de Controle de Qualidade (QA) — PILOTO-002
Data da inspeção: 2026-09-18
Arquivo analisado: ideos/PILOTO-002/export/PILOTO-002_video_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1920x1080 (16:9) | 1920x1080 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 1m15s e 3m00s | 1 minuto e 40 segundos (100.04s) | APROVADO |
| **Áudio - Integrated Loudness** | -16.0 LUFS (± 1 LUFS) | **-16.7 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **0.0 dBFS** | APROVADO |
| **Áudio - Loudness Range** | <= 10 LU | 3.6 LU (dinâmica consistente) | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | PILOTO-002_legendas_pt-BR.srt | APROVADO |
| **Miniatura (Thumbnail)** | 1280x720 PNG legível | 	humbnail.png gerado | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Responde diretamente ao poder de compra de R$ 100 de 1994 a 2026 com base em dados do BACEN.
2. **Checagem de Fatos**:
   - IPCA acumulado = +790,4% (BACEN SGS 433).
   - Equivalência = R$ 890,41 hoje.
   - Poder residual = R$ 11,23 em termos de 1994 (-88,8%).
   - Salário mínimo histórico = R$ 64,79 em jul/1994.
   - Cesta básica DIEESE = R$ 64,30 em jul/1994.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral (Matplotlib/Pillow).
   - Narração sintetizada via Piper TTS (voz Faber medium, dataset CC0 / MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
