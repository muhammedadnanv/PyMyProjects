import pygame
import os
import sys

# Initialize pygame mixer
pygame.mixer.init()

# Define the music player class
class MusicPlayer:
    def __init__(self):
        self.current_song = None

    def load_song(self, song_path):
        if os.path.exists(song_path):
            pygame.mixer.music.load(song_path)
            self.current_song = song_path
            print(f"Loaded {song_path}")
        else:
            print("File does not exist.")

    def play(self):
        if self.current_song:
            pygame.mixer.music.play()
            print("Playing music...")
        else:
            print("No song loaded.")

    def stop(self):
        pygame.mixer.music.stop()
        print("Stopped music.")

    def pause(self):
        pygame.mixer.music.pause()
        print("Paused music.")

    def unpause(self):
        pygame.mixer.music.unpause()
        print("Unpaused music.")

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
        print(f"Volume set to {volume}")

def display_menu():
    print("\nMusic Player Menu")
    print("1. Load Song")
    print("2. Play")
    print("3. Stop")
    print("4. Pause")
    print("5. Unpause")
    print("6. Set Volume")
    print("7. Exit")

def main():
    player = MusicPlayer()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            song_path = input("Enter the path to the song file: ")
            player.load_song(song_path)
        elif choice == '2':
            player.play()
        elif choice == '3':
            player.stop()
        elif choice == '4':
            player.pause()
        elif choice == '5':
            player.unpause()
        elif choice == '6':
            volume = float(input("Enter volume level (0.0 to 1.0): "))
            player.set_volume(volume)
        elif choice == '7':
            print("Exiting...")
            pygame.mixer.quit()
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
