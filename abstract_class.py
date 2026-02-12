from abc import ABC, abstractmethod

class Action(ABC):
    @abstractmethod
    def execute(self): raise NotImplementedError


class WorkAction(Action):
    def execute(self):
        print("work executing...")


class DeleteAction(Action):
    def execute(self):
        print("deletion executing...")


def execute_action(action: Action):
    action.execute()
        

def main():
    try:
        action = Action()
    except TypeError as exc:
        print(exc)

    work_action = WorkAction()
    execute_action(work_action)
    
    delete_action = DeleteAction()
    execute_action(delete_action)

if __name__ == "__main__":
    main()