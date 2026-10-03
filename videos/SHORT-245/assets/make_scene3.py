import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "OPORTUNIDADE & FUTURO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "Os Caminhos para Alavancar a Juventude", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: Ensino Técnico e Permanência
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.64,
        "[ O PAPEL DO ENSINO PROFISSIONALIZANTE ]\n\n"
        "Cursos técnicos integrados ao ensino médio elevam\n"
        "a empregabilidade em 30% e reduzem o abandono escolar,\n"
        "garantindo transição segura para o mercado de trabalho.",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Apoio a Mães Jovens
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#ef4444', linewidth=2)
ax.text(0.5, 0.44,
        "[ CRECHES E INCLUSÃO PRODUTIVA ]\n\n"
        "• Acesso a creches públicas libera mães jovens para estudar e trabalhar\n"
        "• Bolsas de incentivo reduzem a evasão no ensino médio público\n"
        "• O bônus demográfico em sua última janela de oportunidade",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: IBGE / Ipea / Ministério da Educação / MTE", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-245/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
