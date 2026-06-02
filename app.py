import pygame

pygame.mixer.init()

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

if __name__ == "__main__":
    print("Music App Ready")
