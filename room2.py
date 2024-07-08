# Indiana Jones Escape Room Design
import pygame
import sys

# Initialize Pygame
pygame.init()


class EscapeRoom:
    def __init__(self):
        self.current_room = None
        self.rooms = {}

    def add_room(self, room_name, description):
        self.rooms[room_name] = description

    def start_game(self):
        print("Welcome to the Indiana Jones Escape Room!")
        self.current_room = input("Enter the starting room: ")

        while self.current_room:
            if self.current_room in self.rooms:
                print(self.rooms[self.current_room])
                self.current_room = input("Enter the next room (or 'exit' to quit): ")
            elif self.current_room.lower() == "exit":
                print("Thanks for playing! Come back soon.")
                break
            else:
                print("Invalid room name. Try again.")

if __name__ == "__main__":
    cineverse_escape_room = EscapeRoom()

    # Add rooms and descriptions
    cineverse_escape_room.add_room("Temple Entrance", "You stand before a massive stone door adorned with ancient symbols.")
    cineverse_escape_room.add_room("Chamber of Artifacts", "Shelves hold dusty relics: golden idols, crystal skulls, and mysterious scrolls.")
    cineverse_escape_room.add_room("Snake Pit", "A pit filled with slithering snakes blocks your path. Find a way across!")
    cineverse_escape_room.add_room("Final Treasure Vault", "The Holy Grail awaits! Solve the final puzzle to claim your prize.")

    # Start the game
    cineverse_escape_room.start_game()
