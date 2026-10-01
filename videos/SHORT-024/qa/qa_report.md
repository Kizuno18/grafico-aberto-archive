# Relatório de Controle de Qualidade (QA) — SHORT-024
Data da inspeção: 2026-09-21
Arquivo analisado: ideos/SHORT-024/export/SHORT-024_master.mp4
Hash SHA256: $hash
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 30.0 fps | 30.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 25.83 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-15.6 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.4 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-024_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a pauta de exportações brasileiras com dados oficiais do MDIC (Comex Stat), identificando os 3 maiores produtos e o principal parceiro comercial.
2. **Checagem de Fatos**:
   - Total exportado: ~US$ 340 bilhões (recorde recente).
   - Top 3: Soja em grão (US$ 53,2B), Petróleo bruto (US$ 42,5B) e Minério de ferro (US$ 30,5B).
   - Concentração: quase 38% de toda a pauta exportadora nesses 3 itens.
   - Destino principal: China é compradora de mais de 30% das exportações totais.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib/Pillow).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
