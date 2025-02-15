# Python script for tpc1.

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
                break
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



if __name__ == '__main__':
    pass
    #add tests later

