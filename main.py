def amount(a: int, b: int) -> int:
    result = a + b
    return result

def difference(a: int, b: int) -> int:
    result = a - b
    return result

def product(a: int, b: int) -> int:
    result = a * b
    return result

def division(a: int, b: int) -> float:
    result = a / b
    return result

if __name__ == '__main__':
    print(amount(10, 4))
    print(difference(12, 5))
    print(product(10, 4))
    print(division(20, 5))
    