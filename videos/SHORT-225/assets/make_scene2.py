import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "OS ENGENHEIROS NO BRASIL", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Profissionais Registrados por Área (Mil)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Confea / Caged / Ipea
areas = [
    'Engenharia Civil',
    'Agronomia & Agronômica',
    'Mecânica & Metalúrgica',
    'Elétrica & Eletrônica',
    'Computação, Dados & Outras',
    'Química & Ambiental'
]
qtd = [365.0, 125.0, 110.0, 95.0, 65.0, 55.0]
colors = ['#3b82f6', '#10b981', '#f59e0b', '#06b6d4', '#8b5cf6', '#ec4899']

y_pos = np.arange(len(areas))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, qtd, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 450)
ax.set_ylim(-0.8, len(areas) - 0.2)
ax.axis('off')

for bar, area, val in zip(bars, areas, qtd):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 300
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 22
    weight = 'bold' if is_top else 'normal'
    
    ax.text(8, y + 0.38, area.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 10, y, f"{val:.0f} mil", color='#60a5fa' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#3b82f6', linewidth=2)
ax.text(0.5, 0.20, 
        "O MERCADO DA ENGENHARIA NACIONAL\n\n"
        "• Mais de 1,05 milhão de profissionais registrados no Confea/Crea\n"
        "• Civil e Agronomia somam quase metade de toda a categoria\n"
        "• Fuga de cérebros interna: até 40% migram para bancos e tech\n"
        "• Alta demanda por engenharia de software, automação e dados\n"
        "• Concentração geográfica: 55% dos engenheiros atuam no Sudeste", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Confea / Caged (MTE) / Ipea / IBGE", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-225/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
