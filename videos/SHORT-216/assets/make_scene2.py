import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O IMPÉRIO GLOBAL DA EMBRAER", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Grandes Fabricantes de Aviação Comercial no Mundo", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Indicadores Principais de Entrega e Mercado
indicadores = [
    ("3ª MAIOR DO PLANETA", "EMBRAER", "#38bdf8", "Líder global absoluta no segmento até 150 assentos"),
    ("FROTA DE E-JETS ENTREGUE", "+2.000 JATOS", "#10b981", "Voando em mais de 100 companhias aéreas globais"),
    ("PRESENÇA NOS EUA E EUROPA", "~30% DAS ROTAS", "#f59e0b", "Conecta hubs como Nova York, Londres e Paris"),
    ("CARTEIRA DE PEDIDOS (BACKLOG)", "US$ 21 BILHÕES", "#ec4899", "Recorde histórico de encomendas firmes")
]

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

y_start = 7.2
for rotulo, valor, cor, sub in indicadores:
    box = dict(boxstyle='round,pad=1.0', facecolor='#161e2e', edgecolor=cor, linewidth=2)
    ax.text(5, y_start, f"{rotulo}\n", color='#94a3b8', fontsize=22, fontweight='bold', ha='center', va='center')
    ax.text(5, y_start - 0.25, f"{valor}", color=cor, fontsize=36, fontweight='bold', ha='center', va='center')
    ax.text(5, y_start - 0.65, f"{sub}", color='#cbd5e1', fontsize=20, ha='center', va='center')
    
    ax.text(5, y_start - 0.25, " \n \n \n \n ", bbox=box, ha='center', va='center', zorder=1, alpha=0.3)
    y_start -= 1.35

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
ax.text(0.5, 0.17, 
        "ALTA TECNOLOGIA NACIONAL DE EXPORTAÇÃO\n\n"
        "• Polo aeroespacial em São José dos Campos (SP)\n"
        "• Família E2 (E190-E2 / E195-E2) consome 25% menos combustível\n"
        "• Avião de transporte militar multimissão KC-390 adotado pela OTAN", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.05, "Fontes: Embraer Investor Relations / Anac / IATA / FlightRadar24", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-216/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
