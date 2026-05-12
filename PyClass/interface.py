from abc import ABC, abstractmethod
from typing import TypedDict

class Resource(ABC):
    def __init__(self, category: str) -> None:
        self.category = category
    
    @abstractmethod
    def is_available(self) -> bool:
        ...
    

class Machine(Resource):
    def __init__(self, capacity: int, category: str) -> None:
        super().__init__(category)
        self.capacity = capacity
    
    def is_available(self, lot) -> bool:
        required_amount = lot['qty'] * lot['std_proc_time']
        return required_amount < self.capacity

Lot = TypedDict('Lot', {'qty': int, 'std_proc_time': int}, total=True)

m1: Machine = Machine(capacity=10_000, category='Etching')
lot1: Lot = {'qty': 100, 'std_proc_time': 10}
lot2: Lot = {'qty': 200, 'std_proc_time': 1_00}

print(m1.is_available(lot1))
print(m1.is_available(lot2))