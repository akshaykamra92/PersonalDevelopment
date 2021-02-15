input_list=['cat','brt', 'moonalisa', 'draft', 'fmt']
var = 'brt'
if var in input_list:
    print(True)
for word in input_list:
    if len(word) == len(var):
        for i in range(len(var)):
            # print(i)
            if word[i] == var[i] or var[i] == "." :
                flag= True
            else:
                flag= False
                break
        if flag == True :
            print(word)