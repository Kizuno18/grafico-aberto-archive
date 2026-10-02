import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A SAFRA DO CACAU", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Produção Nacional por Estado (Mil Toneladas)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Aipc / Ceplac / Conab / IBGE
estados = [
    'Pará (Transamazônica)',
    'Bahia (Cabruca / Sul)',
    'Espírito Santo',
    'Rondônia & Outros'
]
safra = [148.0, 132.0, 5.2, 2.1]
colors = ['#10b981', '#f59e0b', '#3b82f6', '#64748b']

y_pos = np.arange(len(estados))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, safra, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 190)
ax.set_ylim(-0.8, len(estados) - 0.2)
ax.axis('off')

for bar, est, val in zip(bars, estados, safra):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 100
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(3, y + 0.38, est.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f} mil t".replace('.', ',')
    ax.text(val + 4, y, val_str, color='#fbbf24' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.22, 
        "O RENASCIMENTO DO CACAU BRASILEIRO\n\n"
        "• Safra nacional de quase 290 mil toneladas de amêndoas\n"
        "• Pará e Bahia concentram 97% de toda a produção do país\n"
        "• Mais de 70% do cacau paraense cresce em agroflorestas (SAFs)\n"
        "• Sul da Bahia lidera revolução do cacau fino bean-to-bar\n"
        "• O Brasil planta, processa e consome seu próprio chocolate", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.05, "Fontes: Aipc / Ceplac (MAPA) / Conab / IBGE", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-226/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
