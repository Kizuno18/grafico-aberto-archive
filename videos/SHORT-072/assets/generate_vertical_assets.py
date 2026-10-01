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
ACCENT_YELLOW = '#FDCB6E'
ACCENT_CORAL = '#FF5A5F'

def save_vertical(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', dpi=100)
    plt.close(fig)
    print(f'Salvo: {path}')

def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'DEFICIÊNCIA AUDITIVA (IBGE/PNS)', ha='center', fontsize=21, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'OS SURDOS NO BRASIL', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'A dimensão da perda auditiva no país', ha='center', fontsize=22, color=ACCENT_CYAN)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CYAN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'PESSOAS COM PERDA AUDITIVA', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '10,7 MI', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_CYAN)
    fig.text(0.5, 0.44, 'Cerca de 5% de toda a população brasileira!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Pesquisa Nacional de Saúde — IBGE', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-072/assets/scene1.png')

def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'INTENSIDADE DA PERDA AUDITIVA (MILHÕES)', ha='center', fontsize=19, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'GRAVIDADE E FAIXA ETÁRIA', ha='center', fontsize=32, fontweight='bold', color=ACCENT_YELLOW)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    graus = ['Leve / Mod.', 'Severa / Prof.']
    milhoes = [8.4, 2.3]
    colors = [ACCENT_BLUE, ACCENT_CORAL]
    bars = sub_ax.bar(graus, milhoes, color=colors, width=0.45, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 10.5)
    sub_ax.set_ylabel('Milhões de Pessoas', color=TEXT_MUTED, fontsize=12)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=11)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 0.3, f'{yval:.1f} mi', ha='center', 
                    color=TEXT_MAIN, fontsize=14, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Mais de 2,3 milhões vivem com surdez severa!', ha='center', fontsize=17, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'Mais de 50% dos casos concentram-se acima dos 60 anos', ha='center', fontsize=13, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Instituto Locomotiva / IBGE | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-072/assets/scene2.png')

def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CIDADANIA E INCLUSÃO (LEI 10.436)', ha='center', fontsize=21, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A FORÇA DA LIBRAS', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'LÍNGUA BRASILEIRA DE SINAIS', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, 'LÍNGUA OFICIAL', ha='center', fontsize=36, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.50, 'Educação bilíngue e acessibilidade para milhões!', ha='center', fontsize=15, color=TEXT_MAIN)
    
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-072/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
