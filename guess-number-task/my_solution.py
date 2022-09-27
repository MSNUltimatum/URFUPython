import numpy as np
from game_v2 import score_game


class Randomizer:
    def __init__(self):
        self.number = np.random.randint(1, 101)

    def equals(self, predict: int) -> bool:
        return self.number == predict

    def higher(self, predict: int) -> bool:
        return self.number > predict


def predict_number(num: int) -> int:
    start: int = 1
    end: int = 101
    attempts: int = 0
    while start < end:
        attempts += 1
        mid: int = (start + end) // 2
        if num == mid:
            return attempts
        elif num > mid:
            start: int = mid
        else:
            end = mid