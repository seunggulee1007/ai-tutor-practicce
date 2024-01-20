from typing import Tuple, List, Union

# Typing Variable 
a: int = 1
b: str = 'ABCD'
c: list = [1, 2, 3]


some_list: List[str] = ['a', 'b', 'c']
some_tuple: Tuple[str, int, int] = ('a', 1, 2)


# Typing function
def add(a: int, b: int) -> int:
    return a - b


def n_times(a: Union[int, float], b: List[int]) -> List[Union[int, float]] :
    return [a * elem for elem in b]
