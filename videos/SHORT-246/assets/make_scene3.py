import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "ENERGIA, PROTEÍNA & AGRO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "A Integração Perfeita com a Pecuária", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: O Milagre do DDG
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#ca8a04', linewidth=2)
ax.text(0.5, 0.64,
        "[ O COPRODUTO QUE ALIMENTA O GADO ]\n\n"
        "A destilação do milho extrai apenas o amido.\n"
        "A proteína e a fibra viram DDG, ração premium que\n"
        "engorda rebanhos bovinos e suínos a custos menores.",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Descarbonização
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.44,
        "[ BIOMETANO E CAPTURA DE CARBONO ]\n\n"
        "• Usinas operam em ciclo fechado com pegada de carbono negativa\n"
        "• Geração de energia térmica própria a partir de biomassa florestal\n"
        "• O Brasil consolidando o biocombustível mais competitivo do mundo",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Unem / Conab / NovaCana / Embrapa", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-246/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
