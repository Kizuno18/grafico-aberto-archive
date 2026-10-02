import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O BOOM DOS BLINDADOS", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Veículos Blindados por Ano no Brasil (Mil Unidades)", color='#94a3b8', fontsize=23, ha='center', transform=ax.transAxes)

# Dados Abrablin / Exército Brasileiro (DFPC)
anos = ['2015', '2018', '2021', '2023', 'Hoje (2024)']
blindagens = [18.2, 20.0, 20.1, 29.3, 30.5] # mil veículos
colors = ['#475569', '#64748b', '#0284c7', '#38bdf8', '#0ea5e9']

y_pos = np.arange(len(anos))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, blindagens, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 38)
ax.set_ylim(-0.8, len(anos) - 0.2)
ax.axis('off')

for bar, ano, val in zip(bars, anos, blindagens):
    y = bar.get_y() + bar.get_height() / 2
    is_top = 'Hoje' in ano or '2023' in ano
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(1.0, y + 0.38, ano.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f} mil".replace('.', ',')
    ax.text(val + 1.2, y, val_str, color='#38bdf8' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
ax.text(0.5, 0.20, 
        "O MAIOR MERCADO DO PLANETA\n\n"
        "• Mais de 320 mil veículos blindados em circulação no país\n"
        "• O Brasil blinda mais carros que qualquer outra nação do mundo\n"
        "• São Paulo concentra 73% de todas as blindagens realizadas\n"
        "• 85% dos modelos modificados são SUVs para uso familiar\n"
        "• Nível III-A: proteção contra pistolas e armas curtas até .44 Magnum", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Abrablin (Associação Brasileira de Blindagem) / Exército Brasileiro", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-237/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
