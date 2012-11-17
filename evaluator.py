import re

def evaluate(statement_list, A, B):
    return eval(statement_list[0]) is A and \
           eval(statement_list[1]) is B

def evaluate_puzzle(statement_list):
    result_list = []

    #test if A is Knight and B is Knave
    result_list.append(evaluate(statement_list, True, False))

    #test if A is Knave and B is Knight
    result_list.append(evaluate(statement_list, False, True))

    #test if A is Knight and B is Knight
    result_list.append(evaluate(statement_list, True, True))

    #test if A is Knave and B is Knave
    result_list.append(evaluate(statement_list, False, False))
    
    return result_list



#test_list = ['A is True', 'B is False']
#test_list2 = ['B is not True', 'A is True and B is True']


#print evaluate_puzzle(test_list)
#print evaluate_puzzle(test_list2)
