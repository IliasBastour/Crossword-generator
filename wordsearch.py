import random
import numpy as np

class WordSearch:
    def __init__(self, words, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = self.create_empty_grid()
        self.words = self.add_words(words)
        self.directions = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(-1, -1),(1, -1),(-1, 1)]

    def create_empty_grid(self):
        return np.full((self.width, self.height), "_")

    def add_words(self, words:list[str]) -> list[str]:
        self.words = [word.strip() for word in words.split()]
        self.words = list(dict.fromkeys(self.words))
        self.words.sort(key=len, reverse=True)
        for word in self.words:
            if not word.isalpha():
                raise ValueError(f"Invalid word '{word}'")
            elif len(word) > self.width or len(word) > self.height:
                raise ValueError(f"The word is too long '{word}'")  
        self.words = [word.upper() for word in self.words]
        if not self.words:
            raise ValueError("No words provided.")
        return self.words

    def _can_place_word(self, word: str):
        for i in range(len(word)):
            r = self.row + self.dx * i
            c = self.column + self.dy * i
            if r < 0 or r >= self.width or c < 0 or c >= self.height:
                self.can_place = False
                return False
            if self.grid[r][c] != "_" and self.grid[r][c] != word[i]:
                return False
        return True
                            

    def place_word(self, word:str):
        for i in range(len(word)):
            r = self.row + self.dx * i
            c = self.column + self.dy * i
            self.grid[r, c] = word[i]

    def fill_empty_spaces(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x, y] == "_":
                    self.grid[x, y] = random.choice("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    def generate(self):
        for word in self.words:
            success = False
            tries = 0
            while not success and tries < 5000:
                tries += 1
                shuffled_directions = self.directions.copy()
                random.shuffle(shuffled_directions)
                shuffled_positions = []
                for i in range(self.width):
                    for j in range(self.height):
                        shuffled_positions.append((i, j))
                random.shuffle(shuffled_positions)
                for self.row, self.column in shuffled_positions:
                    for self.dx, self.dy in shuffled_directions:
                        if self._can_place_word(word):
                            self.place_word(word)
                            success = True
                            break
                    if success:
                        break
            if not success:
                raise ValueError(f"The word could not be placed '{word}'")
        self.grid_before_fill = self.grid.copy()
        self.fill_empty_spaces()

    def get_grid_as_list(self):
        return self.grid.tolist()
    def get_grid_before_fill_as_list(self):
        return self.grid_before_fill.tolist()

    def display(self):
        for row in self.grid:
            print(" ".join(row))
