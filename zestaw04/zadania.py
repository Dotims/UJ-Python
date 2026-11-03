# 4.2
def make_ruler(n):
    if n < 0:
        raise ValueError("n must not be negative")
    line = "|" + "....|" * n
    numbers = "0" + "".join(str(i).rjust(5) for i in range(1, n + 1))
    return line + "\n" + numbers


def make_grid(rows, cols):
    if rows < 0 or cols < 0:
        raise ValueError("rows and cols must not be negative")
    border = "+" + "---+" * cols
    row = "|" + "   |" * cols
    return "\n".join([border] + [row, border] * rows)


# 4.3
def factorial(n):
    if n < 0:
        raise ValueError("n must not be negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 4.4
def fibonacci(n):
    if n < 0:
        raise ValueError("n must not be negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 4.5
def odwracanie(L, left, right):
    if left < 0 or right >= len(L):
        raise ValueError("left and right must point inside the list")
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rek(L, left, right):
    if left < 0 or right >= len(L):
        raise ValueError("left and right must point inside the list")
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left + 1, right - 1)


# 4.6
def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total


# 4.7
def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    assert make_ruler(0) == "|\n0"
    assert make_ruler(3) == "|....|....|....|\n0    1    2    3"
    assert make_ruler(12) == (
        "|....|....|....|....|....|....|....|....|....|....|....|....|\n"
        "0    1    2    3    4    5    6    7    8    9   10   11   12")

    assert make_grid(1, 1) == "+---+\n|   |\n+---+"
    assert make_grid(2, 4) == ("+---+---+---+---+\n"
                               "|   |   |   |   |\n"
                               "+---+---+---+---+\n"
                               "|   |   |   |   |\n"
                               "+---+---+---+---+")
    assert make_grid(3, 1).count("\n") == 6
    assert make_grid(0, 2) == "+---+---+"

    for bad_call in (lambda: make_ruler(-1), lambda: make_grid(-1, 2),
                     lambda: make_grid(2, -1), lambda: factorial(-1),
                     lambda: fibonacci(-1),
                     lambda: odwracanie([1, 2, 3], 0, 3),
                     lambda: odwracanie([1, 2, 3], -1, 1),
                     lambda: odwracanie_rek([1, 2, 3], 0, 3),
                     lambda: odwracanie_rek([1, 2, 3], -1, 1)):
        try:
            bad_call()
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError expected")

    assert [factorial(n) for n in range(8)] == [
        1, 1, 2, 6, 24, 120, 720, 5040]
    assert factorial(20) == 2432902008176640000
    assert factorial(25) == 15511210043330985984000000

    assert [fibonacci(n) for n in range(10)] == [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci(50) == 12586269025
    assert fibonacci(90) == 2880067194370816120

    for reverse in (odwracanie, odwracanie_rek):
        L = [0, 1, 2, 3, 4, 5]
        reverse(L, 1, 4)
        assert L == [0, 4, 3, 2, 1, 5]
        reverse(L, 0, 5)
        assert L == [5, 1, 2, 3, 4, 0]
        reverse(L, 2, 2)
        reverse(L, 3, 1)
        assert L == [5, 1, 2, 3, 4, 0]
        E = []
        reverse(E, 0, -1)
        assert E == []
        S = ["a", "b", "c"]
        reverse(S, 0, 2)
        assert S == ["c", "b", "a"]
        alias = S
        reverse(S, 0, 2)
        assert alias is S and S == ["a", "b", "c"]

    assert sum_seq([]) == 0
    assert sum_seq([1, 2, 3]) == 6
    assert sum_seq([1, (2, 3), [4, [5, (6,)]]]) == 21
    assert sum_seq([[], ()]) == 0
    assert sum_seq((1.5, [2.5])) == 4.0

    sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    assert flatten(sequence) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten([]) == []
    assert flatten([[], [[]], ()]) == []
    assert flatten(["ab", ["c", ("d",)]]) == ["ab", "c", "d"]
    assert flatten((1, (2, (3, (4, (5,)))))) == [1, 2, 3, 4, 5]

    print(make_ruler(12))
    print(make_grid(2, 4))
    print(factorial(10), fibonacci(10))
    print(sum_seq(sequence), flatten(sequence))
