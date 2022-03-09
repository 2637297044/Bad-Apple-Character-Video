import pygame
import time
import os
from pathlib import Path

os.system("title Bad Apple 音乐程序")

BGM_PATH = "data/bgm.mp3"

if not Path(BGM_PATH).exists():
    print("音乐不存在: ", BGM_PATH)

pygame.mixer.init()
track = pygame.mixer.music.load(BGM_PATH)
pygame.mixer.music.play()

time.sleep(220)
