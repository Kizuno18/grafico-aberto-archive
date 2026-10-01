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
# CENA 1: Gancho 6 filhos -> 1,6 filho
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'BRASIL EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A QUEDA DA FECUNDIDADE', ha='center', fontsize=36, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'Número médio de filhos por mulher', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    # Card Central
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'TAXA DE FECUNDIDADE TOTAL (IBGE)', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.30, 0.54, '1960\n6,3', ha='center', fontsize=32, fontweight='bold', color=ACCENT_BLUE)
    fig.text(0.50, 0.54, '➔', ha='center', fontsize=36, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.70, 0.54, 'Hoje\n1,57', ha='center', fontsize=32, fontweight='bold', color=ACCENT_CORAL)
    
    fig.text(0.5, 0.42, 'QUEDA DE 75% EM 6 DÉCADAS', ha='center', fontsize=20, fontweight='bold', color=ACCENT_CORAL)
    
    fig.text(0.5, 0.28, 'Fonte oficial: IBGE (Censos Demográficos)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-004/assets/scene1.png')

# ==========================================
# CENA 2: A Curva Histórica de Fecundidade
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'EVOLUÇÃO HISTÓRICA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'FILHOS POR MULHER NO BRASIL', ha='center', fontsize=34, fontweight='bold', color=ACCENT_BLUE)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    years = ['1960', '1980', '2000', '2022']
    rates = [6.28, 4.07, 2.38, 1.57]
    bars = sub_ax.bar(years, rates, color=[ACCENT_BLUE, '#485460', ACCENT_CYAN, ACCENT_CORAL], width=0.55, edgecolor='#233244', lw=2)
    sub_ax.axhline(y=2.1, color=ACCENT_GREEN, linestyle=':', linewidth=3, label='Reposição (2,1)')
    sub_ax.set_ylim(0, 7.5)
    sub_ax.set_ylabel('Filhos por Mulher', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=16)
    sub_ax.legend(loc='upper right', frameon=True, facecolor='#111A24', edgecolor='#233244', labelcolor=TEXT_MAIN, fontsize=12)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 0.2, f'{yval:.2f}', ha='center', 
                    color=TEXT_MAIN, fontsize=17, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Abaixo da taxa de reposição populacional!', ha='center', fontsize=19, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'Para a população não encolher, a taxa mínima é 2,1', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IBGE Censos Demográficos | Gráfico Aberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-004/assets/scene2.png')

# ==========================================
# CENA 3: Conclusão e CTA
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'MENOS NASCIMENTOS', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O BRASIL DO AMANHÃ', ha='center', fontsize=36, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'NASCIMENTOS REGISTRADOS NO ANO', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.60, '< 2,6 MILHÕES', ha='center', fontsize=44, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.52, 'Menor patamar em mais de 40 anos!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_GREEN, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-004/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
