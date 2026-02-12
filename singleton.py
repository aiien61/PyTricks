"""
Singleton 是一種建立型設計模式，目的：

整個系統中只允許某個類別存在唯一一個實例，並提供全域存取點。

常見用途（在 APS / MES 很常見）：

1. 系統設定 Config
2. 排程核心 SchedulerEngine
3. 訊息中介者 Mediator
4. 資源池 ResourceManager
5. 日誌系統 Logger

這些物件若出現多個實例，會造成：

狀態不一致
資源衝突
排程錯亂

因此需要 Singleton。


在 現代架構（DDD / 微服務）中，Singleton 常被濫用

應避免用在：

domain entity
business object
request-scoped service

因為：
1. 難測試
2. 隱藏依賴
3. 破壞 DI
"""

from dataclasses import dataclass, field
from enum import IntEnum
from icecream import ic

"""
implement singleton pattern by setattr decorator

缺點:
不是 thread-safe
會破壞型別（class → function）
"""
def singleton(cls):
    def inner(*args, **kwargs):
        if not hasattr(cls, '__instance'):
            obj = cls(*args, **kwargs)
            setattr(cls, '__instance', obj)
            return obj
        return getattr(cls, '__instance')
    return inner

@singleton
class Agent:
    pass

a1 = Agent()
a2 = Agent()
ic(a1 is a2)

try:
    ic(isinstance(a1, Agent))
except TypeError as exc:
    ic(exc)

try:
    ic(type(a1))
except TypeError as exc:
    ic(exc)

"""
implement singleton pattern by closure

缺點:
class 被 function 取代
破壞 OOP 結構
"""
def closure_singleton(cls):
    _instance: dict[type, object] = {}
    def inner(*args, **kwargs):
        if cls not in _instance:
            obj = cls(*args, **kwargs)
            _instance[cls] = obj
            return obj
        return _instance.get(cls)
    return inner

@closure_singleton
class Proxy:
    pass

p1 = Proxy()
p2 = Proxy()
ic(p1 is p2)


"""
implement singleton pattern by meta class
"""
class SingletonMeta(type):
    _instance: dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]

class Mediator(metaclass=SingletonMeta):
    pass

m1 = Mediator()
m2 = Mediator()
ic(m1 is m2)


"""
implement Scheduler metaclass by singleton pattern
"""

@dataclass
class SchedulerCore(metaclass=SingletonMeta):
    jobs: list[str] = field(default_factory=list)

    def add_job(self, job: str):
        self.jobs.append(job)
    
    def run(self):
        return f"Scheduling {len(self.jobs)} jobs..."
    
s1 = SchedulerCore()
s2 = SchedulerCore()
s1.add_job("A")
s2.add_job("B")
ic(s2.run())
ic(s1 is s2)

"""
implement MES Mediator by singleton pattern

整個工廠：
1. 只有一個協調中心
2. 所有 Agent 共用
"""
class ResourceStatus(IntEnum):
    IDLE = 1
    RUNNING = 2

class JobStatus(IntEnum):
    PENDING = 1
    IN_PROGRESS = 2

@dataclass
class MESMediator(metaclass=SingletonMeta):
    machines: dict = field(default_factory=dict)
    orders: dict = field(default_factory=dict)

    def register_machine(self, machine_id: str) -> bool:
        if machine_id in self.machines:
            return False
        
        self.machines[machine_id] = ResourceStatus.IDLE
        return True
    
    def register_order(self, order_id: str) -> bool:
        if order_id in self.orders:
            return False
        self.orders[order_id] = JobStatus.PENDING
        return True