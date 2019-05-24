def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    punct = ('.', '?', ':')
    lastIndex = 0
    for idx, letter in enumerate(text):
        if letter in punct:
            print(text[lastIndex:idx + 1].strip(), end='\n\n')
            lastIndex = idx + 1
    print(text[lastIndex:].strip(), end="")
