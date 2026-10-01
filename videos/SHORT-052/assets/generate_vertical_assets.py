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
    
    fig.text(0.5, 0.88, 'FORMAÇÃO CIENTÍFICA (CAPES/MEC)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O SALTO DOS DOUTORES', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'A expansão da pós-graduação no Brasil', ha='center', fontsize=22, color=ACCENT_BLUE)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_BLUE, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'CRESCIMENTO EM 25 ANOS', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '8X MAIS', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_BLUE)
    fig.text(0.5, 0.44, 'De 3 mil para mais de 24 mil por ano!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Geocapes / CGEE / MEC', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-052/assets/scene1.png')

def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'DOUTORES TITULADOS POR ANO (CAPES)', ha='center', fontsize=21, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DE 3 MIL PARA 24 MIL', ha='center', fontsize=32, fontweight='bold', color=ACCENT_YELLOW)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    anos = ['1996', '2006', '2016', '2023']
    doutores = [2.8, 9.4, 20.6, 24.2]
    colors = [TEXT_MUTED, ACCENT_YELLOW, ACCENT_GREEN, ACCENT_CYAN]
    bars = sub_ax.bar(anos, doutores, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 28)
    sub_ax.set_ylabel('Milhares de Doutores/ano', color=TEXT_MUTED, fontsize=12)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=11)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 0.6, f'{yval:.1f}k', ha='center', 
                    color=TEXT_MAIN, fontsize=14, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Salto de quase 800% no número de cientistas!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_CYAN)
    fig.text(0.5, 0.28, 'Brasil atingiu o 13º lugar em produção científica', ha='center', fontsize=14, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Capes / CGEE | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-052/assets/scene2.png')

def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ONDE ELES TRABALHAM? (CGEE)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O PARADOXO DA INDÚSTRIA', ha='center', fontsize=33, fontweight='bold', color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'DESTINO PROFISSIONAL FORMAL', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '70% vs < 2%', ha='center', fontsize=54, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.50, '70% nas Universidades | Menos de 2% nas Indústrias!', ha='center', fontsize=14, color=TEXT_MAIN)
    
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-052/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
