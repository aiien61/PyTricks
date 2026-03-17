from icecream import ic

def manipulate_counter():
    from collections import Counter

    machines: list[str] = ["M1","M1","M2","M3","M1"]
    c = Counter(machines)
    ic(c)

    c = Counter()
    c['spam'] += 1
    c[100] += 1
    c[200] += 1
    c[200] += 2
    ic(c)

    c1 = Counter(spam=1, ham=2)
    c2 = Counter(ham=3, egg=4)
    ic(c1, c2)
    ic(c1 + c2)
    ic(c1 & c2)
    ic(c1 | c2)
    c1 += c2
    ic(f'c1 += c2 => {c1}')

    unseen = Counter([1, 1, 2, 3, 3])
    seen = Counter()
    ic(unseen)
    ic(seen)
    seen[1] += 1
    seen[1] += 1
    seen[3] += 1
    ic(seen)
    ic(unseen - seen)

    # Counter 的加減法運算遇到負值不容易理解，盡量少用負值
    # It's not easy to read that how Counter operations deal with negative values under the hood.
    # Avoid to use negatives in Counter
    c1 = Counter(spam=-1, ham=2)
    c2 = Counter(ham=2, egg=-3)
    ic(c1)
    ic(c2)
    ic(c1 + c2) # ignore negative values
    ic(c1 - c2)

    c = Counter(spam=-1, ham=2)
    ic(c)
    ic(+c)
    ic(-c)

def manipulate_chainmap():
    from collections import ChainMap

    # 1. Default Config: 系統最基礎的預設值
    default_config = {
        "theme": "light",
        "language": "en",
        "show_tips": True,
        "max_retries": 3
    }
    
    # 2. Factory Config: 出廠設定（可能覆蓋部分預設值）
    factory_config = {
        "theme": "dark",
        "language": "zh-TW",
        "region": "TW"
    }

    # 3. Scenario Config: 特定情境（例如：簡報模式、測試環境）
    scenario_config = {
        "show_tips": False,
        "fullscreen": True
    }

    # 4. Runtime Config: 執行時期的使用者操作或參數傳遞
    runtime_config = {
        "max_retries": 5,
        "session_id": "ABC-123"
    }

    # 建立 ChainMap，順序由左至右（由高優先權到低優先權）
    config = ChainMap(
        runtime_config,    # 優先權 1
        scenario_config,   # 優先權 2
        factory_config,    # 優先權 3
        default_config     # 優先權 4
    )

    # 驗證執行結果
    print(f"Max Retries (Runtime 優先): {config['max_retries']}")
    print(f"Theme (Factory 覆蓋了 Default): {config['theme']}")
    print(f"Show Tips (Scenario 覆蓋了 Default): {config['show_tips']}")
    print(f"Language (Factory 提供的值): {config['language']}")

    d1 = {'spam': 1}
    d2 = {'ham': 2}
    c = ChainMap(d1, d2)
    ic(c['spam'])
    ic(c['ham'])

    d1 = {'spam': 1}
    d2 = {'ham': 2}
    c = ChainMap(d1, d2)
    c['bacon'] = 3
    ic(d1)
    ic(d2)
    ic(c)
    c.clear()
    ic(c)
    ic(d1)
    ic(d2)

def manipulate_defaultdict():
    from collections import defaultdict

    def value():
        return 'default-value'
    d = defaultdict(value, spam=100)
    ic(d)
    ic(d['ham'])

    c = defaultdict(int)
    ic(c)
    ic(c['spam'])
    c['spam'] += 100
    ic(c)

    c = defaultdict(list)
    ic(c)
    c['spam'].append(100)
    c['spam'].append(200)
    ic(c)

def manipulate_deque():
    import statistics as stats
    from collections import deque

    d = deque('spam')
    ic(d)
    ic(d[1])
    d[1] = 'P'
    ic(d)
    try:
        ic(d[1:-1])
    except TypeError as e:
        print(e)
        print("d[1:-1], slicing is not yet supported in deque.")

    d = deque(maxlen=5)
    ic(d)
    for v in range(10):
        d.append(v)
        if len(d) >= 5:
            ic(list(d), stats.mean(d))

    d = deque('12345')
    ic(d)
    d.rotate(1) # 
    print(f"d.rotate(1) => {d}")
    d.rotate(-3)
    print(f"d.rotate(-3) => {d}")

    d = deque('12345')
    ic(d)
    first = d.popleft()
    print(f"first = d.popleft(), first: {first}")
    ic(d)
    d.rotate(-1)
    print(f"d.rotate(-1) => {d}")
    d.appendleft(first)
    d.rotate(1)
    print(f"d.appendleft(first) => d.rotate(1) => d: {d}")

    d = deque('12345')
    d[0], d[1] = d[1], d[0]
    ic(d)

def manipulate_heapq():
    import heapq

    queue = []
    heapq.heappush(queue, 2)
    heapq.heappush(queue, 1)
    heapq.heappush(queue, 0)
    heapq.heappush(queue, 3)
    ic(queue)
    while queue:
        try:
            ic(heapq.heappop(queue))
        except IndexError as e:
            ic(e)
    
    queue = [5, 4, 3, 2, 1]
    ic(queue)
    heapq.heapify(queue)
    ic(queue)
    # add a new value and remove the min value simultaneousl7
    ic(heapq.heappushpop(queue, 6))
    ic(queue)
    ic(heapq.heappushpop(queue, 7))
    ic(queue)

    # heappushpop vs. heapreplace
    # heappushpop: add the new value first, and remove the min value
    # heapreplace: remove the min value, and add the new value
    queue = [3, 2, 1]
    heapq.heapify(queue)
    ic(queue)
    ic(heapq.heappushpop(queue, 0))
    ic(queue)
    ic(heapq.heapreplace(queue, 0))
    ic(queue)

def manipulate_bisect():
    import bisect

    seq = [0, 1, 2, 2, 3, 4, 5]
    ic(seq)
    # Return the index of first value 2
    ic(bisect.bisect_left(seq, 2))
    # Return the index of the next value of last value 2
    ic(bisect.bisect_right(seq, 2))

    seq = list(range(6))
    ic(seq)
    bisect.insort_left(seq, 3)
    ic(seq)

def manipulate_array():
    import time
    from array import array

    arr = array('f', [1, 2, 3])
    ic(arr)

    arr.append(100)
    arr[2] = 200
    ic(arr)

    del arr[-1]
    ic(arr)

    ic(sum(arr))

    a = array('f', range(1_000_000))
    b = list(range(1_000_000))
    t1 = time.time()
    ic(sum(a))
    ic(time.time() - t1)

    t2 = time.time()
    ic(sum(b))
    ic(time.time() - t2)

    arr_to_save = array('i', range(1, 6))
    ic(arr_to_save)
    with open('bin-int', 'wb') as f:
        arr_to_save.tofile(f)

    arr_to_open = array('i')
    with open('bin-int', 'rb') as f:
        arr_to_open.fromfile(f, 5)
    
    ic(arr_to_open)

def manipulate_weakref():
    import weakref

    def share_file(filename):
        if filename not in _files:
            ret = _files[filename] = open(filename)
        else:
            ret = _files[filename]
        return ret
    
    _files = {}
    ic(share_file('bin-int'))
    _files = weakref.WeakValueDictionary()
    ic(share_file('bin-int'))

def manipulate_enum():
    from enum import Enum, unique
    class City(Enum):
        TOKYO = 'tokyo'
        KYOTO = 'kyoto'
        OSAKA = 'osaka'

    ic(list(City))
    data_center = City.TOKYO
    ic(data_center.name)
    ic(data_center.value) 

    class Spam(Enum):
        HAM = 1
        EGG = 2
        BACON = 3
    
    ic(list(Spam))
    ic(isinstance(Spam.HAM, Spam))
    ic(Spam.HAM == Spam.HAM)
    ic(Spam.EGG == Spam.BACON)

    class Spam2(Enum):
        HAM = 1
        EGG = 2
        BACON = 2

    ic(list(Spam2))
    ic(Spam.HAM == Spam2.HAM)
    ic(Spam.HAM == 1)

    try:
        @unique
        class Spam(Enum):
            HAM = 1
            EGG = 1
    except ValueError as e:
        ic(e)

    class Spam(Enum):
        HAM = 1
        EGG = 2
        BACON = 1
    
    ic(list(Spam))

def manipulate_itertools():
    import itertools

    def spam(left, right):
        ic(left, right)
        return left * right
    
    for v in itertools.accumulate([1, 2, 3], spam):
        ic(v)

    iters = itertools.accumulate([1, 2, 3], spam)
    ic(iters)
    while True:
        try:
            ic(next(iters))
            print('-'*10)
        except StopIteration as e:
            ic(e)
            break

    iters = itertools.chain([1, 2, 3], {'a', 'b', 'c'})
    ic(iters)
    for v in iters:
        ic(v)

    iters = ([1, 2, 3], {'a', 'b', 'c'})
    ic(iters)
    for c in itertools.chain.from_iterable(iters):
        ic(c)

    # Find all the permutations
    print('--- Find all the permutations ---')
    for v in itertools.permutations('ABC', 2):
        ic(v)

    # Find all the combinations
    print('--- Find all the combinations ---')
    for v in itertools.combinations('ABC', 2):
        ic(v)

    # Find all the combinations including identical pairs
    print('--- Find all the combinations ncluding identical pairs ---')
    for v in itertools.combinations_with_replacement('ABC', 2):
        ic(v)

    # Find all the product pairs of two groups
    print('--- Find all the product pairs of two groups ---')
    for v in itertools.product('ABC', [1,2,3]):
        ic(v)

    # Find all the product pairs of two groups
    print('--- Find all the product pairs of two groups, repeat = 1 ---')
    for v in itertools.product('ABC', [1,2,3], repeat=1):
        ic(v)

    def prod():
        for p in 'ABC':
            for q in [1,2,3]:
                yield(p, q)
    print('same as prod')
    for v in prod():
        ic(v)

    # Find all the product pairs of two groups
    print('--- Find all the product pairs of two groups, repeat = 2 ---')
    for v in itertools.product('ABC', [1,2,3], repeat=2):
        ic(v)

    def prod():
        for p in 'ABC':
            for q in [1,2,3]:
                for r in 'ABC':
                    for s in [1,2,3]:
                        yield(p, q, r, s)
    print('same as prod')
    for v in prod():
        ic(v)

    # filter
    print('--- filter vs. itertools.filterfalse ---')
    def is_even(n):
        return n % 2 == 0

    print('--- filter: is even ---')
    for v in filter(is_even, [1,2,3,4,5,6]):
        ic(v)
    
    print('--- filter: is not empty ---')
    items = [1, 0, 'Spam', '', [], [1]]
    ic(items)
    for v in filter(None, items):
        ic(v)

    print('--- itertools.filterfalse: is odd ---')
    for v in itertools.filterfalse(is_even, [1,2,3,4,5,6]):
        ic(v)

    print('--- itertools.filterfalse: is empty ---')
    for v in itertools.filterfalse(None, items):
        ic(v)

    # itertools.compress
    # first group: data
    # second group: selectors / filters for the first group
    print('--- itertools.compress ---')
    for v in itertools.compress(['spam', 'ham', 'egg'], [1, 0, 1]):
        ic(v)

    # 等差級數
    # count(start, step)
    print('--- itertools.count ---')
    for v in itertools.count(1, 2):
        if v > 5:
            break
        ic(v)

    # islice(iterable, stop)
    # islcie(iterable, start, stop, step)
    print('--- itertools.islice ---')
    ic(list(itertools.islice([0,1,2,3,4,5,6,7,8,9], 5)))
    ic(list(itertools.islice(itertools.count(1, 1), 3, 8, 2)))

    print('--- itertools.dropwhile ---')
    def is_odd(v):
        return v % 2
    
    # if true, drop it
    ic(list(itertools.dropwhile(is_odd, [1, 1, 1, 2, 3, 4])))

    print('--- itertools.takewhile ---')
    # if true, take it
    ic(list(itertools.takewhile(is_odd, [1, 1, 1, 2, 3, 4])))

    print('--- itertools.repeat ---')
    # generate repeated values
    ic(list(itertools.repeat('a', 5)))
    ic(['a'] * 5)

    print('--- itertools.cycle ---')
    # repeating the cycle
    for v in itertools.islice(itertools.cycle('abc'), 1, 5):
        ic(v)

    print('--- itertools.groupby by same values ---')
    for value, group in itertools.groupby(['a', 'b', 'b', 'c', 'c', 'c']):
        ic(value, group, tuple(group))
    
    print('--- itertools.groupby by customised key ---')
    for value, group in itertools.groupby([10, 20, 31, 11, 3, 10], key=is_odd):
        ic(value, tuple(group))
    
    print('--- itertools.zip_longest ---')
    for v in zip((1,2,3), ('a','b','c'),('', '', '')):
        ic(v)
    
    matrix = [(1,2,3), (4,5,6), (7,8,9)]
    ic(matrix)
    # transposition
    transformed = list(zip(*matrix))
    ic(transformed)
    # transpose back to original
    ic(list(zip(*transformed)))

    # similar with zip, but if we got iterable values in short, replace with fillvalue 
    for v in itertools.zip_longest('abcdefg', '123', ' ', fillvalue='-'):
        ic(v)

    print('--- itertools.starmap ---')
    # apply chr function to each item in the iterable sequence
    for v in map(chr, [0x40, 0x41, 0x42, 0x43]):
        ic(v)  # v is chr(x) for x == 0x40, 0x41, ...
    
    iterables = [[1,2,3], [-1,-2,-3], [0,100]]
    for v in map(min, iterables):
        ic(v)

    for v in itertools.starmap(min, iterables):
        ic(v)
    
    print('--- itertools.tee ---')
    ic(itertools.tee('abc', 2))
    for u in itertools.tee('abc', 2):
        for v in u:
            ic(v)

if __name__ == "__main__":
    # manipulate_counter()
    # manipulate_chainmap()
    # manipulate_defaultdict()
    # manipulate_deque()
    # manipulate_heapq()
    # manipulate_bisect()
    # manipulate_array()
    # manipulate_weakref()
    # manipulate_enum()
    manipulate_itertools()
