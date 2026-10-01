import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "O GARGALO DA RESIDÊNCIA", color='#ffffff', fontsize=40, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "Desafios da Formação de Especialistas", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: Vagas de Especialização
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#38bdf8', linewidth=2)
ax.text(0.5, 0.64,
        "[ DÉFICIT DE RESIDÊNCIA MÉDICA ]\n\n"
        "Enquanto as vagas de graduação dispararam,\n"
        "as bolsas de residência em hospitais não acompanharam,\n"
        "gerando milhares de médicos generalistas sem especialidade.",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Concentração Geográfica
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.44,
        "[ DISTRIBUIÇÃO REGIONAL ]\n\n"
        "• Mais de 50% dos especialistas seguem no Sudeste\n"
        "• Falta de infraestrutura hospitalar em cidades pequenas\n"
        "• Pressão por revalidação e exames de proficiência",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#0284c7', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#ffffff', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: CFM / Demografia Médica / MEC", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-205/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
