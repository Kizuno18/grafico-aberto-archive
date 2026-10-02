import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O GASTO DE LUZ NAS CAPITAIS", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Consumo Residencial por Habitante (kWh/ano)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados EPE (Anuário Estatístico de Energia Elétrica) / Aneel / IBGE
capitais = [
    'Cuiabá (MT)',
    'Boa Vista (RR)',
    'Palmas (TO)',
    'Rio de Janeiro (RJ)',
    'Florianópolis (SC)',
    'Média do Brasil',
    'Curitiba (PR)'
]
consumo = [985, 915, 870, 810, 795, 580, 515]
colors = ['#ef4444', '#f97316', '#f59e0b', '#06b6d4', '#3b82f6', '#64748b', '#10b981']

y_pos = np.arange(len(capitais))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, consumo, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 1200)
ax.set_ylim(-0.8, len(capitais) - 0.2)
ax.axis('off')

for bar, cap, val in zip(bars, capitais, consumo):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 900
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(25, y + 0.38, cap.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val} kWh"
    ax.text(val + 30, y, val_str, color='#fbbf24' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.20, 
        "O PESO DO CALOR NA FATURA DE ENERGIA\n\n"
        "• Cuiabá consome quase o dobro da média nacional per capita\n"
        "• Uso contínuo de ar-condicionado responde por até 45% da conta\n"
        "• Boa Vista e Palmas: calor equatorial e expansão urbana rápida\n"
        "• Curitiba e capitais de clima ameno têm menor gasto per capita\n"
        "• Renda média e climatização explicam a disparidade entre regiões", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: EPE (Anuário de Energia Elétrica) / Aneel / IBGE", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-233/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
