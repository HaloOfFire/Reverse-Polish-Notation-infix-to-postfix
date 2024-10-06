
import sys


NUMBERS = ['0','1','2','3','4','5','6','7','8','9']         #in caps to show its a constant prob could just add x here to save data but reduces redundancy
LOWERCASELETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPERCASELETTERS = ['A','B''C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   
LETTERS = LOWERCASELETTERS.extend(UPPERCASELETTERS)
NUMBERSANDLETTERS = []
NUMBERSANDLETTERS.extend(LETTERS)
NUMBERSANDLETTERS.extend(NUMBERS)                            #is this more efficent/ useful?
FUNCTIONS = ['sin','cos','tan']          #can add more functions
OPERATORS = {'+':2,'-':2,'*':3,'/':3,'^':4}            #dictionary first value is sign 2nd is presedent of sign


def translate_into_rpn(equation):
    output = []
    operator_stack = []
    count = 0
    equation = equation.replace('**','^')                     #because calculator stores powers as **
    while count < len(equation):
        len_of_number = count


        while (len(equation) > len_of_number) and  (equation[len_of_number] in NUMBERSANDLETTERS):
            len_of_number = len_of_number + 1

        if len_of_number > count:
            output.append(equation[count:len_of_number])
            count = count + (len_of_number - count)

        elif equation[count:count+3] in FUNCTIONS:                         #is not using elif more effiecent because it moves count on and loops through big while loop less                                                            
            operator_stack.append(equation[count:count+3])                     #move to end of elif to increase efficency
            count = count + 3                      

        elif equation[count] in OPERATORS:                   
            while (len(operator_stack) > 0) and (operator_stack[-1] != '(') and ((OPERATORS[equation[count]] < OPERATORS[operator_stack[-1]]) or ((OPERATORS[equation[count]] == OPERATORS[operator_stack[-1]]) and ((OPERATORS[equation[count]] == 2 ) or (OPERATORS[equation[count]] == 3)))):      #add at end? and (OPERATORS[equation[count]] == (2 or 3) )
               output.append(operator_stack.pop())
            operator_stack.append(equation[count])
            count = count + 1

        elif equation[count] == '(':
            operator_stack.append('(')
            count = count + 1
      

        elif (equation[count] == ')') and (len(operator_stack) > 0):
            while operator_stack[-1] != '(':
                output.append(operator_stack.pop())                         
            operator_stack.pop()                                #deletes right bracket from operator stack
            if (len(operator_stack) > 0) and ((operator_stack[-1] in FUNCTIONS)):        
                output.append(operator_stack.pop())
            count = count + 1

        else:
            count = count + 1
            print('error, unaccepted charachter inputed')              #even though error message, program still works

        
    while len(operator_stack) > 0:
        if operator_stack[-1] == '(':
            operator_stack.pop()
        else:
            output.append(operator_stack.pop())
    
    return(output)



equation = input('input:   ')
print(str(translate_into_rpn(equation)))