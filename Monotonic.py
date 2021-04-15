# List = [1,1,2,3,4,5]
List = [1,2,3]

test = all(List[i] <= List[i+1] for i in range(len(List)-1)) or all(List[i] >= List[i+1] for i in range(len(List)-1))

print(test)