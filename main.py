import pygame
import Game


def main():

    game_surface_size = (720, 640)
    button_image_paths = ["images/blue_square.png",
                          "images/green_square.png",
                          "images/orange_square.png",
                          "images/red_square.png"]

    new_game = Game.Game()
    new_game.on_execute()

    # setup the game logo
    # game_logo = pygame.image.load("images/logo.png")
    # pygame.display.set_icon(game_logo)
    # pygame.display.set_caption("Simon")

    # create a game surface using game_surface_size arg
    # screen = pygame.display.set_mode(game_surface_size)
    # blit_button_images = [pygame.image.load(image_path) for image_path in button_image_paths]


# runs the main function only if the module is executed
# as the main script, if imported then nothing is executed
if __name__ == '__main__':
    main()
