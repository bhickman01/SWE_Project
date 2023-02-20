import pygame
from constants import *  # Do NOT remove. Idk why it says its unused
from developmentCards import *
from buttons import Button

pygame.init()

game = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Settlers Project")

dev_card_img = pygame.image.load('devbtn.png').convert_alpha()

# Objects from other classes
dev_btn = Button(100, 200, dev_card_img, 0.5)
devCards = DevelopmentCard()


def main():
    run = True
    clock = pygame.time.Clock()
    devcardtotal = 25

    while run:
        clock.tick(FPS)
        game.fill((202, 228, 241))

        if dev_btn.create(game):
            devcardtotal -= 1
            print("clicked", devcardtotal)
            devCards.genDevelopmentCard([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9])

            if devcardtotal == 0:
                print("NO DEVELOPMENT CARDS REMAINING")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


main()
