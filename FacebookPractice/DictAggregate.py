test = {'India': {'Maha': {'Mumbai': 50, 'Nagpur': 80}, 'Guj': {'Gandhi': 20, 'Ahmedabad':88}}, 'USA':{'Alabama':{'BHM':15}}}
# { India: 2222, USA: 312312}
# for key in test:
#     print(key)

final = {}


def flatten(master, dic):
    for key, val in dic.items():
        if isinstance(val, dict):
            flatten(master, val)
        else:
            final.setdefault(master,0)
            final[master] += dic[key]


for key in test:
    flatten(key, test[key])

print(final)
# final = {key: sum(value) for key, value in final.items()}
# print(final)
