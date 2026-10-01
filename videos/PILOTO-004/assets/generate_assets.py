import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 150

BG_COLOR = '#0E141B'
CARD_COLOR = '#17212D'
TEXT_MAIN = '#F0F4F8'
TEXT_MUTED = '#8B9BAE'
ACCENT_GREEN = '#00D287'
ACCENT_BLUE = '#2E86DE'
ACCENT_CYAN = '#00CEC9'
ACCENT_YELLOW = '#FDCB6E'
ACCENT_CORAL = '#FF5A5F'

def save_fig(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.tight_layout(pad=3.0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close(fig)
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Carga Tributária Total (33% do PIB)
# ==========================================
def make_scene1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('A CARGA TRIBUTÁRIA BRASILEIRA EM PERSPECTIVA\nQuanto o País Arrecada em Relação ao Tamanho da Economia', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Evolução da Carga Tributária
    years = ['1990', '2000', '2010', '2020', '2024']
    carga = [25.0, 30.0, 32.4, 31.8, 33.1]
    ax1.plot(years, carga, marker='o', linewidth=3.5, markersize=10, color=ACCENT_CORAL)
    ax1.fill_between(years, carga, 20, color=ACCENT_CORAL, alpha=0.15)
    ax1.set_title('Evolução da Carga Tributária Bruta (% do PIB)', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('% do PIB', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(20, 40)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(True, linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    for i, txt in enumerate(carga):
        ax1.annotate(f"{txt:.1f}%", (years[i], carga[i]+0.8), ha='center', color=TEXT_MAIN, fontsize=13, fontweight='bold')
        
    # Gráfico 2: Brasil vs América Latina vs OCDE
    regions = ['América Latina\n(Média)', 'Brasil\n(Nacional)', 'OCDE\n(Desenvolvidos)']
    vals = [21.5, 33.1, 34.0]
    colors = ['#576574', ACCENT_CORAL, ACCENT_BLUE]
    bars = ax2.bar(regions, vals, color=colors, width=0.50, edgecolor='#2C3A47', lw=2)
    ax2.set_title('Carga Tributária Comparada (% do PIB)', fontsize=15, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('% do PIB', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 45)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    for b in bars:
        yval = b.get_height()
        ax2.text(b.get_x() + b.get_width()/2.0, yval + 1.0, f'{yval:.1f}%', ha='center', 
                 color=TEXT_MAIN, fontsize=15, fontweight='bold')
    ax2.text(0.5, 0.45, 'O BRASIL COBRA IMPOSTOS NO NÍVEL DA OCDE,\nMAS COM ESTRUTURA MUITO DIFERENTE', ha='center', va='center', 
             transform=ax2.transAxes, fontsize=14, fontweight='bold', color=ACCENT_CORAL,
             bbox=dict(boxstyle='round,pad=0.6', facecolor='#0E141B', edgecolor=ACCENT_CORAL, lw=2))

    fig.text(0.5, 0.04, 'Fonte Primária: Receita Federal do Brasil & OCDE Revenue Statistics | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-004/assets/scene1.png')

# ==========================================
# CENA 2: De Onde Vêm os Impostos (Consumo vs Renda)
# ==========================================
def make_scene2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('DE ONDE VÊM OS IMPOSTOS DO BRASIL?\nA Distribuição da Arrecadação por Base de Incidência', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Barras das 4 bases
    bases = ['Consumo\n(Preços/ICMS/PIS)', 'Folha Salarial\n(Previdência/INSS)', 'Renda e Lucros\n(IRPF/IRPJ/CSLL)', 'Propriedade\n(IPTU/IPVA)']
    shares = [44.2, 26.1, 23.4, 4.8]
    colors = [ACCENT_CORAL, ACCENT_BLUE, ACCENT_GREEN, '#576574']
    bars = ax1.bar(bases, shares, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    ax1.set_title('Composição da Arrecadação Total (%)', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('% da Receita Tributária', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 55)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=11)
    for b in bars:
        yval = b.get_height()
        ax1.text(b.get_x() + b.get_width()/2.0, yval + 1.2, f'{yval:.1f}%', ha='center', 
                 color=TEXT_MAIN, fontsize=15, fontweight='bold')
        
    # Gráfico 2: Contraste Consumo vs Renda
    ax2.bar(['Consumo de Bens e Serviços\n(Impostos nos Preços)', 'Renda e Lucros\n(Ganhos de Capital)'], [44.2, 23.4],
            color=[ACCENT_CORAL, ACCENT_GREEN], width=0.45, edgecolor='#2C3A47', lw=2)
    ax2.set_title('O Desequilíbrio entre Consumo e Renda', fontsize=15, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('% da Arrecadação', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 55)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    ax2.text(0, 46.0, '44.2%', ha='center', color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax2.text(1, 25.0, '23.4%', ha='center', color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax2.text(0.5, 0.55, 'QUASE O DOBRO!\nO Brasil tributa muito mais as compras\ndo que a riqueza e os lucros', ha='center', va='center', 
             transform=ax2.transAxes, fontsize=15, fontweight='bold', color=ACCENT_CORAL,
             bbox=dict(boxstyle='round,pad=0.6', facecolor='#0E141B', edgecolor=ACCENT_CORAL, lw=2))

    fig.text(0.5, 0.04, 'Fonte Primária: Receita Federal do Brasil (Carga Tributária Bruta) | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-004/assets/scene2.png')

# ==========================================
# CENA 3: A Regressividade no Orçamento Familiar
# ==========================================
def make_scene3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('A REGRESSIVIDADE DO SISTEMA TRIBUTÁRIO\nQuanto Cada Família Compromete de Sua Renda Pagando Tributos Indiretos', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Peso dos Tributos Indiretos por Faixa de Renda
    brackets = ['Até 2 SM\n(Baixa Renda)', '2 a 5 SM\n(Renda Média-Baixa)', '5 a 10 SM\n(Classe Média)', 'Mais de 25 SM\n(Mais Ricos)']
    impact = [26.5, 20.2, 16.4, 10.1]
    colors = [ACCENT_CORAL, '#E17055', '#FDCB6E', ACCENT_GREEN]
    bars = ax1.bar(brackets, impact, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    ax1.set_title('Percentual da Renda Gasto com Impostos sobre Consumo (%)', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('% da Renda Familiar', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 32)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=11)
    for b in bars:
        yval = b.get_height()
        ax1.text(b.get_x() + b.get_width()/2.0, yval + 0.8, f'{yval:.1f}%', ha='center', 
                 color=TEXT_MAIN, fontsize=15, fontweight='bold')
        
    # Gráfico 2: Razão Comparativa
    ax2.bar(['Quem Ganha Até 2 SM', 'Os 10% Mais Ricos'], [26.5, 10.1],
            color=[ACCENT_CORAL, ACCENT_GREEN], width=0.45, edgecolor='#2C3A47', lw=2)
    ax2.set_title('Quem Paga Mais Proporcionalmente?', fontsize=15, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('% da Renda Comprometida', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 32)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    ax2.text(0, 27.5, '26.5%', ha='center', color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax2.text(1, 11.0, '10.1%', ha='center', color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax2.text(0.5, 0.55, 'MAIS DE 2,5x MAIOR!\nQuem ganha menos consome toda a renda em itens básicos\ne paga tributos em cada produto comprado', ha='center', va='center', 
             transform=ax2.transAxes, fontsize=13, color=TEXT_MAIN,
             bbox=dict(boxstyle='round,pad=0.6', facecolor='#0E141B', edgecolor=ACCENT_CORAL, lw=2))

    fig.text(0.5, 0.04, 'Fonte Primária: IPEA / IBGE (Pesquisa de Orçamentos Familiares - POF) | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-004/assets/scene3.png')

# ==========================================
# CENA 4: Comparativo Internacional (Brasil vs OCDE)
# ==========================================
def make_scene4():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('BRASIL vs PAÍSES DESENVOLVIDOS (OCDE)\nComo Outros Países Distribuem Sua Arrecadação', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Brasil vs OCDE em Renda vs Consumo
    x = np.arange(2)
    width = 0.35
    brasil_vals = [44.2, 23.4]
    ocde_vals = [32.1, 34.2]
    
    ax1.bar(x - width/2, brasil_vals, width, label='Brasil', color=ACCENT_CORAL)
    ax1.bar(x + width/2, ocde_vals, width, label='Média OCDE', color=ACCENT_BLUE)
    ax1.set_xticks(x)
    ax1.set_xticklabels(['Tributos sobre Consumo', 'Tributos sobre Renda'], fontsize=12)
    ax1.set_title('Consumo vs Renda (% da Arrecadação)', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('% da Receita', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 55)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    ax1.legend(loc='upper right', frameon=True, facecolor=CARD_COLOR, edgecolor='#2C3A47', labelcolor=TEXT_MAIN, fontsize=12)
    
    # Gráfico 2: Resumo de Lições
    ax2.set_facecolor(CARD_COLOR)
    ax2.axis('off')
    ax2.text(0.05, 0.85, '3 LIÇÕES SOBRE OS IMPOSTOS NO BRASIL', fontsize=16, fontweight='bold', color=TEXT_MAIN)
    ax2.text(0.05, 0.65, '1. Imposto invisível:\nQuase metade dos tributos já está embutida nos preços.', fontsize=13, color=ACCENT_CORAL)
    ax2.text(0.05, 0.40, '2. Peso nos mais vulneráveis:\nO sistema tributário penaliza quem gasta tudo o que ganha.', fontsize=13, color=ACCENT_YELLOW)
    ax2.text(0.05, 0.15, '3. O papel da reforma:\nSimplificar e redistribuir tributos é a chave do desenvolvimento.', fontsize=13, color=ACCENT_GREEN)

    fig.text(0.5, 0.04, 'Fontes: Receita Federal, OCDE Revenue Statistics & IPEA | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-004/assets/scene4.png')

# ==========================================
# MINIATURA (THUMBNAIL) 1280x720
# ==========================================
def make_thumbnail():
    fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100, facecolor=BG_COLOR)
    ax.set_facecolor(CARD_COLOR)
    ax.axis('off')
    
    fig.text(0.08, 0.80, 'QUEM PAGA A CONTA?', fontsize=36, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.08, 0.70, 'A verdade sobre os impostos no Brasil', fontsize=20, color=TEXT_MAIN)
    
    # Gráfico miniatura
    sub_ax = fig.add_axes([0.08, 0.16, 0.45, 0.44], facecolor='#111A24')
    sub_ax.bar(['Consumo', 'Renda'], [44.2, 23.4], color=[ACCENT_CORAL, ACCENT_GREEN], width=0.45)
    sub_ax.set_title('Onde Está o Peso dos Impostos (%)', fontsize=13, color=TEXT_MUTED)
    sub_ax.set_ylim(0, 55)
    sub_ax.tick_params(colors=TEXT_MUTED, labelsize=11)
    sub_ax.text(0, 46, '44.2%', ha='center', color=ACCENT_CORAL, fontsize=14, fontweight='bold')
    sub_ax.text(1, 25, '23.4%', ha='center', color=ACCENT_GREEN, fontsize=14, fontweight='bold')
    sub_ax.grid(axis='y', linestyle=':', alpha=0.3, color='#FFF')
    
    # Card de impacto
    card_box = plt.Rectangle((0.58, 0.16), 0.34, 0.44, facecolor='#111A24', edgecolor=ACCENT_CORAL, linewidth=3, 
                             transform=fig.transFigure)
    fig.patches.append(card_box)
    fig.text(0.75, 0.48, 'POBRE PAGA MAIS', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.75, 0.34, '26% vs 10%', ha='center', fontsize=38, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.75, 0.22, 'Do salário comprometido em tributos', ha='center', fontsize=13, color=TEXT_MAIN)
    
    fig.text(0.92, 0.90, 'GRÁFICO ABERTO', ha='right', fontsize=14, fontweight='bold', color=TEXT_MUTED)

    fig.patch.set_facecolor(BG_COLOR)
    plt.savefig('videos/PILOTO-004/export/thumbnail.png', facecolor=BG_COLOR, edgecolor='none')
    plt.close(fig)
    print("Salvo: videos/PILOTO-004/export/thumbnail.png")

make_scene1()
make_scene2()
make_scene3()
make_scene4()
make_thumbnail()

