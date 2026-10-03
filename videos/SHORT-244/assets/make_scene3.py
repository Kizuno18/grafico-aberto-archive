import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "POLOS, COURO & DESIGN", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "Os Clusters da Moda Brasileira", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: A Força dos Polos Industriais
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.64,
        "[ OS POLOS DA PRODUÇÃO NACIONAL ]\n\n"
        "• Franca (SP): referência mundial em calçados masculinos finos\n"
        "• Vale dos Sinos (RS): tradição exportadora em moda e couro\n"
        "• Nova Serrana (MG): polo dinâmico do calçado esportivo\n"
        "• Ceará e Paraíba: gigantes em sandálias e injetados",
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Sustentabilidade e Conforto
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.44,
        "[ DIFERENCIAIS DE COMPETITIVIDADE ]\n\n"
        "• Programa 'Origem Sustentável' com certificação ESG no setor\n"
        "• Couro rastreado e design autoral valorizado no exterior\n"
        "• Sandálias de borracha como ícones globais de brasilidade",
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Abicalçados / ApexBrasil / MDIC", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-244/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
