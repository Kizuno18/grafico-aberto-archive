import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "LOGÍSTICA PLANETÁRIA", color='#ffffff', fontsize=42, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "Do Porto de Santos aos Mercados Globais", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: Infraestrutura Naval
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#3b82f6', linewidth=2)
ax.text(0.5, 0.64,
        "[ LOGÍSTICA NAVAL REFRIGERADA ]\n\n"
        "O suco brasileiro viaja a -10°C em navios\n"
        "especialmente construídos para a rota Santos-Roterdã,\n"
        "preservando aroma, sabor e vitamina C.",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Destinos Principais
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.44,
        "[ MERCADOS COMPRADORES ]\n\n"
        "• União Europeia: ~65% das exportações\n"
        "• Estados Unidos: ~20% das exportações\n"
        "• Japão & China: consumo crescente",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f97316', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#ffffff', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: CitrusBR / Fundecitrus / Comex Stat", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-201/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada sem avisos de glifo!")
