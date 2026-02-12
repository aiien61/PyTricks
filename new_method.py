class Double(int):
    def __new__(cls, value: int):
        return super().__new__(cls, value * 2)

class Agent:
    def __new__(cls, name: str, memebers: None | list[str]):
        agentic_obj = super().__new__(cls)
        agentic_obj.name = name
        agentic_obj.memebers = [] if memebers is None else memebers
        return agentic_obj
    
def main():
    x = int(100)
    print(x)
    doubled_x = Double(100)
    print(doubled_x)

    agent = Agent("ConstraintAgent", ["M1", "M2"])
    print(agent.name)
    print(agent.memebers)

if __name__ == "__main__":
    main()
