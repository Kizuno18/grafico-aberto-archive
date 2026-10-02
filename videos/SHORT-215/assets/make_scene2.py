import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O MAPA DO TRABALHO REMOTO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Trabalhadores em Teletrabalho / Home Office (%)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Ipea / PNAD Contínua (IBGE) - Taxa de teletrabalho efetivo por unidade da federação
estados = ['Distrito Federal', 'São Paulo', 'Rio de Janeiro', 'Santa Catarina', 'Paraná', 'Minas Gerais']
shares = [18.4, 13.2, 11.5, 9.8, 8.9, 7.6] # %
colors = ['#38bdf8', '#0284c7', '#0ea5e9', '#10b981', '#f59e0b', '#64748b']

y_pos = np.arange(len(estados))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, shares, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 24)
ax.set_ylim(-0.8, len(estados) - 0.2)
ax.axis('off')

for bar, est, val in zip(bars, estados, shares):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 12.0
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(0.5, y + 0.38, est.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 0.5, y, f"{val:.1f}%".replace('.', ','), color='#fbbf24' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
ax.text(0.5, 0.25, 
        "+7,4 MILHÕES DE BRASILEIROS EM HOME OFFICE\n\n"
        "• DF lidera puxado pelo funcionalismo e consultorias\n"
        "• SP e RJ concentram tecnologia, bancos e multinacionais\n"
        "• 70% dos trabalhadores remotos têm ensino superior completo\n"
        "• Consolidação definitiva do modelo híbrido (2 a 3 dias em casa)", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.08, "Fontes: Ipea (Carta de Conjuntura) / IBGE (PNAD Contínua) / FGV", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-215/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
