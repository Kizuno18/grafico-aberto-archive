import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "TÁXI VS CARRO DE APP", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Divisão das Viagens Individuais por Aplicativo (%)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Gráfico de Donut da divisão das corridas individuais urbanas nas metrópoles
categorias = ['Carros de Aplicativo (Uber / 99)', 'Táxis Tradicionais']
shares = [86.5, 13.5]
colors = ['#38bdf8', '#fbbf24']

ax_pie = fig.add_axes([0.18, 0.50, 0.64, 0.32])
wedges, texts, autotexts = ax_pie.pie(shares, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.75,
                                      wedgeprops=dict(width=0.45, edgecolor='#0d1117', linewidth=4),
                                      textprops=dict(color='#ffffff', fontsize=24, fontweight='bold'))

for at in autotexts:
    at.set_fontsize(26)
    at.set_color('#ffffff')

ax_pie.legend(wedges, [c.upper() for c in categorias], loc='lower center', bbox_to_anchor=(0.5, -0.20),
              frameon=False, fontsize=20, labelcolor='#cbd5e1')

ax.axis('off')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
fig.text(0.5, 0.22, 
        "+1,5 MILHÃO DE MOTORISTAS DE APP NO BRASIL\n\n"
        "• Frota de app é quase 10x maior que a frota de táxis com alvará\n"
        "• São Paulo concentra mais de 120 mil condutores cadastrados\n"
        "• R$ 45 Bilhões movimentados por ano na economia urbana\n"
        "• Fonte primária ou complementar de renda para milhões de famílias", 
        color='#f8fafc', fontsize=24, ha='center', va='center', bbox=highlight_box, linespacing=1.6)

# Fonte
fig.text(0.5, 0.06, "Fontes: Amobitec / Prefeituras SP e RJ / IBGE / Denatran", color='#64748b', fontsize=20, ha='center')

plt.savefig('videos/SHORT-220/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
