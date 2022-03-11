import json

data = [
    ['A', 123, 'Football'],
    ['B', 458, 'Swimming'],
    ['A', 123, 'TT'],
    ['B', 458, 'Football'],
    ['C', 898, 'Football'],
    ['A', 123, 'Cricket'],
    ['D', 5456, 'Cricket'],
]

final = []


# def jsoncreate(us, uid, sp):
#     if us in [i['user'] for i in final]:
#         for row in final:
#             if row['user'] == us:
#                 # print(row)
#                 row['sports'].append(sp)
#     else:
#         op = {'user': us
#               ,'id': uid
#               ,'sports': [sp]}
#         final.append(op)
#
#
# for val in data:
#     user, usid, sport = val
#     jsoncreate(user, usid, sport)
#
# print(final)

column = ['user', 'id', 'sport']

for line in data:
    op = {column[i]: line[i] for i in range(len(column))}
    final.append(op)

final = json.dumps(final)
print(final)