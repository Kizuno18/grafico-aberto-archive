# Relatório de Controle de Qualidade (QA) — SHORT-041
Data da inspeção: 2026-09-26
Arquivo analisado: videos/SHORT-041/export/SHORT-041_master.mp4
Hash SHA256: c5bfce78584f0a54574e3aa49aaf482c5a6114ca76c004774d14a474f66c0b27
Status de QA: **APROVADO**

---

## 1. Verificação Técnica Objetiva

| Critério | Meta | Medido no Arquivo | Veredito |
|---|---|---|---|
| **Resolução de Vídeo** | 1080x1920 (9:16 Vertical) | 1080x1920 | APROVADO |
| **Taxa de Quadros (FPS)** | 25.0 fps | 25.0 fps | APROVADO |
| **Codec de Vídeo** | H.264 / AVC | H.264 (High profile, yuv420p) | APROVADO |
| **Duração Total** | Entre 20s e 35s | 23.44 segundos | APROVADO |
| **Áudio - Integrated Loudness** | -14.0 a -17.0 LUFS | **-16.6 LUFS** | APROVADO |
| **Áudio - True Peak** | <= 0.0 dBFS | **-0.1 dBFS** | APROVADO |
| **Legendas Sincronizadas** | Formato SRT pt-BR | SHORT-041_legendas_pt-BR.srt | APROVADO |

---

## 2. Verificação Editorial e de Conteúdo

1. **Cumprimento da promessa**: Analisa a desigualdade regional no acesso à água encanada pela rede geral no Brasil com dados oficiais do Censo Demográfico 2022 (IBGE).
2. **Checagem de Fatos**:
   - Cerca de 83% da população brasileira tem acesso à rede geral de abastecimento de água (deixando ~34 milhões fora da rede pública).
   - Região Sudeste lidera com mais de 91% de atendimento domiciliar.
   - Região Norte tem o pior índice do país (apenas 58% atendida pela rede geral), dependendo massivamente de poços e captação direta.
   - O paradoxo da maior bacia de água doce do mundo (Bacia Amazônica) com a menor infraestrutura de rede de distribuição tratada.
3. **Propriedade e Direitos**:
   - Gráficos gerados em código autoral limpo (Matplotlib).
   - Voz neural local Piper TTS (pt_BR-faber-medium, CC0/MIT).
4. **Declarações**:
   - Não direcionado especificamente a crianças.
   - Conteúdo alterado/sintético: Sim (áudio gerado por voz sintetizada com IA).
