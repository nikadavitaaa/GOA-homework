def to_camelcase(text):
    words = text.replace('', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])