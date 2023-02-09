
from typing import types

def fib_from_text(text_input:str)->list:
    
    ''' This functions has one parameter it is a text
        and returns a list of fibonaci numbers with 
        last number not bigger than the length of text_input.'''
        
    num_list = [1]

    for i in range(len(text_input)-1):
        if num_list[-1]<len(text_input):
            if not(text_input[i].isspace()):
                if len(num_list)==1:
                    num_list.append(1)
                else:
                    num_list.append(num_list[-1]+num_list[-2])    
                    
    if num_list[-1]>len(text_input):
        num_list=num_list[:-1]
        
    return num_list






