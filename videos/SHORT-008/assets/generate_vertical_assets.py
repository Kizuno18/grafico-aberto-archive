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
# CENA 1: Casas vs Apartamentos
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CENSO DEMOGRÁFICO IBGE', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'ONDE O BRASILEIRO MORA?', ha='center', fontsize=36, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'Casas versus Apartamentos no Brasil', ha='center', fontsize=22, color=ACCENT_GREEN)
    
    # 2 Cards Grandes
    c1 = plt.Rectangle((0.12, 0.54), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_BLUE, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c1)
    fig.text(0.5, 0.70, 'CASAS E CASAS DE VILA', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.62, '84,8%', ha='center', fontsize=44, fontweight='heavy', color=ACCENT_BLUE)
    fig.text(0.5, 0.56, '171 milhões de brasileiros moram em casas', ha='center', fontsize=16, color=TEXT_MAIN)
    
    c2 = plt.Rectangle((0.12, 0.30), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c2)
    fig.text(0.5, 0.46, 'APARTAMENTOS (EM ALTA)', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.38, '12,5%', ha='center', fontsize=44, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.32, '25,2 milhões de pessoas (crescendo rápido!)', ha='center', fontsize=16, color=TEXT_MAIN)
    
    fig.text(0.5, 0.21, '@ograficoaberto | Gráfico Aberto', ha='center', fontsize=18, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.16, 'Fonte oficial: IBGE — Censo Demográfico 2022', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-008/assets/scene1.png')

# ==========================================
# CENA 2: A Evolução dos Apartamentos
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'A VERTICALIZAÇÃO DO PAÍS', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'AVANÇO DOS APARTAMENTOS', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    years = ['2000', '2010', '2022']
    vals = [7.6, 8.5, 12.5]
    bars = sub_ax.bar(years, vals, color=['#576574', ACCENT_BLUE, ACCENT_GREEN], width=0.50, edgecolor='#2C3A47', lw=2)
    sub_ax.set_ylim(0, 16)
    sub_ax.set_ylabel('% da População em Apartamentos', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=16)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 0.5, f'{yval:.1f}%', ha='center', 
                    color=TEXT_MAIN, fontsize=18, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Aumento de 47% na proporção em 12 anos!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'Já são 25,2 milhões de moradores em edifícios', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IBGE Censos Demográficos | Gráfico Aberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-008/assets/scene2.png')

# ==========================================
# CENA 3: Os Municípios Mais Verticais
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'RANKING DE VERTICALIZAÇÃO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A CIDADE MAIS VERTICAL', ha='center', fontsize=36, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.18, 0.40, 0.68, 0.34], facecolor=CARD_COLOR)
    cities = ['Porto Alegre', 'Vitória', 'São Caetano', 'Balneário C.', 'Santos']
    shares = [42.4, 45.4, 50.8, 57.2, 63.4]
    bars = sub_ax.barh(cities, shares, color=ACCENT_CYAN, height=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_xlim(0, 75)
    sub_ax.set_xlabel('% de Moradores em Apartamentos', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='x', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=14)
    for b in bars:
        w = b.get_width()
        sub_ax.text(w + 1.5, b.get_y() + b.get_height()/2.0, f'{w:.1f}%', va='center', 
                    color=TEXT_MAIN, fontsize=15, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Santos: 63,4% moram em apartamentos!', ha='center', fontsize=20, fontweight='bold', color=ACCENT_CYAN)
    fig.text(0.5, 0.28, 'Vitória (45,4%) e POA (42,4%) lideram entre capitais', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=17, fontweight='bold', color=TEXT_MAIN)
    
    save_vertical(fig, 'videos/SHORT-008/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
