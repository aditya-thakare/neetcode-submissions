from typing import List

def read_integers() -> List[int]:
    i = input()
    l = i.split(",")
    j = []
    for i in l:
        j.append(int(i))
    return j

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
