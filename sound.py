import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.bounce_brick = pygame.mixer.Sound("Assets/bounce.wav")
        self.bounce_pad = pygame.mixer.Sound("Assets/bounce2.mp3")
        self.bounce_wall = pygame.mixer.Sound("Assets/bounce3.mp3")
        self.lost_round = pygame.mixer.Sound("Assets/lost.mp3")
        self.game_song = pygame.mixer.music

    def play_brick_bounce(self):
        pygame.mixer.Sound.play(self.bounce_brick)
    def play_wall_bounce(self):
        pygame.mixer.Sound.play(self.bounce_wall)
    def play_pad_bounce(self):
        pygame.mixer.Sound.play(self.bounce_pad)
    def play_lost_round(self):
        pygame.mixer.Sound.play(self.lost_round)

    def play_game_song(self):
        self.game_song.load("Assets/game_song.mp3")
        self.game_song.set_volume(0.1)
        self.game_song.rewind()
        self.game_song.play(-1)

    def stop_song(self):
        self.game_song.stop()

