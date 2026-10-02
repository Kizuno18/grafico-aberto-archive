import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A SOLAR FLUTUANTE", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "As Vantagens dos Painéis nos Lagos das Represas", color='#94a3b8', fontsize=23, ha='center', transform=ax.transAxes)

# Dados Aneel / Chesf / Absolar / Emae
metricas = [
    'Ganho de Eficiência (Resfriamento)',
    'Redução da Evaporação do Lago',
    'Uso de Linhas de Transmissão Existentes',
    'Economia de Área Terrestre Rural'
]
valores = [15.0, 30.0, 100.0, 100.0] # percentuais
labels = ['+15% mais geração', '-30% de perda de água', '100% aproveitada', 'Zero desapropriação']
colors = ['#38bdf8', '#0284c7', '#10b981', '#f59e0b']

y_pos = np.arange(len(metricas))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, valores, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 135)
ax.set_ylim(-0.8, len(metricas) - 0.2)
ax.axis('off')

for bar, met, val, lab in zip(bars, metricas, valores, labels):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 90
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 26 if is_top else 22
    weight = 'bold' if is_top else 'normal'
    
    ax.text(2.0, y + 0.38, met.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 3.0, y, lab, color='#38bdf8' if 'água' in lab or 'geração' in lab else '#34d399', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
ax.text(0.5, 0.20, 
        "A SINERGIA PERFEITA ENTRE SOL E ÁGUA\n\n"
        "• A água fria reduz a temperatura dos módulos e eleva a potência\n"
        "• A sombra dos flutuadores reduz a proliferação de algas tóxicas\n"
        "• Aproveita subestações e linhas já construídas das hidrelétricas\n"
        "• Projetos pioneiros em Sobradinho (BA) e Represa Billings (SP)\n"
        "• Se cobrisse 5% dos lagos, geraria mais energia que Itaipu", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Aneel / Chesf / Absolar / Emae / EPE", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-236/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
