import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

BG_COLOR = '#0B0F15'
CARD_COLOR = '#141D28'
TEXT_MAIN = '#F0F4F8'
TEXT_MUTED = '#8B9BAE'
ACCENT_GREEN = '#00D287'
ACCENT_BLUE = '#2E86DE'
ACCENT_CORAL = '#FF5A5F'

def save_vertical(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', dpi=100)
    plt.close(fig)
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Gancho Quem Paga Mais Impostos?
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ECONOMIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'QUEM PAGA MAIS IMPOSTOS?', ha='center', fontsize=36, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O peso oculto dos tributos no Brasil', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'SISTEMA TRIBUTÁRIO BRASILEIRO', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'REGRESSIVO', ha='center', fontsize=52, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'Quem ganha menos paga mais proporcionalmente', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fontes: Receita Federal & IPEA', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-006/assets/scene1.png')

# ==========================================
# CENA 2: Composição da Arrecadação
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'DE ONDE VÊM OS IMPOSTOS?', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O PESO NO CONSUMO', ha='center', fontsize=36, fontweight='bold', color=ACCENT_CORAL)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    categories = ['Consumo\n(Preços)', 'Folha\n(Salários)', 'Renda\n(Lucros)']
    shares = [44.0, 26.0, 23.0]
    bars = sub_ax.bar(categories, shares, color=[ACCENT_CORAL, ACCENT_BLUE, ACCENT_GREEN], width=0.55, edgecolor='#2C3A47', lw=2)
    sub_ax.set_ylim(0, 55)
    sub_ax.set_ylabel('% da Arrecadação Total', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=15)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 1.2, f'{yval:.0f}%', ha='center', 
                    color=TEXT_MAIN, fontsize=18, fontweight='bold')
        
    fig.text(0.5, 0.33, '44% da arrecadação está embutida nos preços!', ha='center', fontsize=20, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'Em alimentos, farmácia, energia e combustível', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Receita Federal do Brasil | Gráfico Aberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-006/assets/scene2.png')

# ==========================================
# CENA 3: Impacto Renda Baixa vs Renda Alta
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'PESO NO BOLSO DO CIDADÃO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'QUANTO DA RENDA VAI EM TRIBUTOS?', ha='center', fontsize=30, fontweight='bold', color=ACCENT_CORAL)
    
    # Card Renda Baixa
    c1 = plt.Rectangle((0.12, 0.54), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c1)
    fig.text(0.5, 0.70, 'ATÉ 2 SALÁRIOS MÍNIMOS', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.62, '26% DA RENDA', ha='center', fontsize=36, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.56, 'Consumida por tributos indiretos nos produtos!', ha='center', fontsize=15, color=TEXT_MAIN)
    
    # Card Renda Alta
    c2 = plt.Rectangle((0.12, 0.30), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c2)
    fig.text(0.5, 0.46, '10% MAIS RICOS', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.38, '10% DA RENDA', ha='center', fontsize=36, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.32, 'Menor parcela gasta em consumo básico', ha='center', fontsize=15, color=TEXT_MAIN)
    
    # CTA Card
    fig.text(0.5, 0.21, '@ograficoaberto | Gráfico Aberto', ha='center', fontsize=18, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.16, 'Fonte: IPEA / IBGE (Pesquisa de Orçamentos Familiares)', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-006/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
