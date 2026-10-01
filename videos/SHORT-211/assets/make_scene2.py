import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O GIGANTE DA CARNE BOVINA", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Maiores Exportadores Globais de Carne (Milhões t)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados USDA / Abiec / Comex Stat (Exportações de carne bovina em carcaça equivalente)
exportadores = ['Brasil', 'Austrália', 'Índia', 'Estados Unidos', 'Argentina']
volume = [2.95, 1.65, 1.40, 1.25, 0.85] # Milhões de toneladas
colors = ['#f59e0b', '#3b82f6', '#10b981', '#64748b', '#ef4444']

y_pos = np.arange(len(exportadores))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, volume, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 3.8)
ax.set_ylim(-0.8, len(exportadores) - 0.2)
ax.axis('off')

for bar, exp, val in zip(bars, exportadores, volume):
    y = bar.get_y() + bar.get_height() / 2
    is_br = exp == 'Brasil'
    textColor = '#ffffff' if is_br else '#cbd5e1'
    fontSize = 30 if is_br else 24
    weight = 'bold' if is_br else 'normal'
    
    ax.text(0.08, y + 0.38, exp.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 0.10, y, f"{val:.2f} Mt".replace('.', ','), color='#fbbf24' if is_br else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.24, 
        "+230 MILHÕES DE CABEÇAS DE GADO\n\n"
        "• Brasil responde por ~25% do comércio global de carne\n"
        "• Exportações batem recorde superando US$ 10,5 Bilhões\n"
        "• China compra mais de 50% de todos os embarques brasileiros\n"
        "• 95% do rebanho criado a pasto de forma extensiva", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.07, "Fontes: Abiec (Beef Report) / USDA / MDIC / Conab", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-211/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
