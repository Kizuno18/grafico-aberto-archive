import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "ENGENHARIA & FUTURO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "Os Motores da Produtividade Nacional", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: O Gargalo da Indústria
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#3b82f6', linewidth=2)
ax.text(0.5, 0.64,
        "[ O GARGALO DA PRODUTIVIDADE ]\n\n"
        "Economias avançadas têm até 4 vezes mais engenheiros\n"
        "por habitante trabalhando direto na indústria manufatureira,\n"
        "tornando a atração de talentos um desafio central do país.",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: A Fronteira Tecnológica
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.44,
        "[ A FRONTEIRA DO AGRO E DA ENERGIA ]\n\n"
        "• Explosão da demanda por engenharia agronômica no Centro-Oeste\n"
        "• Projetos bilionários em energia solar, eólica e hidrogênio verde\n"
        "• Atuação global e trabalho remoto para empresas internacionais",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Confea / Caged / Ipea / CNI / IBGE", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-225/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
