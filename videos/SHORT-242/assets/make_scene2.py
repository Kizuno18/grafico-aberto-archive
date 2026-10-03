import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "MAIS PETS QUE CRIANÇAS", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "População Comparada no Brasil (Milhões)", color='#94a3b8', fontsize=23, ha='center', transform=ax.transAxes)

# Dados IBGE (PNS / Censo) / Abinpet / Instituto Pet Brasil
categorias = [
    'Cães de Estimação',
    'Crianças e Jovens (0 a 14 Anos)',
    'Gatos de Estimação',
    'Total de Cães + Gatos'
]
populacao = [68.0, 40.1, 34.0, 102.0]
colors = ['#f59e0b', '#3b82f6', '#10b981', '#ef4444']

y_pos = np.arange(len(categorias))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, populacao, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 130)
ax.set_ylim(-0.8, len(categorias) - 0.2)
ax.axis('off')

for bar, cat, val in zip(bars, categorias, populacao):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 100.0
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 23
    weight = 'bold' if is_top else 'normal'
    
    ax.text(1.5, y + 0.38, cat.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f} milhões".replace('.', ',')
    ax.text(val + 2.0, y, val_str, color='#f87171' if is_top else '#fbbf24' if 'Cães' in cat else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.20, 
        "A VIRADA DOS LARES BRASILEIROS\n\n"
        "• Já existem 2,5 vezes mais cães e gatos que crianças até 14 anos\n"
        "• Quase 50% dos domicílios do país possuem ao menos um cão\n"
        "• Região Sul lidera: 58% dos lares têm cachorro de estimação\n"
        "• 3ª maior população de pets do planeta (mais de 160 mi de animais)\n"
        "• Mercado pet nacional movimenta mais de R$ 68 bilhões por ano", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: IBGE (Pesquisa Nacional de Saúde) / Abinpet / Instituto Pet Brasil", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-242/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
