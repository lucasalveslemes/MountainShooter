#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window

    # Tem nas documentações do pygame
        # CARREGANDO AS IMAGENS
        self.surf = pygame.image.load('./asset/bg.png')
        # Criando o retângulo para adicionar a imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # left zero pq começa no canto esquerdo

        # Precisamos atualizar a imagem agora no run()
    def run(self, ):
        # ADICIONANDO SOM (Tem na biblioteca do pygame)
        pygame.mixer_music.load('./asset/fase1.mp3')
        pygame.mixer_music.play(-1)  # Serve para tocar a música. (-1 toca infinitamente)

        while True:  # Looping infinito da imagem e texto
            # Dizendo que a imagem deve aparecer no retângulo infinitamente
            self.window.blit(source=self.surf, dest=self.rect)
            # Escrevendo o texto
            self.menu_text(text_size=50, text="Mountain", text_color=C_ORANGE,  # Adicionamos essa cor no arquivo Const
                           text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="Shooter", text_color=C_ORANGE,
                           text_center_pos=((WIN_WIDTH / 2), 120))  # lembrar que a esquerda superior da tela é 00

            for i in range(len(MENU_OPTION)):  # ITERAMOS ATE O TAMANHO DO NOSSO MENU_OPTION (TEM CINCO)
                if i == MENU_OPTION:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i)) # QUANDO ITERAMOS ELE FAZ UM PRINT
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            # Agora atualizando a imagem
            pygame.display.flip()

            # 2ª EVENTO DE FECHAR A JANELA: Link: pygame.org procurar por event.html
            # Vamos usar eventos em filas para checar todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha janela
                    quit()  # finaliza pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)  # Fontes que vamos usar
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Renderizando como imagem para texto (surf)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
