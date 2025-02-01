import time
import pygame

from static import *

WIDTH = 800
HEIGHT = 480
FRAMERATE = 32

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT), pygame.NOFRAME
)

clock = pygame.time.Clock()
running = True

positron = Positron()
positron.bootup()

mouse_start = None
mouse_end = None
mouse_click_start = 0
mouse_time = 0

while running:
    for e in pygame.event.get():

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_ESCAPE:
                running = False
                break

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_start = pygame.mouse.get_pos()
            mouse_click_start = time.time()

        if e.type == pygame.MOUSEBUTTONUP:
            mouse_end = pygame.mouse.get_pos()
            mouse_time = time.time() - mouse_click_start
            mouse_click_start = 0

            mouse_delta = (
                mouse_end[0] - mouse_start[0],
                mouse_end[1] - mouse_start[1],
            )

            if mouse_start[0] > WIDTH - 100 and mouse_delta[0] < -25:
                positron.page += 1
                if positron.page > len(positron._apps):
                    positron.page = 0

            if mouse_start[0] < 100 and mouse_delta[0] < 25:
                positron.page -= 1
                if positron.page < 0:
                    positron.page = len(positron._apps)

    if not running: break

    if positron.app == "bootup":
        if positron.t > FRAMERATE * 5:
            positron.homescreen()

    screen.fill("#000000")

    # if not positron.app:
    #     T = (positron.t if positron.t < FRAMERATE else FRAMERATE) / FRAMERATE
    #     if positron.page > 0:
    #         apps = positron._apps[(positron.page - 1) * 3 : positron.page * 3]
    #         appA = 

    if positron.app == "bootup":
        LOGO = pygame.image.load("system/logo.png")
        LOGO = pygame.transform.scale(LOGO, (256, 256))
        screen.blit(
            LOGO, (
                int(WIDTH / 2 - LOGO.get_width() / 2),
                int(HEIGHT / 2 - LOGO.get_height() / 2),
            )
        )

    positron.tick()
    pygame.display.update()
    clock.tick(FRAMERATE)