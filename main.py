def amount(a: int, b: int) -> None:
    result = a + b
    print(f'result: {result}')

def difference(a: int, b: int) -> None:
    result = a - b
    print(f'result: {result}')

def product_strings(string: str, multiplier: int) -> str:
    return string * multiplier

if __name__ == '__main__':
    amount(10, 4)
    difference(12, 5)
    print(product_strings('test ', 10))