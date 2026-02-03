#!/bin/env python3

def main():
    strings = []
    with open("test_3.txt") as f:
        for l in f:
            strings.append(l.strip())
    maxi = 0
    for shorts in strings:
        maxi = max(shorts)
        positions = [i for i, d in enumerate(shorts) if d == maxi]
        print(maxi, positions)
    return "done"
if __name__ == "__main__":
    print(main())
