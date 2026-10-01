# Relatório de Controle de Qualidade (QA) — SHORT-029
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-029/export/SHORT-029_master.mp4
Hash SHA256: 32db5dd214030f6d93bea01dce478fad1d94781f23592b2c570056b04ce03f59
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 24.72 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.2 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.1 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-029_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a decomposição real das emissões de gases de efeito estufa no Brasil com base nos relatórios oficiais do SEEG / Observatório do Clima e MCTI.
2. **Checagem de Fatos**:
   - Mudança no uso da terra (desmatamento) responde por cerca de 48% das emissões brutas.
   - Agropecuária direta responde por ~27%.
   - Juntos, uso da terra e agro respondem por 75% das emissões nacionais.
   - Setor de energia e transporte representa menos de 20%, ao contrário da média global (>75%), graças à matriz elétrica renovável e biocombustíveis.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
