# 2.10
def count_words(line):
    return len(line.split())


# 2.11
def join_with_underscores(word):
    return "_".join(word)


# 2.12
def first_letters(line):
    return "".join(word[0] for word in line.split())


def last_letters(line):
    return "".join(word[-1] for word in line.split())


# 2.13
def total_length(line):
    return sum(len(word) for word in line.split())


# 2.14
def longest_word(line):
    return max(line.split(), key=len)


def longest_word_length(line):
    return len(longest_word(line))


# 2.15
def digits_string(L):
    return "".join(str(number) for number in L)


# 2.16
def replace_gvr(line):
    return line.replace("GvR", "Guido van Rossum")


# 2.17
def sort_alphabetically(line):
    return sorted(line.split())


def sort_by_length(line):
    return sorted(line.split(), key=len)


# 2.18
def count_zeros(number):
    return str(number).count("0")


# 2.19
def three_digit_blocks(L):
    return "".join(str(number).zfill(3) for number in L)


if __name__ == "__main__":
    line = """Python created by GvR
in 1991\tis   still
maintained by many people"""

    assert count_words(line) == 12
    assert count_words("") == 0

    assert join_with_underscores("word") == "w_o_r_d"

    assert first_letters(line) == "PcbGi1ismbmp"
    assert last_letters(line) == "ndyRn1sldyye"

    assert total_length(line) == 53

    assert longest_word(line) == "maintained"
    assert longest_word_length(line) == 10

    assert digits_string([1, 23, 456, 7]) == "1234567"

    assert replace_gvr(line).startswith("Python created by Guido van Rossum\n")
    assert "GvR" not in replace_gvr(line)

    fruits = "pear fig banana kiwi"
    assert sort_alphabetically(fruits) == ["banana", "fig", "kiwi", "pear"]
    assert sort_by_length(fruits) == ["fig", "pear", "kiwi", "banana"]

    assert count_zeros(10 ** 100) == 100
    assert count_zeros(2 ** 100) == 6

    assert three_digit_blocks([7, 24, 365, 1, 99]) == "007024365001099"
