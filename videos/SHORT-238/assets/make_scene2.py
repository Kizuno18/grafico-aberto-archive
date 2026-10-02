import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O SALTO DA LONGEVIDADE", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Esperança de Vida ao Nascer no Nordeste (Anos)", color='#94a3b8', fontsize=23, ha='center', transform=ax.transAxes)

# Dados IBGE (Tábuas de Mortalidade e Censos)
decadas = ['1960', '1980', '2000', '2010', 'Hoje (2024)']
expectativa = [48.2, 58.3, 65.5, 71.2, 74.6]
colors = ['#dc2626', '#f97316', '#f59e0b', '#10b981', '#059669']

y_pos = np.arange(len(decadas))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, expectativa, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 90)
ax.set_ylim(-0.8, len(decadas) - 0.2)
ax.axis('off')

for bar, dec, val in zip(bars, decadas, expectativa):
    y = bar.get_y() + bar.get_height() / 2
    is_top = 'Hoje' in dec
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(2.0, y + 0.38, dec.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f} anos".replace('.', ',')
    ax.text(val + 2.5, y, val_str, color='#34d399' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.20, 
        "A MAIOR CONVERGÊNCIA DEMOGRÁFICA DO PAÍS\n\n"
        "• Ganho de mais de 26 anos de esperança média de vida\n"
        "• A distância para o Sul/Sudeste encolheu de 12 para menos de 3 anos\n"
        "• Despencamento da mortalidade infantil e materna\n"
        "• Cobertura do programa Saúde da Família acima de 85% nos municípios\n"
        "• Universalização da água tratada, energia elétrica e assistência social", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: IBGE (Tábua Completa de Mortalidade) / DataSUS / Ipea", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-238/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
