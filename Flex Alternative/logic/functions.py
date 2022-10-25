import string
import sys
sys.path.append('../data')

from structures import Stack

def add_concatenation_operation(regex, alphabet):
    temp_regex = list(regex)
    new_regex = ""
    for i in range(len(temp_regex)-1):
        if ((temp_regex[i] in alphabet or temp_regex[i]==')') and (temp_regex[i+1] in alphabet or temp_regex[i+1] == '(' )):
            new_regex = new_regex + temp_regex[i] + ".";
        elif ((temp_regex[i]==')' or temp_regex[i]=='*') and (temp_regex[i+1] in alphabet or temp_regex[i+1]=='(')):
            new_regex = new_regex + temp_regex[i] + ".";
        else:
            new_regex += temp_regex[i]
    new_regex += temp_regex[-1]
    return new_regex

def has_higher_precedence(first_operator, second_operator):
    return (first_operator <= second_operator)

def infix_to_postfix(regex, alphabet, operations):
    operation_order = Stack();
    post_string = ""
    for i in range(len(regex)):
        if regex[i] in alphabet:
            post_string += regex[i]
        elif regex[i] in operations:
            while (not operation_order.is_empty() and has_higher_precedence(operation_order.peek(), regex[i])) and (operation_order.peek()!='('):
                post_string += operation_order.pop()
            operation_order.push(regex[i])
        elif regex[i]=='(':
            operation_order.push('(')
        elif regex[i]==')':
            while (not operation_order.is_empty() and operation_order.peek()!='('):
                post_string += operation_order.pop()
            operation_order.pop()

    while (not operation_order.is_empty()):
        post_string += operation_order.pop()
    return post_string

def remove_hyphens(regex):
    while '-' in regex:
        index = regex.index('-')
        replacement = ""
        if regex[index-1] in string.ascii_letters:
            first_char_index = string.ascii_letters.index(regex[index-1])
            last_char_index = string.ascii_letters.index(regex[index+1])
            for i in range(first_char_index, last_char_index):
                replacement += string.ascii_letters[i] + '|'
            #replacement += string.ascii_letters[last_char_index]
            regex = regex[:index-1] + replacement + regex[index+1:]
        if regex[index-1] in string.digits:
            first_char_index = string.digits.index(regex[index-1])
            last_char_index = string.digits.index(regex[index+1])
            for i in range(first_char_index, last_char_index):
                replacement += string.digits[i] + '|'
            #replacement += string.digits[last_char_index]
            regex = regex[:index-1] + replacement + regex[index+1:]
        regex = regex.replace('[','(')
        regex = regex.replace(']',')')
    return regex
