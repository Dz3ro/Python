

def MostRepChar1(text: str):
    uniques = set(text.lower())
    counter = 0
    letterMax = 'a'
    for letter in uniques:
        if text.lower().count(letter) > counter:
            letterMax = letter
            counter = text.count(letter)
    return letterMax


def MostRepChar2(text: str):
    text = text.lower()
    uniques = set(text)
    uniqVal = {}
    for letter in uniques:
        uniqVal[letter] = text.count(letter)

    counter = 0
    letterMax = 'a'
    for key, value in uniqVal.items():
        if value > counter:
            counter = value
            letterMax = key
    return letterMax


def MostRepChar3(text: str):
    dict = {}
    text = text.lower()
    for letter in text:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

    sortedDict = sorted(dict.items(),
                        key=lambda kv: kv[1],
                        reverse=False)

    return sortedDict[-1][0]


def MostRepChar4(text: str):
    text = text.lower()
    dict = {}
    for letter in text:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    countMax, letterMax = 0, 'a'
    for key, val in dict.items():
        if text.count(key) > countMax:
            countMax = text.count(key)
            letterMax = key

    return letterMax



