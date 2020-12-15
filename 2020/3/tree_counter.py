from dataclasses import dataclass
from pathlib import Path


def get_input():
    with open(Path(__file__).parent / "input.txt", "r") as f:
        return f.read().rstrip()


@dataclass
class Position:
    x: int
    y: int


class RepeatingTreeMap:
    """A tilemap starting at the top-left that repeats across the x-axis."""

    def __init__(self, layout: str):
        self._tilemap = [list(line) for line in layout.splitlines()]

    def has_tree_at(self, pos: Position) -> bool:
        return self[pos] == "#"

    @property
    def height(self):
        return len(self._tilemap)

    def __getitem__(self, key: Position):
        if not hasattr(key, "y") or not hasattr(key, "x"):
            raise TypeError("Index must have (x,y) attributes.")
        return self._tilemap[key.y][key.x % len(self._tilemap[0])]


if __name__ == "__main__":
    tree_map = RepeatingTreeMap(get_input())

    current_position = Position(0, 0)
    tree_hit_count = 0
    while current_position.y < tree_map.height:
        if tree_map.has_tree_at(current_position):
            tree_hit_count += 1
        current_position.x += 3
        current_position.y += 1

    print(f"hits={tree_hit_count}")

    # Part 2
    slopes = [
        Position(1, 1),
        Position(3, 1),
        Position(5, 1),
        Position(7, 1),
        Position(1, 2),
    ]
    answer = 1
    for slope in slopes:
        current_position = Position(0, 0)
        tree_hit_count = 0
        while current_position.y < tree_map.height:
            if tree_map.has_tree_at(current_position):
                tree_hit_count += 1
            current_position.x += slope.x
            current_position.y += slope.y
        print(f"{slope} hits={tree_hit_count}")
        answer *= tree_hit_count
    print(f"answer={answer}")
