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
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Gancho Menor Cidade do Brasil
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CENSO DEMOGRÁFICO IBGE', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A MENOR CIDADE DO BRASIL', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'Menos habitantes que um único prédio!', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'SERRA DA SAUDADE (MINAS GERAIS)', ha='center', fontsize=17, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '833', ha='center', fontsize=72, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'HABITANTES NO TOTAL', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: IBGE (Censo Demográfico 2022)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-019/assets/scene1.png')

# ==========================================
# CENA 2: Os 3 Menores Municípios
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'OS MENORES MUNICÍPIOS (IBGE)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'MENOS DE 1.000 MORADORES', ha='center', fontsize=32, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    cidades = ['Anhanguera (GO)', 'Borá (SP)', 'Serra da S. (MG)']
    pop = [924, 907, 833]
    colors = [ACCENT_BLUE, ACCENT_CYAN, ACCENT_CORAL]
    bars = sub_ax.bar(cidades, pop, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 1150)
    sub_ax.set_ylabel('População Residente', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=12)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 30, f'{yval}', ha='center', 
                    color=TEXT_MAIN, fontsize=18, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Apenas 3 cidades no Brasil têm < 1.000 pessoas!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'Mais de 1.200 cidades têm menos de 5.000 habitantes', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IBGE Censo 2022 | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-019/assets/scene2.png')

# ==========================================
# CENA 3: O Contraste com São Paulo
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'A DESIGUALDADE URBANA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O CONTRASTE DOS EXTREMOS', ha='center', fontsize=32, fontweight='bold', color=ACCENT_GREEN)
    
    # 2 Cards Grandes de Contraste
    c1 = plt.Rectangle((0.12, 0.54), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c1)
    fig.text(0.5, 0.70, 'A MENOR CIDADE (SERRA DA SAUDADE)', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.62, '833 PESSOAS', ha='center', fontsize=38, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.56, 'População menor que um condomínio de SP', ha='center', fontsize=15, color=TEXT_MAIN)
    
    c2 = plt.Rectangle((0.12, 0.30), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_BLUE, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c2)
    fig.text(0.5, 0.46, 'A MAIOR CIDADE (SÃO PAULO CAPITAL)', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.38, '11,4 MILHÕES', ha='center', fontsize=38, fontweight='heavy', color=ACCENT_BLUE)
    fig.text(0.5, 0.32, 'Equivale a 13.700 Serras da Saudade juntas!', ha='center', fontsize=15, color=TEXT_MAIN)
    
    # CTA Card
    fig.text(0.5, 0.21, '@ograficoaberto | Gráfico Aberto', ha='center', fontsize=18, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.16, 'Inscreva-se para ver as curiosidades em dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-019/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()

