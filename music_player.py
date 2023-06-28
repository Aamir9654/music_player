import pygame

# Initialize Pygame
pygame.init()


class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_song = 0

    def add_song(self, song_path):
        self.playlist.append(song_path)

    def play(self):
        pygame.mixer.music.load(self.playlist[self.current_song])
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def next_song(self):
        self.current_song = (self.current_song + 1) % len(self.playlist)
        self.play()

    def previous_song(self):
        self.current_song = (self.current_song - 1) % len(self.playlist)
        self.play()

    def stop(self):
        pygame.mixer.music.stop()

# Create an instance of the MusicPlayer class
player = MusicPlayer()

# Add songs to the playlist
player.add_song("D:\.vscode\python_project\silent-wood.mp3")
player.add_song("sea.mp3")

# Play the first song
player.play()

# Wait for user input
while True:
    command = input("Enter a command (pause{p}/resume{r}/next{n}/previous{pr}/stop{s}/quit{q}): ")

    if command == "p":
        player.pause()
    elif command == "r":
        player.resume()
    elif command == "n":
        player.next_song()
    elif command == "pr":
        player.previous_song()
    elif command == "s":
        player.stop()
    elif command == "q":
        break

# Quit Pygame
pygame.quit()
