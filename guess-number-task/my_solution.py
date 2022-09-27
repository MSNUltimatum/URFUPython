import numpy as np


class Randomizer:
    def __init__(self):
        self.number = np.random.randint(1, 101)
        print(f"Random number is: {self.number}")

    def equals(self, predict: int) -> bool:
        return self.number == predict

    def higher(self, predict: int) -> bool:
        return self.number > predict


def predict_number(rnd: Randomizer) -> int:
    start: int = 1
    end: int = 100
    attempts: int = 0
    while start <= end:
        attempts += 1
        mid: int = (start + end) // 2
        if rnd.equals(mid):
            print(f"Attempts count: {attempts}")
            return mid
        elif rnd.higher(mid):
            start: int = mid
        else:
            end = mid


if __name__ == '__main__':
    rand: Randomizer = Randomizer()
    print(f"Result number: {predict_number(rand)}")
