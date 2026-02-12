from dataclasses import dataclass

@dataclass
class Prop:
    name: str

    def __set_name__(self, owner, name):
        self.private_name: str = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)
        
    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)


class Agent(type):
    @staticmethod
    def __new__(mcs, name, bases, namespace, **kwargs):
        class_ = super().__new__(mcs, name, bases, namespace)
        # hardcoded
        # class_.cpu_count = 1

        # flexible
        for key, value in kwargs.items():
            setattr(class_, key, value)

        if hasattr(class_, "props"):
            for prop_name in class_.props:
                prop = Prop(prop_name)
                setattr(class_, prop_name, prop)
                prop.__set_name__(class_, prop_name)

        return class_


class SchedulerAgent(object, metaclass=Agent, cpu_count=1):
    pass

main_agent: SchedulerAgent = SchedulerAgent()


class ResourceAgent(object, metaclass=Agent, cpu_count=1, master=main_agent):
    def __init__(self):
        self.resource_list: list[str] = []


class RuleAgent(object, metaclass=Agent):
    props: list[str] = ["rules"]

def agent(cls):
    return Agent(cls.__name__, cls.__bases__, dict(cls.__dict__))

@agent
class LogAgent:
    props: list[str] = ["logfile"]    
    
def main():
    resource_agent: ResourceAgent = ResourceAgent()
    print(resource_agent.resource_list)
    print(resource_agent.cpu_count)
    print(resource_agent.master)
    print(main_agent.cpu_count)

    try:
        print(main_agent.master)
    except AttributeError as exc:
        print(exc)

    rule_agent: RuleAgent = RuleAgent()
    print(rule_agent.rules)
    rule_agent.rules = {"M1": 100}
    print(rule_agent.rules)


if __name__ == "__main__":
    main()
