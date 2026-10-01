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
# CENA 1: Gancho Selic a 45%
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ECONOMIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A MONTANHA-RUSSA DA SELIC', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O histórico dos juros básicos no Brasil', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'MÁXIMA HISTÓRICA DOS JUROS (1999)', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '45,0%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'A taxa Selic bateu 45% ao ano!', ha='center', fontsize=20, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Banco Central do Brasil (Copom)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-011/assets/scene1.png')

# ==========================================
# CENA 2: Gráfico Histórico da Selic
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'OS EXTREMOS DA TAXA BÁSICA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DE 45% A 2% AO ANO', ha='center', fontsize=36, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    years = ['1999', '2003', '2012', '2016', '2020', 'Hoje']
    selic_vals = [45.0, 26.5, 7.25, 14.25, 2.0, 11.0]
    sub_ax.plot(years, selic_vals, marker='o', linewidth=3.5, markersize=10, color=ACCENT_CORAL)
    sub_ax.fill_between(years, selic_vals, color=ACCENT_CORAL, alpha=0.15)
    sub_ax.set_ylim(0, 52)
    sub_ax.set_ylabel('Taxa Selic (% a.a.)', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(True, linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=13)
    for i, v in enumerate(selic_vals):
        sub_ax.text(i, v + 2.0, f'{v:.1f}%', ha='center', color=TEXT_MAIN, fontsize=14, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Em 2020 foi a 2% | Hoje voltou para 2 dígitos', ha='center', fontsize=18, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'Uma das maiores oscilações de juros do planeta', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Banco Central do Brasil — SGS 432', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-011/assets/scene2.png')

# ==========================================
# CENA 3: Conclusão Juro Real
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'O JURO REAL DO BRASIL', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'UM DOS MAIORES DO MUNDO', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'JURO REAL (DESCONTADA A INFLAÇÃO)', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.60, '6% A 7% a.a.', ha='center', fontsize=48, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.52, 'Brasil lidera ranking global de juro real', ha='center', fontsize=16, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-011/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
