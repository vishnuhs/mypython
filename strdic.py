def convert(text):
    words=text.split(";")
    words=dict(s.split("=")for s in words)
    return words

