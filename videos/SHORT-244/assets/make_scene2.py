import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O BRASIL CALÇA O MUNDO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Principais Destinos dos Calçados Brasileiros (Milhões de Pares)", color='#94a3b8', fontsize=21, ha='center', transform=ax.transAxes)

# Dados Abicalçados / MDIC (Comex Stat) / ApexBrasil
destinos = [
    'Estados Unidos',
    'Argentina',
    'França',
    'Paraguai',
    'Itália',
    'Espanha & Portugal'
]
exportados = [28.4, 15.2, 7.8, 6.9, 4.5, 5.8] # milhões de pares
colors = ['#f59e0b', '#3b82f6', '#06b6d4', '#10b981', '#ec4899', '#64748b']

y_pos = np.arange(len(destinos))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, exportados, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 36)
ax.set_ylim(-0.8, len(destinos) - 0.2)
ax.axis('off')

for bar, dest, val in zip(bars, destinos, exportados):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 20.0
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 27 if is_top else 22
    weight = 'bold' if is_top else 'normal'
    
    ax.text(0.8, y + 0.38, dest.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f} mi pares".replace('.', ',')
    ax.text(val + 1.0, y, val_str, color='#fbbf24' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.20, 
        "O GIGANTE GLOBAL DO CALÇADO\n\n"
        "• Mais de 865 milhões de pares produzidos anualmente no país\n"
        "• 4º maior produtor do mundo e o líder absoluto fora da Ásia\n"
        "• Exportações para mais de 160 países em todos os continentes\n"
        "• Faturamento externo anual superando US$ 1,2 bilhão\n"
        "• Mais de 300 mil trabalhadores diretos na cadeia calçadista", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Abicalçados / MDIC (Comex Stat) / ApexBrasil", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-244/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
