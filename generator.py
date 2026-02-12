from dataclasses import dataclass

# iterator
@dataclass
class Square:
    count: int
    current: int = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.count:
            raise StopIteration
        
        result: int = self.current ** 2
        self.current += 1
        return result
    
# generator
def square(count: int):
    for num in range(count):
        yield num ** 2

def main():
    s1 = Square(5)
    for num in s1:
        print(num)

    s2 = square(5)
    for num in s2:
        print(num)

if __name__ == "__main__":
    main()

