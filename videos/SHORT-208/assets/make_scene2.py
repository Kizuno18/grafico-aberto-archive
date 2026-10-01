import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A VIRADA HISTÓRICA DO EAD", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Ingressantes no Ensino Superior no Brasil (%)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Inep / Censo da Educação Superior (Proporção de Ingressantes EAD vs Presencial)
anos = [2012, 2015, 2018, 2020, 2023]
ead = [16.4, 21.9, 39.8, 53.4, 64.3]
presencial = [83.6, 78.1, 60.2, 46.6, 35.7]

x_pos = np.arange(len(anos))

# Gráfico de barras empilhadas
bar_width = 0.52
p1 = ax.bar(x_pos, ead, bar_width, label='EAD (A Distância)', color='#38bdf8', edgecolor='#1e293b', linewidth=2)
p2 = ax.bar(x_pos, presencial, bar_width, bottom=ead, label='Presencial', color='#64748b', edgecolor='#1e293b', linewidth=2)

ax.set_ylim(0, 115)
ax.set_xticks(x_pos)
ax.set_xticklabels([str(a) for a in anos], color='#cbd5e1', fontsize=24, fontweight='bold')
ax.tick_params(axis='y', colors='#94a3b8', labelsize=20)
ax.grid(True, axis='y', linestyle=':', alpha=0.25, color='#475569')

# Rótulos EAD nas barras
for bar, val in zip(p1, ead):
    ax.text(bar.get_x() + bar.get_width()/2, val / 2, f"{val:.1f}%".replace('.', ','), color='#0f172a', fontsize=22, fontweight='bold', ha='center', va='center')

# Rótulos Presencial nas barras
for bar, val, bot in zip(p2, presencial, ead):
    ax.text(bar.get_x() + bar.get_width()/2, bot + val / 2, f"{val:.1f}%".replace('.', ','), color='#ffffff', fontsize=22, fontweight='bold', ha='center', va='center')

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.14), ncol=2, frameon=False, fontsize=22, labelcolor='#ffffff')

# Posição dos eixos no layout vertical
ax.set_position([0.12, 0.44, 0.80, 0.35])

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
fig.text(0.5, 0.23, 
        "+3,1 MILHÕES DE NOVOS ALUNOS EM EAD\n\n"
        "• Mais de 64% de todos os novos estudantes escolhem EAD\n"
        "• Na rede privada, o EAD já representa mais de 72% dos calouros\n"
        "• Maior flexibilidade e mensalidades até 60% menores", 
        color='#f8fafc', fontsize=24, ha='center', va='center', bbox=highlight_box, linespacing=1.6)

# Fonte
fig.text(0.5, 0.07, "Fonte: Inep (Censo da Educação Superior 2012-2023) / MEC", color='#64748b', fontsize=20, ha='center')

plt.savefig('videos/SHORT-208/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
