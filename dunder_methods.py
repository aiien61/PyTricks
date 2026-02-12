from datetime import date
from typing import Self
from dataclasses import dataclass


@dataclass
class MyDate:
    year: int
    month: int
    day: int

    def __str__(self):
        """for users"""
        print("__str__  is being called")
        return f"{self.year}-{self.month}-{self.day}"
    
    def __repr__(self):
        """for dev use"""
        print("__repr__ is being called")
        return f"({id(self)}){self.year}-{self.month}-{self.day}"
    
    def __eq__(self, other: Self):
        if not isinstance(other, MyDate):
            return False
        
        return self.year == other.year and self.month == other.month and self.day == other.day
    
    def __hash__(self):
        print("__hash__ is being called")
        return id(self)
    
    def __bool__(self):
        return self.year > 2025
    
    def __del__(self):
        print(f"{self} is being deleted.")


def main():
    date1: MyDate = MyDate(2026, 1, 1)

    print(str(date1))
    print(date1)
    print(repr(date1))

    date2: MyDate = MyDate(2026, 1, 1)
    date3: MyDate = MyDate(2025, 1, 1)
    date4: date = date(2026, 1, 1)

    print(f"date2 == date1: {date2 == date1}")
    print(f"date3 == date1: {date3 == date1}")
    print(f"date4 == date1: {date4 == date1}")

    dates: set = set()
    dates.add(date1)

    date5: MyDate = MyDate(2024, 1, 1)
    print(bool(date1))
    print(bool(date5))



if __name__ == "__main__":
    main()