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
ACCENT_CORAL = '#FF5A5F'

def save_fig(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.tight_layout(pad=3.0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close(fig)
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Inflação acumulada e correção de R$ 100
# ==========================================
def make_scene1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('O QUE ACONTECEU COM R$ 100 DESDE 1994?\nA Inflação Acumulada do Plano Real (1994 a 2026)', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Valor corrigido de R$ 100 de 1994 ao longo do tempo
    years = ['1994', '2000', '2006', '2012', '2018', '2026']
    vals = [100.0, 182.5, 276.4, 389.2, 574.8, 890.4]
    ax1.plot(years, vals, marker='o', linewidth=3.5, markersize=10, color=ACCENT_GREEN)
    ax1.fill_between(years, vals, 100, color=ACCENT_GREEN, alpha=0.15)
    ax1.set_title('Valor Necessário para Comprar o Mesmo de R$ 100 de 1994', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('Valor em Reais Correntes (R$)', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 1050)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(True, linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    for i, txt in enumerate(vals):
        ax1.annotate(f"R$ {txt:.0f}", (years[i], vals[i]+35), ha='center', color=TEXT_MAIN, fontsize=13, fontweight='bold')
        
    # Gráfico 2: Fator de Inflação Acumulada
    bars = ax2.bar(['1994\n(Base 100%)', 'Hoje\n(+790% Inflação)'], [100, 890], 
                   color=[ACCENT_BLUE, ACCENT_CORAL], width=0.45, edgecolor='#2C3A47', lw=2)
    ax2.set_title('Multiplicador Acumulado do IPCA (8,9x)', fontsize=15, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('Índice de Preços', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 1050)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    for b in bars:
        yval = b.get_height()
        ax2.text(b.get_x() + b.get_width()/2.0, yval + 25, f'R$ {yval:.0f}', ha='center', 
                 color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax2.text(0.5, 0.45, 'MULTIPLICOU POR 8,9x\nInflação acumulada: +790%', ha='center', va='center', 
             transform=ax2.transAxes, fontsize=16, fontweight='bold', color=ACCENT_CORAL,
             bbox=dict(boxstyle='round,pad=0.6', facecolor='#0E141B', edgecolor=ACCENT_CORAL, lw=2))

    fig.text(0.5, 0.04, 'Fonte Primária: Banco Central do Brasil (Série SGS 433) / IBGE (IPCA) | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-002/assets/scene1.png')

# ==========================================
# CENA 2: Poder de compra residual (-88.8%)
# ==========================================
def make_scene2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('A CORROSÃO DO PODER DE COMPRA DA CÉDULA DE R$ 100', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Curva da queda do poder de compra
    years = ['1994', '2000', '2006', '2012', '2018', '2026']
    purchasing_power = [100.0, 54.8, 36.2, 25.7, 17.4, 11.2]
    ax1.plot(years, purchasing_power, marker='s', linewidth=3.5, markersize=10, color=ACCENT_CORAL)
    ax1.fill_between(years, purchasing_power, color=ACCENT_CORAL, alpha=0.15)
    ax1.set_title('Poder de Compra de uma Nota de R$ 100 ao Longo das Décadas', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('Poder de Compra (%)', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 115)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(True, linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    for i, txt in enumerate(purchasing_power):
        ax1.annotate(f"{txt:.1f}%", (years[i], purchasing_power[i]+4), ha='center', color=TEXT_MAIN, fontsize=13, fontweight='bold')
        
    # Gráfico 2: O que R$ 100 de hoje compram em valores de 1994
    bars = ax2.bar(['1994\n(R$ 100 completos)', 'Hoje\n(Equivale a R$ 11,23)'], [100.0, 11.23], 
                   color=[ACCENT_BLUE, ACCENT_CORAL], width=0.45, edgecolor='#2C3A47', lw=2)
    ax2.set_title('Poder Residual: O Que R$ 100 Compram Hoje', fontsize=15, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('Valor Real Equivalente (R$ de 1994)', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 115)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    for b in bars:
        yval = b.get_height()
        ax2.text(b.get_x() + b.get_width()/2.0, yval + 3, f'R$ {yval:.2f}', ha='center', 
                 color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax2.text(0.5, 0.45, 'PERDA DE 88,8%\nDO PODER AQUISITIVO', ha='center', va='center', 
             transform=ax2.transAxes, fontsize=18, fontweight='bold', color=ACCENT_CORAL,
             bbox=dict(boxstyle='round,pad=0.6', facecolor='#0E141B', edgecolor=ACCENT_CORAL, lw=2))

    fig.text(0.5, 0.04, 'Cálculo com base no IPCA acumulado pelo Banco Central do Brasil | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-002/assets/scene2.png')

# ==========================================
# CENA 3: Comparação Real: Salário Mínimo e Cesta Básica
# ==========================================
def make_scene3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('O QUE R$ 100 COMPRAVAM NA PRÁTICA: 1994 vs HOJE', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: R$ 100 comparado ao Salário Mínimo
    bars1 = ax1.bar(['1994\n(Salário R$ 64,79)', 'Hoje\n(Salário > R$ 1.500)'], [154.3, 6.6], 
                    color=[ACCENT_GREEN, ACCENT_CORAL], width=0.45, edgecolor='#2C3A47', lw=2)
    ax1.set_title('R$ 100 em Relação ao Salário Mínimo (%)', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('% do Salário Mínimo', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 180)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    for b in bars1:
        yval = b.get_height()
        ax1.text(b.get_x() + b.get_width()/2.0, yval + 4, f'{yval:.1f}%', ha='center', 
                 color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax1.text(0.5, 0.55, 'Em 1994: Pagava 1,5 salário!\nHoje: Menos de 7% de um salário', ha='center', va='center', 
             transform=ax1.transAxes, fontsize=14, color=TEXT_MAIN,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#0E141B', edgecolor='#2C3A47', lw=1.5))
        
    # Gráfico 2: Cestas Básicas Compradas com R$ 100 (DIEESE)
    bars2 = ax2.bar(['1994\n(Cesta R$ 64,30)', 'Hoje\n(Cesta > R$ 800)'], [1.55, 0.12], 
                    color=[ACCENT_BLUE, ACCENT_CORAL], width=0.45, edgecolor='#2C3A47', lw=2)
    ax2.set_title('Quantidade de Cestas Básicas Compradas com R$ 100', fontsize=15, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('Cestas Básicas do DIEESE', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 1.9)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    for b in bars2:
        yval = b.get_height()
        ax2.text(b.get_x() + b.get_width()/2.0, yval + 0.05, f'{yval:.2f} cesta', ha='center', 
                 color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax2.text(0.5, 0.55, 'Em 1994: 1 cesta e meia!\nHoje: Não paga 15% de uma cesta', ha='center', va='center', 
             transform=ax2.transAxes, fontsize=14, color=TEXT_MAIN,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#0E141B', edgecolor='#2C3A47', lw=1.5))

    fig.text(0.5, 0.04, 'Fontes: DIEESE (Pesquisa Nacional da Cesta Básica) & Ministério da Fazenda | Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-002/assets/scene3.png')

# ==========================================
# CENA 4: Painel de Conclusões Econômicas
# ==========================================
def make_scene4():
    fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_COLOR)
    ax.axis('off')
    
    fig.suptitle('3 LIÇÕES ECONÔMICAS SOBRE O NOSSO DINHEIRO', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.92)
    
    cards = [
        ("1. DINHEIRO PARADO É PERDA", 
         "• Inflação de 790% em 30 anos corrói poupança não investida\n• A preservação de patrimônio exige ativos que superem o IPCA\n• A moeda fiduciária sempre perde valor nominal", 
         0.12, ACCENT_BLUE),
        ("2. O PAPEL DA ESTABILIDADE", 
         "• Antes de 1994 a inflação era de 40% a 80% AO MÊS\n• O Real permitiu planejar o futuro e consolidar o crédito\n• Perda de 88% em 30 anos é triunfo perto do padrão pré-94", 
         0.42, ACCENT_GREEN),
        ("3. PODER DE COMPRA REAL", 
         "• Mais importante que a quantidade de notas é o que ela compra\n• Salários e preços devem ser avaliados em termos reais\n• Entender dados protege contra ilusões monetárias", 
         0.72, ACCENT_CORAL)
    ]
    
    for title, content, xpos, color in cards:
        rect = plt.Rectangle((xpos, 0.20), 0.24, 0.58, facecolor='#111A24', edgecolor=color, linewidth=2.5, 
                             transform=fig.transFigure, zorder=2)
        fig.patches.append(rect)
        fig.text(xpos + 0.02, 0.73, title, fontsize=15, fontweight='bold', color=color, transform=fig.transFigure)
        fig.text(xpos + 0.02, 0.46, content, fontsize=12, color=TEXT_MAIN, transform=fig.transFigure, linespacing=1.8)

    fig.text(0.5, 0.10, 'Canal Gráfico Aberto | A realidade explicada através dos dados oficiais', 
             ha='center', fontsize=14, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.05, 'Fontes: Banco Central do Brasil (Série SGS 433) / IBGE / DIEESE', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-002/assets/scene4.png')

# ==========================================
# MINIATURA (THUMBNAIL) 1280x720
# ==========================================
def make_thumbnail():
    fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100, facecolor=BG_COLOR)
    ax.set_facecolor(CARD_COLOR)
    ax.axis('off')
    
    fig.text(0.08, 0.80, 'R$ 100 EM 1994 vs HOJE', fontsize=34, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.08, 0.70, 'O que sobrou do poder de compra do Real?', fontsize=20, color=TEXT_MAIN)
    
    # Gráfico miniatura
    sub_ax = fig.add_axes([0.08, 0.16, 0.45, 0.44], facecolor='#111A24')
    sub_ax.bar(['1994', 'Hoje'], [100.0, 11.2], color=[ACCENT_BLUE, ACCENT_CORAL], width=0.45)
    sub_ax.set_title('Poder de Compra Real (R$)', fontsize=13, color=TEXT_MUTED)
    sub_ax.set_ylim(0, 115)
    sub_ax.tick_params(colors=TEXT_MUTED, labelsize=11)
    sub_ax.text(0, 103, 'R$ 100', ha='center', color=TEXT_MAIN, fontsize=14, fontweight='bold')
    sub_ax.text(1, 14.5, 'R$ 11,23', ha='center', color=ACCENT_CORAL, fontsize=14, fontweight='bold')
    sub_ax.grid(axis='y', linestyle=':', alpha=0.3, color='#FFF')
    
    # Card de impacto
    card_box = plt.Rectangle((0.58, 0.16), 0.34, 0.44, facecolor='#111A24', edgecolor=ACCENT_CORAL, linewidth=3, 
                             transform=fig.transFigure)
    fig.patches.append(card_box)
    fig.text(0.75, 0.48, 'PERDA REAL', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.75, 0.34, '-88,8%', ha='center', fontsize=40, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.75, 0.22, 'Inflação IPCA: +790%', ha='center', fontsize=15, color=TEXT_MAIN)
    
    fig.text(0.92, 0.90, 'GRÁFICO ABERTO', ha='right', fontsize=14, fontweight='bold', color=TEXT_MUTED)

    fig.patch.set_facecolor(BG_COLOR)
    plt.savefig('videos/PILOTO-002/export/thumbnail.png', facecolor=BG_COLOR, edgecolor='none')
    plt.close(fig)
    print("Salvo: videos/PILOTO-002/export/thumbnail.png")

make_scene1()
make_scene2()
make_scene3()
make_scene4()
make_thumbnail()
