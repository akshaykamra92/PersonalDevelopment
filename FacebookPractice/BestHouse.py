blocks = [
    {"gym": False,
     "school": True,
     "store": False
     },
    {"gym": True,
     "school": False,
     "store": False
     },
    {"gym": True,
     "school": True,
     "store": False
     },
    {"gym": False,
     "school": True,
     "store": False
     },
    {"gym": False,
     "school": True,
     "store": True
     }]

requirement = ["gym", "store", "school"]

dist = {}
for req in range(len(requirement)):
    for bl in range(len(blocks)):
    # blocks[bl]['gym']
        if blocks[bl][requirement[req]] is True:
            if bl+1 in dist:
                old = dist[bl+1]
                dist[bl+1] = old+(10**req)
            else:
                dist[bl+1] = 10**req
print(dist)
