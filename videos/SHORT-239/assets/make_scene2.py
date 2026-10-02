import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "ARÁBICA VS CONILON", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "A Safra de Café por Espécie (Milhões de Sacas)", color='#94a3b8', fontsize=23, ha='center', transform=ax.transAxes)

# Dados Conab / Cecafé / Embrapa Café
categorias = [
    'Arábica (Total Nacional)',
    '  ↳ Minas Gerais (Líder Arábica)',
    'Conilon / Robusta (Total)',
    '  ↳ Espírito Santo (Líder Conilon)',
    '  ↳ Rondônia (Amazônia / Clima Tropical)'
]
producao = [40.2, 29.0, 17.8, 12.5, 3.2] # milhões de sacas
colors = ['#f59e0b', '#d97706', '#10b981', '#059669', '#047857']

y_pos = np.arange(len(categorias))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, producao, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 50)
ax.set_ylim(-0.8, len(categorias) - 0.2)
ax.axis('off')

for bar, cat, val in zip(bars, categorias, producao):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 35
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 23
    weight = 'bold' if is_top else 'normal'
    
    ax.text(1.0, y + 0.38, cat.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f} mi sacas".replace('.', ',')
    ax.text(val + 1.2, y, val_str, color='#fbbf24' if 'Arábica' in cat else '#34d399', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.20, 
        "O GIGANTE GLOBAL DO CAFÉ\n\n"
        "• Safra nacional de 58 milhões de sacas de 60 kg\n"
        "• Brasil responde por 1 em cada 3 xícaras bebidas no planeta\n"
        "• Arábica (70%): aromas suaves, cafés especiais e altitude\n"
        "• Conilon (30%): mais cafeína, encorpado e base de solúveis\n"
        "• Espírito Santo e Rondônia: alta produtividade e tolerância térmica", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Conab (Acompanhamento Safra Café) / Cecafé / Embrapa Café", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-239/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
