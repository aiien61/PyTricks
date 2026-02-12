from dataclasses import dataclass

@dataclass
class Machine:
    __capacity: int = 100

    def get_capacity(self) -> int:
        return self.__capacity
    
    def set_capacity(self, value: int) -> None:
        if value <= 0:
            raise ValueError("capacity must greater than 0")
        
        self.__capacity = value
        return None
    
    capacity = property(fget=get_capacity, fset=set_capacity)

@dataclass
class Resource:
    __capacity: int = 100
    __workload: int = 0
    
    @property
    def workload(self) -> int:
        return self.__workload
    

    def add_workload(self, value: int) -> bool:
        if self.is_full:
            raise Exception("capacity is full.")
        if self.daily_capacity < self.__workload + value:
            raise Exception("capacity is less than expected.")
        self.__workload += value
        return True

    @property
    def capacity(self) -> int:
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= 0:
            raise ValueError("capacity must greater than 0")
        self.__capacity = value
        return None
    
    @property
    def daily_capacity(self) -> int:
        return self.__capacity * 8
    
    @property
    def is_full(self) -> bool:
        return self.__workload == self.daily_capacity
    

def main():
    machine = Machine()
    print(machine.capacity)
    machine.capacity = 200
    print(machine.capacity)

    resource = Resource()
    print(resource.capacity)
    resource.capacity = 300
    print(resource.capacity)
    print(resource.daily_capacity)
    resource.add_workload(100)
    print(resource.workload)
    print(resource.is_full)
    try:
        resource.add_workload(3000)
    except Exception as exc:
        print(exc)

    resource.add_workload(2300)
    print(resource.is_full)


if __name__ == "__main__":
    main()
