import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "ONDE AS MOTOS DOMINAM AS RUAS", color='#ffffff', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Participação de Motos na Frota Total de Veículos (%)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Senatran (Ministério dos Transportes) - Proporção de Motocicletas/Motonetas
regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sul', 'Sudeste']
shares = [56.2, 53.8, 34.5, 27.2, 23.4] # % da frota
colors = ['#f59e0b', '#f97316', '#3b82f6', '#10b981', '#64748b']

y_pos = np.arange(len(regioes))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, shares, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 68)
ax.set_ylim(-0.8, len(regioes) - 0.2)
ax.axis('off')

for bar, reg, val in zip(bars, regioes, shares):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 50.0
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(1.0, y + 0.38, reg.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 1.2, y, f"{val:.1f}%".replace('.', ','), color='#fbbf24' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.25, 
        "MAIS DE 33 MILHÕES DE MOTOS NO PAÍS\n\n"
        "• Em mais de 2.400 municípios há mais motos do que carros\n"
        "• No Maranhão e Piauí, motos chegam a quase 60% da frota\n"
        "• Custo por km rodado até 4 vezes menor que automóvel\n"
        "• Motor do delivery, mototáxi e locomoção rural", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.08, "Fontes: Senatran (Frota de Veículos) / IBGE / Abraciclo", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-213/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
