# Relatório de Controle de Qualidade (QA) — SHORT-022
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-022/export/SHORT-022_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 24.01 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.1 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.4 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-022_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a cobertura e as carências de saneamento básico no Brasil com base no Censo 2022 do IBGE.
2. **Checagem de Fatos**:
   - Sem esgoto adequado: 37,5% da população (> 75 milhões de pessoas).
   - Cobertura regional de esgoto: Sudeste (86,2%), Sul (68,7%), Centro-Oeste (58,9%), Nordeste (41,3%), Norte (14,7%).
   - Sem rede geral de água encanada: 17,1% da população (33,8 milhões de pessoas).
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
