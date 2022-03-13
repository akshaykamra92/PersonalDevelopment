a = {
    "items": [
        {
            "id": "12345",
            "links": {
                "self": "https://www.google.com"
            },
            "name": "beast",
            "type": "Device"
        }
    ],
    "links": {
        "self": "https://www.google.com"
    },
    "paging": {
        "count": 1,
        "limit": 1,
        "offset": 0,
        "pages": 1
    }
}


def dict_get(x, key, here=None):
    x = x.copy()
    if here is None: here = []
    if x.get(key):
        here.append(x.get(key))
        x.pop(key)
    else:
        for i, j in x.items():
            if isinstance(x[i], list): dict_get(x[i][0], key, here)
            if isinstance(x[i], dict): dict_get(x[i], key, here)
    return here


print(dict_get(a, 'self'))

# test = {'apple': 12, 'mango': 34}
# # op = test.get('apple')
# # print(op)
# # print(test)
