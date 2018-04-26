# !/usr/bin/env python

import pygame
import time

def main():
    screen = pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load("./feiji/background.png")

    while True:
        screen.blit(background,(0,0))
        pygame.display.update()

    pass


if __name__ == "__main__":
    main()
