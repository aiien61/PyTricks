class CapacityArithmeticException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def capacity_addition(resource1: dict[str, int], resource2: dict[str, int]) -> int:
    c1: int = resource1.get("capacity")
    c2: int = resource2.get("capacity")
    
    if not c1 or not c2:
        raise ValueError("resource must have key 'capacity' and corresponding integer value.")
    
    if not isinstance(c1, int) or not isinstance(c2, int):
        raise CapacityArithmeticException("resource capacity must be integer.")
    
    return c1 + c2


def main():
    try:
        r1 = {"capacity": 1_000}
        r2 = {"capacity": 2_000.0}
        total_capacity: int = capacity_addition(r1, r2)
        print(total_capacity)

    except CapacityArithmeticException as exc:
        print(exc)
    
    except ValueError as exc:
        print(exc)

    except Exception as exc:
        print(f"{type(exc)} | {exc}")

if __name__ == "__main__":
    main()
