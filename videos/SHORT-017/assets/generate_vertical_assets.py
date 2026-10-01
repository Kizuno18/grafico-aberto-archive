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
# CENA 1: Gancho 7% ou 25%?
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ECONOMIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O PESO DO AGRO NO BRASIL', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, '7% ou 25% do PIB? Entenda os dados', ha='center', fontsize=22, color=ACCENT_GREEN)
    
    # 2 Cards Grandes
    c1 = plt.Rectangle((0.12, 0.54), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_BLUE, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c1)
    fig.text(0.5, 0.70, 'IBGE (SÓ DENTRO DA PORTEIRA)', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.62, '~7% DO PIB', ha='center', fontsize=44, fontweight='heavy', color=ACCENT_BLUE)
    fig.text(0.5, 0.56, 'Apenas a colheita e criação primária', ha='center', fontsize=16, color=TEXT_MAIN)
    
    c2 = plt.Rectangle((0.12, 0.30), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c2)
    fig.text(0.5, 0.46, 'CEPEA/USP (CADEIA COMPLETA)', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.38, '~25% DO PIB', ha='center', fontsize=44, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.32, 'Máquinas, alimentos, transporte e portos', ha='center', fontsize=16, color=TEXT_MAIN)
    
    fig.text(0.5, 0.21, '@ograficoaberto | Gráfico Aberto', ha='center', fontsize=18, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.16, 'Fontes: IBGE Contas Nacionais & CEPEA-Esalq/USP', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-017/assets/scene1.png')

# ==========================================
# CENA 2: Decomposição da Cadeia
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'A CADEIA DO AGRONEGÓCIO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DE ONDE VÊM OS 25%? (USP)', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    setores = ['Insumos\n(Química/Máquinas)', 'Agroindústria\n(Alimentos/Carnes)', 'Agropecuária\n(Campo)', 'Agrosserviços\n(Logística/Portos)']
    shares = [4.0, 6.0, 7.0, 8.0]
    colors = [ACCENT_CORAL, ACCENT_BLUE, ACCENT_GREEN, ACCENT_CYAN]
    bars = sub_ax.bar(setores, shares, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 11)
    sub_ax.set_ylabel('% do PIB Brasileiro', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=11)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 0.3, f'{yval:.0f}%', ha='center', 
                    color=TEXT_MAIN, fontsize=16, fontweight='bold')
        
    fig.text(0.5, 0.33, 'A soma das 4 etapas forma 25% do PIB nacional!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'O campo movimenta fábricas, estradas e bancos', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Centro de Estudos Avançados em Economia Aplicada (USP)', ha='center', fontsize=13, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-017/assets/scene2.png')

# ==========================================
# CENA 3: Balança Comercial e Conclusão
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'O MOTOR DAS EXPORTAÇÕES', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'METADE DAS VENDAS EXTERNAS', ha='center', fontsize=30, fontweight='bold', color=ACCENT_CYAN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CYAN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'EXPORTAÇÕES BRASILEIRAS (MDIC)', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '~50%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_CYAN)
    fig.text(0.5, 0.50, 'De tudo o que o Brasil vende pro mundo vem do agro', ha='center', fontsize=16, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-017/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
