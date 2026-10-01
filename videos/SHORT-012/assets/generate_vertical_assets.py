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
# CENA 1: Gancho Desigualdade de Renda
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ECONOMIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DESIGUALDADE DE RENDA', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O Brasil melhorou ou piorou em 30 anos?', ha='center', fontsize=22, color=ACCENT_CYAN)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CYAN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'O QUE OS DADOS OFICIAIS MOSTRAM', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'ÍNDICE DE GINI', ha='center', fontsize=48, fontweight='heavy', color=ACCENT_CYAN)
    fig.text(0.5, 0.44, 'A trajetória da desigualdade de 1995 a 2024', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fontes oficiais: IBGE (PNAD) & IPEA', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-012/assets/scene1.png')

# ==========================================
# CENA 2: Gráfico Histórico do Índice de Gini
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'HISTÓRICO DO GINI NO BRASIL', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'QUEDA DE 14% NA DESIGUALDADE', ha='center', fontsize=32, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    years = ['1995', '2001', '2008', '2014', '2020', 'Hoje']
    gini_vals = [0.600, 0.593, 0.544, 0.515, 0.524, 0.518]
    sub_ax.plot(years, gini_vals, marker='o', linewidth=3.5, markersize=10, color=ACCENT_GREEN)
    sub_ax.fill_between(years, gini_vals, 0.50, color=ACCENT_GREEN, alpha=0.15)
    sub_ax.set_ylim(0.48, 0.63)
    sub_ax.set_ylabel('Índice de Gini (0 a 1)', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(True, linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=13)
    for i, v in enumerate(gini_vals):
        sub_ax.text(i, v + 0.008, f'{v:.3f}', ha='center', color=TEXT_MAIN, fontsize=14, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Caiu de 0,600 para ~0,518 (menor desigualdade)', ha='center', fontsize=17, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'Impacto da estabilidade, educação e programas sociais', ha='center', fontsize=14, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IBGE PNAD Contínua | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-012/assets/scene2.png')

# ==========================================
# CENA 3: Conclusão e Posição Global
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'O DESAFIO QUE CONTINUA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'ENTRE OS MAIS DESIGUAIS', ha='center', fontsize=34, fontweight='bold', color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'POSIÇÃO INTERNACIONAL', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.60, 'TOP 15 MUNDIAL', ha='center', fontsize=48, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.52, 'Entre os países com maior concentração de renda', ha='center', fontsize=16, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-012/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
