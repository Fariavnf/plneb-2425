# Python script do tpc1.

def ex1(string):
    return string[::-1]


def ex2(string):
    char_map = {'a': 0, 'A': 0}

    for char in string:
        if char in char_map.keys():
            char_map[char] += 1

    return char_map


def ex3(string):

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count


def ex4(string):
    return string.lower()


def ex5(string):
    return string.upper()


def ex6(string):

    lenght = len(string)

    for i in range(lenght//2):
        if string[i] != string[lenght-i-1]:
            return False

    return True


def ex7(string1, string2):

    for char in string1:
        if char not in string2:
            return False

    return True


def ex8(string1, string2):

    if len(string1) > 0:
        count = 0
        start = 0

        while True:
            start = string2.find(string1, start)
            if start == -1:
                return count
            count += 1
            start += 1
    else:
        return 0


def ex9(string1, string2):
    char_map = {}

    if len(string1) != len(string2):
        return False

    for char in string1:
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map[char] += 1

    for char in string2:
        if char not in char_map:
            return False
        else:
            char_map[char] -= 1

    if sum(char_map.values())  != 0:
        return False

    return True

def ex10(stringList):
        anagram_map = {}

        for string in stringList:
            key = ''.join(sorted(string))
            if key not in anagram_map:
                anagram_map[key] = [string]
            else:
                anagram_map[key].append(string)

        return anagram_map


def test(num_exercise, func, expected_output, *args):
    try:
        output = func(*args)
        assert output == expected_output, f"Test {num_exercise} failed: Expected {expected_output}, but got {output}"
        print(f"\n----- EX{num_exercise} PASSED -----")
        print(f"Output: {output} -----> Expected: {expected_output} ")
    except AssertionError as e:
        print(f"\n----- EX{num_exercise} FAILED -----")
        print(e)



if __name__ == "__main__":

    test(1, ex1, "aid mob", "bom dia")
    test(2, ex2, {'a': 2, 'A': 1}, "boA tArde")
    test(2, ex2, {'a': 0, 'A': 2}, "boA tArde")
    test(3, ex3, 4, "bOa noIte")
    test(3, ex3, 5, "bOa noIte")
    test(4, ex4, "bom dia", "bOM diA")
    test(5, ex5, "BOA TARDE", "Boa tardE")
    test(6, ex6, True, "radar")
    test(6, ex6, False, "boa noite")
    test(7, ex7, True, "dois", "esternocleidomastoideu")
    test(7, ex7, False, "esternocleidomastoideu", "bom dia")
    test(8, ex8, 2, "aba", "abababa")
    test(8, ex8, 3, "aba", "abababa")
    test(8, ex8, 0, "abc", "")
    test(9, ex9, True, "listen", "silent")
    test(9, ex9, False, "hello", "world")
    test(9, ex9, False, "roma", "")
    test(9, ex9, True, "", "")
    test(10, ex10,
         {'amor': ['roma', 'amor'], 'aacss': ['sacas', 'casas'], 'egirt': ['tigre', 'trige'], 'aceimn': ['iceman', 'cinema'], 'hinoosz': ['sozinho']},
         ["roma", "amor", "sacas", "casas", "tigre", "trige", "iceman", "cinema", "sozinho"])

