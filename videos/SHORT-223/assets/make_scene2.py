import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A FROTA DE CAMINHÕES", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Composição da Frota de Transporte (Mil Veículos)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados CNT / ANTT / Senatran - Categorias de Caminhões
categorias = [
    'Pesados e Carretas',
    'Semipesados (Trucks)',
    'Médios (Intermunicipal)',
    'Leves e VUCs (Urbanos)'
]
frota = [1250.0, 1080.0, 780.0, 710.0]  # mil unidades
colors = ['#f59e0b', '#3b82f6', '#10b981', '#64748b']

y_pos = np.arange(len(categorias))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, frota, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 1600)
ax.set_ylim(-0.8, len(categorias) - 0.2)
ax.axis('off')

for bar, cat, val in zip(bars, categorias, frota):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 1200
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(25, y + 0.38, cat.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:,.0f} mil".replace(',', '.')
    ax.text(val + 30, y, val_str, color='#fbbf24' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.22, 
        "O GIGANTE LOGÍSTICO DAS RODOVIAS\n\n"
        "• 3,82 milhões de caminhões registrados no Brasil (Renavam/CNT)\n"
        "• 65% de toda a carga do país viaja sobre a malha rodoviária\n"
        "• Mais de 1,2 milhão de carretas pesadas, bitrens e rodotrens\n"
        "• Escoamento de mais de 300 milhões de toneladas de grãos\n"
        "• BR-163 e BR-364: fluxos intensos de dezenas de milhares/dia", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.05, "Fontes: CNT (Pesquisa Rodovias) / ANTT (RNTRC) / Fenabrave", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-223/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
