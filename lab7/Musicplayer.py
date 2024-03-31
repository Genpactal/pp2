import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Music Player')
fps = pygame.time.Clock()

_image_library = dict()
def load_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

list_music = ["di.mp3", "love.mp3", "line.mp3"]
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

current_track = 0
pause = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pause == False:
                    pygame.mixer.music.pause()
                    pause = True
                else:
                    pygame.mixer.music.unpause()
                    pause = False
            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_w:
                screen.blit(pygame.transform.scale(load_image("di.jpg"), (1200,800)), (0,0))
                pygame.mixer.music.load(list_music[0])
                pygame.mixer.music.play(0)
            elif event.key == pygame.K_d:
                screen.blit(pygame.transform.scale(load_image("love.webp"), (1200, 800)), (0,0))
                list_music = list_music[1:] + [list_music[0]]
                pygame.mixer.music.load(list_music[0])
                pygame.mixer.music.play()
            elif event.key == pygame.K_a:
                screen.blit(pygame.transform.scale(load_image("line.jpeg"), (1200, 800)), (0,0))
                list_music = [list_music[-1]] + list_music[0:-1]
                pygame.mixer.music.load(list_music[0])
                pygame.mixer.music.play()

    pygame.display.update()
    fps.tick(60)