import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A EÓLICA NO MAR", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Projetos em Licenciamento no Ibama por Estado (GW)", color='#94a3b8', fontsize=23, ha='center', transform=ax.transAxes)

# Dados Ibama / EPE / Abeeólica
estados = [
    'Rio Grande do Sul (Litoral Sul)',
    'Ceará (Ventos Alísios)',
    'Rio de Janeiro (Sudeste)',
    'Rio Grande do Norte',
    'Piauí & Maranhão',
    'Espírito Santo & Bahia'
]
potencia = [65.4, 64.8, 37.2, 25.6, 22.1, 19.5] # Gigawatts (GW)
colors = ['#0284c7', '#06b6d4', '#38bdf8', '#10b981', '#f59e0b', '#64748b']

y_pos = np.arange(len(estados))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, potencia, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 85)
ax.set_ylim(-0.8, len(estados) - 0.2)
ax.axis('off')

for bar, est, val in zip(bars, estados, potencia):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 60.0
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 26 if is_top else 22
    weight = 'bold' if is_top else 'normal'
    
    ax.text(1.2, y + 0.38, est.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f} GW".replace('.', ',')
    ax.text(val + 1.5, y, val_str, color='#38bdf8' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#0284c7', linewidth=2)
ax.text(0.5, 0.20, 
        "O GIGANTE DOS VENTOS MARÍTIMOS\n\n"
        "• Mais de 230 GW em mais de 90 projetos em análise no Ibama\n"
        "• Esse potencial supera toda a capacidade elétrica atual do Brasil\n"
        "• Aerogeradores marítimos gigantes com até 250 metros de altura\n"
        "• Ventos no oceano são mais fortes, estáveis e sem barreiras físicas\n"
        "• Sinergia direta para produzir Hidrogênio Verde (H2V) em portos", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Ibama (Complexos em Licenciamento) / EPE / Abeeólica", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-243/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
