import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "DIGNIDADE, SAÚDE & TEMPO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "A Revolução Silenciosa do Sertão", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: As Causas da Mudança
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.64,
        "[ OS PILARES DA LONGEVIDADE ]\n\n"
        "• Programa de cisternas de placa garantindo água potável\n"
        "• Agentes comunitários de saúde na porta das casas\n"
        "• Vacinação e queda vertiginosa de doenças infecciosas",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: O Novo Envelhecimento
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.44,
        "[ ENVELHECER COM DIGNIDADE ]\n\n"
        "• Mais de 3 milhões de idosos nordestinos ativos hoje\n"
        "• Aposentadoria rural sustentando a economia dos pequenos municípios\n"
        "• Uma vitória coletiva de políticas públicas continuadas",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: IBGE / DataSUS / Ministério da Saúde / Ipea", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-238/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
