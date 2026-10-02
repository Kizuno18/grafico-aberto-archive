import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A POPULAÇÃO QUILOMBOLA", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Habitantes Quilombolas por Estado (Mil Pessoas)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Censo Demográfico 2022 (IBGE) - Maiores Estados Quilombolas
estados = ['Bahia', 'Maranhão', 'Minas Gerais', 'Pará', 'Pernambuco', 'Alagoas', 'Sergipe', 'Goiás']
pop = [397.5, 269.1, 135.3, 135.0, 78.8, 37.7, 36.1, 30.4] # mil pessoas
colors = ['#f59e0b', '#f97316', '#3b82f6', '#10b981', '#06b6d4', '#ec4899', '#8b5cf6', '#64748b']

y_pos = np.arange(len(estados))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, pop, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 480)
ax.set_ylim(-0.8, len(estados) - 0.2)
ax.axis('off')

for bar, est, val in zip(bars, estados, pop):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 200
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 22
    weight = 'bold' if is_top else 'normal'
    
    ax.text(8, y + 0.38, est.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 10, y, f"{val:.1f} mil".replace('.', ','), color='#fbbf24' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.17, 
        "1.327.802 QUILOMBOLAS NO CENSO 2022\n\n"
        "• Primeiro levantamento censitário oficial da história do Brasil\n"
        "• Bahia e Maranhão concentram metade (50,2%) de toda a população\n"
        "• Presentes em 1.696 municípios brasileiros (quase 1 em cada 3)\n"
        "• Apenas 4,3% residem em territórios já formalmente titulados", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fonte: IBGE (Censo Demográfico 2022: Quilombolas) / Conaq / Incra", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-222/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
