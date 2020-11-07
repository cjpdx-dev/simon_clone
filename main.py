import pygame


def main():

    game_surface_size = (440, 380)

    # init the pygame module
    pygame.init()

    # setup the game logo
    game_logo = pygame.image.load("images/logo.png")
    pygame.display.set_icon(game_logo)
    pygame.display.set_caption("Simon")

    # create a game surface using game_surface_size arg
    screen = pygame.display.set_mode(game_surface_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


# runs the main function only if the module is executed
# as the main script, if imported then nothing is executed
if __name__ == '__main__':
    main()
