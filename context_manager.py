"""
scenarios for context_manager
1. open & close
2. lock & release
3. activate & stop
4. alter & reset
"""

import time
from dataclasses import dataclass
from contextlib import contextmanager
import logging

class Timer:
    def __init__(self):
        self.elapsed: float = 0
        self.__start: float = 0
        self.__stop: float = 0

    def __enter__(self):
        self.__start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type:
            logging.error("Something went wrong", exc_info=(exc_type, exc_val, exc_tb))
        
        self.__stop = time.perf_counter()
        self.elapsed = self.__stop - self.__start
        print(f"exc_type: {exc_type}, exc_val: {exc_val}, exc_tb: {exc_tb}")
        return False
    
@dataclass
class TimeResult:
    elapsed: float = 0.0

    
@contextmanager
def timer(*, suppress: type[Exception] | tuple[type[Exception]] | None = None):
    """
    :param suppress: exception to ignore
    """
    result: TimeResult = TimeResult()
    start: float = time.perf_counter()
    try:
        yield result
    except Exception as exc:
        if suppress and isinstance(exc, suppress):
            print(f"[suppressed {type(exc).__name__}] {exc}")
        else:
            raise
    finally:
        stop: float = time.perf_counter()
        result.elapsed = stop - start


def main():
    # without context manager
    file = open("myfile.txt", "w")
    file.write("This is a text file.")
    file.close()

    # with context manager
    with open("mytext.txt", "w") as file:
        file.write("This is a text file.")

    # without context manager
    start: float = time.perf_counter()
    nums: list[int] = [n ** 2 for n in range(10_000)]
    stop: float = time.perf_counter()
    elapsed: float = stop - start
    print(elapsed)

    # with context manager
    with Timer() as t:
        nums: list[int] = [n ** 2 for n in range(10_000)]
    print(t.elapsed)

    with timer() as t:
        nums: list[int] = [n ** 2 for n in range(10_000)]
    print(t.elapsed)

    with timer(suppress=ZeroDivisionError):
        1 / 0

    with timer(suppress=(KeyError, ValueError)):
        {}["x"]
    
    with timer(suppress=KeyError):
        1 / 0



if __name__ == "__main__":
    main()
