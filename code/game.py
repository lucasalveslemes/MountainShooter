#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1º INICIAR O JOGO E CRIANDO A JANELA
import pygame

from code.menu import Menu


class Game:
    def __init__(self):  # nosso construtor

        pygame.init()
        # INICIANDO A JANELA
        # OBS: Ao selecionar o comando e clicar com ctrl da para entrar nele (teste com set_mode)
        self.window = pygame.display.set_mode(size=(600, 400))

    def run(self, ):  # É nosso método de execução
        while True:
            menu = Menu(self.window)  # importante adicionar na classe menu esse parâmetro passado aqui depois de self
            menu.run()
            pass

            # # 2ª EVENTO DE FECHAR A JANELA: Link: pygame.org procurar por event.html
            # # Vamos usar eventos em filas para checar todos os eventos
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # fecha janela
            #         quit()  # finaliza pygame
