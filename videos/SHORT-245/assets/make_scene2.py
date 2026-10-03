import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "OS JOVENS NO BRASIL", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Condição de Ocupação da Faixa de 15 a 29 Anos (%)", color='#94a3b8', fontsize=22, ha='center', transform=ax.transAxes)

# Dados IBGE (PNAD Contínua - Educação) / Ipea
categorias = [
    'Apenas Trabalham',
    'Apenas Estudam',
    'Nem Estudam Nem Trabalham (Nem-Nem)',
    'Trabalham e Estudam Simultaneamente'
]
proporcao = [40.2, 25.4, 19.8, 14.6] # % dos 48,5 milhões de jovens
colors = ['#3b82f6', '#10b981', '#ef4444', '#f59e0b']

y_pos = np.arange(len(categorias))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, proporcao, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 52)
ax.set_ylim(-0.8, len(categorias) - 0.2)
ax.axis('off')

for bar, cat, val in zip(bars, categorias, proporcao):
    y = bar.get_y() + bar.get_height() / 2
    is_work = 'Apenas Trabalham' in cat
    is_nem = 'Nem' in cat
    textColor = '#ffffff' if is_work else '#cbd5e1'
    fontSize = 26 if is_work else 22
    weight = 'bold' if is_work else 'normal'
    
    ax.text(1.0, y + 0.38, cat.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f}%".replace('.', ',')
    cor_val = '#60a5fa' if is_work else '#f87171' if is_nem else '#94a3b8'
    ax.text(val + 1.2, y, val_str, color=cor_val, fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#3b82f6', linewidth=2)
ax.text(0.5, 0.20, 
        "O RAIO-X DA JUVENTUDE BRASILEIRA\n\n"
        "• População de 48,5 milhões de pessoas entre 15 e 29 anos\n"
        "• 80,2% dos jovens estão integrados ao trabalho, estudo ou ambos\n"
        "• A taxa de 'nem-nem' caiu abaixo de 20%, o menor índice em anos\n"
        "• Perfil nem-nem: 66% são mulheres (maioria com filhos e afazeres)\n"
        "• Mais de 7 milhões de jovens equilibram dupla jornada de estudo e emprego", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: IBGE (PNAD Contínua - Educação) / Ipea", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-245/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
