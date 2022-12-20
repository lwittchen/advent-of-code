from collections import namedtuple

Motion = namedtuple("Motion", "x y")


class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, motion: Motion):
        self.x += motion.x
        self.y += motion.y

    def to_tuple(self):
        return (self.x, self.y)

    def __str__(self):
        return f"x: {self.x} - y: {self.y}"


class Rope:
    def __init__(self, num_parts: int):
        self._parts = [Coord(0, 0) for _ in range(num_parts)]
        self.trail = []

    def move_head(self, motion: Motion) -> None:
        self._parts[0].move(motion)

        for i in range(len(self._parts) - 1):
            head = self._parts[i]
            tail = self._parts[i + 1]
            x_diff = head.x - tail.x
            y_diff = head.y - tail.y

            if abs(x_diff) > 1:
                tail.x += x_diff / abs(x_diff)
                if abs(y_diff) > 0:
                    tail.y += y_diff / abs(y_diff)

            elif abs(y_diff) > 1:
                tail.y += y_diff / abs(y_diff)
                if abs(x_diff) > 0:
                    tail.x += x_diff / abs(x_diff)

        self.trail.append(self._parts[-1].to_tuple())


motion_map = {
    "D": Motion(x=0, y=-1),
    "U": Motion(x=0, y=1),
    "R": Motion(x=1, y=0),
    "L": Motion(x=-1, y=-0),
}

if __name__ == "__main__":
    filename = "input.txt"
    lines = [line.strip() for line in open(filename) if line.strip()]

    rope = Rope(num_parts=10)
    for line in lines:
        d, i = line.split()
        motion = motion_map[d]
        for _ in range(int(i)):
            rope.move_head(motion)

    trail = rope.trail
    print(f"--- result ---")
    print(f"{len(set(trail))=}")
