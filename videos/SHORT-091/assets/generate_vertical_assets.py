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
    
    fig.text(0.5, 0.88, 'DEMOGRAFIA RELIGIOSA (IBGE/DATAFOLHA)', ha='center', fontsize=19, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A VIRADA RELIGIOSA', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'A transição mais veloz do Ocidente', ha='center', fontsize=22, color=ACCENT_YELLOW)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_YELLOW, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'SALTO DOS EVANGÉLICOS NO BRASIL', ha='center', fontsize=14, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '6% -> 31%', ha='center', fontsize=54, fontweight='heavy', color=ACCENT_YELLOW)
    fig.text(0.5, 0.44, 'Crescimento constante nas últimas quatro décadas!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Censos Demográficos — IBGE / Datafolha', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-091/assets/scene1.png')

def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'A EVOLUÇÃO DAS DUAS CURVAS (%)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'CATÓLICOS VS EVANGÉLICOS', ha='center', fontsize=32, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.15, 0.38, 0.70, 0.35], facecolor=CARD_COLOR)
    anos = ['1980', '2000', '2010', '2024', '2035*']
    catolicos = [89.0, 73.6, 64.6, 50.0, 38.0]
    evangelicos = [6.6, 15.4, 22.2, 31.0, 39.0]
    
    sub_ax.plot(anos, catolicos, marker='o', markersize=8, color=ACCENT_BLUE, linewidth=3, label='Católicos')
    sub_ax.plot(anos, evangelicos, marker='s', markersize=8, color=ACCENT_YELLOW, linewidth=3, label='Evangélicos')
    sub_ax.set_ylim(0, 100)
    sub_ax.set_ylabel('% da População Brasileira', color=TEXT_MUTED, fontsize=11)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=10)
    sub_ax.legend(facecolor='#141D28', edgecolor='none', labelcolor=TEXT_MAIN, loc='center left')
    
    sub_ax.annotate('Ponto de Inflexão\n(~2035)', ('2035*', 38.5), textcoords='offset points', xytext=(-25, 20), 
                     ha='center', color=ACCENT_CORAL, fontweight='bold', fontsize=10,
                     arrowprops=dict(arrowstyle='->', color=ACCENT_CORAL, lw=1.5))
        
    fig.text(0.5, 0.31, 'Projeções indicam empate técnico por volta de 2035!', ha='center', fontsize=15, fontweight='bold', color=ACCENT_YELLOW)
    fig.text(0.5, 0.26, 'Católicos caíram de 89% para metade da população', ha='center', fontsize=13, color=TEXT_MUTED)
    fig.text(0.5, 0.21, 'Fonte: Séries Censos / CEM-USP | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-091/assets/scene2.png')

def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'PERFIL SOCIODEMOGRÁFICO (DATAFOLHA)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A FORÇA NAS PERIFERIAS', ha='center', fontsize=33, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'ONDE O CRESCIMENTO É MAIS INTENSO', ha='center', fontsize=14, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, 'METRÓPOLES', ha='center', fontsize=48, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.50, 'Forte presença feminina e nas faixas de menor renda!', ha='center', fontsize=15, color=TEXT_MAIN)
    
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-091/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
