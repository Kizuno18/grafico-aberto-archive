# Relatório de Controle de Qualidade (QA) — SHORT-023
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-023/export/SHORT-023_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 26.02 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.7 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **0.0 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-023_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a explosão das matrículas universitárias e o avanço do EAD com base no Censo da Educação Superior do Inep.
2. **Checagem de Fatos**:
   - Total de matrículas: quase 10 milhões (9,98 milhões no Inep).
   - Evolução: 2,7 milhões (2000) -> 6,3 milhões (2010) -> 10,0 milhões (hoje).
   - EAD: representa mais de 65% dos novos ingressantes no ensino superior.
   - Setor privado: concentra 78,5% das matrículas.
   - Adultos com curso superior: saltou de ~7% para 21% da população (IBGE PNAD).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
