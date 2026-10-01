import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A QUEDA DA FECUNDIDADE", color='#ffffff', fontsize=40, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Filhos por Mulher no Brasil (1960 - 2022)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Históricos do Censo IBGE
anos = [1960, 1970, 1980, 1991, 2000, 2010, 2022]
taxas = [6.28, 5.76, 4.07, 2.68, 2.38, 1.90, 1.57]

# Plot da linha histórica
ax.plot(anos, taxas, color='#f43f5e', linewidth=5, marker='o', markersize=14, markerfacecolor='#ffffff', markeredgecolor='#f43f5e', markeredgewidth=4, zorder=5)

# Linha de Nível de Reposição (2.1)
ax.axhline(2.10, color='#38bdf8', linestyle='--', linewidth=3, alpha=0.8, zorder=3)
ax.text(1961, 2.25, "NÍVEL DE REPOSIÇÃO: 2,1 FILHOS", color='#38bdf8', fontsize=22, fontweight='bold')

# Configurar Eixos
ax.set_xlim(1956, 2026)
ax.set_ylim(0.8, 7.2)
ax.set_xticks(anos)
ax.set_xticklabels([str(a) for a in anos], color='#cbd5e1', fontsize=24, fontweight='bold')
ax.tick_params(axis='y', colors='#94a3b8', labelsize=22)
ax.grid(True, linestyle=':', alpha=0.25, color='#475569')

# Rótulos de dados nos pontos
for a, t in zip(anos, taxas):
    offset_y = 0.35 if a != 2022 else -0.55
    color = '#fbbf24' if a in [1960, 2022] else '#ffffff'
    weight = 'bold' if a in [1960, 2022] else 'normal'
    fontSize = 28 if a in [1960, 2022] else 22
    ax.text(a, t + offset_y, f"{t:.2f}".replace('.', ','), color=color, fontsize=fontSize, fontweight=weight, ha='center', zorder=6)

# Posição dos eixos no layout vertical
ax.set_position([0.12, 0.46, 0.80, 0.35])

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f43f5e', linewidth=2)
fig.text(0.5, 0.26, 
        "INVERSÃO DEMOGRÁFICA HISTÓRICA\n\n"
        "• Redução de 75% na fecundidade em 6 décadas\n"
        "• Brasil abaixo do nível de reposição desde 2005\n"
        "• População brasileira começará a encolher antes de 2045", 
        color='#f8fafc', fontsize=26, ha='center', va='center', bbox=highlight_box, linespacing=1.6)

# Fonte
fig.text(0.5, 0.08, "Fonte: IBGE (Censos Demográficos 1960-2022 / Projeções Populacionais)", color='#64748b', fontsize=20, ha='center')

plt.savefig('videos/SHORT-202/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
