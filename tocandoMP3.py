import pygame

pygame.init()
pygame.mixer.music.load('lugar_distante.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()