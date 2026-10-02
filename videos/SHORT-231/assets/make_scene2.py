import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O SALTO DOS DRONES NO AGRO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Frota Agrícola Registrada no Brasil (Unidades)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Sindag / Anac / MAPA / Embrapa
anos = ['2020', '2021', '2022', '2023', '2024 (Hoje)']
frota = [1250, 2400, 4800, 7200, 10800]
colors = ['#1e3a8a', '#2563eb', '#3b82f6', '#10b981', '#059669']

y_pos = np.arange(len(anos))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, frota, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 13500)
ax.set_ylim(-0.8, len(anos) - 0.2)
ax.axis('off')

for bar, ano, val in zip(bars, anos, frota):
    y = bar.get_y() + bar.get_height() / 2
    is_top = 'Hoje' in ano
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(300, y + 0.38, ano.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:,} drones".replace(',', '.')
    ax.text(val + 350, y, val_str, color='#34d399' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.20, 
        "A REVOLUÇÃO DA PULVERIZAÇÃO AÉREA\n\n"
        "• Crescimento vertiginoso de quase 900% em 4 anos\n"
        "• Economia de até 90% de água na calda de pulverização\n"
        "• Zero amassamento de lavoura (tratores perdem até 4% da safra)\n"
        "• Operações noturnas autônomas com menor deriva de vento\n"
        "• Acesso a terrenos inclinados de café, frutas e cana", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Sindag / Anac / MAPA / Embrapa Instrumentação", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-231/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
