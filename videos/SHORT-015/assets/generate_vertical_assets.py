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
# CENA 1: Gancho 60% Acesso Exclusivo por Celular
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'TECNOLOGIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'INTERNET SÓ NO CELULAR?', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O Brasil conectado na palma da mão', ha='center', fontsize=22, color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'ACESSO EXCLUSIVO PELO SMARTPHONE', ha='center', fontsize=17, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '+60%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.44, 'Navegam na internet sem nenhum computador!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: IBGE (PNAD Contínua TIC)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-015/assets/scene1.png')

# ==========================================
# CENA 2: Dispositivos de Acesso (Celular vs TV vs PC)
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'DISPOSITIVOS MAIS USADOS (IBGE)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'COMO O BRASIL CONECTA?', ha='center', fontsize=34, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    devices = ['Tablet', 'Computador (PC)', 'Smart TV', 'Celular']
    shares = [9.9, 35.5, 44.4, 99.0]
    colors = ['#576574', ACCENT_CORAL, ACCENT_BLUE, ACCENT_GREEN]
    bars = sub_ax.barh(devices, shares, color=colors, height=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_xlim(0, 115)
    sub_ax.set_xlabel('% dos Usuários de Internet', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='x', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=13)
    for b in bars:
        w = b.get_width()
        sub_ax.text(w + 1.5, b.get_y() + b.get_height()/2.0, f'{w:.1f}%', va='center', 
                    color=TEXT_MAIN, fontsize=15, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Internet em 92,5% dos lares (69 milhões de casas)!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'O celular superou todos os outros aparelhos juntos', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IBGE PNAD Contínua TIC | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-015/assets/scene2.png')

# ==========================================
# CENA 3: A Janela Digital do País
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'A REALIDADE DO BRASIL', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A JANELA DIGITAL DO PAÍS', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    # 3 Cards explicativos
    points = [
        ("BANCO E PAGAMENTOS", "Pix e contas digitais movimentadas só pelo smartphone", ACCENT_GREEN, 0.65),
        ("TRABALHO E FRETE", "Ferramenta essencial de entregas, comércio e vendas", ACCENT_BLUE, 0.51),
        ("ESTUDO E NOTÍCIAS", "Principal fonte de informação e redes da população", ACCENT_CYAN, 0.37)
    ]
    for tag, desc, col, ypos in points:
        box = plt.Rectangle((0.12, ypos), 0.76, 0.11, facecolor=CARD_COLOR, edgecolor=col, 
                            linewidth=2.5, transform=fig.transFigure, zorder=2)
        fig.patches.append(box)
        fig.text(0.16, ypos + 0.07, tag, fontsize=15, fontweight='bold', color=col)
        fig.text(0.16, ypos + 0.03, desc, fontsize=15, color=TEXT_MAIN)
        
    # CTA Card
    cta_box = plt.Rectangle((0.12, 0.18), 0.76, 0.13, facecolor='#111A24', edgecolor=ACCENT_GREEN, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.26, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.21, 'Inscreva-se para ver a realidade dos dados', ha='center', fontsize=15, color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-015/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
