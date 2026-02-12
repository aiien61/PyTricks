from icecream import ic

class Resource:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise Exception("name must be str.")
        
        if not name:
            raise Exception("name can't be empty.")
        
        self.__name = name
        return None
    
    @property
    def capacity(self) -> int:
        return self.__capacity
    
    @capacity.setter
    def capacity(self, capacity: int) -> None:
        if capacity < 0:
            raise Exception("capacity can't be negative.")
    
        self.__capacity = capacity
        return None
    
class RequireString:
    def __init__(self, to_trim: bool):
        self.__to_trim = to_trim

    def __set_name__(self, owner, name):
        self.__property_name = name
        
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.__property_name} is not str.")
        
        if self.__to_trim:
            value = value.strip()

        if not value:
            raise ValueError(f"{self.__property_name} is empty")

        instance.__dict__[self.__property_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.__property_name)

class RequireInteger:
    def __set_name__(self, owner, name):
        self.__property_name = name
        
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.__property_name} can't be negative.")
        
        if not isinstance(value, int):
            raise ValueError(f"{self.__property_name} must be integer.")

        instance.__dict__[self.__property_name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.__property_name)

    
class Agent:
    name: str = RequireString(True)
    capacity: int = RequireInteger()
    
def main():
    res = Resource("Machine", 100)

    scheduler_agent = Agent()
    scheduler_agent.name = "scheduler"
    scheduler_agent.capacity = 1_000

    resource_agent = Agent()
    resource_agent.name = "resourcer"
    resource_agent.capacity = 2_000

    order_agent = Agent()
    try:
        order_agent.name = "    "
    except ValueError as exc:
        ic(exc)

    try:
        order_agent.capacity = 100.1
    except ValueError as exc:
        ic(exc)

    ic(scheduler_agent.name)
    ic(resource_agent.name)
    ic(scheduler_agent.capacity)
    ic(resource_agent.capacity)


if __name__ == "__main__":
    main()
    