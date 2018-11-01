#Faça um programa em Py que abra e reproduza o áudio de um arquivo mp3

from pygame import mixer
mixer.init()
mixer.music.load('pm.mp3')
mixer.music.play()
input('Agora você escuta?')
