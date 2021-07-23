#check notes for question adn scenarios in work

data = [
    ['Live', 1, 100],
    ['A', 1, 101],
    ['B', 1, 110],
    ['C', 1, 110],
    ['D', 1, 150],
    ['A', 0, 140],
    ['E', 1, 160],
    ['E', 0, 162],
    ['A', 1, 165],
    ['D', 0, 180],
    ['A', 0, 185],
    ['Live', 0, 200]
]

active_users = {}
visited_users = {}

def calculations(user, state, time):
    if user == 'Live':
        if state == 1:
            print('Live session Started at ', time)
        else:
            endtime = time
            remains = len(active_users.keys())
            if remains > 0:
                for usr in active_users.keys():
                    visited_users.setdefault(usr, []).append(endtime-active_users[usr])
                    print(usr + ' was removed as Live is over')
            print('Live session ended at ', endtime)
            active_users.clear()
    if user != 'Live' and state == 0 and active_users[user]:
        visited_users.setdefault(user, []).append(time - active_users[user])
        active_users.pop(user)
        print('The user '+user + ' Left the session')
    if user != 'Live' and state == 1:
        active_users[user] = time
        if user in visited_users:
            print(user + ' is a Returned user')
    print('Total Active users ', len(active_users.keys()))
    print('Active Users ', active_users)
    print('Visited Users ', visited_users)


for inp in data:
    user, state, time = inp
    calculations(user, state, time)

vals = list(visited_users.values())
print(vals)
x = [sum(tm) for tm in visited_users.values()]
print(x)
print('Average time spent per users are ', round(sum(x)/len(x),2))
