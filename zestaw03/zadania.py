# 3.3
def without_multiples_of_3_for(n):
    L = []
    for i in range(n + 1):
        if i % 3 != 0:
            L.append(str(i))
    return " ".join(L)


def without_multiples_of_3_while(n):
    L = []
    i = 0
    while i <= n:
        if i % 3 != 0:
            L.append(str(i))
        i += 1
    return " ".join(L)


# 3.5
def ruler(x):
    line = "|" + "....|" * x
    numbers = "0" + "".join(str(i).rjust(5) for i in range(1, x + 1))
    return line + "\n" + numbers


# 3.6
def rectangle(x, y):
    border = "+" + "---+" * x
    row = "|" + "   |" * x
    return "\n".join([border] + [row, border] * y)


# 3.8
def common_elements(a, b):
    return sorted(set(a) & set(b))


def all_elements(a, b):
    return sorted(set(a) | set(b))


# 3.9
def sums(sequences):
    return [sum(seq) for seq in sequences]


# 3.10
D1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

D2 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

D3 = dict(zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000]))

D4 = {}
for letter, value in [("I", 1), ("V", 5), ("X", 10), ("L", 50),
                      ("C", 100), ("D", 500), ("M", 1000)]:
    D4[letter] = value


def roman2int(roman):
    total = 0
    for i, letter in enumerate(roman):
        value = D1[letter]
        if i + 1 < len(roman) and value < D1[roman[i + 1]]:
            total -= value
        else:
            total += value
    return total


if __name__ == "__main__":
    expected = ("1 2 4 5 7 8 10 11 13 14 16 17 19 20 "
                "22 23 25 26 28 29")
    assert without_multiples_of_3_for(30) == expected
    assert without_multiples_of_3_while(30) == expected
    assert without_multiples_of_3_for(0) == ""

    assert ruler(0) == "|\n0"
    assert ruler(3) == "|....|....|....|\n0    1    2    3"
    assert ruler(12).split("\n")[1].endswith("9   10   11   12")

    assert rectangle(1, 1) == "+---+\n|   |\n+---+"
    assert rectangle(4, 2) == ("+---+---+---+---+\n"
                               "|   |   |   |   |\n"
                               "+---+---+---+---+\n"
                               "|   |   |   |   |\n"
                               "+---+---+---+---+")

    assert common_elements([1, 2, 2, 3], (3, 2, 4)) == [2, 3]
    assert all_elements([1, 2, 2, 3], (3, 2, 4)) == [1, 2, 3, 4]
    assert common_elements("abca", "bcd") == ["b", "c"]
    assert all_elements("abca", "bcd") == ["a", "b", "c", "d"]
    assert common_elements([1, 2], [3]) == []

    assert sums([[], [4], (1, 2), [3, 4], (5, 6, 7)]) == [0, 4, 3, 7, 18]
    assert sums([]) == []

    assert D1 == D2 == D3 == D4
    assert roman2int("III") == 3
    assert roman2int("IV") == 4
    assert roman2int("IX") == 9
    assert roman2int("XLII") == 42
    assert roman2int("MCMXCIV") == 1994
    assert roman2int("MMXXVI") == 2026

    x = 12
    y = 2
    print(without_multiples_of_3_for(30))
    print(ruler(x))
    print(rectangle(4, y))
