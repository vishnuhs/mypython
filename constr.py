def convert(text):
    words=text.split(";")
    for word in words:
        strwords=word.split("=")
        words[words.index(word)]=(strwords[0],strwords[1])
    return words

    
