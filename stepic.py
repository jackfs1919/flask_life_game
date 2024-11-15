##%%
def alphabet():
    letter = yield
    while True:
        try:
            value = DICTIONARY[letter]
            letter = yield value
        except KeyError:
            letter = yield 'default'
            