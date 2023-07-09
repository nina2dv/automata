class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q              # states
        self.Sigma = Sigma      # alphabet
        self.delta = delta      # transition function
        self.q0 = q0            # start state
        self.F = F              # accepting states

    def __repr__(self):
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    def run(self, w):
        input_string = w
        q = self.q0
        while w != "":
            p = q
            q = self.delta[(q, w[0])]
            print(str(p) + ', ' + str(w) + ' -> ' + str(q))
            w = w[1:]
        print("State landed on: " + str(q))
        if q in self.F:
            return "Accept " + input_string
        else:
            return "Reject  " + input_string


M = DFA({0, 1, 2}, {"a", "b"},
    {(0, "a"): 0, (0, "b"): 1,
     (1, "a"): 2, (1, "b"): 1,
     (2, "a"): 2, (2, "b"): 2},
    0,
    {0, 1})

print(M.run("aa"))      # true
print(M.run("ba"))      # false
