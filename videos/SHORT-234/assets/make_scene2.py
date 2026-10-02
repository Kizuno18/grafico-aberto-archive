import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O CAMPEÃO DA RECICLAGEM", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Taxa de Reciclagem de Latas de Alumínio (%)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Abal / Abralatas / Cempre
paises = [
    'Brasil',
    'Japão',
    'União Europeia',
    'Reino Unido',
    'Estados Unidos'
]
taxas = [98.7, 94.0, 76.0, 74.0, 49.0]
colors = ['#10b981', '#3b82f6', '#06b6d4', '#f59e0b', '#ef4444']

y_pos = np.arange(len(paises))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, taxas, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 120)
ax.set_ylim(-0.8, len(paises) - 0.2)
ax.axis('off')

for bar, pais, val in zip(bars, paises, taxas):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 95.0
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(2.0, y + 0.38, pais.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f}%".replace('.', ',')
    ax.text(val + 2.5, y, val_str, color='#34d399' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.20, 
        "O CICLO PERFEITO DA ECONOMIA CIRCULAR\n\n"
        "• O Brasil recicla mais de 31 bilhões de latinhas por ano\n"
        "• Ciclo fechado: em 60 dias a lata volta nova para o supermercado\n"
        "• Economia de 95% de energia elétrica vs extração de bauxita virgem\n"
        "• Mais de 800 mil catadores e cooperativas sustentados pela cadeia\n"
        "• Liderança global ininterrupta há mais de 15 anos consecutivos", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Abal (Associação do Alumínio) / Abralatas / Cempre", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-234/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
