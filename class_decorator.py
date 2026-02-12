from dataclasses import dataclass
from enum import IntEnum
from icecream import ic
import uuid


@dataclass
class Operation:
    process_time: int

class SetupTimeDecorator:
    def __init__(self, setup_time: int):
        self.setup_time = setup_time

    def __call__(self, func):
        def wrapper(operation: Operation):
            return operation.process_time + self.setup_time
        return wrapper

@SetupTimeDecorator(setup_time=5)
def calc_operation_time(operation: Operation) -> int:
    return operation.process_time

"""
所有 Task 在建立時：
1. 自動給 task_id
2. 印 log（或之後可以接事件 / Agent）
"""

class TaskStatus(IntEnum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

def mes_task(cls):
    print(f"[MES] register task class: {cls.__name__}")

    def wrapper(*args, **kwargs):
        print("[MES] create task instance.")
        obj = cls(*args, **kwargs)

        obj.task_id = str(uuid.uuid4())
        obj.status = TaskStatus.PENDING

        print(f"[MES] task_id: {obj.task_id}")
        return obj
    return wrapper

@mes_task
@dataclass
class Task:
    name: str

def main():
    operation = Operation(process_time=30)
    ic(calc_operation_time(operation))

    t1 = Task("Cutting")
    t2 = Task("Assembly")
    ic(t1.name, t1.task_id, t1.status)
    ic(t2.name, t2.task_id, t2.status)


if __name__ == "__main__":
    main()
