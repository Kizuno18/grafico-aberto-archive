import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O MAPA DAS PCHs NO BRASIL", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Capacidade Instalada por Estado (Megawatts)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Aneel (SIGEL) / Abrapch
estados = [
    'Minas Gerais',
    'Mato Grosso',
    'Paraná',
    'Santa Catarina',
    'Goiás',
    'São Paulo & Outros'
]
potencia = [1520.0, 1180.0, 890.0, 780.0, 710.0, 680.0]
colors = ['#0284c7', '#06b6d4', '#10b981', '#3b82f6', '#f59e0b', '#64748b']

y_pos = np.arange(len(estados))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, potencia, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 1900)
ax.set_ylim(-0.8, len(estados) - 0.2)
ax.axis('off')

for bar, est, val in zip(bars, estados, potencia):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 1000
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(30, y + 0.38, est.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:,.0f} MW".replace(',', '.')
    ax.text(val + 35, y, val_str, color='#38bdf8' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#0284c7', linewidth=2)
ax.text(0.5, 0.20, 
        "A ENERGIA DESCENTRALIZADA DOS RIOS\n\n"
        "• Quase 6.000 MW de potência instalada em PCHs e CGHs\n"
        "• Mais de 580 usinas compactas em operação pelo Brasil\n"
        "• Geração a fio d’água: reservatórios pequenos ou inexistentes\n"
        "• Energia gerada perto do consumo, aliviando o linhão nacional\n"
        "• Minas Gerais e Centro-Oeste somam quase 60% da potência", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Aneel (SIGEL) / Abrapch / ONS / EPE", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-227/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
