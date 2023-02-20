import pygame


class Button:
    def __init__(self, x, y, image, scale): # These are each of the a parameters which must be filled when creating a GeneralButton object
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # example width: 1000px * 0.8 = new width of 800px
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def create(self, game):  # To create button on main View class. This function will create the button on the screem (object.draw()) - within draw
        # parameter, use the variable that holds the game display
        action = False
        position = pygame.mouse.get_pos() # if printed on its own, it will continously print the current coordinates of the mouse on the display pane

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # [0] on get_pressed means that left click on mouse
                self.clicked = True # changes the state of being clicked to true
                action = True #runs the action after the click. The action can be anything you want to define on each button object

        if pygame.mouse.get_pressed()[0] == 0: # button not clicked
            self.clicked = False

        game.blit(self.image, (self.rect.x, self.rect.y))

        return action # final output of the button click

# The button class above can be used to create any sort of button you wish. It is a standardised button that you can
# change the size, and scale it up or down with an image. For example, if your image you import is (100 x 80) pixels,
# you can change the scale of the original image to allow flexible image sizes. Default of scale is 1 (the size of
# the import image), below 1 makes it smaller and vice versa
