def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in range(len(text)):
            subseq = text[j:j + i]
            if len(subseq) == i:
                yield subseq
            else:
                continue


a = all_variants("abc")
for i in a:
    print(i)
