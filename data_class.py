import operator
from dataclasses import dataclass, field, FrozenInstanceError

@dataclass
class Machine:
    capacity: int
    tooling: list[str]

@dataclass(frozen=True)
class Resource:
    capacity: int
    setup_time: int = 0

@dataclass
class Agent:
    name: str = field(init=False) # if required to be initialised
    state: str = field(repr=False) # if printable
    id: int = field(hash=False) # 計算Hash值時是否考慮此屬性
    size: int = field(compare=False) # if comparable
    type_: str = field(default="RA")
    jobs: list[str] = field(default_factory=list)

# 預設用第一個屬性排序
@dataclass(order=True)
class Job:
    sort_index: int = field(init=False, repr=False)
    length: int
    deadline: int = 2880

    def __post_init__(self):
        if self.length < 0:
            raise ValueError("Job length can't be negative.")
        self.sort_index = self.deadline

def main():
    m1 = Machine(100, ["wire"])
    m2 = Machine(100, ["wire"])
    print(m1)
    print(m2)
    print(m1 == m2)

    r1 = Resource(100)

    try:
        r1.capacity = 200
    except FrozenInstanceError as exc:
        print(exc)

    a1 = Agent(state="in progress", id=1, size=10)
    a2 = Agent(state="in progress", id=1, size=20)
    a1.name = "001"
    a2.name = "001"
    print(a1)
    print(a2)
    print(a1 == a2)  # no need to compare size, so a1 is equal to a2

    try:
        j1 = Job(-100)
    except ValueError as exc:
        print(exc)

    j1 = Job(length=100, deadline=2880)
    j2 = Job(length=200, deadline=1440)
    sorted_jobs: list[Job] = sorted([j1, j2], reverse=True)
    print(sorted_jobs)

    # alternative for sorting (BETTER)
    r100 = Resource(capacity=100, setup_time=10)
    r200 = Resource(capacity=200, setup_time=5)
    r300 = Resource(capacity=150, setup_time=1)
    resources: list[Resource] = [r100, r200, r300]
    print(resources)
    resources.sort(key=operator.attrgetter("capacity"))
    print(resources)
    resources.sort(key=operator.attrgetter("setup_time"))
    print(resources)


if __name__ == "__main__":
    main()