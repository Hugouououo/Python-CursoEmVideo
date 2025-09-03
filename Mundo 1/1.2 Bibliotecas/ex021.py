#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame #Usado para fazer jogos no python, e será usado pra tocar áudio.
pygame.init() #Iniciar a biblioteca do Pygame

pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#esse arquivo está sem a música