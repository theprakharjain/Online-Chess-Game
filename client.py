import pygame


# Setting window for the game
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


# Setting client Variable
clientNumber = 0


# Setting Player Class
class player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    # To draw the player itself onto its position
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    # Player mover function
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)

# To redraw the playernand update the window after the player moves


def redrawWindow(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True

    # Making Player and giving it attributes
    p = player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        # Initializinng player move function
        p.move()
        # Initializinng player and window update function
        redrawWindow(win, p)


# Initializinng main function
main()
