"""
Mixin Design Pattern: 
composing similar toolkit into a mixin class, and other classes can inherit from the mixin as a 
toolkit to use and no need to worry about multiple inheritance issues.
"""

from dataclasses import dataclass, field
from typing import Any
from icecream import ic
import json

class MapMixin:
    def __getitem__(self, key) -> Any:
        return self.__dict__.get(key)
    
    def __setitem__(self, key, value) -> None:
        self.__dict__[key] = value
        return None
    
class DictMixin:
    def to_dict(self) -> dict[Any, Any]:
        return self.__convert_dict(self.__dict__)
    
    def __convert_dict(self, attrs: dict):
        result = {}
        for key, value in attrs.items():
            result[key] = self.__convert_value(value)
        return result
    
    def __convert_value(self, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self
        elif isinstance(value, list):
            return [self.__convert_value(v) for v in value]
        elif hasattr(value, '__dict__'):
            return self.__convert_dict(value.__dict__)
        else:
            return value


class JSONMixin:
    def to_json(self):
        return json.dumps(self.to_dict())


@dataclass
class Resource(DictMixin):
    resource_id: str
    capacity: int

@dataclass
class Job:
    job_id: str
    due_date: int
    quantity: int

@dataclass
class SchedulerAgent(MapMixin, DictMixin, JSONMixin):
    jobs: list[Job] = field(default_factory=list)
    resources: list[Resource] = field(default_factory=list)



scheduler = SchedulerAgent()
ic(scheduler.jobs)
ic(scheduler["jobs"])
scheduler["jobs"] = [Job("J001", 1200, 100)]
scheduler["jobs"].append(Job("J002", 1000, 100))
ic(scheduler["jobs"])
ic(scheduler.jobs)

ic(scheduler.to_dict())
ic(scheduler.to_json())