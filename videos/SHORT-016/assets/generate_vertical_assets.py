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
ACCENT_CYAN = '#00CEC9'
ACCENT_CORAL = '#FF5A5F'

def save_vertical(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', dpi=100)
    plt.close(fig)
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Gancho Dívida Pública
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ECONOMIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A DÍVIDA PÚBLICA DO BRASIL', ha='center', fontsize=32, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'Para quem o governo realmente deve?', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'VALOR TOTAL DA DÍVIDA BRUTA', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'R$ 8,8 TRI', ha='center', fontsize=56, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'Equivale a quase 78% do PIB nacional', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fontes: Banco Central & Tesouro Nacional', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-016/assets/scene1.png')

# ==========================================
# CENA 2: Quem São os Credores?
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'QUEM SÃO OS CREDORES? (TESOURO)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'MAIS DE 90% É INTERNA!', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.22, 0.42, 0.65, 0.30], facecolor=CARD_COLOR)
    credores = ['Estrangeiros', 'Previdência', 'Bancos', 'Fundos Invest.']
    shares = [10.0, 23.0, 29.0, 30.0]
    colors = ['#576574', ACCENT_CYAN, ACCENT_BLUE, ACCENT_GREEN]
    bars = sub_ax.barh(credores, shares, color=colors, height=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_xlim(0, 40)
    sub_ax.set_xlabel('% da Dívida Pública Federal', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='x', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=13)
    for b in bars:
        w = b.get_width()
        sub_ax.text(w + 1.0, b.get_y() + b.get_height()/2.0, f'{int(w)}%', va='center', 
                    color=TEXT_MAIN, fontsize=15, fontweight='bold')
        
    fig.text(0.5, 0.34, 'Bancos, fundos e aposentadorias têm > 80%!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.29, 'O Brasil quase não deve em moeda estrangeira', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Relatório Mensal da Dívida — Tesouro Nacional', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-016/assets/scene2.png')

# ==========================================
# CENA 3: A Realidade Econômica
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'A REALIDADE ECONÔMICA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'PARA QUEM O GOVERNO PAGA?', ha='center', fontsize=32, fontweight='bold', color=ACCENT_CYAN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CYAN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'ONDE ESTÁ APLICADA A DÍVIDA', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.60, 'POUPANÇAS E FUNDOS', ha='center', fontsize=36, fontweight='heavy', color=ACCENT_CYAN)
    fig.text(0.5, 0.52, 'Nos investimentos dos próprios brasileiros!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-016/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
