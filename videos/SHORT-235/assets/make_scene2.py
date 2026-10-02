import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O APAGÃO DOS PROFESSORES", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Aulas do Ensino Médio com Docente com Licenciatura Adequada (%)", color='#94a3b8', fontsize=22, ha='center', transform=ax.transAxes)

# Dados Inep (Censo Escolar) / MEC / Todos Pela Educação
disciplinas = [
    'Biologia',
    'Língua Portuguesa',
    'Matemática',
    'História & Geografia',
    'Química',
    'Física (Maior Apagão)'
]
adequacao = [78.2, 74.5, 62.1, 58.4, 43.2, 22.8]
colors = ['#10b981', '#3b82f6', '#06b6d4', '#f59e0b', '#f97316', '#ef4444']

y_pos = np.arange(len(disciplinas))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, adequacao, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 100)
ax.set_ylim(-0.8, len(disciplinas) - 0.2)
ax.axis('off')

for bar, disc, val in zip(bars, disciplinas, adequacao):
    y = bar.get_y() + bar.get_height() / 2
    is_critical = val < 30
    textColor = '#ffffff' if is_critical else '#cbd5e1'
    fontSize = 28 if is_critical else 23
    weight = 'bold' if is_critical else 'normal'
    
    ax.text(2.0, y + 0.38, disc.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f}%".replace('.', ',')
    ax.text(val + 2.5, y, val_str, color='#f87171' if is_critical else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#ef4444', linewidth=2)
ax.text(0.5, 0.20, 
        "O DESAFIO DA FORMAÇÃO DOCENTE NO BRASIL\n\n"
        "• Apenas 22,8% das aulas de Física contam com físico formado\n"
        "• Química tem menos da metade (43%) dos professores com diploma na área\n"
        "• Déficit nacional de mais de 235 mil docentes licenciados na rede pública\n"
        "• Queda na procura por cursos de licenciatura em universidades públicas\n"
        "• Urgência em planos de carreira e atratividade salarial", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Inep (Censo da Educação Básica) / MEC / Todos Pela Educação", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-235/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
