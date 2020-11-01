N = int(input())
my_string_list = []
for i in range(N):
    my_string_list.append(input())

def is_valid_ps(test_string):
    test_list = list(test_string)             
    l = len(test_list)                         
    while len(test_list) > 0:                   
        if len(test_list) == 1:
            return "NO"
        is_change = False
        for i in range(l - 1):
            if i >= len(test_list) - 1:
                break
            if test_list[i] == '(' and test_list[i + 1] == ')':
                del (test_list[i + 1])
                del (test_list[i])
                is_change = True
        if is_change == False:                                              
            return "NO"
    return "YES"

for i in range(N):
    print(is_valid_ps(my_string_list[i]))