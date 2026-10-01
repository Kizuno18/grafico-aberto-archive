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
    
    fig.text(0.5, 0.88, 'CONSUMO GLOBAL DE CAFÉ (ABIC/ICO)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'OS BEBEDORES DE CAFÉ', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O Brasil como o 2º maior consumidor do mundo', ha='center', fontsize=20, color=ACCENT_YELLOW)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_YELLOW, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'CONSUMO INTERNO NACIONAL', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '22 MI SACAS', ha='center', fontsize=60, fontweight='heavy', color=ACCENT_YELLOW)
    fig.text(0.5, 0.44, 'Atrás apenas dos Estados Unidos no consumo!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Associação Brasileira de Café (ABIC)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-077/assets/scene1.png')

def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'DESTINO DA SAFRA BRASILEIRA (CONAB)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'EXPORTAÇÃO VS CONSUMO', ha='center', fontsize=32, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    destinos = ['Exportação', 'Consumo Interno']
    sacas = [35.0, 22.0]
    colors = [ACCENT_BLUE, ACCENT_YELLOW]
    bars = sub_ax.bar(destinos, sacas, color=colors, width=0.45, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 45)
    sub_ax.set_ylabel('Milhões de Sacas de 60 kg', color=TEXT_MUTED, fontsize=11)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=11)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 1.0, f'{yval:.0f} mi sacas', ha='center', 
                    color=TEXT_MAIN, fontsize=13, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Quarenta por cento de toda a safra é bebida aqui!', ha='center', fontsize=16, fontweight='bold', color=ACCENT_YELLOW)
    fig.text(0.5, 0.28, 'O café está presente em mais de 98% dos lares brasileiros', ha='center', fontsize=13, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Conab / ABIC | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-077/assets/scene2.png')

def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'HÁBITO COTIDIANO (ABIC)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O FAMOSO CAFEZINHO', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'CONSUMO MÉDIO POR PESSOA / ANO', ha='center', fontsize=14, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '~ 1.000 XÍCARAS', ha='center', fontsize=50, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.50, 'A bebida mais consumida no Brasil depois da água!', ha='center', fontsize=15, color=TEXT_MAIN)
    
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-077/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
