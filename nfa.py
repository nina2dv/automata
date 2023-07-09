class NFA:
    def __init__(self, Q, Sigma, delta, S, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.S = S
        self.F = F

    def __repr__(self):
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.S},\n\t{self.F})"

    def do_delta(self, q, x):
        try:
            return self.delta[(q, x)]
        except KeyError:
            return set({})  # Empty set

    def run(self, w):
        input_string = w
        P = self.S
        while w != "":
            Pnew = set({})
            for q in P:
                Pnew = Pnew | self.do_delta(q, w[0])
            print(str(P) + ', ' + str(w) + ' -> ' + str(Pnew))
            w = w[1:]
            P = Pnew
        print("State(s) landed on: " + str(P))
        is_final = (P & self.F) != set({})
        if is_final:
            return "Accept " + input_string
        else:
            return "Reject  " + input_string


M = NFA({0, 1, 2}, {"0", 1},
        {(0, "0"): {0},
         (0, "1"): {0, 1},
         (1, "0"): {2},
         (1, "1"): {2}},
        {0},
        {2})

print(M.run("10"))      # true
print(M.run("100"))     # false
