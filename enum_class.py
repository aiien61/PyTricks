from enum import Enum, IntEnum, unique 
from functools import total_ordering
from dataclasses import dataclass, field
from typing import Self, Union
from icecream import ic

class TaskStatus(Enum):
    # before running
    DRAFT = "draft" # 草稿，資料未完成
    PENDING = "pending" # 待排程 / 待處理
    PLANNED = "planned" # 已納入 APS 排程
    SCHEDULED = "scheduled" # 已指定時間與資源
    RELEASED = "released" # 已釋放到現場
    DISPATCHED = "dispatched" # 已派工到機台 / 人員

    # running
    IN_PROGRESS = "in_progress" # 加工中
    WAITING = "waiting" # 已開始但等待中
    PAUSED = "paused" # 人工暫停
    BLOCKED = "blocked" # 條件不足（缺料 / 前製程）

    # after running
    COMPLETED = "completed" # 成功完成
    REWORK = "rework" # 需重工
    SCRAPPED = "scrapped" # 報廢
    FAILED = "failed" # 執行失敗
    CANCELLED = "cancelled" # 取消

    def __str__(self):
        return f"{self.name}({self.value})"

class ResourceStatus(Enum):
    # before running
    IDLE = "idle" # 閒置，可接單
    SETUP = "setup" # 換模 / 設定中
    READY = "ready" # 已設定完成，待開機

    # running
    RUNNING = "running" # 加工中
    WAITING = "waiting" # 等料 / 等人 / 等指令

    # abnormal
    DOWN = "down" # 故障
    MAINTENANCE = "maintenance" # 保養 / 維修
    PAUSED = "paused" # 人工暫停

    # management
    OFFLINE = "offline" # 關機 / 不在排程範圍
    LOCKED = "locked" # 被系統鎖定（插單 / 保護）

    def __str__(self):
        return f"{self.name}({self.value})"

class OrderPriority(IntEnum):
    LOW = 10 # 低優先（可延後）
    NORMAL = 20 # 一般訂單（預設）
    HIGH = 30 # 高優先（急單）
    URGENT = 40 # 緊急插單
    CRITICAL = 50 # 關鍵訂單（停線風險 / 客戶事故）

    def __str__(self):
        return f"{self.name}({self.value})"

class Status(Enum):
    SUCCESS = 1
    OK = 1
    FAIL = 2
    WRONG = 2

    def __str__(self):
        return f"{self.name}({self.value})"
    
    def __eq__(self, other: Union[Self, str, int]):
        match other:
            case str():
                return self.name == other.upper()
            case int():
                return self.value == other
            case Status():
                return self is other
            case _:
                return False

@total_ordering
class WorkFlowStatus(Enum):
    PENDING = 1
    SCHEDULED = 2
    IN_PROGRESS = 3
    COMPLETED = 4

    def __lt__(self, other: Union[Self, int]):
        if isinstance(other, int):
            return self.value < other
        if isinstance(other, WorkFlowStatus):
            return self.value < other.value
        return False



@dataclass
class Job:
    job_id: str
    order_id: str = field(repr=False)
    position_in_order: int = field(repr=False)
    status: TaskStatus = field(default=TaskStatus.DRAFT, repr=False)

@dataclass
class Machine:
    machine_id: str
    capacity: int = field(repr=False)
    status: ResourceStatus = field(default=ResourceStatus.IDLE, repr=False)

def main():
    job1 = Job("J101", "PO1001", 1, TaskStatus.IN_PROGRESS)
    job2 = Job("J102", "PO1001", 2, TaskStatus.SCHEDULED)

    m1 = Machine("M101", 1_000, ResourceStatus.RUNNING)
    m2 = Machine("M102", 2_000)
    
    for m in [m1, m2]:
        match m.status:
            case ResourceStatus.IDLE:
                m.status = ResourceStatus.RUNNING
                print(f"[{m}] status: {m.status} | message: {m} starts running.")
            case ResourceStatus.RUNNING:
                m.status = ResourceStatus.LOCKED
                print(f"[{m}] status: {m.status} | message: running resource {m} is being locked.")
            case _:
                pass

    job_status: str = "COMPLETED"
    print(job2)
    job2.status = TaskStatus[job_status]
    print(job2)

    machine_status: str = "waiting"
    print(m1)
    m1.status = ResourceStatus(machine_status)
    print(m1)

    for status in TaskStatus:
        print(status)

    for status in ResourceStatus:
        print(status.value)

    for status in Status:
        print(status)
    
    print(Status.__members__)

    print(Status.SUCCESS == Status.OK)
    print(Status.SUCCESS is Status.OK)

    print(Status.SUCCESS == 1)
    print(Status.SUCCESS == "success")

    print(WorkFlowStatus.IN_PROGRESS < 2)
    print(WorkFlowStatus.IN_PROGRESS < WorkFlowStatus.COMPLETED)


if __name__ == "__main__":
    main()
    
    try:

        # Use enum.unique to avoid duplicate values in enum members
        @unique
        class Location(Enum):
            IN_HOUSE = 1
            OUTSOURCING = 1
    
    except ValueError as exc:
        ic(exc)
