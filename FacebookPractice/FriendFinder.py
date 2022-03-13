friends = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'C'], ['R','M'], ['S'], ['P'], ['A'], ['B', 'A']]

frnds_dict = {}


def friendships(inp):
    if len(inp) == 1:
        frnds_dict.setdefault(inp[0], [])
    elif len(inp) == 2:
        frnds_dict.setdefault(inp[0], []).append(inp[1])
        frnds_dict.setdefault(inp[1], []).append(inp[0])


for frd in friends:
    friendships(frd)

print(frnds_dict)
number = {key: len(set(value)) for key,value in frnds_dict.items()}
print(number)
top_friend = max(number, key=number.get)
print(top_friend)