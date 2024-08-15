def all_variants(text):
    def generate_subsequences(index, current):
        if index == len(text):
            if current:
                yield current
            return
        yield from generate_subsequences(index + 1, current + text[index])
        yield from generate_subsequences(index + 1, current)
    yield from generate_subsequences(0, "")

a = all_variants("abc")
for i in a:
    print(i)