class BasePlugin:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'version'):
            raise TypeError(f"Class {cls.__name__} must have property 'version'.")

class GoodPlugin(BasePlugin):
    version = "1.0.0"

try:
    class BadPlugin(BasePlugin):
        pass
except TypeError as exc:
    print(exc)

"""
Agent (abstract)
 ├── SchedulerAgent
 ├── ResourceAgent
 ├── OrderAgent
 └── RuleAgent

Infrastructure
 ├── EventBus
 ├── Repository (DB)
 └── AgentRegistry

Application
 ├── Bootstrap / DI
 └── FastAPI
"""
from abc import ABC, abstractmethod
from typing import Dict, Optional, Self, Callable, List
from collections import defaultdict
from enum import Enum
from fastapi import FastAPI

class AgentType(Enum):
    SCHEDULER = "scheduler"
    RESOURCER = "resourcer"
    RULER = "ruler"

class Agent(ABC):
    _registry: Dict[AgentType, Self] = {}

    agent_type: Optional[AgentType] = None
    capabilities: set[str] = set()

    def __init_subclass__(cls, agent_type: AgentType, provides: list[str], **kwargs):
        super().__init_subclass__(**kwargs)
        if agent_type:
            cls.agent_type = agent_type
            Agent._registry[agent_type] = cls
        
        if provides:
            cls.capabilities = set(provides)
    
    def __init__(self, agent_id: str, event_bus, repository):
        self.agent_id = agent_id
        self.event_bus = event_bus
        self.repo = repository
    
    @abstractmethod
    def start(self): raise NotImplementedError
    
    @abstractmethod
    def stop(self): raise NotImplementedError

class EventBus:
    def __init__(self):
        self._subscribers: dict[str, List[Callable]] = defaultdict(list)
    
    def subscribe(self, event: str, handler: Callable) -> None:
        self._subscribers[event].append(handler)

    def publish(self, event: str, payload: dict) -> None:
        for handler in self._subscribers[event]:
            handler(payload)

class Repository:
    def save(self, entity: str, data: dict) -> None:
        print(f"[DB] save {entity}: {data}")
    
    def load(self, entity: str, entity_id: str) -> dict:
        print(f"[DB] load {entity} {entity_id}")
        return {}

class SchedulerAgent(Agent, agent_type=AgentType.SCHEDULER, provides=["schedule", "reschedule"]):
    def start(self) -> None:
        self.event_bus.subscribe("order_created", self.on_order_created)
    
    def stop(self):
        pass

    def on_order_created(self, event) -> None:
        print(f"[Scheduler] scheduling order {event['order_id']}")
        self.repo.save("schedule", {"order": event["order_id"]})

class ResourceAgent(Agent, agent_type=AgentType.RESOURCER, provides=["capacity", "status"]):
    def start(self) -> None:
        self.event_bus.subscribe("schedule_created", self.on_schedule)
    
    def stop(sefl):
        pass

    def on_schedule(self, event) -> None:
        print(f"[Resource] allocate resources for {event}")

class RuleAgent(Agent, agent_type=AgentType.RULER, provides=["dispatching_rules"]):
    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

def bootstrap() -> tuple:
    event_bus = EventBus()
    repo = Repository()

    agents = {}

    for agent_type, agent_cls in Agent._registry.items():
        agents[agent_type] = agent_cls(agent_id=agent_type.value, event_bus=event_bus, repository=repo)
        agents[agent_type].start()
    
    return agents, event_bus

app = FastAPI()
agents, event_bus = bootstrap()

@app.post("/orders")
def create_order(order: dict):
    event_bus.publish("order_created", order)
    return {"status": "ok"}
