import graphviz

class drawDFA:
    def __init__(self, DFA):
        self.DFA = DFA
        self.dfa = graphviz.Digraph("dfa", format='png') 
        self.dfa.attr(rankdir='LR', size='9')
        self.setStates()
        self.setTransitions()
        self.draw()
    def setStates(self):
        self.dfa.node("", style="invis")
        self.dfa.attr('node', shape='circle')
        self.dfa.node(str(self.DFA.initial_state))
        self.dfa.attr('node', shape='doublecircle')

        for state in self.DFA.accepting_states:
            self.dfa.node(str(state))
    def setTransitions(self):
        self.dfa.edge("", str(self.DFA.initial_state))
        self.dfa.attr('node', shape='circle')
        for state in self.DFA.transitions:
            for substates in self.DFA.transitions[state]:
                for con in self.DFA.transitions[state][substates]:
                    self.dfa.edge(str(state), str(con), label=str(substates))

    def draw(self):
        self.dfa.render(directory='output').replace('\\', '/')

