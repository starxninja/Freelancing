from abc import ABC, abstractmethod
from random import randint
from collections import Counter

class Dice(ABC):
    def __init__(self):
        self.face = None

    @abstractmethod
    def roll(self) -> int:
        pass

class SixSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 6)
        return self.face

class TenSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 10)
        return self.face

def histogram(rolls: list) -> str:
    counts = Counter(rolls)
    result = ["Roll Histogram:"]
    for value in sorted(counts.keys()):
        result.append(f"{value}: {'*' * counts[value]} ({counts[value]})")
    return "\n".join(result)

def main():
    # Test SixSidedDice
    six_sided = SixSidedDice()
    six_sided_rolls = [six_sided.roll() for _ in range(1000)]
    print("Six-Sided Dice Rolls (1000 rolls):")
    print(histogram(six_sided_rolls))
    print()

    # Test TenSidedDice
    ten_sided = TenSidedDice()
    ten_sided_rolls = [ten_sided.roll() for _ in range(1000)]
    print("Ten-Sided Dice Rolls (1000 rolls):")
    print(histogram(ten_sided_rolls))

if __name__ == "__main__":
    main()