import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A QUEDA DA MORTALIDADE INFANTIL", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Óbitos por 1.000 Nascidos Vivos no Brasil", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados DataSUS / SIM / IBGE Censos / Unicef
anos = ['1990', '2000', '2010', '2020', 'Hoje (2024)']
taxas = [47.1, 29.7, 17.2, 12.4, 11.9]
colors = ['#ef4444', '#f97316', '#f59e0b', '#10b981', '#059669']

y_pos = np.arange(len(anos))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, taxas, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 58)
ax.set_ylim(-0.8, len(anos) - 0.2)
ax.axis('off')

for bar, ano, val in zip(bars, anos, taxas):
    y = bar.get_y() + bar.get_height() / 2
    is_top = 'Hoje' in ano
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(1.5, y + 0.38, ano.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f} por mil".replace('.', ',')
    ax.text(val + 1.5, y, val_str, color='#34d399' if is_top else '#f87171' if val > 40 else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.20, 
        "A MAIOR VITÓRIA DA SAÚDE PÚBLICA\n\n"
        "• Queda histórica de quase 75% na mortalidade infantil\n"
        "• Em 1990, quase 50 crianças morriam antes de completar 1 ano\n"
        "• Hoje a taxa está em 11,9 por mil, padrão próximo a países ricos\n"
        "• Fatores determinantes: vacinação em massa (PNI),\n"
        "  expansão do saneamento básico e Estratégia Saúde da Família\n"
        "• Centenas de milhares de vidas salvas a cada década", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Ministério da Saúde (DataSUS / SIM) / IBGE / Unicef", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-228/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
