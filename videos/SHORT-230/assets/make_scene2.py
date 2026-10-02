import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O MAPA DA CACHAÇA", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Produtores Registrados no MAPA por Estado", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados MAPA (Anuário da Cachaça) / Ibrac
estados = [
    'Minas Gerais',
    'São Paulo',
    'Espírito Santo',
    'Rio de Janeiro',
    'Rio Grande do Sul',
    'Paraná & Nordeste'
]
produtores = [504, 165, 78, 68, 59, 145]
colors = ['#f59e0b', '#d97706', '#b45309', '#78350f', '#3b82f6', '#64748b']

y_pos = np.arange(len(estados))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, produtores, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 620)
ax.set_ylim(-0.8, len(estados) - 0.2)
ax.axis('off')

for bar, est, val in zip(bars, estados, produtores):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 500
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(10, y + 0.38, est.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 12, y, f"{val} alambiques", color='#fbbf24' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.20, 
        "O PATRIMÔNIO LÍQUIDO BRASILEIRO\n\n"
        "• 1.150 produtores registrados oficialmente no Ministério\n"
        "• Minas Gerais abriga quase 45% de todos os alambiques do país\n"
        "• São Paulo lidera as exportações industriais em volume\n"
        "• Exportada para mais de 75 países (EUA, Alemanha e França)\n"
        "• Mais de 5.000 marcas ativas com proteção de denominação", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: MAPA (Anuário da Cachaça) / Ibrac / MDIC", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-230/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
