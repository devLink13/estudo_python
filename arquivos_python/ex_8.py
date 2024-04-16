import pygame

pygame.mixer.init()
pygame.mixer.music.load('estudo_python/arquivos_python/music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
