from icecream import ic
from enum import Enum
import datetime

"""
建立帶狀態的 Logger
"""
def make_logger(prefix: str):
    count: int = 0

    def log(msg: str):
        nonlocal count
        count += 1
        print(f"[{datetime.datetime.now()}][{prefix}] {count}: {msg}")
    
    return log

scheduler_log = make_logger("Scheduler")
scheduler_log("start")
scheduler_log("finish")

"""
APS 排程策略工廠
"""
class DispatchRule(Enum):
    SPT = "spt"
    EDD = "edd"

def make_dispatch_rule(rule_name: DispatchRule):
    def dispatch(jobs):
        if rule_name == DispatchRule.SPT:
            return sorted(jobs.keys(), key=lambda job: jobs[job]["proc_time"])
        elif rule_name == DispatchRule.EDD:
            return sorted(jobs.keys(), key=lambda job: jobs[job]["due"])
        return jobs
    return dispatch

spt = make_dispatch_rule(DispatchRule.SPT)
edd = make_dispatch_rule(DispatchRule.EDD)

jobs: dict = {"job1": {"proc_time": 100, "due": 300}, "job2": {"proc_time": 150, "due": 250}}
ic(spt(jobs))
ic(edd(jobs))

"""
設備容量計算器
"""
def make_capacity(machine_speed: float):
    def calc(hours: float):
        return machine_speed * hours
    return calc

m1 = make_capacity(120)
ic(m1(8))

"""
取代簡單 class
"""
# by class
class Counter:
    def __init__(self):
        self.count: int = 0
    def __call__(self):
        self.count += 1
        return self.count

# by closure
def make_counter():
    count = 0 
    def increment():
        nonlocal count
        count += 1
        return count
    return increment


counter = Counter()
ic(counter())
ic(counter())

counter_lite = make_counter()
ic(counter_lite())
ic(counter_lite())
