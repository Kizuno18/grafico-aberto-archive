import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A EXPLOSÃO SOLAR NO BRASIL", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Capacidade Instalada por Estado (GW)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados da Absolar / Aneel (Top Estados em Potência Solar Centralizada + Distribuída)
estados = ['Minas Gerais', 'São Paulo', 'Bahia', 'Rio Grande do Sul', 'Paraná', 'Piauí']
potencia = [8.4, 7.9, 6.2, 5.1, 4.3, 3.8] # GW
colors = ['#f59e0b', '#fbbf24', '#38bdf8', '#10b981', '#6366f1', '#ec4899']

y_pos = np.arange(len(estados))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, potencia, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 11)
ax.set_ylim(-0.8, len(estados) - 0.2)
ax.axis('off')

for bar, est, val in zip(bars, estados, potencia):
    y = bar.get_y() + bar.get_height() / 2
    textColor = '#ffffff' if val >= 7.0 else '#cbd5e1'
    fontSize = 30 if val >= 7.0 else 26
    weight = 'bold' if val >= 7.0 else 'normal'
    
    ax.text(0.2, y + 0.38, est.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 0.3, y, f"{val:.1f} GW".replace('.', ','), color='#fbbf24', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.26, 
        "+45 GIGAWATTS DE POTÊNCIA\n\n"
        "• 2ª maior fonte da matriz elétrica nacional\n"
        "• 80% da energia vem de telhados (geração distribuída)\n"
        "• +R$ 200 Bilhões em investimentos acumulados", 
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.08, "Fontes: Absolar / Aneel (SIGEL) / ONS", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-203/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
