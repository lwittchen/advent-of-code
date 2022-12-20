from collections import namedtuple

Motion = namedtuple("Motion", "x y")


class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, motion: Motion):
        self.x += motion.x
        self.y += motion.y

    def __str__(self):
        return f"x: {self.x} - y: {self.y}"


class Rope:
    def __init__(self, head: Coord = Coord(0, 0), tail: Coord = Coord(0, 0)):
        self._head = head
        self._tail = tail
        self.trail = []

    def move_head(self, motion: Motion) -> None:
        self.trail.append((self._tail.x, self._tail.y))
        self._head.move(motion)

        x_diff = self._head.x - self._tail.x
        y_diff = self._head.y - self._tail.y

        if abs(x_diff) > 1:
            self._tail.x += x_diff / abs(x_diff)
            if abs(y_diff) == 1:
                self._tail.y += y_diff / abs(y_diff)

        if abs(y_diff) > 1:
            self._tail.y += y_diff / abs(y_diff)
            if abs(x_diff) == 1:
                self._tail.x += x_diff / abs(x_diff)

    def close(self) -> None:
        self.trail.append((self._tail.x, self._tail.y))


motion_map = {
    "D": Motion(x=0, y=-1),
    "U": Motion(x=0, y=1),
    "R": Motion(x=1, y=0),
    "L": Motion(x=-1, y=-0),
}

if __name__ == "__main__":
    filename = "input.txt"
    lines = [line.strip() for line in open(filename) if line.strip()]

    rope = Rope()
    for line in lines:
        d, i = line.split()
        motion = motion_map[d]
        [rope.move_head(motion) for _ in range(int(i))]
        rope.close()

    trail = rope.trail
    print(f"--- result ---")
    print(f"{len(set(trail))=}")
