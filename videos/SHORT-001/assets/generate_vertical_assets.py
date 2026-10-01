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
# CENA 1: Gancho da Idade Mediana (1080x1920)
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    # Topo (Área visível segura)
    fig.text(0.5, 0.88, 'BRASIL EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O BRASIL ENVELHECEU', ha='center', fontsize=40, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.77, '+6 anos em apenas 12 anos', ha='center', fontsize=24, color=TEXT_MAIN)
    
    # Card Central Gigante
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'IDADE MEDIANA DO BRASILEIRO', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    
    # 2010 vs 2022
    fig.text(0.30, 0.54, '2010\n29 anos', ha='center', fontsize=26, fontweight='bold', color=ACCENT_BLUE)
    fig.text(0.50, 0.54, '➔', ha='center', fontsize=36, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.70, 0.54, '2022\n35 anos', ha='center', fontsize=26, fontweight='bold', color=ACCENT_GREEN)
    
    fig.text(0.5, 0.42, 'Metade da população tem mais de 35 anos', ha='center', fontsize=16, color=TEXT_MAIN)
    
    # Rodapé informativo
    fig.text(0.5, 0.28, 'Fonte oficial: IBGE — Censo Demográfico', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    ax.set_xlim(0, 1080)
    ax.set_ylim(0, 1920)
    save_vertical(fig, 'videos/SHORT-001/assets/scene1.png')

# ==========================================
# CENA 2: Queda da Base Jovem (1080x1920)
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CRIANÇAS E JOVENS (0 A 14 ANOS)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A BASE DA PIRÂMIDE ENCOLHEU', ha='center', fontsize=36, fontweight='bold', color=ACCENT_BLUE)
    
    # Gráfico de barras central
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    bars = sub_ax.bar(['1980', '2010', '2022'], [38.2, 24.1, 19.8], 
                      color=[ACCENT_BLUE, '#485460', ACCENT_CORAL], width=0.55, edgecolor='#233244', lw=2)
    sub_ax.set_ylim(0, 48)
    sub_ax.set_ylabel('% da População', color=TEXT_MUTED, fontsize=14)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=16)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 1.2, f'{yval:.1f}%', ha='center', 
                    color=TEXT_MAIN, fontsize=18, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Caiu pela metade em 4 décadas', ha='center', fontsize=22, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'Taxa de fecundidade caiu para menos de 1,6 filhos por mulher', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IBGE Censos Demográficos | Gráfico Aberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-001/assets/scene2.png')

# ==========================================
# CENA 3: A Explosão dos Idosos (1080x1920)
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ÍNDICE DE ENVELHECIMENTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A EXPLOSÃO DE IDOSOS NO PAÍS', ha='center', fontsize=36, fontweight='bold', color=ACCENT_CORAL)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    years = ['1980', '2000', '2010', '2022']
    vals = [10.5, 19.8, 30.7, 55.2]
    bars = sub_ax.bar(years, vals, color=['#576574', '#576574', ACCENT_BLUE, ACCENT_CORAL], width=0.55, edgecolor='#233244', lw=2)
    sub_ax.set_ylim(0, 68)
    sub_ax.set_ylabel('Idosos para cada 100 crianças', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=16)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 1.5, f'{yval:.1f}', ha='center', 
                    color=TEXT_MAIN, fontsize=18, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Hoje: 55 idosos para cada 100 crianças', ha='center', fontsize=22, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'Em 1980 eram apenas 10 idosos para 100 crianças', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IBGE Censo 2022 | Gráfico Aberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-001/assets/scene3.png')

# ==========================================
# CENA 4: Conclusão e CTA (1080x1920)
# ==========================================
def make_scene4():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'FIM DO BÔNUS DEMOGRÁFICO', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.81, 'O FUTURO DO BRASIL EM NÚMEROS', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    # 3 Bullet Points em cards
    points = [
        ("ESCOLA", "Menos matrículas e salas fechando", ACCENT_BLUE, 0.65),
        ("TRABALHO", "Força de trabalho vai encolher", ACCENT_GREEN, 0.51),
        ("PREVIDÊNCIA", "Mais de 32 milhões acima de 60 anos", ACCENT_CORAL, 0.37)
    ]
    for tag, desc, col, ypos in points:
        box = plt.Rectangle((0.12, ypos), 0.76, 0.11, facecolor=CARD_COLOR, edgecolor=col, 
                            linewidth=2.5, transform=fig.transFigure, zorder=2)
        fig.patches.append(box)
        fig.text(0.16, ypos + 0.07, tag, fontsize=15, fontweight='bold', color=col)
        fig.text(0.16, ypos + 0.03, desc, fontsize=16, color=TEXT_MAIN)
        
    # CTA Card
    cta_box = plt.Rectangle((0.12, 0.18), 0.76, 0.13, facecolor='#111A24', edgecolor=ACCENT_GREEN, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.26, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.21, 'Inscreva-se para ver os dados reais do país', ha='center', fontsize=15, color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-001/assets/scene4.png')

make_scene1()
make_scene2()
make_scene3()
make_scene4()
