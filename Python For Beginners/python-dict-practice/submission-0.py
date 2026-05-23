from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    out = {}
    for c in word:
        if c in out:
            out[c] = out[c]+1
        else:
            out[c] = 1
    return out




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
