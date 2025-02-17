#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1º INICIAR O JOGO E CRIANDO A JANELA
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):  # nosso construtor

        pygame.init()
        # INICIANDO A JANELA
        # OBS: Ao selecionar o comando e clicar com ctrl da para entrar nele (teste com set_mode)
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):  # É nosso método de execução

        while True:
            menu = Menu(self.window)  # importante adicionar na classe menu esse parâmetro passado aqui após de self
            menu.run()
            pass

