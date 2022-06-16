import copy
import random


class Hat:

    def __init__(self, **kwargs):

        self.contents = []

        for colour, count in kwargs.items():
            for _ in range(count):
                self.contents.append(colour)

        self.contents_copy = copy.copy(self.contents)

    def draw(self, num_balls_drawn: int) -> list:

        if num_balls_drawn > len(self.contents_copy):
            contents_drawn = copy.copy(self.contents)
            self.contents = []
            return contents_drawn
        elif num_balls_drawn == 0:
            return []

        contents_drawn = random.sample(self.contents, k=num_balls_drawn)

        for content in contents_drawn:
            self.contents.remove(content)

        return contents_drawn


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:

    num_expected_results = 0

    for _ in range(num_experiments):
        num_accurate_comparisons = 0
        balls_drawn = hat.draw(num_balls_drawn)

        for colour, count in expected_balls.items():
            if count <= balls_drawn.count(colour):
                num_accurate_comparisons += 1

        if num_accurate_comparisons == len(expected_balls):
            num_expected_results += 1

        hat.contents = copy.copy(hat.contents_copy)

    return num_expected_results / num_experiments
