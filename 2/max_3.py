#!/usr/bin/python3

MAX = 33
data = [6, 22, 93, 35, 44, 34, 5, 13, 50, 50, 47, 5, 44, 11, 31, 21, 6, 41, 78, 3]
print([r for r in filter(lambda x: x > MAX, data)][:3])
