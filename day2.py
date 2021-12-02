import dataclasses


@dataclasses.dataclass
class Position:
    horiz: int = 0
    vert: int = 0

    def forward(self, units: int):
        self.horiz += units

    def up(self, units: int):
        self.vert -= units

    def down(self, units: int):
        self.vert += units

    @property
    def multiplied(self):
        return self.horiz * self.vert


@dataclasses.dataclass
class Day2Position(Position):
    aim: int = 0

    def forward(self, units: int):
        self.horiz += units
        self.vert += units * self.aim

    def up(self, units: int):
        self.aim -= units

    def down(self, units: int):
        self.aim += units


with open("day2-1.txt", "r") as in_handle:
    pos = Position()

    for line in in_handle:
        command, arg = line.strip().split()
        getattr(pos, command)(int(arg))

    print(pos.multiplied)


with open("day2-1.txt", "r") as in_handle:
    pos = Day2Position()

    for line in in_handle:
        command, arg = line.strip().split()
        getattr(pos, command)(int(arg))

    print(pos.multiplied)