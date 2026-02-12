from icecream import ic
import re

def test_search():
    pattern: str = r"\d{2}"
    source: str = "There are 20 books."

    result = re.search(pattern, source)
    print(result)


def test_match():
    pattern: str = r"\d{2}"
    source: str = "20 books."

    result = re.match(pattern, source)
    print(result)

def test_fullmatch():
    pattern: str = r"\d{2}"
    source: str = "20"

    result = re.fullmatch(pattern, source)
    print(result)

def test_findall():
    pattern: str = r"\d{2}"
    source: str = "There are 20 books and 30 pencils."

    result = re.findall(pattern, source)
    print(result)

def test_finditer():
    pattern: str = r"\d{2}"
    source: str = "There are 20 books and 30 pens."

    result = re.finditer(pattern, source)
    print([x for x in result])

def test_compile():
    pattern: str = r"\d{2}"
    pattern_obj = re.compile(pattern)

    source: str = "There are 20 books and 30 pens."
    ic(pattern_obj.search(source))
    ic(pattern_obj.match(source))
    ic(pattern_obj.fullmatch(source))
    ic(pattern_obj.findall(source))
    ic([x for x in pattern_obj.finditer(source)])

def main():
    test_search()
    test_match()
    test_fullmatch()
    test_findall()
    test_finditer()
    test_compile()

if __name__ == "__main__":
    main()
