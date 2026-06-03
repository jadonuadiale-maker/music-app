from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

pygame.mixer.init()

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

if __name__ == "__main__":
    print("Music App Ready")
