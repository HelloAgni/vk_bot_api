import timeit

first = """
a = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
new_d = []
for x in a:
    if x not in new_d:
        new_d.append(x)
    """

second = """
a = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
s = set([tuple(x.items()) for x in a])
z = [dict(x) for x in s]
    """

print(timeit.timeit(first, number=100000))
print(timeit.timeit(second, number=10000))


def remove_duplicates(s):
    new = []
    for x in s:
        if x not in new:
            new.append(x)
    return new


a = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {}, {},
    {"key1": "value1"},
    {"key1": "value1"},
    {"key2": "value2"}
]
print(remove_duplicates(a))
