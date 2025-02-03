# 1º INICIAR O JOGO E CRIANDO A JANELA
import pygame

print('Setup Start!')
pygame.init()

# INICIANDO A JANELA
# OBS: Ao selecionar o comando e clicar com ctrl da para entrar nele (teste com set_mode)
window = pygame.display.set_mode(size=(600, 400))

print('Setup end!')

# Para que a janela fique aberta utilizamos um loop
print('Loop Start!')
while True:

    # 2ª EVENTO DE FECHAR A JANELA: Link: pygame.org procurar por event.html
    # Vamos usar eventos em filas para checar todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # fecha janela
            quit()  # finaliza pygame
