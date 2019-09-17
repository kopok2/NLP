# coding=utf-8
"""Key Word in Context viewer."""


def load_text(path="NLP.txt"):
    return open(path).read().replace("\n", "|").replace("\t", "|").lower()


def kwic(text, key, context_len=48):
    division = text.split(key)
    result = []
    for x in range(1, len(division)):
        result.append(division[x - 1][-context_len:] + "  {0}  ".format(key) + division[x][:context_len])
    return result


if __name__ == "__main__":
    word = input("Enter key word:").lower()
    print("\n".join(kwic(load_text(), word)))
