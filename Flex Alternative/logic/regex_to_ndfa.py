import string
import sys
import os.path
sys.path.insert(0, os.path.abspath('../data'))

from structures import Finite_automata
from structures import Node
from structures import Stack
from functions import infix_to_postfix
from functions import add_concatenation_operation
from functions import remove_hyphens

def main(regex):
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_ =';
    operations = "|.*";
    
    regex = remove_hyphens(regex)
    regex = add_concatenation_operation(regex, alphabet)
    print(regex)
    postfix_regex = infix_to_postfix(regex, alphabet, operations)
    print(postfix_regex)

    diff_symbols = []
    for char in postfix_regex:
        if (char in alphabet and char not in diff_symbols):
            diff_symbols.append(char)
    diff_symbols.sort()
    columns = len(diff_symbols) + 1

    states = []
    initial_states = []
    accepting_states = []
    operands = Stack()
    transitions = {}
    rows  = 0
    for char in postfix_regex:
        if char == '.':
            transitions[accepting_states.pop(-2)][-1].append(initial_states.pop())
            second_operand = operands.pop()
            first_operand = operands.pop()
            operands.push(first_operand+"."+second_operand)
        else:
            initial_state = "q"+str(rows)
            states.append(initial_state)
            rows+=1
            transitions[initial_state] = [None]*columns
            transitions[initial_state][-1] = []
            accepting_state = "q"+str(rows)
            states.append(accepting_state)
            transitions[accepting_state] = [None]*columns
            transitions[accepting_state][-1] = []
            rows+=1
            if char in alphabet:
                transitions[initial_state][diff_symbols.index(char)] = accepting_state
                operands.push(char)
            if char == '|':
                temp_accepting_states = []
                temp_accepting_states.append(accepting_states.pop())
                temp_accepting_states.append(accepting_states.pop())
                for current_state in temp_accepting_states:
                    transitions[current_state][-1].append(accepting_state)

                transitions[initial_state][-1].append(initial_states.pop())
                transitions[initial_state][-1].append(initial_states.pop())

                second_operand = operands.pop()
                first_operand = operands.pop()
                operands.push("("+first_operand + "|" + second_operand+")")
            if char == '*':
                transitions[initial_state][-1].append(initial_states.pop())
                transitions[initial_state][-1].append(accepting_state)

                transitions[accepting_states.pop()][-1].append(accepting_state)

                transitions[accepting_state][-1].append(initial_state)

                operand = operands.pop()
                operands.push(operand+"*")

            initial_states.append(initial_state)
            accepting_states.append(accepting_state)

    nfda = Finite_automata(alphabet, states, "".join(initial_states), accepting_states)
    nfda.copy_transitions(transitions)

    print(transitions)

if __name__=="__main__":
    with open('../data/regex.txt') as regex_file:
        while(regex:=regex_file.readline().rsplit(' ')):
            main(regex[2])
