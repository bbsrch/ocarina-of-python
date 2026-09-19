import pygame
from musicas import musicas, arquivos_musicas, imagens_musicas, cores_musicas
from sons import sons, sons_oitava, nomes_notas, nomes_exibicao
from tempos import tempos_musicas

pygame.init()

janela = pygame.display.set_mode((600, 650))
pygame.display.set_caption("Ocarina of Python")
imagem = pygame.image.load("assets/mapa_teclado_dark.png")
imagem = pygame.transform.scale(imagem, (500, 250))
fonte = pygame.font.SysFont("Trebuchet MS", 32, bold=True)
fonte_modos = pygame.font.SysFont("Trebuchet MS", 12)
fonte_livro = pygame.font.SysFont("Trebuchet MS", 18, bold=True)
reconhecimento = pygame.mixer.Sound("sounds/ocarina.wav")
EVENTO_MUSICA = pygame.USEREVENT + 1
EVENTO_NOTA = pygame.USEREVENT + 2
modo = "livre"
nota_atual = ""
musica_reconhecida = ""
imagem_musica = None
cor_musica = (255, 255, 255)
som_musica = None
sequencia = []
sequencia_exibida = []
indice_nota = 0
tempos_atuais = []
livro_aberto = False

def verificar_musica(sequencia): # Procura uma música cuja sequência tocada seja exatamente igual
    for nome, notas in musicas.items():
        if sequencia == notas:
            return nome
    return None

def verificar_sequencia(sequencia): # Verifica se a 'sequencia' AINDA pode ser o começo de uma música
    for notas in musicas.values():          # 
        if len(sequencia) <= len(notas):
            if sequencia == notas[:len(sequencia)]:
                return True
    # Se passou do comprimento máximo ou não bate com nenhuma sequência retorna False
    return False   

def encontrar_sequencia_valida(sequencia): # Procura o maior trecho final da sequência que ainda pode ser o começo de uma música
    for inicio in range(len(sequencia)):
        tentativa = sequencia[inicio:]
        for notas in musicas.values():
            if len(tentativa) <= len(notas):
                if tentativa == notas[:len(tentativa)]:
                    return tentativa
    return []

def desenhar_livro():  # Livro de canções
    janela.fill((30, 30, 30))

    titulo = fonte_livro.render(
        "LIVRO DE CANÇÕES",
        True,
        (255, 255, 255)
    )

    janela.blit(titulo, (30, 30))

    lista_musicas = list(musicas.items())

    # Divide as 12 músicas em duas listas de 6
    coluna_esquerda = lista_musicas[:6]
    coluna_direita = lista_musicas[6:]

    for x, coluna in [(30, coluna_esquerda), (310, coluna_direita)]:

        y = 100

        for nome, notas in coluna:

            texto_nome = fonte_livro.render(
                nome,
                True,
                cores_musicas[nome]
            )

            janela.blit(texto_nome, (x, y))

            sequencia_notas = "  ".join(
                nomes_exibicao[nota]
                for nota in notas
            )

            texto_notas = fonte_livro.render(
                sequencia_notas,
                True,
                (200, 200, 200)
            )

            texto_sair = fonte_modos.render(
                "[3] ou [ESC] para sair",
                True,
                (128, 128, 128)
            )

            janela.blit(texto_sair, (470, 10))
            janela.blit(texto_notas, (x, y + 30))

            y += 85

def desenhar_interface(): # Desenha a interface atual   
    janela.fill((30, 30, 30))
    if modo == "livre":
        texto_modol = fonte_modos.render(
            ">[1] MODO LIVRE<",
            True,
            (157, 0, 255)
        )
        retangulo_modol = texto_modol.get_rect(center=(60, 15))
        janela.blit(texto_modol, retangulo_modol)

        texto_modom = fonte_modos.render(
            "[2] MODO MÚSICAS",
            True,
            (128, 128, 128)
        )
        retangulo_modom = texto_modom.get_rect(center=(170, 15))
        janela.blit(texto_modom, retangulo_modom)

        texto_livro = fonte_modos.render(
            "[3] LIVRO DE CANÇÕES",
            True,
            (255, 255, 0)
        )
        retangulo_livro = texto_livro.get_rect(center=(530, 15))
        janela.blit(texto_livro, retangulo_livro)

    elif modo == "musicas":
        texto_modom = fonte_modos.render(
            ">[2] MODO MÚSICAS<",
            True,
            (157, 0, 255)
        )
        retangulo_modom = texto_modom.get_rect(center=(170, 15))
        janela.blit(texto_modom, retangulo_modom)

        texto_modol = fonte_modos.render(
            "[1] MODO LIVRE",
            True,
            (128, 128, 128)
        )
        retangulo_modol = texto_modol.get_rect(center=(60, 15))
        janela.blit(texto_modol, retangulo_modol)

        texto_livro = fonte_modos.render(
            "[3] LIVRO DE CANÇÕES",
            True,
            (255, 255, 0)
        )
        retangulo_livro = texto_livro.get_rect(center=(530, 15))
        janela.blit(texto_livro, retangulo_livro)

    janela.blit(imagem, (50, 380))

    if imagem_musica:
        retangulo_imagem = imagem_musica.get_rect(center=(300, 200))
        janela.blit(imagem_musica, retangulo_imagem)

    if musica_reconhecida:
        texto_musica = fonte.render(
            musica_reconhecida,
            True,
            cor_musica
        )
        retangulo_musica = texto_musica.get_rect(center=(300, 60))
        janela.blit(texto_musica, retangulo_musica)

    if musica_reconhecida:
        texto_sequencia = fonte.render(
            "  ".join(nomes_exibicao[nota] for nota in sequencia_exibida),
            True,
            cor_musica
        )
        retangulo_sequencia = texto_sequencia.get_rect(center=(300, 350))
        janela.blit(texto_sequencia, retangulo_sequencia)

    elif nota_atual:
        texto_nota = fonte.render(
            nomes_exibicao[nota_atual],
            True,
            (157, 0, 255)
        )
        retangulo_nota = texto_nota.get_rect(center=(300, 350))
        janela.blit(texto_nota, retangulo_nota)

rodando = True
while rodando:

    if livro_aberto:
        desenhar_livro()
    else:
        desenhar_interface()
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN: # Tudo relacionado ao teclado
            pygame.time.set_timer(EVENTO_MUSICA, 0)
            pygame.time.set_timer(EVENTO_NOTA, 0)
            shift = pygame.key.get_mods() & pygame.KMOD_SHIFT

            if evento.key == pygame.K_3:
                livro_aberto = not livro_aberto
                pygame.mixer.stop()
                sequencia = []
                musica_reconhecida = ""
                imagem_musica = None

            elif evento.key == pygame.K_ESCAPE:
                livro_aberto = False

            elif not livro_aberto:
                if evento.key == pygame.K_1:
                    modo = "livre"
                    sequencia = []
                    musica_reconhecida = ""
                    imagem_musica = None
                    pygame.mixer.stop()
                    print("Modo Livre")

                elif evento.key == pygame.K_2:
                    modo = "musicas"
                    sequencia = []
                    musica_reconhecida = ""
                    imagem_musica = None
                    pygame.mixer.stop()
                    print("Modo Músicas")

                if shift and evento.key in sons_oitava: # SE o Shift estiver pressionado = oitava maior
                    pygame.mixer.stop()
                    sons_oitava[evento.key].play()

                elif evento.key in sons:                # SENÃO estiver pressionado = oitava normal
                    pygame.mixer.stop()
                    sons[evento.key].play()

                if evento.key in nomes_notas:
                    if musica_reconhecida:
                        sequencia = []
                    shift = pygame.key.get_mods() & pygame.KMOD_SHIFT
                    nota = nomes_notas[evento.key]
                    if shift:
                        nota = nota + "8"
                    print(nota)             # Mostra a última nota tocada

                    nota_atual = nota
                    musica_reconhecida = ""
                    imagem_musica = None

                    desenhar_interface()
                    pygame.display.flip()

                    if modo == "musicas":
                        sequencia.append(nota)  # Adiciona a nota tocada na lista "sequencia"
                        if not verificar_sequencia(sequencia):
                            sequencia = encontrar_sequencia_valida(sequencia)
                            # Verifica se algum trecho da sequência inicia uma música, senão reinicia   
                                
                        musica = verificar_musica(sequencia)

                        if musica:
                            musica_reconhecida = musica
                            reconhecimento.play()

                            cor_musica = cores_musicas[musica]
                            imagem_musica = pygame.image.load(imagens_musicas[musica])
                            som_musica = pygame.mixer.Sound(arquivos_musicas[musica])
                            largura = 400
                            altura = int(imagem_musica.get_height() * largura / imagem_musica.get_width())
                            imagem_musica = pygame.transform.scale(
                                imagem_musica,
                                (largura, altura)
                            )

                            sequencia_exibida = [sequencia[0]]
                            indice_nota = 1
                            tempos_atuais = tempos_musicas[musica]
                            pygame.time.set_timer(EVENTO_NOTA, tempos_atuais[0])

                            pygame.time.set_timer(EVENTO_MUSICA, 1000)

        elif evento.type == EVENTO_MUSICA: # Toca a música depois de 1 segundo
            pygame.time.set_timer(EVENTO_MUSICA, 0)
            som_musica.play()

        elif evento.type == EVENTO_NOTA:
            if musica_reconhecida:
                if indice_nota < len(musicas[musica_reconhecida]):

                    sequencia_exibida.append(musicas[musica_reconhecida][indice_nota])
                    indice_nota += 1

                    if indice_nota < len(musicas[musica_reconhecida]):
                        pygame.time.set_timer(EVENTO_NOTA,tempos_atuais[indice_nota - 1])
                    else:
                        pygame.time.set_timer(EVENTO_NOTA, 0)

        elif evento.type == pygame.QUIT:
            rodando = False
pygame.quit()