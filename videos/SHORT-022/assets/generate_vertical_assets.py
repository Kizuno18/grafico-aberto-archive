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
# CENA 1: Gancho 75 Milhões Sem Esgoto
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CENSO DEMOGRÁFICO IBGE', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'SANEAMENTO BÁSICO NO BRASIL', ha='center', fontsize=32, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'Quem ainda vive sem esgoto tratado?', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'SEM ESGOTAMENTO ADEQUADO (IBGE)', ha='center', fontsize=17, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '75 MILHÕES', ha='center', fontsize=52, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'Mais de 37% de toda a população do país!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: IBGE (Censo Demográfico 2022)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-022/assets/scene1.png')

# ==========================================
# CENA 2: Desigualdade Regional de Esgoto
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'REDE DE ESGOTO POR REGIÃO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O ABISMO REGIONAL (IBGE)', ha='center', fontsize=34, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sul', 'Sudeste']
    cobertura = [14.7, 41.3, 58.9, 68.7, 86.2]
    colors = [ACCENT_CORAL, ACCENT_YELLOW, ACCENT_CYAN, ACCENT_BLUE, ACCENT_GREEN]
    bars = sub_ax.barh(regioes, cobertura, color=colors, height=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_xlim(0, 100)
    sub_ax.set_xlabel('% da População com Esgoto Adequado', color=TEXT_MUTED, fontsize=12)
    sub_ax.grid(axis='x', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=12)
    for b in bars:
        w = b.get_width()
        sub_ax.text(w + 1.5, b.get_y() + b.get_height()/2.0, f'{w:.1f}%', va='center', 
                    color=TEXT_MAIN, fontsize=14, fontweight='bold')
        
    fig.text(0.5, 0.33, 'No Norte, menos de 15% têm rede de esgoto!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'No Sudeste, a cobertura supera 86% da população', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IBGE Censo 2022 | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-022/assets/scene2.png')

# ==========================================
# CENA 3: Água Encanada e Conclusão
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'O DESAFIO DA ÁGUA POTÁVEL', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'SEM ÁGUA ENCANADA', ha='center', fontsize=34, fontweight='bold', color=ACCENT_BLUE)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_BLUE, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'SEM REDE GERAL DE DISTRIBUIÇÃO', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '33,8 MILHÕES', ha='center', fontsize=48, fontweight='heavy', color=ACCENT_BLUE)
    fig.text(0.5, 0.50, 'Dependem de poços, caminhão-pipa ou rios', ha='center', fontsize=16, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_GREEN, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-022/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
