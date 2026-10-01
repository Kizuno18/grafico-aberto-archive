import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A FORÇA DA INDÚSTRIA TÊXTIL", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Raio-X da Cadeia Têxtil e de Confecção no Brasil", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Indicadores Principais
cards = [
    ("FATURAMENTO ANUAL", "R$ 190 BILHÕES", "#38bdf8", "5ª maior indústria têxtil do mundo"),
    ("EMPREGOS GERADOS", "1,34 MILHÃO", "#10b981", "2ª maior empregadora da indústria"),
    ("PRODUÇÃO DE VESTUÁRIO", "8,9 BILHÕES DE PEÇAS", "#f59e0b", "Maior cadeia integrada do Ocidente"),
    ("LIDERANÇA EM ALGODÃO", "MAIOR EXPORTADOR GLOBAL", "#ec4899", "Superou os Estados Unidos em 2024")
]

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

y_start = 7.2
for rotulo, valor, cor, sub in cards:
    box = dict(boxstyle='round,pad=1.0', facecolor='#161e2e', edgecolor=cor, linewidth=2)
    ax.text(5, y_start, f"{rotulo}\n", color='#94a3b8', fontsize=22, fontweight='bold', ha='center', va='center')
    ax.text(5, y_start - 0.25, f"{valor}", color=cor, fontsize=36, fontweight='bold', ha='center', va='center')
    ax.text(5, y_start - 0.65, f"{sub}", color='#cbd5e1', fontsize=20, ha='center', va='center')
    
    # Desenhar caixa de fundo em torno do grupo
    ax.text(5, y_start - 0.25, " \n \n \n \n ", bbox=box, ha='center', va='center', zorder=1, alpha=0.3)
    y_start -= 1.35

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.17, 
        "CADEIA COMPLETA: DA SEMENTE AO CONSUMIDOR\n\n"
        "• Plantação de algodão no Mato Grosso e Bahia\n"
        "• Fiação, tecelagem e estamparia industrial\n"
        "• 75% da mão de obra na confecção é feminina", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.05, "Fontes: Abit (Agenda Têxtil) / Abrapa / Conab / Caged", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-206/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
