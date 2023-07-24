
import pygame



if __name__ == '__main__':

    SCREEN_HEIGHT = 500
    #check
    SCREEN_WIDTH = 800

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Button Demo')

    bracket = pygame.image.load('Bracket.png').convert_alpha()
    buy_1 = pygame.image.load('Buy.png').convert_alpha()
    sell_1 = pygame.image.load('Sell.png').convert_alpha()
    buy_2 = pygame.image.load('Buy.png').convert_alpha()
    sell_2 = pygame.image.load('Sell.png').convert_alpha()
    buy_3 = pygame.image.load('Buy.png').convert_alpha()
    sell_3 = pygame.image.load('Sell.png').convert_alpha()
    buy_4 = pygame.image.load('Buy.png').convert_alpha()
    sell_4 = pygame.image.load('Sell.png').convert_alpha()
    next_round = pygame.image.load('Next.png').convert_alpha()
    BRACKET_SCALE = (800,500)
    BUTTON_SCALE = (50,40)
    NEXT_SCALE = (180,60)
    #NEXT_SCALE
    buy_1 = pygame.transform.scale(buy_1, BUTTON_SCALE)
    buy_2 = pygame.transform.scale(buy_2, BUTTON_SCALE)
    buy_3 = pygame.transform.scale(buy_3, BUTTON_SCALE)
    buy_4 = pygame.transform.scale(buy_4, BUTTON_SCALE)

    bracket = pygame.transform.scale(bracket, BRACKET_SCALE)


    sell_1 = pygame.transform.scale(sell_1, BUTTON_SCALE)
    sell_2 = pygame.transform.scale(sell_2, BUTTON_SCALE)
    sell_3 = pygame.transform.scale(sell_3, BUTTON_SCALE)
    sell_4 = pygame.transform.scale(sell_4, BUTTON_SCALE)

    next_round = pygame.transform.scale(next_round, NEXT_SCALE)




    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)

        def draw(self):
            #draw button on screen
            screen.blit(self.image, (self.rect.x, self.rect.y))

#create instances

    buy_1_button = Button(60,70,buy_1)
    sell_1_button = Button(210,71, sell_1)

    buy_2_button = Button(60, 140, buy_2)
    sell_2_button = Button(210, 141, sell_2)

    buy_3_button = Button(60, 330, buy_3)
    sell_3_button = Button(210, 331, sell_3)

    buy_4_button = Button(60, 400, buy_4)
    sell_4_button = Button(210, 401, sell_4)

    next_button = Button(597, 420, next_round)

    run = True
    while run:
        screen.fill((202, 228, 241))
        screen.blit(bracket, (0, 0))
        buy_1_button.draw()
        buy_2_button.draw()
        buy_3_button.draw()
        buy_4_button.draw()
        sell_4_button.draw()
        sell_3_button.draw()
        sell_2_button.draw()
        sell_1_button.draw()


        next_button.draw()
        #screen.blit(next_button, (300, self.rect.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()