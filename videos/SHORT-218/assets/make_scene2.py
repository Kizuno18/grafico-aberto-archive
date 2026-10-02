import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A EXPLOSÃO DOS PSICÓLOGOS", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Densidade de Psicólogos por 100 Mil Habitantes", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados CFP (Conselho Federal de Psicologia) - Densidade por região
regioes = ['Distrito Federal', 'Sudeste', 'Sul', 'Centro-Oeste', 'Nordeste', 'Norte']
densidade = [385, 265, 240, 185, 125, 85] # por 100k hab
colors = ['#ec4899', '#38bdf8', '#0ea5e9', '#10b981', '#f59e0b', '#64748b']

y_pos = np.arange(len(regioes))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, densidade, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 480)
ax.set_ylim(-0.8, len(regioes) - 0.2)
ax.axis('off')

for bar, reg, val in zip(bars, regioes, densidade):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 250
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(8, y + 0.38, reg.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 10, y, f"{val}", color='#fbbf24' if is_top else '#94a3b8', fontsize=26, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#ec4899', linewidth=2)
ax.text(0.5, 0.24, 
        "+460 MIL PSICÓLOGOS ATIVOS NO BRASIL\n\n"
        "• Brasil é um dos países com mais psicólogos per capita no mundo\n"
        "• DF tem quase 5x mais terapeutas por habitante que a região Norte\n"
        "• Mais de 85% dos profissionais atuantes são mulheres\n"
        "• Teleatendimento / terapia online democratizou o acesso", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.07, "Fontes: CFP (Cadastro Nacional de Psicólogos) / IBGE / DataSUS", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-218/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
