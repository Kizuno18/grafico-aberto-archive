# Relatório de Controle de Qualidade (QA) — SHORT-027
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-027/export/SHORT-027_master.mp4
Hash SHA256: f8b8b62f511884e50575a61308c98e22088ddf27c06647b82f0c7509bd12569d
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 23.48 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.6 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.6 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-027_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a extrema dependência do modal rodoviário no transporte de cargas no Brasil usando dados oficiais da CNT e EPL/Ministério dos Transportes.
2. **Checagem de Fatos**:
   - Modal rodoviário responde por cerca de 65% da carga total transportada (TKU).
   - Ferrovias representam ~15% e hidrovias/cabotagem ~11%.
   - Nos EUA, o transporte ferroviário ultrapassa 40% da matriz de carga.
   - Ferrovias consom até 4x menos combustível por tonelada transportada em longas distâncias.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
