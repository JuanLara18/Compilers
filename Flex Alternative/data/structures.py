from collections import deque
from pickle import NONE
class Finite_automata:
    def __init__(self, alphabet, states, initial_state, accepting_states, transitions = None):
        self.alphabet = alphabet
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transitions = transitions

    def give_info(self):
        print("----------------- Automata -----------------")
        print("The alphabet work with was: %s".format(self.alphabet))
        print("The states of the automata was: %s".format(self.states))
        print("The initial states is: %s".format(self.initial_state))
        print("The accepting_states are: %s".format(self.accepting_states))
        print("The transition function is given by:")
        print(self.transitions)

    def copy_transitions(self, transitions):
        self.transitions = transitions
    def __str__(self) -> str:
        return ("Alphabet: " + str(self.alphabet) + "\n" +
                "States: " + str(self.states) + "\n" +
                "Initial State: " + str(self.initial_state) + "\n" +
                "Accepting States: " + str(self.accepting_states) + "\n" +
                "Transition Function: " + str(self.transitions))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def get_value(self):
        return self.value

class Stack:
    def __init__(self, initial = None):
        if initial == None:
            self.items = deque()
        else:
            self.items = deque(initial)
    def __len__(self):
        return len(self.items)
    def __contains__(self, item):
        return item in self._items
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None
    def popleft(self):
        try:
            return self.items.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None
    def push(self, value):
        if not hasattr(value, "__len__"):
            self.items.append(value)
        else:
            for elm in value:
                self.items.append(elm)
    def get_size(self):
        return self.__len__();
    def is_empty(self):
        return self.__len__() == 0
    def peek(self):
        if self.is_empty():
            raise Exception("It's empty");
        return self.items[len(self.items) - 1];
    def __str__(self):
        to_print = "["
        for elm in self.items:
            to_print += str(elm) + ", "
        to_print += "]"
        return to_print;
