import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "MADEIRAS, ARTE & SABOR", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "A Riqueza Sensorial das Espécies Nativas", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: O Segredo das Madeiras Brasileiras
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.64,
        "[ O DIFERENCIAL DAS MADEIRAS NATIVAS ]\n\n"
        "O Brasil é o único país a envelhecer destilados em\n"
        "árvores nativas como umburana, jequitibá, bálsamo e ipê,\n"
        "criando aromas exclusivos premiados mundialmente.",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: A Conquista dos Mercados Globais
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.44,
        "[ VALORIZAÇÃO INTERNACIONAL ]\n\n"
        "• Reconhecimento da 'Cachaça' como produto exclusivo do Brasil\n"
        "• Avanço em coquetelaria sofisticada na Europa e nos EUA\n"
        "• Valor médio por litro exportado em alta sustentada",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: MAPA / Ibrac / Ministério das Relações Exteriores", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-230/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
