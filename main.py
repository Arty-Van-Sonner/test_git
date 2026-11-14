def amount(a: int, b: int) -> None:
    result = a + b
    print(f'result: {result}')

def difference(a: int, b: int) -> None:
    result = a - b
    print(f'result: {result}')

if __name__ == '__main__':
    amount(10, 4)
    difference(12, 5)