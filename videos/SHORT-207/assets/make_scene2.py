import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A FROTA DE ÔNIBUS NO BRASIL", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Divisão do Transporte Público Coletivo Urbano", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Gráfico de Divisão Modal do Transporte Coletivo Urbano (NTU / ANTP)
modais = ['Ônibus Urbano / BRT', 'Metrô / Trem Urbano', 'VLT / Barca / Outros']
shares = [84.5, 14.2, 1.3]
colors = ['#f59e0b', '#3b82f6', '#10b981']

# Gráfico de pizza / donut
ax_pie = fig.add_axes([0.18, 0.50, 0.64, 0.32])
wedges, texts, autotexts = ax_pie.pie(shares, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.75,
                                      wedgeprops=dict(width=0.45, edgecolor='#0d1117', linewidth=4),
                                      textprops=dict(color='#ffffff', fontsize=22, fontweight='bold'))

for at in autotexts:
    at.set_fontsize(24)
    at.set_color('#ffffff')

# Legenda do Donut
ax_pie.legend(wedges, [m.upper() for m in modais], loc='lower center', bbox_to_anchor=(0.5, -0.22),
              frameon=False, fontsize=20, labelcolor='#cbd5e1')

ax.axis('off')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
fig.text(0.5, 0.22, 
        "+30 MILHÕES DE PASSAGEIROS POR DIA\n\n"
        "• +107 mil ônibus em operação nas linhas municipais\n"
        "• 85% das cidades dependem exclusivamente de ônibus\n"
        "• Avanço da eletrificação: +4.000 ônibus elétricos previstos", 
        color='#f8fafc', fontsize=24, ha='center', va='center', bbox=highlight_box, linespacing=1.6)

# Fonte
fig.text(0.5, 0.06, "Fontes: NTU (Anuário do Transporte Urbano) / ANTP / Senatran", color='#64748b', fontsize=20, ha='center')

plt.savefig('videos/SHORT-207/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
