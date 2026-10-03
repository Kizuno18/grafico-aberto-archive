import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O BOOM DO ETANOL DE MILHO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Produção Nacional por Safra (Bilhões de Litros)", color='#94a3b8', fontsize=23, ha='center', transform=ax.transAxes)

# Dados Unem / Conab / NovaCana
safras = ['2017/18', '2019/20', '2021/22', '2023/24', 'Hoje (2024/25)']
producao = [0.52, 1.62, 3.47, 6.27, 7.50] # bilhões de litros
colors = ['#854d0e', '#a16207', '#ca8a04', '#eab308', '#facc15']

y_pos = np.arange(len(safras))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, producao, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 9.5)
ax.set_ylim(-0.8, len(safras) - 0.2)
ax.axis('off')

for bar, saf, val in zip(bars, safras, producao):
    y = bar.get_y() + bar.get_height() / 2
    is_top = 'Hoje' in saf or '2023' in saf
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(0.2, y + 0.38, saf.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.2f} bi L".replace('.', ',')
    ax.text(val + 0.25, y, val_str, color='#fde047' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#ca8a04', linewidth=2)
ax.text(0.5, 0.20, 
        "A REVOLUÇÃO VERDE DO CENTRO-OESTE\n\n"
        "• Crescimento de 14 vezes na produção em menos de 8 anos\n"
        "• Já responde por mais de 20% de todo o etanol do Brasil\n"
        "• Mato Grosso lidera isolado com mais de 70% da fabricação\n"
        "• Usa o milho da 2ª safra (safrinha), sem competir com terras de soja\n"
        "• Gera milhões de toneladas de DDG: ração nobre para a pecuária", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Unem (União Nacional do Etanol de Milho) / Conab / NovaCana", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-246/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
