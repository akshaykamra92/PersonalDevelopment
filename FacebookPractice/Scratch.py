# data = {"headers": {"Employee": ["Id", "Name", "Salary", "DepartmentId"], "Department": ["Id", "Name"]},
#         "rows": {"Employee": [[1, "Joe", 85000, 1], [2, "Henry", 80000, 2], [3, "Sam", 60000, 2], [4, "Max", 90000, 1],
#                               [5, "Janet", 69000, 1], [6, "Randy", 85000, 1], [7, "Will", 70000, 1]],
#                  "Department": [[1, "IT"], [2, "Sales"]]}}
#
#
# for hd in data:
#     if hd == 'headers':
#         emp_headers = data[hd]['Employee']
#         dept_headers = data[hd]['Department']
#     else:
#         emp = data[hd]['Employee']
#         dept = data[hd]['Department']
#
# for lines in emp:
#     op = 'Insert into '+','.join(emp_headers) + ' values ('+','.join(map(str, lines)) + ')'
#     print(op)


data = [
    ['A', 'AL', 150],
    ['B', 'NH', 150],
    ['C', 'NY', 150],
    ['D', 'NY', 150],
    ['B', 'GA', 150],
    ['F', 'FL', 150],
    ['G', 'IL', 150],
    ['H', 'AL', 150],
]
#
#
# def jsoncreater(li):
#     out = {'user': li[0],
#            'state': li[1],
#            'score': li[2]}
#     return out
#
#
# L_states = list(filter(lambda x: x[1][1] == 'L', data))
# other_states = list(filter(lambda x: x[1][1] != 'L', data))
#
# L_json = list(map(jsoncreater, L_states))
# print(L_states)
# print(L_json)
#
# dic = {'A': [1,2], 'C': [23,1], 'B': [4,7]}
# dic1 = max(dic, key= lambda x: len(dic[x]))
# # #
# print(dic1)
# # test = dic.get('D', 'balasdk')
# print(dic.get('D'))
# op = max(dic,key=dic.get)
# print(op)

# op = sorted(data, key=lambda x: x[1] ,reverse = True)
# op = min(data,key=lambda x: x[1])
# print(op)
# dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
# dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
#
# op = dict(zip(dict_one.items(), dict_two.items()))
# print(op)
t1 = [1,2,3,4]
t2 = [2,3,4,5]
t3 = [6,7,8,8]

op = dict(zip(t1,t2,t3))
print(op)