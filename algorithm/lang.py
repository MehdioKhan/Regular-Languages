class DFA:

    def __init__(self, alphabet=set(), q=set(), q0='', delta=[], f=set()):
        self.__alphabet = alphabet
        self.__q = q
        self.__q0 = q0
        self.__delta = delta
        self.__f = f

    def __str__(self):
        print("Alphabets = {a}\nStates = {q}\nStart States = {q0}\nFinal State = {f}\n"
              "Delta Function = {d}".format(a=self.alphabet, q=self.q,
                                            f=self.f, q0=self.q0, d=self.delta))

    @property
    def alphabet(self):
        return self.__alphabet

    @property
    def q(self):
        return self.__q

    @property
    def q0(self):
        return self.__q0

    @property
    def delta(self):
        return self.__delta

    @property
    def f(self):
        return self.__f

    @alphabet.setter
    def alphabet(self, alphabet):
        self.__alphabet = alphabet

    @q.setter
    def q(self, states):
        self.__q = states

    @q0.setter
    def q0(self, q0):
        self.__q0 = q0

    @delta.setter
    def delta(self, delta):
        self.__delta = delta

    @f.setter
    def f(self, f):
        self.__f = f

    def add_state(self, state):
        if state not in self.__q:
            self.__q.update(state)

    def add_delta(self, qi, a, qj):
        if (qi, a, qj) not in self.__delta:
            self.__delta.append((qi, a, qj))

    def get_delta(self, qi, a):
        r = set()
        for d in self.__delta:
            if d[0] == qi and d[1] == a:
                r.add(d[2])
        return r

class NFA:

    def __init__(self, alphabet=set(), q=set(), q0='', delta=[], f=set()):
        self.__alphabet = alphabet
        self.__q = q
        self.__q0 = q0
        self.__delta = delta
        self.__f = f

    def __str__(self):
        print("Alphabets = {a}\nStates = {q}\nStart States = {q0}\nFinal State = {f}\n"
              "Delta Function = {d}".format(a=self.alphabet, q=self.q,
                                            f=self.f, q0=self.q0, d=self.delta))

    @property
    def alphabet(self):
        return self.__alphabet

    @property
    def q(self):
        return self.__q

    @property
    def q0(self):
        return self.__q0

    @property
    def delta(self):
        return self.__delta

    @property
    def f(self):
        return self.__f

    @alphabet.setter
    def alphabet(self, alphabet):
        self.__alphabet = alphabet

    @q.setter
    def q(self, states):
        self.__q = states

    @q0.setter
    def q0(self, q0):
        self.__q0 = q0

    @delta.setter
    def delta(self, delta):
        self.__delta = delta

    @f.setter
    def f(self, f):
        self.__f = f

    def add_state(self, state):
        if state not in self.__q:
            self.__q.update(state)

    def add_delta(self, qi, a, qj):
            if not (qi, a, qj) in self.__delta:
                self.__delta.append((qi, a, qj))

    def get_delta(self, qi, a):
        r = set()
        for d in self.__delta:
            if d[0] == qi and d[1] == a:
                r.add(d[2])
        return r

    def landa_closure(self, q):
        stack = [q]
        r = set()
        while stack:
            state = stack.pop()
            for d in self.__delta:
                r.add(state)
                if d[0] == state and d[1] == 'L':
                    r.add(d[2])
                    stack.append(d[2])
        return r

    def transition(self, q, a):
        t = []
        s = set()
        lc = self.landa_closure(q)
        for l in lc:
            temp = self.get_delta(l, a)
            if temp:
                for m in temp:
                    s.update(self.landa_closure(m))
        t.append((q, a, s))
        return t

    def transition_table(self):
        t = []
        for q in self.q:
            for a in self.alphabet:
                t += self.transition(q, a)
        return t

def nfa_to_dfa(nfa):

    dfa = DFA(alphabet=nfa.alphabet)   # Set Alphabet
    start = nfa.landa_closure(nfa.q0)
    dfa.q0 = start   # Set First State
    tt = nfa.transition_table()     # Get Transition Table
    current_state = set(dfa.q0)
    states = [current_state]
    stack = [current_state]
    while stack:
        current_state = stack.pop()
        for a in nfa.alphabet:
            next_state = set()
            for q in current_state:
                for e in tt:
                    if q == e[0] and a == e[1]:
                        next_state.update(e[2])
            if next_state not in states:
                states.append(next_state)
                stack.append(next_state)
    dfa.q = [s for s in states]
    final = []
    for q in dfa.q:
        for w in q:
            for f in nfa.f:
                if w == f:
                    final.append(q)
    dfa.f = final
    stack = states
    while stack:
        current_state = stack.pop()
        for a in nfa.alphabet:
            next_state = set()
            for q in current_state:
                for e in tt:
                    if q == e[0] and a == e[1]:
                        next_state.update(e[2])
            dfa.add_delta(current_state, a, next_state)
    dfa.delta.reverse()
    return dfa
#
# def main():
#
#     nfa = NFA()
#     nfa.alphabet = {'a', 'b'}
#     nfa.q = {'q0', 'q1'}
#     nfa.q0 = 'q0'
#     nfa.f = {'q1'}
#     nfa.delta = [('q0', 'a', 'q0'), ('q0', 'a', 'q1'), ('q1', 'a', 'q0'), ('q1', 'b', 'q1')]
#     # nfa.add_delta('q0', 'a', 'q0')
#     # nfa.add_delta('q0', 'b', 'q0')
#     # nfa.add_delta('q0', 'b', 'q1')
#     # nfa.add_delta('q1', 'a', 'q2')
#     # nfa.add_delta('q2', 'b', 'q3')
#     # nfa.add_delta('q3', 'a', 'q3')
#     # nfa.add_delta('q3', 'b', 'q3')
#     dfa = nfa_to_dfa(nfa)
#     dfa.__str__()
# main()
