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
# CENA 1: Gancho Capitais Encolhendo
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CENSO DEMOGRÁFICO IBGE', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'CAPITAIS ENCOLHENDO?', ha='center', fontsize=38, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.77, 'O novo mapa da população brasileira', ha='center', fontsize=22, color=TEXT_MAIN)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'MUDANÇA HISTÓRICA NO BRASIL', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'PELA 1ª VEZ', ha='center', fontsize=52, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'Grandes capitais perderam habitantes', ha='center', fontsize=20, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: IBGE (Censo 2022 vs 2010)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-005/assets/scene1.png')

# ==========================================
# CENA 2: As Capitais que Mais Encolheram
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'QUEDA POPULACIONAL (2010 A 2022)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'AS CAPITAIS QUE ENCOLHERAM', ha='center', fontsize=34, fontweight='bold', color=ACCENT_CORAL)
    
    sub_ax = fig.add_axes([0.18, 0.40, 0.68, 0.34], facecolor=CARD_COLOR)
    capitais = ['Rio de Janeiro', 'Porto Alegre', 'Belém', 'Natal', 'Salvador']
    perdas = [1.7, 5.4, 6.5, 6.5, 9.6]
    bars = sub_ax.barh(capitais, perdas, color=ACCENT_CORAL, height=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_xlim(0, 12)
    sub_ax.set_xlabel('Perda de População (%)', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='x', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=15)
    for b in bars:
        w = b.get_width()
        sub_ax.text(w + 0.3, b.get_y() + b.get_height()/2.0, f'-{w:.1f}%', va='center', 
                    color=TEXT_MAIN, fontsize=16, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Salvador perdeu 258 mil pessoas!', ha='center', fontsize=22, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'Porto Alegre: -76 mil | Rio de Janeiro: -109 mil', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IBGE Censo Demográfico 2022 | Gráfico Aberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-005/assets/scene2.png')

# ==========================================
# CENA 3: Para Onde Vão e Conclusão
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'PARA ONDE OS BRASILEIROS VÃO?', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A EXPLOSÃO DO CENTRO-OESTE', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'CRESCIMENTO ANUAL (CENSO 2022)', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.60, '+1,23%', ha='center', fontsize=52, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.52, 'A maior taxa de crescimento do Brasil!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-005/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
