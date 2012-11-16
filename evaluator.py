import re

def set_values(statement_list, aval, bval):
    new_list = []

    #for each statement replace each A with aval and B with bval
    for statement in statement_list:
        temp = re.sub('A', aval, statement)
        new_list.append(re.sub('B', bval, temp))

    return ' and '.join(new_list)

def evaluate_puzzle(statement_list):
    result_list = []

    #test if A is Knight and B is Knave
    result_list.append(eval(set_values(statement_list, 'True', 'False')))

    #test if A is Knave and B is Knight
    result_list.append(eval(set_values(statement_list, 'False', 'True')))

    #test if A is Knight and B is Knight
    result_list.append(eval(set_values(statement_list, 'True', 'True')))

    #test if A is Knave and B is Knave
    result_list.append(eval(set_values(statement_list, 'False', 'False')))
    
    return result_list



#test_list = ['A is True', 'B is False']
#test_list2 = ['B is not True', 'A is True and B is True']


#print evaluate_puzzle(test_list)
#print evaluate_puzzle(test_list2)
