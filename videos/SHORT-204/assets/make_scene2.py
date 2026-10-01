import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O GIGANTE DA MADEIRA PLANTADA", color='#ffffff', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Produtividade Florestal Média (m³/ha/ano)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Ibá / FAO / Poyry (Produtividade média de madeira industrial)
paises = ['Brasil (Eucalipto)', 'Brasil (Pinus)', 'África do Sul', 'EUA (Sul)', 'Canadá / Nórdicos']
prod = [36.0, 30.0, 18.0, 12.0, 5.0]
colors = ['#10b981', '#059669', '#3b82f6', '#f59e0b', '#64748b']

y_pos = np.arange(len(paises))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, prod, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 46)
ax.set_ylim(-0.8, len(paises) - 0.2)
ax.axis('off')

for bar, pais, val in zip(bars, paises, prod):
    y = bar.get_y() + bar.get_height() / 2
    is_br = 'Brasil' in pais
    textColor = '#ffffff' if is_br else '#cbd5e1'
    fontSize = 28 if is_br else 24
    weight = 'bold' if is_br else 'normal'
    
    ax.text(0.8, y + 0.38, pais.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 1.2, y, f"{val:.0f} m³", color='#10b981' if is_br else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.26, 
        "10 MILHÕES DE HECTARES CULTIVADOS\n\n"
        "• 100% da celulose e papel vem de florestas plantadas\n"
        "• O eucalipto cresce no Brasil em 7 anos (vs 30 anos no exterior)\n"
        "• Para cada hectare plantado, 1 ha nativo é conservado", 
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.08, "Fontes: Ibá (Relatório Anual) / MDIC / Embrapa Florestas", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-204/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
