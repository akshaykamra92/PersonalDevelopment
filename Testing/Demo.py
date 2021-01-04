fruits = ['apple', 123, 'cherries']

mixed = [{'_id': '1234', 'email': '1 email', 'Canada': 'Montreal', 'Maharashtra': 'Mumbai'},
         {'_id': '5678', 'email': '2 email'}]

resourceid = []
print(resourceid)
for i in range(len(mixed)):
    # print(mixed[i])
    resourceid.append(mixed[i]['_id'])
print(resourceid)

# print(type(fruits[1]))
# print(dict1[0])



# print(dict1['_id'])
# print(dict1['email'])