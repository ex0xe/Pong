
import pygame

# Initializes all imported pygame modules
pygame.init()

"""
TODO:
players can only move till edge of screen
"""

pygame.display.set_caption("Pong")

# Variable for later use of width and height of the screen
infoObject = pygame.display.Info()


WIDTH, HEIGHT = 1920, 1080
FPS = 60
PLAYER_VEL = 6
BALL_VEL_X = 15
BALL_VEL_Y = 1
CIRCLE_RADIUS = 10

# Set window size to screen width and height
window = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))


def main(window, BALL_VEL_X, BALL_VEL_Y):
    #
    clock = pygame.time.Clock()

    # Define 
    rectOne = pygame.Rect(infoObject.current_w - infoObject.current_w, infoObject.current_h // 2.5, 20, infoObject.current_h // 8)
    rectTwo = pygame.Rect(infoObject.current_w - 20, infoObject.current_h / 2.5, 20, infoObject.current_h // 8)
    #print(infoObject.current_h)
    rectUpperPart = [*range(0, infoObject.current_h // 8 // 2, 1)]
    rectLowerPart = [*range(infoObject.current_h // 8 // 2, infoObject.current_h // 8, 1)]
    #print(rectOneUpperPart)
    #print(rectOneLowerPart)
    circleBall = pygame.Rect(
        infoObject.current_w // 2 - CIRCLE_RADIUS,
        infoObject.current_h // 2 - CIRCLE_RADIUS,
        2 * CIRCLE_RADIUS,
        2 * CIRCLE_RADIUS,
    )

    run = True
    while run:
        clock.tick(FPS)

        circleBall.move_ip(BALL_VEL_X, BALL_VEL_Y)           

        if circleBall.colliderect(rectTwo):
            BALL_VEL_X = -BALL_VEL_X
            #print(circleBall.collidepoint(rectTwo.x, rectTwo.y))
            BALL_VEL_Y = -BALL_VEL_Y if circleBall.y < rectTwo.y + infoObject.current_h // 8 / 2 else BALL_VEL_Y
            

        if circleBall.colliderect(rectOne):
            BALL_VEL_X = abs(BALL_VEL_X)

            collision_point_y = circleBall.y
            if collision_point_y < rectOne.y + infoObject.current_h // 8 / 2:
                BALL_VEL_Y = -BALL_VEL_Y
            elif collision_point_y > rectOne.y + infoObject.current_h // 8 / 2:
                BALL_VEL_Y = abs(BALL_VEL_Y)

        if circleBall.y - CIRCLE_RADIUS < 0 or circleBall.y + CIRCLE_RADIUS > infoObject.current_h:
            BALL_VEL_Y = -BALL_VEL_Y

        if circleBall.x - CIRCLE_RADIUS < 0 or circleBall.x + CIRCLE_RADIUS > infoObject.current_w:
            run = False
            
            
        window.fill((0, 0, 0))

        pygame.draw.circle(window, (255, 255, 255), circleBall.center, CIRCLE_RADIUS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            rectOne.y += PLAYER_VEL
        if keys[pygame.K_w]:
            rectOne.y -= PLAYER_VEL
        if keys[pygame.K_DOWN]:
            rectTwo.y += PLAYER_VEL
        if keys[pygame.K_UP]:
            rectTwo.y -= PLAYER_VEL

        pygame.draw.rect(window, (255, 255, 255), rectOne)
        pygame.draw.rect(window, (255, 255, 255), rectTwo)

        pygame.display.flip()

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window, BALL_VEL_X, BALL_VEL_Y)
