import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "MEMÓRIA, DIREITOS & CIDADES", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "A Visibilidade Histórica dos Povos Originários", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: Acesso a Direitos Urbanos
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#dc2626', linewidth=2)
ax.text(0.5, 0.64,
        "[ O DESAFIO DA CIDADANIA NAS CIDADES ]\n\n"
        "Indígenas em áreas urbanas exigem políticas específicas\n"
        "de saúde intercultural, moradia digna e educação bilíngue,\n"
        "preservando línguas maternas e identidade ancestral.",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Mapeamento em Todo o País
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.44,
        "[ O BRASIL INDÍGENA REVELADO ]\n\n"
        "• Amazonas e Bahia concentram as maiores populações absolutas\n"
        "• Presença ativa em universidades, parlamentos e tecnologia\n"
        "• O Censo que finalmente quebrou a invisibilidade estatística",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: IBGE / Funai / Ministério dos Povos Indígenas", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-232/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
